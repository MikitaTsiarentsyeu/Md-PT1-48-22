from sqlite3 import connect
import psycopg2
from psycopg2 import Error


def creat_database():
    try:
        connected = psycopg2.connect(dbname="testdb",
                                     user="postgres",
                                     password="postgres",
                                     port=2713)

        data = connected.cursor()

        data.execute('''create table underwear  
                    (id serial PRIMARY KEY,
                    underwear_name TEXT NOT NULL,
                    products_code INT NOT NULL,
                    price INT,
                    in_stock int);''')

        data.execute('''insert underwear (underwear_name, products_code, price, in_stock) VALUES
                    ('socks', 11, 100, 210),
                    ('thongs', 12, 10, 480),
                    ('body', 13, 500, 942),
                    ('pants', 14, 300, 670)''')

        data.execute('''create tABLE outerwear 
                    (outerwear_id serial PRIMARY KEY,
                    outerwear_name TEXT NOT NULL,
                    products_code INT NOT NULL,
                    price INT,
                    in_stock int);''')

        data.execute('''insert outerwear (outerwear_name, products_code, price, in_stock) VALUES
                    ('t - shirts', 21, 110, 1300),
                    ('shirts', 22, 1034, 3984),
                    ('sweatshirts', 23, 503, 1134),
                    ('jackets', 24, 602, 2500)''')

        data.execute('''create table shoes  
                    (shoes_id serial PRIMARY KEY,
                    shoes_name TEXT NOT NULL,
                    products_code INT NOT NULL,
                    price INT,
                    in_stock int);''')

        data.execute('''insert shoes (shoes_name, products_code, price, in_stock) VALUES
                    ('sneakers', 31, 2390, 2650),
                    ('boots', 32, 3900, 9933),
                    ('shoes', 33, 8500, 2500)''')

        data.commit()
    except (Exception, Error) as error:
        print("Error  PostgreSQL", error)
    finally:
        if connected:
            data.close()
            connected.close()
            print("Connection PostgreSQL")


def database(name_table):
    try:
        connected = psycopg2.connect(dbname="testdb",
                                     user="postgres",
                                     password="postgres",
                                     port=2713)

        data = connected.cursor()
        postgresql_select_query = f"select * from {name_table}"

        data.execute(postgresql_select_query)
        mobile_records = data.fetchall()

        products_category = {}

        for row in mobile_records:
            products_category[row[1]] = list(row[2::])

    except (Exception, Error) as error:
        print("Error PostgreSQL", error)
    finally:
        if connected:
            data.close()
            connected.close()
            print("Connection PostgreSQL")
            return products_category


def return_data_from_database():
    categories = ['underwear', 'outerwear', 'shoes']
    products = {}
    creat_database()

    for name_categories in categories:
        products[name_categories] = database(name_categories)

    return products
