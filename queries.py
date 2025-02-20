# pylint:disable=C0111,C0103
import sqlite3




def query_orders(db):
    # return a list of orders displaying each column

    conn = sqlite3.connect('data/ecommerce.sqlite')
    db = conn.cursor()
    query = """
            SELECT * FROM Orders o ORDER BY OrderID
            """
    db.execute(query)

    return db.fetchall()



def get_orders_range(db, date_from, date_to):
    # return a list of orders displaying all columns with OrderDate between
    # date_from and date_to (excluding date_from and including date_to)

    conn = sqlite3.connect('data/ecommerce.sqlite')
    db = conn.cursor()
    query = """
            SELECT * FROM Orders o WHERE OrderDate > ? and OrderDate <= ?

            """
    db.execute(query,(date_from,date_to))

    return db.fetchall()


def get_waiting_time(db):
    # get a list with all the orders displaying each column
    # and calculate an extra TimeDelta column displaying the number of days
    # between OrderDate and ShippedDate, ordered by ascending TimeDelta
    conn = sqlite3.connect('data/ecommerce.sqlite')
    db = conn.cursor()
    query = """
                SELECT *,
                (JULIANDAY(ShippedDate) - JULIANDAY(OrderDate)) AS waiting_time
                FROM Orders
                WHERE ShippedDate IS NOT NULL
                ORDER BY waiting_time ASC

            """
    db.execute(query)

    return db.fetchall()
