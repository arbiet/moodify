import tkinter as tk
from PIL import Image, ImageTk

class MusicController:
    @staticmethod
    def create_controls(frame):
        # Fungsi untuk meresize gambar ikon
        def resize_icon(path, size=(30, 30)):
            img = Image.open(path)
            img = img.resize(size, Image.Resampling.LANCZOS)
            return ImageTk.PhotoImage(img)

        # Load dan resize ikon untuk tombol
        play_icon = resize_icon("assets/icons/play.png")
        stop_icon = resize_icon("assets/icons/stop.png")
        pause_icon = resize_icon("assets/icons/pause.png")
        next_icon = resize_icon("assets/icons/next.png")
        previous_icon = resize_icon("assets/icons/previous.png")

        # Buat tombol kontrol dengan ikon menggunakan grid dan membuatnya terpusat
        play_button = tk.Button(frame, image=play_icon, command=lambda: print("Memainkan Musik"))
        play_button.image = play_icon  # Simpan referensi ikon agar tidak dihapus oleh garbage collector
        play_button.grid(row=0, column=0, padx=10, pady=5)

        stop_button = tk.Button(frame, image=stop_icon, command=lambda: print("Menghentikan Musik"))
        stop_button.image = stop_icon
        stop_button.grid(row=0, column=1, padx=10, pady=5)

        pause_button = tk.Button(frame, image=pause_icon, command=lambda: print("Menjeda Musik"))
        pause_button.image = pause_icon
        pause_button.grid(row=0, column=2, padx=10, pady=5)

        previous_button = tk.Button(frame, image=previous_icon, command=lambda: print("Lagu Sebelumnya"))
        previous_button.image = previous_icon
        previous_button.grid(row=0, column=3, padx=10, pady=5)

        next_button = tk.Button(frame, image=next_icon, command=lambda: print("Lagu Berikutnya"))
        next_button.image = next_icon
        next_button.grid(row=0, column=4, padx=10, pady=5)

        # Buat kolom frame agar berkembang sesuai ukuran layar
        frame.grid_columnconfigure(0, weight=1)
        frame.grid_columnconfigure(1, weight=1)
        frame.grid_columnconfigure(2, weight=1)
        frame.grid_columnconfigure(3, weight=1)
        frame.grid_columnconfigure(4, weight=1)
