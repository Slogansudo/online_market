from db_connect_2 import Database


class Base:
    @staticmethod
    def delete(column, search_data, table):
        if search_data is int or search_data is float or search_data is bool:
            query = f"""DELETE FROM {table} WHERE {column}={search_data};"""
        else:
            query = f"""DELETE FROM {table} WHERE {column}='{search_data}';"""
        return Database.connect(query, 'DELETE')

    @staticmethod
    def update(search_id, column, new_data, table, id_column):
        if new_data is int or new_data is bool:
            query = f"""UPDATE {table} SET {column}={new_data} WHERE {id_column}={search_id};"""
        else:
            query = f"""UPDATE {table} SET {column}='{new_data}' WHERE {id_column}={search_id};"""
        return Database.connect(query, 'UPDATE')

    @staticmethod
    def select(table):
        query = f"""SELECT * FROM {table};"""
        return Database.connect(query, 'SELECT')


class Country:

    def __init__(self, name):
        self.name = name

    @staticmethod
    def select(quer, table="country"):
        if quer == 'SELECT':
            query = f"""SELECT * FROM {table}"""
            return Database.connect(query, 'SELECT')
        else:
            return Database.connect(quer, 'SELECT')

    def insert(self, table="country"):
        query = f"""INSERT INTO {table}(name) VALUES('{self.name}')"""
        return Database.connect(query, 'INSERT')

    def update(self, country_id, table="country", column="country_id"):
        query = f"""UPDATE {table} SET name = '{self.name}' WHERE {column}={country_id}"""
        return Database.connect(query, 'UPDATE')

    def delete(self, country_id, table='country', column="country_id"):
        query = f"""DELETE FROM {table} WHERE name = '{self.name}' and {column} = {country_id}"""
        return Database.connect(query, 'DELETE')

    @staticmethod
    def update_id(old_id, new_id, column_name='country_id', table="country"):
        query = f"""UPDATE {table} SET {column_name}={new_id} WHERE {column_name}={old_id}"""
        return Database.connect(query, 'UPDATE')

    @staticmethod
    def get_id(table="country", column_name='country_id'):
        query = f"""SELECT {column_name} FROM {table}"""
        return Database.connect(query, 'SELECT')


class City(Country):
    def __init__(self, name):
        super().__init__(name)

    def insert(self, country_id, table="city"):
        query = f"""INSERT INTO {table}(name, country_id) VALUES('{self.name}', {country_id});"""
        return Database.connect(query, 'INSERT')


class Address(Country):
    def __init__(self, name):
        super().__init__(name)

    def insert(self, city_id, table='address'):
        query = f"""INSERT INTO {table}(name, city_id) VALUES('{self.name}',{city_id});"""
        return Database.connect(query, 'INSERT')


class PaymentStatus(Base):
    def __init__(self, status_pay):
        self.status_pay = status_pay

    def insert(self, table):
        query = f"""INSERT INTO {table}(status_pay) VALUES ({self.status_pay});"""
        return Database.connect(query, 'INSERT')


class PaymentType(Base):
    def __init__(self, name):
        self.name = name

    def insert(self, table):
        query = f"""INSERT INTO {table}(name) VALUES('{self.name}');"""
        return Database.connect(query, "INSERT")


class Payment(Base):
    def __init__(self, amount:float, payment_type_id:int, payment_status_id:int):
        self.amount = amount
        self.payment_type_id = payment_type_id
        self.payment_status_id = payment_status_id

    def insert(self, table):
        query = f"""INSERT INTO {table}(amount, payment_type_id, payment_status_id) VALUES({self.amount}, {self.payment_type_id}, {self.payment_status_id});"""
        return Database.connect(query, "INSERT")


class Customer(Base):
    def __init__(self, first_name, last_name, password, username, status, gmail, address_id: int, payment_id: int):
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.username = username
        self.status = status
        self.gmail = gmail
        self.address_id = address_id
        self.payment_id = payment_id

    def insert(self, table):
        query = f"""INSERT INTO {table}(first_name, last_name, password, username, status, gmail, address_id, payment_id) 
        VALUES('{self.first_name}', '{self.last_name}', '{self.password}', '{self.username}', '{self.status}', '{self.gmail}', {self.address_id}, {self.payment_id});"""
        return Database.connect(query, "INSERT")


class Product(Base):
    def __init__(self, name, price, rating):
        self.name = name
        self.price = float(price)
        self.rating = float(rating)

    def insert(self, table):
        query = f"""INSERT INTO {table}(name, price, rating) VALUES('{self.name}', {self.price}, {self.rating});"""
        return Database.connect(query, "INSERT")


class Category(Base):
    def __init__(self, title, description, create_date):
        self.title = title
        self.description = str(description)
        self.create_date = str(create_date)

    def insert(self, table):
        query = f"""INSERT INTO {table}(title, description, create_date) VALUES('{self.title}', '{self.description}', '{self.create_date}');"""
        return Database.connect(query, "INSERT")


class ProductCategory(Base):
    def __init__(self, product_id:int, category_id:int):
        self.product_id = product_id
        self.category_id = category_id

    def insert(self, table):
        query = f"""INSERT INTO {table}(product_id, category_id) VALUES({self.product_id}, {self.category_id});"""
        return Database.connect(query, "INSERT")


class ProductCustomer(Base):
    def __init__(self, product_id:int, customer_id:int, payment_id:int):
        self.product_id = int(product_id)
        self.customer_id = int(customer_id)
        self.payment_id = int(payment_id)

    def insert(self, table):
        query = f"""INSERT INTO {table}(product_id, customer_id, payment_id) VALUES( {self.product_id}, {self.customer_id}, {self.payment_id});"""
        return Database.connect(query, "INSERT")


class ProductOrder(Base):
    def __init__(self, product_customer_id:int, customer_id:int, order_product_count:int, total_price:float):
        self.product_customer_id = product_customer_id
        self.customer_id = customer_id
        self.order_product_count = int(order_product_count)
        self.total_price = float(total_price)

    def insert(self, table):
        query = f"""INSERT INTO {table}(product_customer_id, customer_id, order_product_count, total_price) 
        VALUES( {self.product_customer_id}, {self.customer_id}, {self.order_product_count}, {self.total_price});"""
        return Database.connect(query, "INSERT")


class Punk(Base):
    def __init__(self, name):
        self.name = name

    def insert(self, table):
        query = f"""INSERT INTO {table}(name) VALUES( '{self.name}');"""
        return Database.connect(query, "INSERT")
