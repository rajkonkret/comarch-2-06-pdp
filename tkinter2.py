import tkinter as tk


def on_click():
    print("Przycisk został nacisniety")


app = tk.Tk()
app.title("Przykład")

button = tk.Button(app, text="Kliknij mnie", command=on_click)

button.pack()
app.mainloop()
