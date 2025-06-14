import sqlite3

DB = "/data/events.db"
conn = sqlite3.connect(DB)
cur = conn.cursor()
cur.execute("""
    CREATE TABLE IF NOT EXISTS events (
      device_id   TEXT,
      event_id    TEXT,
      timestamp   TEXT,
      salt        TEXT,
      hash_value  TEXT
    )
""")

with open("/data/events.log") as f:
    for line in f:
        parts = [p.strip() for p in line.split("|")]
        if len(parts) == 5:
            cur.execute(
                "INSERT INTO events VALUES (?, ?, ?, ?, ?)",
                parts
            )

conn.commit()
conn.close()
print("Załadowano dane do", DB)
