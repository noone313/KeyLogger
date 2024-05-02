import tkinter as tk
import keyboard

def on_key_pressed(event):
    char = event.name
    english_alphabet = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    if char in english_alphabet:
        label.config(text=char)
    elif char == 'space':
        label.config(text=' ')
    elif char == 'enter':
        label.config(text='<Enter>')
    else:
        label.config(text='')

root = tk.Tk()
root.attributes("-topmost", True)  # جعل النافذة في الأمام
root.configure(bg="black")  # تعيين لون الخلفية للنافذة إلى الأسود

# إنشاء عنصر نصي لعرض الحرف المضغوط
label = tk.Label(root, text="", fg="white", bg="black", font=("Arial", 48))
label.pack(expand=True)

keyboard.on_press(on_key_pressed)

root.mainloop()
