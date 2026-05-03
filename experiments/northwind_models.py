from peewee import *

database = SqliteDatabase('northwind.db')

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class Categories(BaseModel):
    category_id = AutoField(column_name='CategoryID', null=True,primary_key=True)
    category_name = TextField(column_name='CategoryName', null=True)
    description = TextField(column_name='Description', null=True)
    picture = BlobField(column_name='Picture', null=True)

    class Meta:
        table_name = 'Categories'

class CustomerDemographics(BaseModel):
    customer_desc = TextField(column_name='CustomerDesc', null=True)
    customer_type_id = TextField(column_name='CustomerTypeID', primary_key=True)

    class Meta:
        table_name = 'CustomerDemographics'

class Customers(BaseModel):
    address = TextField(column_name='Address', null=True)
    city = TextField(column_name='City', null=True)
    company_name = TextField(column_name='CompanyName', null=True)
    contact_name = TextField(column_name='ContactName', null=True)
    contact_title = TextField(column_name='ContactTitle', null=True)
    country = TextField(column_name='Country', null=True)
    customer_id = TextField(column_name='CustomerID', null=True, primary_key=True)
    fax = TextField(column_name='Fax', null=True)
    phone = TextField(column_name='Phone', null=True)
    postal_code = TextField(column_name='PostalCode', null=True)
    region = TextField(column_name='Region', null=True)

    class Meta:
        table_name = 'Customers'

class CustomerCustomerDemo(BaseModel):
    customer = ForeignKeyField(column_name='CustomerID', field='customer_id', model=Customers)
    customer_type = ForeignKeyField(column_name='CustomerTypeID', field='customer_type_id', model=CustomerDemographics)

    class Meta:
        table_name = 'CustomerCustomerDemo'
        indexes = (
            (('customer', 'customer_type'), True),
        )
        primary_key = CompositeKey('customer', 'customer_type')

class Regions(BaseModel):
    region_description = TextField(column_name='RegionDescription')
    region_id = AutoField(column_name='RegionID')

    class Meta:
        table_name = 'Regions'

class Territories(BaseModel):
    region = ForeignKeyField(column_name='RegionID', field='region_id', model=Regions)
    territory_description = TextField(column_name='TerritoryDescription')
    territory_id = TextField(column_name='TerritoryID', primary_key=True)

    class Meta:
        table_name = 'Territories'

class Employees(BaseModel):
    address = TextField(column_name='Address', null=True)
    birth_date = DateField(column_name='BirthDate', null=True)
    city = TextField(column_name='City', null=True)
    country = TextField(column_name='Country', null=True)
    employee_id = AutoField(column_name='EmployeeID', null=True)
    extension = TextField(column_name='Extension', null=True)
    first_name = TextField(column_name='FirstName', null=True)
    hire_date = DateField(column_name='HireDate', null=True)
    home_phone = TextField(column_name='HomePhone', null=True)
    last_name = TextField(column_name='LastName', null=True)
    notes = TextField(column_name='Notes', null=True)
    photo = BlobField(column_name='Photo', null=True)
    photo_path = TextField(column_name='PhotoPath', null=True)
    postal_code = TextField(column_name='PostalCode', null=True)
    region = TextField(column_name='Region', null=True)
    reports_to = ForeignKeyField(column_name='ReportsTo', field='employee_id', model='self', null=True)
    title = TextField(column_name='Title', null=True)
    title_of_courtesy = TextField(column_name='TitleOfCourtesy', null=True)

    class Meta:
        table_name = 'Employees'

class EmployeeTerritories(BaseModel):
    employee = ForeignKeyField(column_name='EmployeeID', field='employee_id', model=Employees)
    territory = ForeignKeyField(column_name='TerritoryID', field='territory_id', model=Territories)

    class Meta:
        table_name = 'EmployeeTerritories'
        indexes = (
            (('employee', 'territory'), True),
        )
        primary_key = CompositeKey('employee', 'territory')

class Suppliers(BaseModel):
    address = TextField(column_name='Address', null=True)
    city = TextField(column_name='City', null=True)
    company_name = TextField(column_name='CompanyName')
    contact_name = TextField(column_name='ContactName', null=True)
    contact_title = TextField(column_name='ContactTitle', null=True)
    country = TextField(column_name='Country', null=True)
    fax = TextField(column_name='Fax', null=True)
    home_page = TextField(column_name='HomePage', null=True)
    phone = TextField(column_name='Phone', null=True)
    postal_code = TextField(column_name='PostalCode', null=True)
    region = TextField(column_name='Region', null=True)
    supplier_id = AutoField(column_name='SupplierID')

    class Meta:
        table_name = 'Suppliers'

class Products(BaseModel):
    category = ForeignKeyField(column_name='CategoryID', field='category_id', model=Categories, null=True)
    discontinued = TextField(column_name='Discontinued', constraints=[SQL("DEFAULT '0'")])
    product_id = AutoField(column_name='ProductID',primary_key=True)
    product_name = TextField(column_name='ProductName')
    quantity_per_unit = TextField(column_name='QuantityPerUnit', null=True)
    reorder_level = IntegerField(column_name='ReorderLevel', constraints=[SQL("DEFAULT 0")], null=True)
    supplier = ForeignKeyField(column_name='SupplierID', field='supplier_id', model=Suppliers, null=True)
    unit_price = DecimalField(column_name='UnitPrice', constraints=[SQL("DEFAULT 0")], null=True)
    units_in_stock = IntegerField(column_name='UnitsInStock', constraints=[SQL("DEFAULT 0")], null=True)
    units_on_order = IntegerField(column_name='UnitsOnOrder', constraints=[SQL("DEFAULT 0")], null=True)

    class Meta:
        table_name = 'Products'

class Shippers(BaseModel):
    company_name = TextField(column_name='CompanyName')
    phone = TextField(column_name='Phone', null=True)
    shipper_id = AutoField(column_name='ShipperID')

    class Meta:
        table_name = 'Shippers'

class Orders(BaseModel):
    customer = ForeignKeyField(column_name='CustomerID', field='customer_id', model=Customers, null=True)
    employee = ForeignKeyField(column_name='EmployeeID', field='employee_id', model=Employees, null=True)
    freight = DecimalField(column_name='Freight', constraints=[SQL("DEFAULT 0")], null=True)
    order_date = DateTimeField(column_name='OrderDate', null=True)
    order_id = AutoField(column_name='OrderID')
    required_date = DateTimeField(column_name='RequiredDate', null=True)
    ship_address = TextField(column_name='ShipAddress', null=True)
    ship_city = TextField(column_name='ShipCity', null=True)
    ship_country = TextField(column_name='ShipCountry', null=True)
    ship_name = TextField(column_name='ShipName', null=True)
    ship_postal_code = TextField(column_name='ShipPostalCode', null=True)
    ship_region = TextField(column_name='ShipRegion', null=True)
    ship_via = ForeignKeyField(column_name='ShipVia', field='shipper_id', model=Shippers, null=True)
    shipped_date = DateTimeField(column_name='ShippedDate', null=True)

    class Meta:
        table_name = 'Orders'

class OrderDetails(BaseModel):
    discount = FloatField(column_name='Discount', constraints=[SQL("DEFAULT 0")])
    order = ForeignKeyField(column_name='OrderID', field='order_id', model=Orders)
    product = ForeignKeyField(column_name='ProductID', field='product_id', model=Products)
    quantity = IntegerField(column_name='Quantity', constraints=[SQL("DEFAULT 1")])
    unit_price = DecimalField(column_name='UnitPrice', constraints=[SQL("DEFAULT 0")])

    class Meta:
        table_name = 'Order Details'
        indexes = (
            (('order', 'product'), True),
        )
        primary_key = CompositeKey('order', 'product')

class SqliteSequence(BaseModel):
    name = BareField(null=True)
    seq = BareField(null=True)

    class Meta:
        table_name = 'sqlite_sequence'
        primary_key = False

