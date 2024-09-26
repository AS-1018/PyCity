import tkinter as tk

#Вывод окнв \\разгобрать чо и как
root = tk.Tk()
root.title('game')

window_width = 640
window_height = 480

# get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# find the center point
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

# set the position of the window to the center of the screen
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

mess = tk.Label(root, text = f"Ход: Деньги; Население:")
mess.pack()

root.mainloop()