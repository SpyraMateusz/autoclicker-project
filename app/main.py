from fastapi import FastAPI
from pydantic import BaseModel
import psycopg2
import os

app = FastAPI(title="Autoclicker API")

DB_HOST = os.environ.get("POSTGRES_HOST", "db")
DB_NAME = os.environ.get("POSTGRES_DB", "autoclicker")
DB_USER = os.environ.get("POSTGRES_USER", "user")
DB_PASSWORD = os.environ.get("POSTGRES_PASSWORD", "password")

def get_connection():
    return psycopg2.connect(
        host=DB_HOST, dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD
    )

def init_db():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS clicks (
            id SERIAL PRIMARY KEY,
            count INTEGER NOT NULL
        );
    """)
    cur.execute("INSERT INTO clicks (count) SELECT 0 WHERE NOT EXISTS (SELECT * FROM clicks);")
    conn.commit()
    cur.close()
    conn.close()

init_db()

@app.post("/click")
def click():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("UPDATE clicks SET count = count + 1 WHERE id = 1;")
    conn.commit()
    cur.execute("SELECT count FROM clicks WHERE id = 1;")
    current_count = cur.fetchone()[0]
    cur.close()
    conn.close()
    return {"clicks": current_count}

@app.get("/status")
def status():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT count FROM clicks WHERE id = 1;")
    current_count = cur.fetchone()[0]
    cur.close()
    conn.close()
    return {"clicks": current_count}