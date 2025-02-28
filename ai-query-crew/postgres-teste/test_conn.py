from postgres_connection import PostgresConnection  # Certifique-se de que está importando a conexão corretamente
from postgres_databases import PostgresDatabases
from psycopg2 import sql

ecommerce_database = PostgresDatabases.ECOMMERCE

conn = PostgresConnection(database_uri=ecommerce_database)
conn.connect()

print(conn.get_current_database())

cursor = conn.cursor

sql_query ='SELECT * from "categorias";'

cursor.execute(sql_query)

# Obtendo os resultados
results = cursor.fetchall()

print(results)

i=0