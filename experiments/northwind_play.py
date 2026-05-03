from lessons.data_base import create_connection, select_query

if __name__ == "__main__":
    connection = create_connection('northwind.db')

    # result= select_query(
    #     connection,
    #     "select MAX(UnitPrice) from Products order by UnitPrice DESC LIMIT 1;"
    # )
    # for row in result:
    #     print(row)
    #     print('-'*80)

    count_customers_countrys = """
                         SELECT COUNT(distinct Country) from customers
                         """
    # result=select_query(
    #     connection,
    #     count_customers_countrys)
    # for row in result:
    #     print(row)
    #     print('-'*80)

    orders_from_countries = """
    select * from Orders 
    where ShipCountry in ('France', 'Germany', 'Brazil')
    order by OrderDate desc, ShippedDate;
    """

    # result = select_query(
    #     connection,
    #     orders_from_countries)
    # for row in result:
    #     print(row)
    #     print('-' * 80)

    min_product_price_from_group = """
                                   SELECT MIN(UnitPrice)
                                   FROM Products
                                   WHERE UnitPrice >= 100 \
                                   """

    # result = select_query(connection, min_product_price_from_group)
    # for row in result:
    #     print(row)
    #     print('-' * 80)

    average_usa_order_days = """
    select AVG(JULIANDAY(ShippedDate) - JULIANDAY(OrderDate)) from Orders
    where ShipCountry = 'USA'
    """
    # result = select_query(connection, average_usa_order_days)
    # for row in result:
    #     print(row)
    #     print('-' * 80)


    products_summary = """
    SELECT sUM(UnitPrice * UnitsInStock) from Products
    """
    # result = select_query(connection, products_summary)
    # for row in result:
    #     print(row)
    #     print('-' * 80)
    #

    orders_from_P = """
    select * from Orders where ShipCountry like 'P%'
    """
    result = select_query(connection, orders_from_P)
    for row in result:
        print(row)
        print('-' * 80)
