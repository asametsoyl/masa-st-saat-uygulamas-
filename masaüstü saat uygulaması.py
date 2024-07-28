import tkinter as tk
import time

class Clock:
    def __init__(self, root):
        self.root = root
        self.root.title("Masaüstü Saat")
        self.root.geometry("300x150")
        self.root.resizable(False, False)

        self.label = tk.Label(root, font=('calibri', 40, 'bold'), background='purple', foreground='white')
        self.label.pack(anchor='center')

        self.update_clock()

    def update_clock(self):
        current_time = time.strftime('%H:%M:%S')
        self.label.config(text=current_time)
        self.root.after(1000, self.update_clock)  # 1 saniyede bir günceller

if __name__ == "__main__":
    root = tk.Tk()
    clock = Clock(root)
    root.mainloop()
