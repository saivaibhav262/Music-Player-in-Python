import os
import tkinter as tk
from tkinter import filedialog
import pygame
class MusicPlayer(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Music Player")
        self.geometry("400x150")
        self.current_file = None
        pygame.mixer.init()
        self.create_widgets()
    def create_widgets(self):
        self.btn_open = tk.Button(self, text="Open", command=self.open_file)
        self.btn_open.pack(pady=20)
        self.btn_play = tk.Button(self, text="Play", command=self.play_music)
        self.btn_play.pack(pady=10)
        self.btn_stop = tk.Button(self, text="Stop", command=self.stop_music)
        self.btn_stop.pack(pady=10)
    def open_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3 *.wav")])
        if file_path:
            self.current_file = file_path
            pygame.mixer.music.load(file_path)
    def play_music(self):
        if self.current_file:
            pygame.mixer.music.play()
    def stop_music(self):
        pygame.mixer.music.stop()
if __name__ == "__main__":
    app = MusicPlayer()
    app.mainloop()
