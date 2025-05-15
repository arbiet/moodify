import sqlite3

def create_database():
    # Koneksi ke database (akan membuat file database jika belum ada)
    conn = sqlite3.connect('music_recommendation.db')
    cursor = conn.cursor()

    # Buat tabel 'mood'
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS mood (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        image TEXT
    )
    ''')

    # Buat tabel 'song' dengan foreign key ke tabel 'mood'
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS song (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        artist TEXT NOT NULL,
        duration TEXT NOT NULL,
        image TEXT,
        mood_id INTEGER,
        FOREIGN KEY (mood_id) REFERENCES mood(id)
    )
    ''')

    # Commit perubahan dan tutup koneksi
    conn.commit()
    conn.close()

# Panggil fungsi untuk membuat database dan tabel
create_database()
