import tkinter as tk
from screeninfo import get_monitors
from components.left import LeftPanel
from components.center import CenterPanel
from components.right import RightPanel
from data.songs_data import get_moods  # Mengambil mood dari database

# Fungsi untuk mendapatkan ukuran layar desktop
def get_screen_size():
    monitor = get_monitors()[0]  # Mengambil monitor pertama (utama)
    return monitor.width, monitor.height

# Inisialisasi tkinter
root = tk.Tk()
root.title("Rekomendasi Lagu Berdasarkan Ekspresi Wajah")

# Dapatkan ukuran layar
screen_width, screen_height = get_screen_size()

# Atur ukuran window berdasarkan ukuran layar
root.geometry(f"{screen_width}x{screen_height}")  # Ukuran sesuai layar
root.minsize(600, 400)  # Ukuran minimal

# Ambil data mood dari database
moods = get_moods()

# Pilih mood pertama sebagai default (contoh: mood 'Sedih')
default_mood_id = moods[0]["id"]  # Mengambil mood_id dari mood pertama

# Grid Layout
root.grid_columnconfigure(0, weight=1)  # Kiri
root.grid_columnconfigure(1, weight=3)  # Tengah
root.grid_columnconfigure(2, weight=1)  # Kanan
root.grid_rowconfigure(0, weight=1)

# Inisialisasi Panel Kiri, Tengah, Kanan
LeftPanel(root, default_mood_id).grid(row=0, column=0, sticky="nsew")
CenterPanel(root).grid(row=0, column=1, sticky="nsew")
RightPanel(root).grid(row=0, column=2, sticky="nsew")

# Mainloop tkinter
root.mainloop()
