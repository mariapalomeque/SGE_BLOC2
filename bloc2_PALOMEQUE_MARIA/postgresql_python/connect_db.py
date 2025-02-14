import psycopg2
    def connection_db(): 1 usage new.
    conn = psycopg2.connect(
    database="the_bear",
    password="maria2003",
    user="maria",
    host="localhost",
    port="5432"
)

return conn