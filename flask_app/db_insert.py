import sqlite3

conn = sqlite3.connect("users.db")
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT,
    role TEXT,
    bio TEXT
)
""")


c.execute("INSERT OR IGNORE INTO users VALUES (1, 'admin', 'flag{g00d_j0b_1337}', 'admin', 'System administrator')")
c.execute("INSERT OR IGNORE INTO users VALUES (2, 'rowlet', 'studeNt3', 'user', 'I love birds!')")
c.execute("INSERT OR IGNORE INTO users VALUES (3, 'bob', 'n5Jl47O_oQM9N', 'user', 'I once tried to high-five a statue. It did not go well.')")
c.execute("INSERT OR IGNORE INTO users VALUES (4, 'alice', '0z6*E5q5Wh!*9m9', 'user', 'I believe sandwiches taste better when cut diagonally.')")
c.execute("INSERT OR IGNORE INTO users VALUES (5, 'anne', 'unguessabL3_Pa5s', 'user', 'I am a CTF beginner!')")
c.execute("INSERT OR IGNORE INTO users VALUES (6, 'marlin', 'MyPassword123', 'user', 'I believe leftovers taste better at midnight.')")
c.execute("INSERT OR IGNORE INTO users VALUES (7, 'ash', 'sUp3r_H4rd_to_g4355', 'user', 'I can not dance, but I absolutely will.')")
c.execute("INSERT OR IGNORE INTO users VALUES (8, 'tina', 'zFJ4ZyL}d?#3:54N', 'user', 'I laugh at my own jokes because someone has to.')")
c.execute("INSERT OR IGNORE INTO users VALUES (9, 'ludwig', 'W2p=8<fGo55?3', 'user', 'I talk to plants and they sometimes listen.')")
c.execute("INSERT OR IGNORE INTO users VALUES (10, 'felix', 'VxsS2anf6y982c', 'user', 'I like trains...')")

conn.commit()
conn.close()