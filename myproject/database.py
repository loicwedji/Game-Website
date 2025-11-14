import psycopg2

conn = psycopg2.connect(host ="localhost",dbname="SnakeDB", user="postgres",password="1234",port=6767)
print("We connected successfully")
cur = conn.cursor()
cur.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")
conn.commit()
cur.close()
conn.close()


   


