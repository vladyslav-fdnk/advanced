import sqlite3
from sqlite3 import Error

import os
print(os.path.abspath('northwind.db'))


top_orders_n_countries_by_weight= """
    select * from Orders
    where ShipCountry LIKE 'N%'
    order by Freight desc
    limit 10
    """


    #2. Знайти замовників у яких ми не маємо телефонів

clients_without_phone="""
        SELECT * FROM Customers
            where Phone IS NULL
    """


    #3. Порахувати клієнтів, що мають телефон

get_customers_with_phone_count="""
        SELECT COUNT(*)
        FROM Customers
        WHERE Phone IS NOT NULL
    """


    #4. Порахувати постачальників з кожної країни, відсортувати по кількості по зменшенню
count_suppliers_by_country = """
        SELECT 
            Country,
            COUNT(*) AS suppliers_count
        FROM Suppliers
        Group by Country
        ORDER BY suppliers_count DESC
    """


    #5. Порахувати сумарну вагу замовлень в яких відомий регіон потім відфільтрувати
    # тільки ті в яких вага більше 2750 та відсортувати по зменшенню

get_total_order_weight_by_region = """
        SELECT ShipRegion,
               SUM(Freight) AS total_weight
        FROM Orders
        WHERE ShipRegion IS NOT NULL
        GROUP BY ShipRegion
        HAVING SUM(Freight) > 2750
        ORDER BY total_weight DESC 
        """




    #6. Вибрати унікальні країни замовників та постачальників та відсортувати по збільшенню

get_unique_countries_from_customers_and_suppliers= """
        SELECT COUNTRY 
        FROM Customers
        UNION 
        SELECT COUNTRY
        FROM Suppliers
        ORDER BY COUNTRY ASC
    """



#7. Знайти замовників та співробітників, що обслуговують їх замовлення вони мають бути з Лондона
# і ті і ті, а доставка має йти компанією доставки Speedy Express вивести ім'я прізвище
# робітника та компанії замовника

get_london_customers_and_employees_by_speedy_express= """
        SELECT 
            e.FirstName,
            e.LastName,
            c.CompanyName
        FROM Orders o
        JOIN Customers c ON o.CustomerID = c.CustomerID
        JOIN Employees e ON o.EmployeeID = e.EmployeeID
        JOIN Shippers s ON o.ShipVia = s.ShipperID
        WHERE c.City = 'London'
          AND e.City = 'London'
          AND s.CompanyName = 'Speedy Express';
    """



    #8. Знайти замовників, що не зробили жодного замовлення
get_customers_without_orders= """
        SELECT c.*
        FROM Customers c
        LEFT JOIN Orders o ON c.CustomerID = o.CustomerID
        WHERE o.CustomerID IS NULL;
    """

#9

get_products_with_exact_10_units = """
        SELECT 
            p.ProductName,
            SUM(od.Quantity) AS total_qty
        FROM Products p
        JOIN "Order Details" od ON p.ProductID = od.ProductID
        GROUP BY p.ProductID, p.ProductName
        HAVING SUM(od.Quantity) = 10
        ORDER BY total_qty;
       """




def create_connection(path:str) -> sqlite3.Connection:
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection established")
    except Error as e:
        print(e)
    return connection


def execute_query(connection:sqlite3.Connection, query:str) -> None:
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed")
    except Error as e:
        print(e)
        connection.rollback()
        print("Rollback executed")

def select_query(connection: sqlite3.Connection, query: str) -> list | None:
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        return cursor.fetchall()
    except Error as e:
        print(e)
        return []


def run_task(connection, title, query):
    print(f'\n{20 * "#"} {title} {50 * "#"}\n')

    result = select_query(connection, query)

    if not result:
        print("No data")
        return

    for row in result:
        print(row)
        print('-' * 80)

if __name__ == "__main__":
    connection = create_connection('../northwind.db')

    run_task(connection, "Task 1", top_orders_n_countries_by_weight)
    run_task(connection, "Task 2", clients_without_phone)
    run_task(connection, "Task 3", get_customers_with_phone_count)
    run_task(connection, "Task 4", count_suppliers_by_country)
    run_task(connection, "Task 5", get_total_order_weight_by_region)
    run_task(connection, "Task 6", get_unique_countries_from_customers_and_suppliers)
    run_task(connection, "Task 7", get_london_customers_and_employees_by_speedy_express)
    run_task(connection, "Task 8", get_customers_without_orders)
    run_task(connection, "Task 9", get_products_with_exact_10_units)

    top_orders_n_countries_by_weight= """
    select * from Orders
    where ShipCountry LIKE 'N%'
    order by Freight desc
    limit 10
    """


    #2. Знайти замовників у яких ми не маємо телефонів

    clients_without_phone="""
        SELECT * FROM Customers
            where Phone IS NULL
    """


    #3. Порахувати клієнтів, що мають телефон

    get_customers_with_phone_count="""
        SELECT COUNT(*)
        FROM Customers
        WHERE Phone IS NOT NULL
    """


    #4. Порахувати постачальників з кожної країни, відсортувати по кількості по зменшенню
    count_suppliers_by_country = """
        SELECT 
            Country,
            COUNT(*) AS suppliers_count
        FROM Suppliers
        Group by Country
        ORDER BY suppliers_count DESC
    """


    #5. Порахувати сумарну вагу замовлень в яких відомий регіон потім відфільтрувати
    # тільки ті в яких вага більше 2750 та відсортувати по зменшенню

    get_total_order_weight_by_region = """
        SELECT ShipRegion,
               SUM(Freight) AS total_weight
        FROM Orders
        WHERE ShipRegion IS NOT NULL
        GROUP BY ShipRegion
        HAVING SUM(Freight) > 2750
        ORDER BY total_weight DESC 
        """




    #6. Вибрати унікальні країни замовників та постачальників та відсортувати по збільшенню

    get_unique_countries_from_customers_and_suppliers= """
        SELECT COUNTRY 
        FROM Customers
        UNION 
        SELECT COUNTRY
        FROM Suppliers
        ORDER BY COUNTRY ASC
    """



#7. Знайти замовників та співробітників, що обслуговують їх замовлення вони мають бути з Лондона
# і ті і ті, а доставка має йти компанією доставки Speedy Express вивести ім'я прізвище
# робітника та компанії замовника

    get_london_customers_and_employees_by_speedy_express= """
        SELECT 
            e.FirstName,
            e.LastName,
            c.CompanyName
        FROM Orders o
        JOIN Customers c ON o.CustomerID = c.CustomerID
        JOIN Employees e ON o.EmployeeID = e.EmployeeID
        JOIN Shippers s ON o.ShipVia = s.ShipperID
        WHERE c.City = 'London'
          AND e.City = 'London'
          AND s.CompanyName = 'Speedy Express';
    """



    #8. Знайти замовників, що не зробили жодного замовлення
    get_customers_without_orders= """
        SELECT c.*
        FROM Customers c
        LEFT JOIN Orders o ON c.CustomerID = o.CustomerID
        WHERE o.CustomerID IS NULL;
    """

#9

    get_products_with_exact_10_units = """
        SELECT 
            p.ProductName,
            SUM(od.Quantity) AS total_qty
        FROM Products p
        JOIN "Order Details" od ON p.ProductID = od.ProductID
        GROUP BY p.ProductID, p.ProductName
        HAVING SUM(od.Quantity) = 10
        ORDER BY total_qty;
       """


