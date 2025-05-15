import os
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageDraw
from controllers.pagination_controller import PaginationController
from data.songs_data import get_songs_by_mood

class LeftPanel(tk.Frame):
    def __init__(self, master, mood_id):
        super().__init__(master, bg='lightgrey')
        self.current_page = 0
        self.songs_per_page = 8  # Menampilkan 8 lagu per halaman
        self.songs = get_songs_by_mood(mood_id)  # Ambil data lagu berdasarkan mood
        self.photo_path = "assets/expressions/default_expression.png"  # Gambar default ekspresi
        self.create_widgets()

    def create_widgets(self):
        # Bagian User dan Ekspresi
        user_label = tk.Label(self, text="User: Nama User", bg='lightgrey')
        user_label.pack(pady=10)

        # Load gambar ekspresi
        self.load_photo(self.photo_path)

        # Tombol Ambil Foto
        take_photo_button = tk.Button(self, text="Ambil Foto", command=self.take_photo)
        take_photo_button.pack(pady=10)

        expression_label = tk.Label(self, text="Ekspresi: Senyum", bg='lightgrey')
        expression_label.pack(pady=10)
        
        # Bagian Rekomendasi Lagu
        recommended_label = tk.Label(self, text="Rekomendasi Lagu Berdasarkan Mood:", bg='lightgrey')
        recommended_label.pack(pady=10)
        self.songs_frame = tk.Frame(self, bg='lightgrey')
        self.songs_frame.pack(fill="both", expand=True)

        # Load gambar rekomendasi lagu
        self.display_songs()

    def load_photo(self, image_path):
        # Load gambar dari file
        img = Image.open(image_path)
        img = img.resize((150, 150), Image.Resampling.LANCZOS)  # Sesuaikan ukuran gambar
        self.photo = ImageTk.PhotoImage(img)

        # Label untuk menampilkan gambar
        self.photo_label = tk.Label(self, image=self.photo, bg='lightgrey')
        self.photo_label.pack(pady=10)

    def take_photo(self):
        # Fungsi untuk mengambil foto dari file (simulasi webcam bisa menggunakan file dialog)
        file_path = filedialog.askopenfilename(
            title="Pilih Foto",
            filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")]
        )
        if file_path:
            self.photo_path = file_path  # Set path foto yang baru diambil
            self.update_photo()

    def update_photo(self):
        # Update gambar di label
        self.photo_label.pack_forget()  # Hapus label foto lama
        self.load_photo(self.photo_path)  # Load dan tampilkan foto baru

    def load_song_image(self, song_image):
        # Fungsi untuk memuat gambar lagu dari file, dengan fallback ke default jika tidak ditemukan
        song_image_path = f"assets/songs/{song_image}"
        default_song_image_path = "assets/images/default_song.png"  # Gambar default lagu

        if not os.path.exists(song_image_path):
            song_image_path = default_song_image_path  # Gunakan default jika tidak ada gambar

        # Load gambar dari file dan buat sudut gambar lebih bulat
        img = Image.open(song_image_path).resize((50, 50), Image.Resampling.LANCZOS)
        img = self.round_corners(img, 15)  # Membulatkan sudut gambar dengan radius 15px
        return ImageTk.PhotoImage(img)

    def round_corners(self, img, radius):
        # Fungsi untuk membulatkan sudut gambar
        mask = Image.new('L', img.size, 0)
        draw = ImageDraw.Draw(mask)
        draw.rounded_rectangle([0, 0, *img.size], radius=radius, fill=255)
        img.putalpha(mask)
        return img

    def display_songs(self):
        # Bersihkan frame lama
        for widget in self.songs_frame.winfo_children():
            widget.destroy()

        start = self.current_page * self.songs_per_page
        end = start + self.songs_per_page
        current_songs = self.songs[start:end]

        # Tampilkan setiap lagu dengan gambar, nama lagu, dan artis
        for song in current_songs:
            song_frame = tk.Frame(self.songs_frame, bg='lightgrey', bd=1, relief="solid")
            song_frame.pack(fill="x", pady=2, padx=5)  # Mengurangi jarak antar lagu

            # Load gambar lagu atau default
            song_img = self.load_song_image(song["image"])

            # Label gambar lagu
            song_image_label = tk.Label(song_frame, image=song_img, bg='lightgrey')
            song_image_label.image = song_img  # Simpan referensi untuk menjaga agar tidak dihapus oleh garbage collector
            song_image_label.pack(side="left", padx=10)

            # Label untuk nama lagu dan penyanyi
            song_info_frame = tk.Frame(song_frame, bg='lightgrey')
            song_info_frame.pack(side="left")

            song_name_label = tk.Label(song_info_frame, text=song["name"], bg='lightgrey', font=("Arial", 12))
            song_name_label.pack(anchor="w")

            song_artist_label = tk.Label(song_info_frame, text=song["artist"], bg='lightgrey', font=("Arial", 10))
            song_artist_label.pack(anchor="w")

        # Pagination Controls
        pagination_frame = tk.Frame(self.songs_frame, bg='lightgrey')
        pagination_frame.pack(pady=10)

        prev_button = tk.Button(pagination_frame, text="<< Sebelumnya", command=lambda: self.change_page(-1))
        prev_button.grid(row=0, column=0)

        next_button = tk.Button(pagination_frame, text="Berikutnya >>", command=lambda: self.change_page(1))
        next_button.grid(row=0, column=1)

        # Disable tombol jika sudah di halaman pertama atau terakhir
        if self.current_page == 0:
            prev_button.config(state=tk.DISABLED)
        if end >= len(self.songs):
            next_button.config(state=tk.DISABLED)

    def change_page(self, direction):
        self.current_page += direction
        self.display_songs()
