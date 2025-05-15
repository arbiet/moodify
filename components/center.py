import tkinter as tk
from controllers.music_controller import MusicController
from PIL import Image, ImageTk

class CenterPanel(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg='white')
        self.create_widgets()

    def create_widgets(self):
        # Buat frame untuk kontrol musik yang ditempatkan di atas dan lebar penuh
        control_frame = tk.Frame(self, bg='white', bd=2, relief='solid')
        control_frame.grid(row=0, column=0, padx=20, pady=10, sticky='ew')  # Lebar penuh dengan grid

        # Konfigurasi grid agar lebar control_frame memenuhi
        self.grid_columnconfigure(0, weight=1)  # Membuat kolom melebar

        # Menampilkan kontrol musik di dalam frame dengan ikon
        MusicController.create_controls(control_frame)

        # Bagian untuk informasi album dan lagu
        self.album_image_label = tk.Label(self, text="[Gambar Album Musik]", bg='white')
        self.album_image_label.grid(row=1, column=0, pady=10)

        self.song_title_label = tk.Label(self, text="Judul Lagu: [Belum ada lagu]", bg='white', font=("Arial", 14))
        self.song_title_label.grid(row=2, column=0, pady=5)

        self.artist_label = tk.Label(self, text="Penyanyi: [Belum ada penyanyi]", bg='white', font=("Arial", 12))
        self.artist_label.grid(row=3, column=0, pady=5)

        self.mood_album_label = tk.Label(self, text="Berasal dari Album: [Belum ada mood album]", bg='white', font=("Arial", 10))
        self.mood_album_label.grid(row=4, column=0, pady=5)

        self.lyrics_label = tk.Label(self, text="Lirik Lagu: [Lirik belum tersedia]", bg='white', wraplength=400)
        self.lyrics_label.grid(row=5, column=0, pady=20)

    def update_song_info(self, album_image_path, song_title, artist, mood_album, lyrics):
        """
        Memperbarui informasi lagu dan album.
        """
        # Update gambar album
        self.load_album_image(album_image_path)

        # Update informasi lagu
        self.song_title_label.config(text=f"Judul Lagu: {song_title}")
        self.artist_label.config(text=f"Penyanyi: {artist}")
        self.mood_album_label.config(text=f"Berasal dari Album: {mood_album}")

        # Update lirik lagu
        if lyrics:
            self.lyrics_label.config(text=f"Lirik Lagu: {lyrics}")
        else:
            self.lyrics_label.config(text="Lagu tanpa lirik")

    def load_album_image(self, image_path):
        """
        Load gambar album dari path yang diberikan dan menampilkannya.
        """
        # Load gambar album
        img = Image.open(image_path)
        img = img.resize((150, 150), Image.Resampling.LANCZOS)
        self.album_photo = ImageTk.PhotoImage(img)

        # Update label gambar album
        self.album_image_label.config(image=self.album_photo)
        self.album_image_label.image = self.album_photo
