import sqlite3
import random

def insert_data():
    conn = sqlite3.connect('music_recommendation.db')
    cursor = conn.cursor()

    # Data mood
    moods = [
        ('Sedih', '[Gambar Album Sedih]'),
        ('Gembira', '[Gambar Album Gembira]'),
        ('Tenang', '[Gambar Album Tenang]'),
        ('Bersemangat', '[Gambar Album Bersemangat]'),
        ('Romantis', '[Gambar Album Romantis]'),
        ('Santai', '[Gambar Album Santai]'),
        ('Galau', '[Gambar Album Galau]')
    ]

    # Masukkan mood
    mood_ids = {}
    for mood in moods:
        cursor.execute("INSERT INTO mood (name, image) VALUES (?, ?)", (mood[0], mood[1]))
        mood_id = cursor.lastrowid  # Dapatkan id dari mood yang baru dimasukkan
        mood_ids[mood[0]] = mood_id

    # Generate dummy data lagu untuk setiap mood
    def generate_song_data(mood_name, mood_id, num_songs):
        songs = []
        for i in range(1, num_songs + 1):
            name = f"Lagu {mood_name} {i}"
            artist = f"Penyanyi {mood_name} {i}"
            duration = f"{random.randint(2, 5)}:{random.randint(0, 59):02d}"  # Durasi acak antara 2:00 - 5:59
            image = f"[Gambar Lagu {mood_name} {i}]"
            songs.append((name, artist, duration, image, mood_id))
        return songs

    # Masukkan lagu ke dalam database untuk setiap mood
    for mood_name, mood_id in mood_ids.items():
        num_songs = random.randint(40, 50)  # Lagu antara 40-50 per mood
        songs = generate_song_data(mood_name, mood_id, num_songs)
        cursor.executemany("INSERT INTO song (name, artist, duration, image, mood_id) VALUES (?, ?, ?, ?, ?)", songs)

    # Commit perubahan dan tutup koneksi
    conn.commit()
    conn.close()

# Panggil fungsi untuk memasukkan data
insert_data()
