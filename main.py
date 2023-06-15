import tkinter as tk
from tkinter import filedialog
from pygame import mixer
from tkinter import ttk


class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Music Player")
        self.root.geometry("400x400")
        self.root.resizable(False, False)

        self.music_file = None
        self.paused = False

        self.create_widgets()