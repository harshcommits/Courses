import psycopg2

def insert_sale(conn, order_num, order_type, cust_name, prod_number, prod_name, 
                quantity, price, discount, order_total):
    order_total = quantity * price
    if discount != 0:
        order_total = order_total * discount
    sales_data = (order_num, order_type, cust_name, prod_number, prod_name, 
                quantity, price, discount, order_total)
    cursor = conn.cursor()

    cursor.execute('''INSERT INTO SALES(ORDER_NUM, ORDER_TYPE, CUST_NAME, PROD_NUMBER, 
                    PROD_NAME, QUANTITY, PRICE, DISCOUNT, ORDER_TOTAL) VALUES
                    (%s, %s, %s, %s, %s, %s, %s, %s, %s)''', sales_data)

    conn.commit()

    cursor.execute('''SELECT CUST_NAME, ORDER_TOTAL FROM SALES WHERE ORDER_NUM=%s;''', (order_num,))

    rows = cursor.fetchall()
    for row in rows:
        print("CUST_NAME = ", row[0])
        print("ORDER_TOTAL = ", row[1], "\n")



if __name__ == "__main__":
    conn = psycopg2.connect(database="red30", 
                    user="postgres", 
                    password="password",
                    host="localhost",
                    port="5432")

    order_num = int(input("Enter Order Number"))
    order_type = int(input("Enter Order Type"))
    cust_name = int(input("Enter Customer Name"))
    prod_number = int(input("Enter Product Number"))
    prod_name = int(input("Enter Product Name"))
    price = int(input("Enter Price"))
    discount = int(input("Enter Discount"))

    insert_sale(conn)
    print("Data inserted")

    conn.close()