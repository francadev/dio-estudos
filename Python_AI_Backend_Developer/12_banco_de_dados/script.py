import psycopg2
import psycopg2.extras

db = psycopg2.connect("dbname=dio_estudos user=postgres password=")
cur = db.cursor(cursor_factory=psycopg2.extras.DictCursor)
cur.execute("SELECT * FROM usuarios WHERE id = 1")

# procura por todos
records = cur.fetchall()

for record in records:
    print(dict(record))

# procura por dois registros
# records = cur.fetchmany(size=2)
# print(records)

db.commit()
cur.close()
