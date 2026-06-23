import psycopg2

db_connect = psycopg2.connect(
    host="127.0.0.1",
    database="postgres",
    user="postgres",
    password="postgres",
    port="5432"
)

db_cursor = db_connect.cursor()

sql = """
CREATE TABLE IF NOT EXISTS public.users (
	user_id SERIAL,
	user_name VARCHAR(20) NULL,
	CONSTRAINT users_pk PRIMARY KEY (user_id)
);"""

db_cursor.execute(sql)
db_connect.commit()

sql_insert = """
INSERT INTO users (useruser_name) VALUES ('ahmet','ali');
"""

db_cursor.execute(sql_insert)
db_connect.commit()
  
db_connect.close()