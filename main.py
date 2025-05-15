import tkinter as tk
from tkinter import ttk

# Dummy data untuk rekomendasi lagu
songs = [
    {"image": "[Gambar Lagu]", "name": "Lagu 1", "artist": "Penyanyi 1", "duration": "3:15"},
    {"image": "[Gambar Lagu]", "name": "Lagu 2", "artist": "Penyanyi 2", "duration": "4:00"},
    {"image": "[Gambar Lagu]", "name": "Lagu 3", "artist": "Penyanyi 3", "duration": "2:45"},
    {"image": "[Gambar Lagu]", "name": "Lagu 4", "artist": "Penyanyi 4", "duration": "3:30"},
    {"image": "[Gambar Lagu]", "name": "Lagu 5", "artist": "Penyanyi 5", "duration": "3:50"},
    {"image": "[Gambar Lagu]", "name": "Lagu 6", "artist": "Penyanyi 6", "duration": "4:10"},
    {"image": "[Gambar Lagu]", "name": "Lagu 7", "artist": "Penyanyi 7", "duration": "3:25"},
    {"image": "[Gambar Lagu]", "name": "Lagu 8", "artist": "Penyanyi 8", "duration": "4:05"},
    {"image": "[Gambar Lagu]", "name": "Lagu 9", "artist": "Penyanyi 9", "duration": "3:40"},
    {"image": "[Gambar Lagu]", "name": "Lagu 10", "artist": "Penyanyi 10", "duration": "3:55"},
    {"image": "[Gambar Lagu]", "name": "Lagu 11", "artist": "Penyanyi 11", "duration": "4:20"},
    {"image": "[Gambar Lagu]", "name": "Lagu 12", "artist": "Penyanyi 12", "duration": "3:35"}
]

# Global variable for pagination
current_page = 0
songs_per_page = 10

# Fungsi untuk menampilkan lagu berdasarkan halaman
def display_songs(page):
    # Bersihkan frame rekomendasi sebelumnya
    for widget in recommended_songs_frame.winfo_children():
        widget.destroy()

    start = page * songs_per_page
    end = start + songs_per_page
    current_songs = songs[start:end]

    # Tampilkan 10 lagu per halaman
    for song in current_songs:
        song_frame = tk.Frame(recommended_songs_frame, bg='lightgrey')
        song_frame.pack(fill="x", pady=5, padx=5)

        # Gambar Lagu (Placeholder)
        song_image_label = tk.Label(song_frame, text=song["image"], bg='lightgrey', width=10)
        song_image_label.pack(side="left")

        # Nama Lagu dan Penyanyi
        song_info_frame = tk.Frame(song_frame, bg='lightgrey')
        song_info_frame.pack(side="left", padx=10)

        song_name_label = tk.Label(song_info_frame, text=song["name"], bg='lightgrey', font=("Arial", 12))
        song_name_label.pack(anchor="w")

        song_artist_label = tk.Label(song_info_frame, text=song["artist"], bg='lightgrey', font=("Arial", 10))
        song_artist_label.pack(anchor="w")

        # Durasi Lagu
        song_duration_label = tk.Label(song_frame, text=song["duration"], bg='lightgrey', font=("Arial", 10))
        song_duration_label.pack(side="right")

    # Pagination Controls
    pagination_frame = tk.Frame(recommended_songs_frame, bg='lightgrey')
    pagination_frame.pack(pady=10)

    prev_button = tk.Button(pagination_frame, text="<< Sebelumnya", command=lambda: change_page(-1))
    prev_button.grid(row=0, column=0)

    next_button = tk.Button(pagination_frame, text="Berikutnya >>", command=lambda: change_page(1))
    next_button.grid(row=0, column=1)

    # Disable tombol jika sudah di halaman pertama atau terakhir
    if page == 0:
        prev_button.config(state=tk.DISABLED)
    if end >= len(songs):
        next_button.config(state=tk.DISABLED)

# Fungsi untuk mengganti halaman
def change_page(direction):
    global current_page
    current_page += direction
    display_songs(current_page)

# Fungsi untuk menampilkan lagu yang sedang diputar
def play_song(song):
    current_song_label.config(text=f"Sedang Memainkan: {song}")
    song_title_label.config(text=f"Judul Lagu: {song}")
    artist_label.config(text="Penyanyi: Penyanyi 1")
    lyrics_label.config(text="Lirik Lagu: [Lirik lagu akan muncul di sini]")

# Fungsi untuk kontrol musik
def play_music():
    current_song_label.config(text="Memainkan Musik")

def stop_music():
    current_song_label.config(text="Musik Dihentikan")

def pause_music():
    current_song_label.config(text="Musik Dijeda")

def next_music():
    current_song_label.config(text="Lagu Berikutnya")

def previous_music():
    current_song_label.config(text="Lagu Sebelumnya")

# Inisialisasi tkinter
root = tk.Tk()
root.title("Rekomendasi Lagu Berdasarkan Ekspresi Wajah")

# Membuat agar ukuran window dinamis
root.geometry("800x600")
root.minsize(600, 400)

# Membuat Grid Layout
root.grid_columnconfigure(0, weight=1)  # Untuk membuat kolom dinamis
root.grid_columnconfigure(1, weight=3)  # Tengah lebih lebar
root.grid_columnconfigure(2, weight=1)  # Kanan
root.grid_rowconfigure(0, weight=1)

# Frame Kiri (User, Ekspresi, Rekomendasi Lagu)
left_frame = tk.Frame(root, bg='lightgrey')
left_frame.grid(row=0, column=0, sticky="nsew")

# Bagian User, Ekspresi Foto, Nama Ekspresi
user_label = tk.Label(left_frame, text="User: Nama User", bg='lightgrey')
user_label.pack(pady=10)

# Foto Ekspresi (sebagai placeholder, bisa diganti dengan gambar ekspresi asli)
photo_label = tk.Label(left_frame, text="[Foto Ekspresi]", bg='lightgrey')
photo_label.pack(pady=10)

# Tombol Ambil Foto di bawah foto ekspresi
take_photo_button = tk.Button(left_frame, text="Ambil Foto", command=lambda: print("Mengambil foto..."))
take_photo_button.pack(pady=10)

# Nama Ekspresi
expression_label = tk.Label(left_frame, text="Ekspresi: Senyum", bg='lightgrey')
expression_label.pack(pady=10)

# Rekomendasi Lagu
recommended_label = tk.Label(left_frame, text="Rekomendasi Lagu Berdasarkan Mood:", bg='lightgrey')
recommended_label.pack(pady=10)

# Frame untuk menampilkan list lagu berdasarkan mood
recommended_songs_frame = tk.Frame(left_frame, bg='lightgrey')
recommended_songs_frame.pack(fill="both", expand=True)

# Menampilkan halaman pertama rekomendasi lagu
display_songs(current_page)

# Frame Tengah (Gambar Musik, Judul Lagu, Penyanyi, Lirik, dan Kontrol)
center_frame = tk.Frame(root, bg='white')
center_frame.grid(row=0, column=1, sticky="nsew")

# Gambar Album (Placeholder)
album_image_label = tk.Label(center_frame, text="[Gambar Album Musik]", bg='white')
album_image_label.pack(pady=10)

# Judul Lagu
song_title_label = tk.Label(center_frame, text="Judul Lagu: [Belum ada lagu]", bg='white', font=("Arial", 14))
song_title_label.pack(pady=5)

# Penyanyi Lagu
artist_label = tk.Label(center_frame, text="Penyanyi: [Belum ada penyanyi]", bg='white', font=("Arial", 12))
artist_label.pack(pady=5)

# Lirik Lagu
lyrics_label = tk.Label(center_frame, text="Lirik Lagu: [Lirik belum tersedia]", bg='white', wraplength=400)
lyrics_label.pack(pady=20)

# Frame untuk Kontrol Musik di bagian bawah
control_frame = tk.Frame(center_frame, bg='white')
control_frame.pack(side="bottom", pady=20)

# Tombol Kontrol Musik (Play, Stop, Pause, Next, Previous)
play_button = tk.Button(control_frame, text="Play", command=play_music)
play_button.grid(row=0, column=0, padx=10)

stop_button = tk.Button(control_frame, text="Stop", command=stop_music)
stop_button.grid(row=0, column=1, padx=10)

pause_button = tk.Button(control_frame, text="Pause", command=pause_music)
pause_button.grid(row=0, column=2, padx=10)

previous_button = tk.Button(control_frame, text="Previous", command=previous_music)
previous_button.grid(row=0, column=3, padx=10)

next_button = tk.Button(control_frame, text="Next", command=next_music)
next_button.grid(row=0, column=4, padx=10)

# Frame Kanan (List Lagu Berdasarkan Mood)
right_frame = tk.Frame(root, bg='lightblue')
right_frame.grid(row=0, column=2, sticky="nsew")

mood_label = tk.Label(right_frame, text="Lagu Berdasarkan Mood:", bg='lightblue')
mood_label.pack(pady=10)

# Membuat container untuk daftar mood
moods = [
    {"image": "[Gambar Album]", "name": "Sedih", "count": 5},
    {"image": "[Gambar Album]", "name": "Gembira", "count": 8},
    {"image": "[Gambar Album]", "name": "Tenang", "count": 7},
    {"image": "[Gambar Album]", "name": "Bersemangat", "count": 9},
    {"image": "[Gambar Album]", "name": "Romantis", "count": 4},
    {"image": "[Gambar Album]", "name": "Santai", "count": 6},
    {"image": "[Gambar Album]", "name": "Galau", "count": 3},
]

# Membuat frame untuk setiap mood
for mood in moods:
    mood_frame = tk.Frame(right_frame, bg='lightblue')
    mood_frame.pack(fill="x", padx=10, pady=5)
    
    # Gambar Album (Placeholder)
    mood_image_label = tk.Label(mood_frame, text=mood["image"], bg='lightblue', width=12)
    mood_image_label.pack(side="left")
    
    # Nama Mood
    mood_name_label = tk.Label(mood_frame, text=mood["name"], bg='lightblue')
    mood_name_label.pack(side="left", padx=10)
    
    # Jumlah Lagu
    mood_count_label = tk.Label(mood_frame, text=f"{mood['count']} Lagu", bg='lightblue')
    mood_count_label.pack(side="right")

# Mainloop tkinter
root.mainloop()
