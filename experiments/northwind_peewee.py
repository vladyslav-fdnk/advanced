from peewee import *
from northwind_models import Products, Categories


if __name__ == '__main__':
    # query= Products.select().where(Products.unit_price > 50).order_by(Products.unit_price.desc())
    # for product in query:
    #     print(product.name, product.unit_price)

    query = (
        Products
        .select(
            Categories.category_name,
            fn.COUNT(Products.id).alias('count')
        )
        .join(Categories, on=(Categories.category_id == Products.CategoryID))
        .group_by(Categories.category_name)
    )

    for product in query:
        print(product.category_name, product.count)