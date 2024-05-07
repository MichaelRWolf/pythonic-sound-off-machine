import tkinter as tk
import pygame

sound_files = {
    "kick-fx": "105623__soniktec__kick-fx-marker-249.wav",
    "Bad Guy Laughter": "214504__robinhood76__04751-bad-guy-male-laughter.wav",
    "Demon Ghost Speaking": "362674__osiruswaltz__demon_ghost-speaking-2.wav",
    "Bell": "575253__psy_kshy__bell.wav",
    "Handbrake Turn": "71741__audible-edge__nissan-maxima-handbrake-turn-04-25-2009.wav",
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
