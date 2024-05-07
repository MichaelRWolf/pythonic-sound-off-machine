import tkinter as tk
import pygame

sound_files = {
    "boing": "boing-SBA-300156634.wav",
    "clock": "clock-fast-ticking-SBA-300419272.wav",
    "applause": "concert-scream-applause-short-SBA-300054812.wav",
    "zombie groan": "crowd-zombie-groan-moan-SBA-300156819.wav",
    "ding": "good-idea-shiny-ding-SBA-300457977.wav"
}

def play_sound(label):
    file_path = sound_files.get(label)
    if file_path:
        pygame.mixer.init()
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()

def main():
    root = tk.Tk()
    root.title("Sound Player")

    for label, _ in sound_files.items():
        button = tk.Button(root, text=label, command=lambda l=label: play_sound(l))
        button.pack(pady=5)

    root.mainloop()

if __name__ == '__main__':
    main()
