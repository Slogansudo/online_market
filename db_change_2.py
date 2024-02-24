
import classes_db_2
import db_connect_2
import main


def country():
    ask = input("""country table
    1. INSERT
    2. DELETE
    3. UPDATE
    4. SELECT
    5. BACK
    >>>  """)
    if ask == "1":
        name = (input("insert country name: "))
        result = classes_db_2.Country(name)
        print(result.insert())
        return country()
    elif ask == '2':
        name = input("insert country name: ")
        country_id = int(input("insert country_id: "))
        result = classes_db_2.Country(name)
        print(result.delete(country_id))
        return country()
    elif ask == '3':
        query = input("""qaysi malumotni yangilashni hohlaysiz:
            1. country_id
            2. country_name
            >>> """)
        if query == '1':
            result = classes_db_2.Country.get_id()
            for i in result:
                print(i[0])
            print('yuqoridagi idlarni tanlash mumkin emas')
            old_id = int(input('eski country_id ni kiriting: '))
            new_id = int(input('yangi id ni kiriting: '))
            natija = classes_db_2.Country.update_id(old_id, new_id)
            print(natija)
            return country()
        elif query == "2":
            name = input("insert country name: ")
            country_id = int(input("insert country_id: "))
            result = classes_db_2.Country(name)
            print(result.update(country_id))
            return country()
        else:
            print('invalid input')
            return country()
    elif ask == '4':
        ask = input("""
            1. all data
            2. conditional search
            >>>> """)
        if ask == '1':
            data = classes_db_2.Country.select('SELECT')
            for row in data:
                print(row)
            return country()
        elif ask == '2':
            ask_1 = input("""qaysi shart bo'yicha qidirmoqchisiz 
            1. country_id
            2. name
            3. search with all conditions
            4. ORDER by
            5. search by letter
            >>>>""")
            if ask_1 == '1':
                id = int(input('insert country_id: '))
                quer = f"""SELECT * FROM country WHERE country_id={id} ORDER BY country_id;"""
                result = classes_db_2.Country.select(quer)
                for row in result:
                    print(row)
                return country()
            elif ask_1 == '2':
                name = input('insert name: ')
                quer = f"""SELECT * FROM country WHERE name='{name}' ORDER BY country_id;"""
                result = classes_db_2.Country.select(quer)
                for i in result:
                    print(i)
                return country()
            elif ask_1 == '3':
                id = int(input('insert country_id: '))
                name = input('insert name: ')
                quer = f"""SELECT * FROM country WHERE country_id={id} and name='{name}' ORDER BY country_id;"""
                result = classes_db_2.Country.select(quer)
                for i in result:
                    print(i)
                return country()
            elif ask_1 == "4":
                quer = f"""SELECT * FROM country ORDER BY country_id;"""
                result = classes_db_2.Country.select(quer)
                for i in result:
                    print(i)
                return country()
            elif ask_1 == "5":
                letter = input('Enter the letter in the text you are looking for: ')
                quer = f"""SELECT * FROM country WHERE name LIKE '%{letter}%';"""
                result = classes_db_2.Country.select(quer)
                for i in result:
                    print(i)
                return country()
            else:
                print('ERROR')
                return country()
        else:
            print('ERROR')
            return country()
    elif ask == '5':
        return main.main()
    else:
        print('ERROR ')
        return country()



def city():
    ask = input("""city table
    1. INSERT
    2. DELETE
    3. UPDATE
    4. SELECT
    5. BACK
    >>>  """)
    if ask == '1':
        name = input('insert name: ')
        data = classes_db_2.Country.get_id()
        print('mavjud country_idlar>>')
        for i in data:
            print(i[0])
        country_id = int(input('insert country_id: '))
        result = classes_db_2.City(name)
        print(result.insert(country_id))
        return city()
    elif ask == '2':
        name = input('insert name: ')
        city_id = int(input('insert city_id: '))
        result = classes_db_2.City(name)
        print(result.delete(city_id, 'city', 'city_id'))
        return city()
    elif ask == '3':
        name = input('insert name: ')
        city_id = int(input('insert city_id: '))
        result = classes_db_2.City(name)
        print(result.update(city_id, 'city', 'city_id'))
        return city()
    elif ask == '4':
        query = input(""" qaysi shart bo'yicha qidirmoqchisiz
        1. all data
        2. city_id
        3. country_id
        4. name
        5. search by letter
        6. ORDER by
        >>> """)
        if query == '1':
            result = classes_db_2.City.select('SELECT', 'city')
            for i in result:
                print(i)
            return city()
        elif query == '2':
            city_id = int(input('insert city_id: '))
            query_2 =f"""SELECT*FROM city WHERE city_id = {city_id}"""
            result = classes_db_2.City.select(query_2, 'city')
            for i in result:
                print(i)
            return city()
        elif query == '3':
            country_id = int(input('insert country_id: '))
            query_2 = f"""SELECT*FROM city WHERE country_id = {country_id}"""
            result = classes_db_2.Country.select(query_2, 'city')
            for i in result:
                print(i)
            return city()
        elif query == '4':
            name = input('insert name: ')
            query_2 = f"""SELECT*FROM city WHERE name = '{name}'"""
            result = classes_db_2.City.select(query_2, 'city')
            for i in result:
                print(i)
            return city()
        elif query == '5':
            search = input('Enter the letter in the text you are looking for: ')
            query_2 = f"""SELECT*FROM city WHERE name LIKE '%{search}%'"""
            result = classes_db_2.City.select(query_2, 'city')
            for i in result:
                print(i)
            return city()
        elif query == '6':
            query_2 = f"""SELECT * FROM city ORDER BY city_id"""
            result = classes_db_2.City.select(query_2, 'city')
            for i in result:
                print(i)
            return city()
        else:
            print('Invalid')
            return city()
    elif ask == '5':
        return main.main()
    else:
        print('Invalid')
        return city()


# ADDRESS PAGE
def address():
    ask = input("""address table
    1. INSERT
    2. DELETE
    3. UPDATE
    4. SELECT
    5. BACK
    >>>  """)
    if ask == "1":
        name = input('insert name: ')
        result = classes_db_2.Address(name)
        data = classes_db_2.Country.get_id('city', 'city_id')
        for i in data:
            print(i[0])
        print('mavjud city_id lar ')
        city_id = input('insert city_id: ')
        print(result.insert(city_id))
        return address()
    elif ask == '2':
        name = input('insert name: ')
        address_id = input('insert address_id: ')
        result = classes_db_2.Address(name)
        print(result.delete(address_id, 'address', 'address_id'))
        return address()
    elif ask == '3':
        query = input("""qaysi malumotni yangilashni hohlaysiz:
        1. address_id
        2. address_name
        3. city_id
        >>> """)
        if query == '1':
            result_1 = classes_db_2.Country.get_id('address', 'address_id')
            for j in result_1:
                print(j[0])
            print('yuqoridagi idlarni tanlash mumkin emas')
            old_id = int(input('eski address_id ni kiriting: '))
            new_id = int(input('yangi id ni kiriting: '))
            natija = classes_db_2.Address.update_id(old_id, new_id, 'address_id', 'address')
            print(natija)
            return address()
        elif query == '2':
            name = input('insert name: ')
            address_id = int(input('insert address_id: '))
            result = classes_db_2.Address(name)
            print(result.update(address_id, 'address', 'address_id'))
            return address()
        elif query == '3':
            print('mavjud city_id lar>>>')
            data = classes_db_2.Country.get_id('city', 'city_id')
            for i in data:
                print(i[0])
            city_id_1 = input('insert old city_id: ')
            city_id_2 = input('insert new city_id: ')
            print(classes_db_2.Address.update_id(city_id_1, city_id_2, 'city_id', 'address'))
            return address()
        else:
            print('ERROR')
            return address()
    elif ask == '4':
        query = input("""
        1. all data
        2. conditional search
        >>> """)
        if query == '1':
            result_1 = classes_db_2.Address.select('SELECT', 'address')
            for i in result_1:
                print(i)
            return address()
        elif query == '2':
            query_2 = input("""
            1. search by city_id 
            2. search by name
            3. search by address_id
            4. Order by
            5. Search by letter
            >>>>> """)
            if query_2 == '1':
                city_id = input('insert city_id: ')
                query_x = f"""SELECT * FROM address WHERE city_id = {city_id};"""
                result = classes_db_2.Address.select(query_x, 'address')
                for i in result:
                    print(i)
                return address()
            elif query_2 == '2':
                name = input('insert name: ')
                query_x = f"""SELECT * FROM address WHERE name = '{name}';"""
                result = classes_db_2.Address.select(query_x, 'address')
                for i in result:
                    print(i)
                return address()
            elif query_2 == '3':
                address_id = input('insert address_id: ')
                query_x = f"""SELECT * FROM address WHERE address_id = {address_id};"""
                result = classes_db_2.Address.select(query_x, 'address')
                for i in result:
                    print(i)
                return address()
            elif query_2 == '4':
                query_x = f"""SELECT * FROM address ORDER BY address_id;"""
                result = classes_db_2.Address.select(query_x, 'address')
                for i in result:
                    print(i)
                return address()
            elif query_2 == '5':
                letter = input('insert letter: ')
                query_x = f"""SELECT * FROM address WHERE name LIKE '%{letter}%';"""
                result = classes_db_2.Address.select(query_x, 'address')
                for i in result:
                    print(i)
                return address()
            else:
                print('Invalid')
                return address()
        else:
            print('Invalid')
            return address()
    elif ask == '5':
        return main.main()
    else:
        print('Invalid')
        return address()


def payment_status():
    ask = input("""payment_status table
     1. INSERT
     2. DELETE
     3. UPDATE
     4. SELECT
     5. BACK
     >>>  """)

    if ask == '1':
        status_pay = bool(input('insert status_pay(True or False): '))
        data = classes_db_2.PaymentStatus(status_pay)
        print(data.insert('payment_status'))
        return payment_status()
    elif ask == '2':
        column = input('insert column name: ')
        if column == 'payment_status_id':
            search_data = int(input('insert search data: '))
        else:
            search_data = bool(input('insert search data: '))
        print(classes_db_2.PaymentStatus.delete(column, search_data, 'payment_status'))
        return payment_status()
    elif ask == '3':
        search_id = input('insert payment_status_id: ')
        column = input('insert column name: ')
        if column == 'payment_status_id':
            search_data = int(input('insert search data: '))
        else:
            search_data = bool(input('insert search data: '))
        print(classes_db_2.PaymentStatus.update(search_id, column, search_data, 'payment_status', 'payment_status_id'))
        return payment_status()
    elif ask == '4':
        data = classes_db_2.PaymentStatus.select('payment_status')
        for i in data:
            print(i)
        return payment_status()
    elif ask == '5':
        return main.main()
    else:
        print('Invalid')
        return payment_status()


def payment_type():
    ask = input("""payment_type table
     1. INSERT
     2. DELETE
     3. UPDATE
     4. SELECT
     5. BACK
     >>>  """)

    if ask == '1':
        name = input('insert name(card or cash): ')
        data = classes_db_2.PaymentType(name)
        print(data.insert('payment_type'))
        return payment_type()
    elif ask == '2':
        column = input('insert column name: ')
        if column == 'payment_type_id':
            search_data = int(input('insert search data: '))
        else:
            search_data = input('insert search data: ')
        print(classes_db_2.PaymentType.delete(column, search_data, 'payment_type'))
        return payment_type()
    elif ask == '3':
        search_id = input('insert payment_type_id: ')
        column = input('insert column name: ')
        if column == 'payment_type_id':
            new_data = int(input('insert new data: '))
        else:
            new_data = input('insert new data: ')
        print(classes_db_2.PaymentType.update(search_id, column, new_data, 'payment_type', 'payment_type_id'))
        return payment_type()
    elif ask == '4':
        data_x = classes_db_2.PaymentType.select('payment_type')
        for i in data_x:
            print(i)
        return payment_type()
    elif ask == '5':
        return main.main()
    else:
        print('Invalid')
        return payment_type()


def payment():
    ask = input("""payment table
     1. INSERT
     2. DELETE
     3. UPDATE
     4. SELECT
     5. BACK
     >>>  """)

    if ask == '1':
        amount = float(input('insert new amount: '))
        payment_type_id = int(input('insert  payment_type_id: '))
        payment_status_id = int(input('insert payment status id: '))
        data = classes_db_2.Payment(amount, payment_type_id, payment_status_id)
        print(data.insert('payment'))
        return payment()
    elif ask == '2':
        column = input('insert column name: ')
        if column == 'amount':
            search_data = float(input('insert search amount: '))
        else:
            search_data = int(input('insert search amount: '))
        print(classes_db_2.Payment.delete(column, search_data, 'payment'))
        return payment()
    elif ask == '3':
        id = input('insert payment_id: ')
        column = input('insert column name: ')
        if column == 'amount':
            new_data = float(input('insert new data: '))
        else:
            new_data = int(input('insert new data: '))
        print(classes_db_2.Payment.update(id, column, new_data, 'payment', 'payment_id'))
        return payment()
    elif ask == '4':
        data = classes_db_2.Payment.select('payment')
        for i in data:
            print(i)
        return payment()
    elif ask == '5':
        return main.main()
    else:
        print('Invalid')
        return payment()


def customer():
    ask = input("""customer table
     1. INSERT
     2. DELETE
     3. UPDATE
     4. SELECT
     5. BACK
     >>>  """)

    if ask == '1':
        first_name = input('insert first name: ')
        last_name = input('insert last_name: ')
        password = input('insert password: ')
        username = input('insert username: ')
        status = 'customer'
        gmail = input('insert gmail: ')
        address_id = int(input('insert address_id: '))
        payment_id = int(input('insert payment_id: '))
        data = classes_db_2.Customer(first_name, last_name, password, username, status, gmail, address_id, payment_id)
        print(data.insert('customer'))
        return customer()
    elif ask == '2':
        column = input('insert column name: ')
        if column == 'address_id' or column == 'payment_id' or column == 'customer_id':
            search_data = int(input('insert search_data: '))
        else:
            search_data = input('insert search_data: ')
        print(classes_db_2.Customer.delete(column, search_data, 'customer'))
        return customer()
    elif ask == '3':
        search_id = int(input('insert customer_id: '))
        column = input('insert column name: ')
        if column == 'address_id' or column == 'payment_id' or column == 'customer_id':
            new_data = int(input('insert new data : '))
        else:
            new_data = input('insert new data: ')
        print(classes_db_2.Customer.update(search_id, column, new_data, 'customer', 'customer_id'))
        return customer()
    elif ask == '4':
        data = classes_db_2.Customer.select('customer')
        for i in data:
            print(i)
        return customer()
    elif ask == '5':
        return main.main()
    else:
        print('Invalid')
        return customer()


def product():
    ask = input("""product table
     1. INSERT
     2. DELETE
     3. UPDATE
     4. SELECT
     5. BACK
     >>>  """)

    if ask == '1':
        name = input('insert product name: ')
        price = float(input('insert product price: '))
        rating = float(input('insert rating: '))
        data = classes_db_2.Product(name, price, rating)
        print(data.insert('product'))
        return product()
    elif ask == '2':
        column = input('insert column name: ')
        if column == 'product_id':
            search_data = int(input('insert search data : '))
        else:
            search_data = input('insert search: ')
        print(classes_db_2.Product.delete(column, search_data, 'product'))
        return product()
    elif ask == '3':
        search_id = int(input('insert product_id : '))
        column = input('insert column name: ')
        if column == 'product_id':
            new_data = int(input('insert new data: '))
        else:
            new_data = input('insert new data: ')
        print(classes_db_2.Product.update(search_id, column, new_data, 'product', 'product_id'))
        return product()
    elif ask == '4':
        data = classes_db_2.Product.select('product')
        for i in data:
            print(i)
        return product()
    elif ask == '5':
        return main.main()
    else:
        print('Invalid')
        return product()


def category():
    ask = input("""category table
     1. INSERT
     2. DELETE
     3. UPDATE
     4. SELECT
     5. BACK
     >>>  """)

    if ask == '1':
        title = input('insert category title: ')
        description = input('insert category description: ')
        create_date = input('insert create_date: ')
        data = classes_db_2.Category(title, description, create_date)
        print(data.insert('category'))
        return category()
    elif ask == '2':
        column = input('insert column name: ')
        if column == 'category_id':
            search_data = int(input('insert search_data: '))
        else:
            search_data = input('insert search_data: ')
        print(classes_db_2.Category.delete(column, search_data, 'category'))
        return category()
    elif ask == '3':
        search_id = int(input('insert category_id: '))
        column = input('insert column name: ')
        if column == 'category_id':
            new_data = int(input('insert new data: '))
        else:
            new_data = input('insert new data: ')
        print(classes_db_2.Category.update(search_id, column, new_data, 'category', 'category_id'))
        return category()
    elif ask == '4':
        data = classes_db_2.Category.select('category')
        for i in data:
            print(i)
        return category()
    elif ask == '5':
        return main.main()
    else:
        print('Invalid')
        return category()


def product_category():
    ask = input("""product_category table
     1. INSERT
     2. DELETE
     3. UPDATE
     4. SELECT
     5. BACK
     >>>  """)

    if ask == '1':
        product_id = int(input('insert product_id: '))
        category_id = int(input('insert category_id: '))
        data = classes_db_2.ProductCategory(product_id, category_id)
        print(data.insert('product_category'))
        return product_category()
    elif ask == '2':
        column = input('insert column name: ')
        search_data = int(input('insert search data: '))
        data = classes_db_2.ProductCategory.delete(column, search_data, 'product_category')
        print(data)
        return product_category()
    elif ask == '3':
        search_id = int(input('insert product_category_id: '))
        column = input('insert column name: ')
        new_data = int(input('insert new data: '))
        print(classes_db_2.ProductCategory.update(search_id, column, new_data, 'product_category', 'product_category_id'))
        return product_category()
    elif ask == '4':
        data = classes_db_2.ProductCategory.select('product_category')
        for i in data:
            print(i)
        return product_category()
    elif ask == '5':
        return main.main()
    else:
        print('Invalid')
        return product_category()


def product_customer():
    ask = input("""product_customer table
     1. INSERT
     2. DELETE
     3. UPDATE
     4. SELECT
     5. BACK
     >>>  """)

    if ask == '1':
        product_id = int(input('insert product_id: '))
        customer_id = int(input('insert customer id: '))
        payment_id = int(input('insert payment id: '))
        data = classes_db_2.ProductCustomer(product_id, customer_id, payment_id)
        print(data.insert('product_customer'))
        return product_customer()
    elif ask == '2':
        column = input('insert column name: ')
        search_data = int(input('insert search_data: '))
        print(classes_db_2.ProductCustomer.delete(column, search_data, 'product_customer'))
        return product_customer()
    elif ask == '3':
        search_id = int(input('insert product_customer_id: '))
        column = input('insert column name: ')
        new_data = int(input('insert new data: '))
        print(classes_db_2.ProductCustomer.update(search_id, column, new_data, 'product_customer', 'product_customer_id'))
        return product_customer()
    elif ask == '4':
        data = classes_db_2.ProductCustomer.select('product_customer')
        for i in data:
            print(i)
        return product_customer()
    elif ask == '5':
        return main.main()
    else:
        print('Invalid')
        return product_customer()


def product_order():
    ask = input("""product_order table
     1. INSERT
     2. DELETE
     3. UPDATE
     4. SELECT
     5. BACK
     >>>  """)

    if ask == '1':
        product_customer_id = int(input('insert product customer id: '))
        customer_id = int(input('insert customer id: '))
        order_product_count = int(input('insert order product count: '))
        total_price = float(input('insert total price: '))
        data = classes_db_2.ProductOrder(product_customer_id, customer_id, order_product_count, total_price)
        print(data.insert('product_order'))
        return product_order()
    elif ask == '2':
        column = input('insert column name: ')
        if column == 'total_price':
            search_data = float(input('insert search_data: '))
        else:
            search_data = int(input('insert search_data: '))
        print(classes_db_2.ProductOrder.delete(column, search_data, 'product_order'))
        return product_order()
    elif ask == '3':
        search_id = int(input('insert product order ID: '))
        column = input('insert column name: ')
        if column == 'total_price':
            new_data = float(input('insert new data: '))
        else:
            new_data = int(input('insert new data: '))
        print(classes_db_2.ProductOrder.update(search_id, column, new_data, 'product_order', 'product_order_id'))
        return product_order()
    elif ask == '4':
        data = classes_db_2.ProductOrder.select('product_order')
        for row in data:
            print(row)
        return product_order()
    elif ask == '5':
        return main.main()
    else:
        print('Invalid')
        return product_order()


def punk():
    ask = input("""punk table
     1. INSERT
     2. DELETE
     3. UPDATE
     4. SELECT
     5. BACK
     >>>  """)

    if ask == '1':
        name = input('insert name: ')
        data = classes_db_2.Punk(name)
        print(data.insert('punk'))
        return punk()
    elif ask == '2':
        column = input('insert column name: ')
        if column == 'punk_id':
            search_data = int(input('insert search_data: '))
        else:
            search_data = input('insert search_data: ')
        print(classes_db_2.Punk.delete(column, search_data, 'punk'))
        return punk()
    elif ask == '3':
        search_id = int(input('insert punk_id: '))
        column = input('insert column name: ')
        if column == 'punk_id':
            new_data = int(input('insert new data: '))
        else:
            new_data = input('insert new data: ')
        print(classes_db_2.Punk.update(search_id, column, new_data, 'punk', 'punk_id'))
        return punk()
    elif ask == '4':
        data = classes_db_2.Punk.select('punk')
        for row in data:
            print(row)
        return punk()
    elif ask == '5':
        return main.main()
    else:
        print('Invalid')
        return punk()