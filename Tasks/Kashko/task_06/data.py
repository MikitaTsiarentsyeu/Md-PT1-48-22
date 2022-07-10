import os
import sqlite3 as sql


# Get admin's login and passowrd
ADMIN_LOGIN = os.environ.get("ADMIN_LOGIN")
ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD")

# Path to database
db_path = os.path.realpath(os.path.join(os.path.dirname(__file__),
                                        'meters.db'))

# Database connection, creating tables if not exist
# and filling with initial data.
con = sql.connect(db_path)
with con:
    con.executescript('''
        CREATE TABLE IF NOT EXISTS category(
        category_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE NOT NULL
        );

        CREATE TABLE IF NOT EXISTS meter(
        meter_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        type TEXT NOT NULL,
        category_id INTEGER NOT NULL,
        price REAL,
        amount INTEGER,
        UNIQUE (name, type),
        FOREIGN KEY (category_id) REFERENCES category (id)
        );

        CREATE TABLE IF NOT EXISTS order_(
        order_id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT NOT NULL,
        user TEXT NOT NULL,
        order_content BLOB NOT NULL
        );
        ''')

try:
    with con:
        con.executescript('''
            INSERT INTO category(name)
            VALUES
                ("Insulator resistance"),
                ("Ground resistance"),
                ("Loop impedance"),
                ("RCD parameters");

            INSERT INTO meter(name, type, category_id, price, amount)
            VALUES
                ("Megohmmeter", "Е6-24",
                (SELECT category_id FROM category
                WHERE name = "Insulator resistance"), 580.26, 15),
                ("Megohmmeter", "Е6-24/1",
                (SELECT category_id FROM category
                WHERE name = "Insulator resistance"), 562.42, 7),
                ("Megohmmeter", "Е6-31",
                (SELECT category_id FROM category
                WHERE name = "Insulator resistance"), 765.05, 5),
                ("Megohmmeter", "Е6-31/1",
                (SELECT category_id FROM category
                WHERE name = "Insulator resistance"), 695.34, 6),
                ("Megohmmeter", "Е6-32",
                (SELECT category_id FROM category
                WHERE name = "Insulator resistance"), 784.95, 2),
                ("Earth Ground Tester", "ИС-10",
                (SELECT category_id FROM category
                WHERE name = "Ground resistance"), 643.13, 10),
                ("Earth Ground Tester", "ИС-10/1",
                (SELECT category_id FROM category
                WHERE name = "Ground resistance"), 654.96, 7),
                ("Earth Ground Tester", "ИС-20",
                (SELECT category_id FROM category
                WHERE name = "Ground resistance"), 816.02, 5),
                ("Earth Ground Tester", "ИС-20/1",
                (SELECT category_id FROM category
                WHERE name = "Ground resistance"), 754.13, 12),
                ("Loop Impedance Meter", "ЕР180",
                (SELECT category_id FROM category
                WHERE name = "Loop impedance"), 1023.26, 11),
                ("Loop Impedance Meter", "ЕР180М",
                (SELECT category_id FROM category
                WHERE name = "Loop impedance"), 964.35, 17),
                ("Loop Impedance Meter", "ИФН-200",
                (SELECT category_id FROM category
                WHERE name = "Loop impedance"), 1256.48, 14),
                ("Loop Impedance Meter", "ИФН-300",
                (SELECT category_id FROM category
                WHERE name = "Loop impedance"), 1543.12, 11),
                ("Loop Impedance Meter", "ИФН-300/1",
                (SELECT category_id FROM category
                WHERE name = "Loop impedance"), 962.37, 7),
                ("RCD Meter", "ПЗО-500",
                (SELECT category_id FROM category
                WHERE name = "RCD parameters"), 968.88, 5),
                ("RCD Meter", "ПЗО-500 ПРО",
                (SELECT category_id FROM category
                WHERE name = "RCD parameters"), 1123.65, 7),
                ("RCD Meter", "ПЗО-510",
                (SELECT category_id FROM category
                WHERE name = "RCD parameters"), 1413.12, 10),
                ("RCD Meter", "ПЗО-510/1",
                (SELECT category_id FROM category
                WHERE name = "RCD parameters"), 1568.13, 6);
        ''')
        print('Initial data uploaded successfully.')
except sql.IntegrityError:
    print('Initial data already exists.')


def get_all_meters() -> list[tuple]:
    """Returns all data from meter table in database.

    Returns:
        list[tuple]: meters data.
    """
    with con:
        return con.execute(
            '''SELECT m.meter_id, m.name, m.type, c.name, m.price, m.amount
               FROM meter AS m LEFT JOIN category AS c
               ON m.category_id = c.category_id
               ORDER BY m.meter_id''').fetchall()


def get_categories() -> list[tuple]:
    """Returns all data from categories table in database.

    Returns:
        list[tuple]: categories.
    """
    with con:
        return con.execute(
            'SELECT * FROM category ORDER BY category_id').fetchall()


def get_category(id: int) -> list[tuple]:
    """Returns meters in one category by id from meter table in database.

    Args:
        id (int): category id.

    Returns:
        list[tuple]: meters data.
    """
    with con:
        return con.execute(
            f'''SELECT m.meter_id, m.name, m.type, c.name, m.price, m.amount
            FROM meter AS m LEFT JOIN category AS c
            ON m.category_id = c.category_id
            WHERE m.category_id = {id}
            ORDER BY m.meter_id''').fetchall()


def get_meters_by_ids(ids: tuple) -> list[tuple]:
    """Returns meters data by ids.

    Args:
        ids (tuple): ids.

    Returns:
        list[tuple]: meter data.
    """
    with con:
        return con.execute(
            f'''SELECT m.meter_id, m.name, m.type, c.name, m.price
            FROM meter AS m LEFT JOIN category AS c
            ON m.category_id = c.category_id
            WHERE m.meter_id {f'IN {ids}' if len(ids) > 1 else f'= {ids[0]}'}
            ORDER BY m.meter_id''').fetchall()


def get_orders(user: str) -> list[tuple]:
    """Returns all orders data for current user.

    Args:
        user (str): username.

    Returns:
        list[tuple]: orders data.
    """
    with con:
        return con.execute(
            '''SELECT order_id, date
               FROM order_ AS o
               WHERE o.user = (?)
               ORDER BY date''', (user, )).fetchall()


def place_order(user: str, content: bytes) -> bool:
    """Adds order made by user to orders table in database
    and returns result of operation.

    Args:
        user (str): username.
        content (bytes): order binary data.

    Returns:
        bool: True or False.
    """
    try:
        with con:
            con.execute(
                '''INSERT INTO order_(date, user, order_content)
                VALUES (datetime(), (?), (?))''', (user, sql.Binary(content)))
        return True
    except sql.Error:
        return


def get_order(id: int) -> list[tuple]:
    """Returns order binary data by order id.

    Args:
        id (int): order id.

    Returns:
        list[tuple]: order binary data.
    """
    with con:
        return con.execute(f'''SELECT order_content
                               FROM order_
                               WHERE order_id = {id}''').fetchall()


def insert_meter(meter: tuple) -> bool:
    """Adds a new item to meters table in database
    and returns the result of operation.

    Args:
        meter (tuple): meter data.

    Returns:
        bool: True or False
    """
    try:
        with con:
            con.execute(
                '''INSERT INTO meter(name, type, category_id, price, amount)
                   VALUES
                        ((?), (?),
                        (SELECT category_id FROM category
                        WHERE name = (?)), (?), (?))''', meter)
        return True
    except sql.Error:
        return


def insert_category(name: str) -> bool:
    """Adds a new item to categories table in database
    and returns the result of operation.

    Args:
        name (str): category.

    Returns:
        bool: True or False
    """
    try:
        with con:
            con.execute('''INSERT INTO category(name) VALUES (?)''', (name, ))
        return True
    except sql.Error:
        return


def get_all_orders() -> list[tuple]:
    """Returns all orders from orders table in database.

    Returns:
        list[tuple]: orders data.
    """
    with con:
        return con.execute('''SELECT order_id, date, user
                              FROM order_
                              ORDER BY date''').fetchall()
