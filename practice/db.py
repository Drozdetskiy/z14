import psycopg2

connection = psycopg2.connect(
    dsn='postgres://z14:3778952@localhost:5432/db_z14'
)

cursor = connection.cursor()

cursor.execute("SELECT * FROM customer;")

result = cursor.fetchall()
print(result)

items = []
for i in range(100):
    user_name = f'User_{i}'
    email = f'email{i}@gmail.com'
    items.append(f"('{user_name}', '{email}')")

cursor.execute(f'''
INSERT INTO customer (name, email) VALUES {','.join(items)};
''')
connection.commit()
cursor.execute("SELECT * FROM customer;")
result = cursor.fetchall()
print(result)
connection.close()