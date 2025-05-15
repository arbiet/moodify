import sqlite3

def get_moods():
    # Mengambil data mood dari database
    conn = sqlite3.connect('music_recommendation.db')
    cursor = conn.cursor()

    cursor.execute("SELECT id, name, image FROM mood")
    moods = cursor.fetchall()

    conn.close()

    # Mengembalikan data mood sebagai list of dict
    return [{"id": mood[0], "name": mood[1], "image": mood[2]} for mood in moods]

def get_songs_by_mood(mood_id):
    # Mengambil lagu berdasarkan mood dari database
    conn = sqlite3.connect('music_recommendation.db')
    cursor = conn.cursor()

    cursor.execute("SELECT name, artist, duration, image FROM song WHERE mood_id = ?", (mood_id,))
    songs = cursor.fetchall()

    conn.close()

    # Mengembalikan data lagu sebagai list of dict
    return [{"name": song[0], "artist": song[1], "duration": song[2], "image": song[3]} for song in songs]

def get_song_count_by_mood(mood_id):
    # Hitung jumlah lagu untuk mood tertentu
    conn = sqlite3.connect('music_recommendation.db')
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM song WHERE mood_id = ?", (mood_id,))
    count = cursor.fetchone()[0]

    conn.close()
    return count

def get_artist_count_by_mood(mood_id):
    # Hitung jumlah penyanyi unik untuk mood tertentu
    conn = sqlite3.connect('music_recommendation.db')
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(DISTINCT artist) FROM song WHERE mood_id = ?", (mood_id,))
    count = cursor.fetchone()[0]

    conn.close()
    return count