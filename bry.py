import tkinter as tk
import screen_brightness_control as sbc


def set_brightness_85():
    try:
        sbc.set_brightness(85)
        status_label.config(text="Яркость установлена на 85%")
    except Exception as e:
        status_label.config(text=f"Ошибка: {e}")


def set_brightness_70():
    try:
        sbc.set_brightness(70)
        status_label.config(text="Яркость установлена на 70%")
    except Exception as e:
        status_label.config(text=f"Ошибка: {e}")


def set_brightness_55():
    try:
        sbc.set_brightness(55)
        status_label.config(text="Яркость установлена на 55%")
    except Exception as e:
        status_label.config(text=f"Ошибка: {e}")


def set_brightness_40():
    try:
        sbc.set_brightness(40)
        status_label.config(text="Яркость установлена на 40%")
    except Exception as e:
        status_label.config(text=f"Ошибка: {e}")


def set_brightness_25():
    try:
        sbc.set_brightness(25)
        status_label.config(text="Яркость установлена на 25%")
    except Exception as e:
        status_label.config(text=f"Ошибка: {e}")


# Создание окна
root = tk.Tk()
root.title("Контроль яркости монитора")
root.geometry("230x250")

# Кнопки
btn_85 = tk.Button(root, text="Установить 85%", command=set_brightness_85, width=25)
btn_85.pack(pady=10)

btn_70 = tk.Button(root, text="Установить 70%", command=set_brightness_70, width=25)
btn_70.pack(pady=10)

btn_55 = tk.Button(root, text="Установить 55%", command=set_brightness_55, width=25)
btn_55.pack(pady=10)

btn_40 = tk.Button(root, text="Установить 40%", command=set_brightness_40, width=25)
btn_40.pack(pady=10)

btn_25 = tk.Button(root, text="Установить 25%", command=set_brightness_25, width=25)
btn_25.pack(pady=10)

# Статус
status_label = tk.Label(root, text="")
status_label.pack()

# Запуск GUI
root.mainloop()
