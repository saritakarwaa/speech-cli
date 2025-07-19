import sqlite3, json, time

DB = "history.db"
def init_db():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS sessions(
                   id INTEGER PRIMARY KEY,
                   ts REAL,
                   audio TEXT,
                   metrics TEXT)""")
    conn.commit(); conn.close()

def save_session(audio_path: str, metrics: dict):
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("INSERT INTO sessions(ts,audio,metrics) VALUES(?,?,?)",
              (time.time(), audio_path, json.dumps(metrics)))
    conn.commit(); conn.close()

def get_last(n=5):
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("SELECT ts,audio,metrics FROM sessions ORDER BY id DESC LIMIT ?", (n,))
    rows = c.fetchall()
    conn.close()
    return [{
        "timestamp": r[0],
        "audio": r[1],
        **json.loads(r[2])
    } for r in rows]
