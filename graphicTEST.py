import tkinter as tk

# Вывод окна
root = tk.Tk()
root.title('PyCity Graphic')

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

st = tk.Label(root, text=f"Ход: Деньги: Население:", font=("Arial Bold", 20))
st.place(x=0, y=0)

nh = tk.Button(root, text="Следущий ход",  font=("Arial Bold", 20))
nh.place(x=432, y=425)

cmd = tk.Text(root, height=3, width=54)
cmd.place(x=0, y=430)

root.mainloop()
