import numpy as np
color = list(np.random.choice(range(256), size=5))
print(color)
import random
color = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])]
print(color)
import random

import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)

        self.master.title("タイトル")    # ウィンドウタイトル
        self.master.geometry("300x200") # ウィンドウサイズ(幅x高さ)

        # Canvasの作成
        canvas = tk.Canvas(
            self.master, 
            width = 200,
            height = 100,
            bg = ""
            )
        # Canvasを配置
        canvas.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master = root)
    app.mainloopcolor = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])]
print(color)

tk.scatter(random.randint(0, 10), random.randint(0,10), c=color, s=200)
tk.show()