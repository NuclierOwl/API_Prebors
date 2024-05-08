import psycopg2

def connect_to_db():
    conn = psycopg2.connect(
        host="193.176.78.35",
        database="postgres",
        user="user46",
        password="y1f20",
        port="5433"
    )
    return conn
