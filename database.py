import sqlite3 

def init_db():
    conn = sqlite3.connect("siem.db")
    c = conn.cursor()

    c.execute("""
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIAMRY KEY AUTOINCREMENT,
            timestamp TEXT,
            source TEXT, 
            event type TEXT,
            message TEXT,
            risk_score INTEGER
        )
    """)

    c.execute("""
        CREATE TABLE IF NOT EXISTS alerts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            rule_triggered TEXT,
            severity TEXT
        )
    """)

    conn.commit()
    conn.close()
