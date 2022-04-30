import psycopg2

connection = psycopg2.connect(database="red30",
                user="postgres",
                password="password",
                host="localhost",
                port="5432")

#grab the cursor for executing DB commands on postgresql
cursor = connection.cursor()

cursor.execute('''CREATE TABLE Sales
            (ORDER_NUM INT PRIMARY KEY,
            ORDER_TYPE TEXT,
            CUST_NAME TEXT,
            PROD_NUMBER TEXT,
            PROD_NAME TEXT,
            QUANTITY INT,
            PRICE REAL,
            DISCOUNT REAL,
            ORDER_TOTAL REAL);''')

connection.commit()
connection.close()
