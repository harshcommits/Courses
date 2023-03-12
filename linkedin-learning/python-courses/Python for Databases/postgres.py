import psycopg2

connection = psycopg2.connect(database="red30",
                user="postgres",
                password="password",
                host="localhost",
                port="5432")

#grab the cursor for executing DB commands on postgresql
cursor = connection.cursor()


# cursor.execute('''CREATE TABLE Sales
#             (ORDER_NUM INT PRIMARY KEY,
#             ORDER_TYPE TEXT,
#             CUST_NAME TEXT,
#             PROD_NUMBER TEXT,
#             PROD_NAME TEXT,
#             QUANTITY INT,
#             PRICE REAL,
#             DISCOUNT REAL,
#             ORDER_TOTAL REAL);''')

#get 10 values
cursor.execute("SELECT * FROM sales LIMIT 10")
print(cursor.fetchall())

#insert values
cursor.execute('''
INSERT INTO SALES(ORDER_NUM, ORDER_TYPE, CUST_NAME, PROD_NUMBER, 
PROD_NAME, QUANTITY, PRICE, DISCOUNT, ORDER_TOTAL) VALUES
(1105910, 'Retail', 'Syman Mapstone', 'EB521',
'Understanding Artificial Intelligence', 3, 19.5, 0, 58.5)''')

connection.commit()

#query specific values
cursor.execute("SELECT CUST_NAME, ORDER_TOTAL from SALES WHERE ORDER_NUM=1105910")  
rows = cursor.fetchall()
for row in rows:
    print("CUST_NAME =", row[0])
    print("ORDER_TOTAL=", row[1],"\n")

connection.close()
