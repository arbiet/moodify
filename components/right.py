import os
import tkinter as tk
from PIL import Image, ImageTk, ImageDraw  # Pastikan ImageDraw diimpor
from data.songs_data import get_moods, get_song_count_by_mood, get_artist_count_by_mood  # Fungsi untuk mendapatkan jumlah penyanyi

class RightPanel(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg='lightblue')
        self.create_widgets()

    def create_widgets(self):
        mood_label = tk.Label(self, text="Lagu Berdasarkan Mood:", bg='lightblue')
        mood_label.pack(pady=10)

        moods = get_moods()  # Ambil data mood dari database

        for mood in moods:
            # Hitung jumlah lagu dan penyanyi untuk mood ini
            song_count = get_song_count_by_mood(mood['id'])
            artist_count = get_artist_count_by_mood(mood['id'])  # Hitung jumlah penyanyi

            mood_frame = tk.Frame(self, bg='lightblue', bd=1, relief="solid")
            mood_frame.pack(fill="x", padx=10, pady=5)

            # Load gambar album atau default
            mood_img = self.load_album_image(mood["image"])

            # Label gambar album
            mood_image_label = tk.Label(mood_frame, image=mood_img, bg='lightblue')
            mood_image_label.image = mood_img  # Simpan referensi agar tidak terhapus oleh garbage collector
            mood_image_label.pack(side="left", padx=10)

            # Nama Mood
            mood_name_label = tk.Label(mood_frame, text=mood["name"], bg='lightblue')
            mood_name_label.pack(side="left", padx=10)

            # Jumlah Lagu dan Penyanyi
            mood_count_label = tk.Label(mood_frame, text=f"{song_count} Lagu, {artist_count} Penyanyi", bg='lightblue')
            mood_count_label.pack(side="right")

    def load_album_image(self, album_image):
        # Fungsi untuk memuat gambar album dari file, dengan fallback ke default jika tidak ditemukan
        album_image_path = f"assets/albums/{album_image}"
        default_album_image_path = "assets/images/default_album.png"  # Gambar default album

        if not os.path.exists(album_image_path):
            album_image_path = default_album_image_path  # Gunakan default jika tidak ada gambar

        # Load gambar dari file dan buat sudut gambar lebih bulat
        img = Image.open(album_image_path).resize((50, 50), Image.Resampling.LANCZOS)
        img = self.round_corners(img, 15)  # Membulatkan sudut gambar dengan radius 15px
        return ImageTk.PhotoImage(img)

    def round_corners(self, img, radius):
        # Fungsi untuk membulatkan sudut gambar
        mask = Image.new('L', img.size, 0)
        draw = ImageDraw.Draw(mask)  # Menggunakan ImageDraw untuk menggambar bentuk
        draw.rounded_rectangle([0, 0, *img.size], radius=radius, fill=255)
        img.putalpha(mask)
        return img
