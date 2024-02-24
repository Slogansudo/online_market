import db_change_2


def main():
    ask = input("""main page
        1. country              8. product
        2. city                 9. category
        3. address              10. product_category
        4. payment_status       11. product_customer
        5. payment_type         12. product_order
        6. payment              13. punk
        7. customer
        >>>> """)
    if ask == '1':
        return db_change_2.country()
    elif ask == '2':
        return db_change_2.city()
    elif ask == '3':
        return db_change_2.address()
    elif ask == '4':
        return db_change_2.payment_status()
    elif ask == '5':
        return db_change_2.payment_type()
    elif ask == '6':
        return db_change_2.payment()
    elif ask == '7':
        return db_change_2.customer()
    elif ask == '8':
        return db_change_2.product()
    elif ask == '9':
        return db_change_2.category()
    elif ask == '10':
        return db_change_2.product_category()
    elif ask == '11':
        return db_change_2.product_customer()
    elif ask == '12':
        return db_change_2.product_order()
    elif ask == '13':
        return db_change_2.punk()
    else:
        print("invalid input")
        return main()


if __name__ == '__main__':
    main()
