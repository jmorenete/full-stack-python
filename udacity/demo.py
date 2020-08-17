import psycopg2

conn = psycopg2.connect('dbname=library')

#to queue up work for a transaction, we need to interact with a coursor
cursor = conn.cursor()

cursor.execute('DROP TABLE IF EXISTS staff')

cursor.execute('''
    CREATE TABLE staff (
        id INTEGER PRIMARY KEY,
        name VARCHAR NOT NULL,
        on_holiday BOOLEAN NOT NULL DEFAULT False
    );
''')
SQL = 'INSERT INTO staff (id, name, on_holiday) VALUES (%(id)s, %(name)s, %(on_holiday)s);'
data = {
    'id': 2,
    'name': 'Jose',
    'on_holiday': False
}
cursor.execute('INSERT INTO staff (id, name, on_holiday) VALUES (%s, %s, %s);', (1, 'Josefina', True))
cursor.execute(SQL, data)
cursor.execute('SELECT * FROM staff;')

result = cursor.fetchall()

print(result)

conn.commit()
cursor.close()
conn.close()
