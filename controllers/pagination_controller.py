import tkinter as tk

class PaginationController:
    @staticmethod
    def display_songs(parent, songs, current_page, change_page_callback):
        for widget in parent.winfo_children():
            widget.destroy()

        start = current_page * 10
        end = start + 10
        for song in songs[start:end]:
            song_frame = tk.Frame(parent, bg='lightgrey')
            song_frame.pack(fill="x", pady=5, padx=5)
            song_image_label = tk.Label(song_frame, text=song["image"], bg='lightgrey', width=10)
            song_image_label.pack(side="left")
            song_info_frame = tk.Frame(song_frame, bg='lightgrey')
            song_info_frame.pack(side="left", padx=10)
            song_name_label = tk.Label(song_info_frame, text=song["name"], bg='lightgrey', font=("Arial", 12))
            song_name_label.pack(anchor="w")
            song_artist_label = tk.Label(song_info_frame, text=song["artist"], bg='lightgrey', font=("Arial", 10))
            song_artist_label.pack(anchor="w")
            song_duration_label = tk.Label(song_frame, text=song["duration"], bg='lightgrey', font=("Arial", 10))
            song_duration_label.pack(side="right")

        # Pagination Controls
        pagination_frame = tk.Frame(parent, bg='lightgrey')
        pagination_frame.pack(pady=10)
        prev_button = tk.Button(pagination_frame, text="<< Sebelumnya", command=lambda: change_page_callback(-1))
        prev_button.grid(row=0, column=0)
        next_button = tk.Button(pagination_frame, text="Berikutnya >>", command=lambda: change_page_callback(1))
        next_button.grid(row=0, column=1)

        if current_page == 0:
            prev_button.config(state=tk.DISABLED)
        if end >= len(songs):
            next_button.config(state=tk.DISABLED)
