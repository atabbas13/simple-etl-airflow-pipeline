# Load script
import psycopg2

def load(df):
    conn = psycopg2.connect(
        host="postgres",
        database="airflow",
        user="airflow",
        password="airflow"
    )
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id INT PRIMARY KEY,
            name TEXT,
            email TEXT,
            phone TEXT,
            website TEXT
        )
    """)
    
    for _, row in df.iterrows():
        cursor.execute("""
            INSERT INTO users (user_id, name, email, phone, website)
            VALUES (%s, %s, %s, %s, %s)
            ON CONFLICT (user_id) DO NOTHING
        """, tuple(row))

    conn.commit()
    cursor.close()
    conn.close()
