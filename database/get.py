def get_moods_from_db():
    conn = sqlite3.connect('music_recommendation.db')
    cursor = conn.cursor()

    # Ambil semua data mood
    cursor.execute("SELECT * FROM mood")
    moods = cursor.fetchall()

    conn.close()
    return moods

def get_songs_by_mood(mood_id):
    conn = sqlite3.connect('music_recommendation.db')
    cursor = conn.cursor()

    # Ambil semua lagu berdasarkan mood_id
    cursor.execute("SELECT * FROM song WHERE mood_id = ?", (mood_id,))
    songs = cursor.fetchall()

    conn.close()
    return songs
