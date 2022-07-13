import sqlite3 as sq
import os
import bl


def write_user_cart(info):
    with sq.connect("usercart.db") as file:
        cur = file.cursor()
        new_table = '''CREATE TABLE IF NOT EXISTS cart(
			item_id INTEGER  PRIMARY KEY AUTOINCREMENT DEFAULT 1,
			item_name TEXT NOT NULL,
			item_articul TEXT NOT NULL,
			price TEXT NOT NULL
		)'''
        cur.execute(new_table)
        cur.execute("INSERT INTO cart(item_name,item_articul,price)VALUES (?,?,?)", (info))


def read_user_cart():
    with sq.connect("usercart.db") as file:
        cur = file.cursor()
        return cur.execute("SELECT rowid,item_name,item_articul,price FROM cart").fetchall()


def read_cart_price():
    with sq.connect("usercart.db") as file:
        cur = file.cursor()
        return cur.execute("SELECT SUM(price) FROM cart").fetchall()


def delete_user_item(number_of_deletion_item):
    with sq.connect("usercart.db") as file:
        cur = file.cursor()
        list_of_item_numbers = []
        for row in cur.execute("SELECT item_id FROM cart").fetchall():
            list_of_item_numbers.append(row[0])

        if number_of_deletion_item in list_of_item_numbers:
            cur.execute("DELETE FROM cart WHERE item_id = ?", (number_of_deletion_item,))
            return True
        else:
            return False


def delete_all_items():
    with sq.connect("usercart.db") as file:
        cur = file.cursor()
        cur.execute("DELETE FROM cart")


def use_database(ide=None, table_name=None):
    with sq.connect("database1.db") as file:
        cur = file.cursor()

        if ide:
            if ide and table_name == None:
                num = bl.prepatate_str(
                    cur.execute("SELECT product_link FROM product_title WHERE product_id = ?;", (ide,)).fetchall())
                query = "SELECT * FROM {}".format(num)

                return cur.execute(query).fetchall()
            else:
                tem = "SELECT * FROM {}".format(table_name)
                return cur.execute(tem).fetchall()
        return cur.execute("SELECT product_id, product_name FROM product_title").fetchall()
