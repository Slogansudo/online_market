import db_connect_2


def create_table():
    country = """
    CREATE TABLE country(
    country_id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    last_update TIMESTAMP DEFAULT now());"""

    city = """
       CREATE TABLE city(
       city_id SERIAL PRIMARY KEY,
       name VARCHAR(50),
       country_id INT REFERENCES country(country_id),
       last_update TIMESTAMP DEFAULT now());"""

    address = """
           CREATE TABLE address(
           address_id SERIAL PRIMARY KEY,
           name VARCHAR(50),
           city_id INT REFERENCES city(city_id),
           last_update TIMESTAMP DEFAULT now());"""

    payment_status = """
           CREATE TABLE payment_status(
           payment_status_id SERIAL PRIMARY KEY,
           status_pay BOOLEAN,
           last_update TIMESTAMP DEFAULT now());"""

    payment_type = """
           CREATE TABLE payment_type(
           payment_type_id SERIAL PRIMARY KEY,
           name VARCHAR(50),
           last_update TIMESTAMP DEFAULT now());"""

    payment = """
           CREATE TABLE payment(
           payment_id SERIAL PRIMARY KEY,
           amount FLOAT,
           payment_type_id INT REFERENCES payment_type(payment_type_id),
           payment_status_id INT REFERENCES payment_status(payment_status_id),
           last_update TIMESTAMP DEFAULT now());"""

    customer = """
           CREATE TABLE customer(
           customer_id SERIAL PRIMARY KEY,
           first_name VARCHAR(40),
           last_name VARCHAR(40),
           password VARCHAR(12),
           username VARCHAR(40),
           status VARCHAR(20),
           gmail VARCHAR(40),
           address_id INT REFERENCES address(address_id),
           payment_id INT REFERENCES payment(payment_id),
           last_update TIMESTAMP DEFAULT now());"""

    product = """
           CREATE TABLE product(
           product_id SERIAL PRIMARY KEY,
           name VARCHAR(50),
           price FLOAT,
           rating FLOAT NOT NULL, 
           last_update TIMESTAMP DEFAULT now());"""

    category = """
           CREATE TABLE category(
           category_id SERIAL PRIMARY KEY,
           title VARCHAR(50),
           description VARCHAR(50),
           last_update TIMESTAMP DEFAULT now(),
           create_date DATE DEFAULT now());"""

    product_category = """
           CREATE TABLE product_category(
           product_category_id SERIAL PRIMARY KEY,
           product_id INT REFERENCES product(product_id),
           category_id INT REFERENCES category(category_id),
           last_update TIMESTAMP DEFAULT now());"""

    product_customer = """CREATE TABLE product_customer(
           product_customer_id SERIAL PRIMARY KEY,
           product_id INT REFERENCES product(product_id),
           customer_id INT REFERENCES customer(customer_id),
           payment_id INT REFERENCES payment(payment_id),
           last_update TIMESTAMP DEFAULT now());"""

    product_order = """CREATE TABLE product_order(
           product_order_id SERIAL PRIMARY KEY,
           product_customer_id INT REFERENCES product_customer(product_customer_id),
           customer_id INT REFERENCES customer(customer_id),
           order_product_count INT,
           total_price FLOAT,
           last_update TIMESTAMP DEFAULT now());"""

    punk = """CREATE TABLE punk(
           punk_id SERIAL PRIMARY KEY,
           name VARCHAR(50),
           last_update TIMESTAMP DEFAULT now());"""

    data = {
        'country': country,
        'city': city,
        'address': address,
        'payment_status': payment_status,
        'payment_type': payment_type,
        'payment': payment,
        'customer': customer,
        'product': product,
        'category': category,
        'product_category': product_category,
        'product_customer': product_customer,
        'product_order': product_order,
        'punk': punk
    }
    for i in data:
        print(f"{i} {db_connect_2.Database.connect(data[i], 'create')}")
