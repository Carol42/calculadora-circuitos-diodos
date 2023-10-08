from math import sqrt
import tkinter as tk
from PIL import ImageTk, Image
import customtkinter as cTK
import tkinter.messagebox

cTK.set_appearance_mode("dark")
cTK.set_default_color_theme("dark-blue")

def ignore_input(event):
    """Ignore key press events."""
    return "break"

def calculate():

    try:
        freq = float(freq_entry.get())
        rms = float(rms_entry.get())
        res = float(res_entry.get())
        cap = float(cap_entry.get())
    except ValueError:

        tkinter.messagebox.showwarning("Input Inválido", "Por favor, apenas números")
        return
        
        
    i = rms/res
    vripple = i/freq*cap
    max_volt = rms * sqrt(2)
    min_volt = max_volt - vripple
    avg_volt = (max_volt + min_volt)/2

    max_volt_entry.delete(0, tk.END)
    max_volt_entry.insert(0, str(round(max_volt,2))+" V")
    min_volt_entry.delete(0, tk.END)
    min_volt_entry.insert(0, str(round(min_volt,2))+" V")
    avg_volt_entry.delete(0, tk.END)
    avg_volt_entry.insert(0, str(round(avg_volt,2))+" V")

def calculate2():
    try:
        r_diodo = float(r_diodo_entry.get())
        r_carga = float(r_carga_entry.get())
        w_fonte = float(w_fonte_entry.get())
        w_diodo = float(w_diodo_entry.get())
    except ValueError:
 
        tkinter.messagebox.showwarning("Input Inválido", "Por favor, apenas números")
        return

    # Tensao do divisor de tensao
    div_w = w_fonte * (r_carga / (r_diodo + r_carga))
    # Tensao sobre o resistor em serie
    w_res_s = w_fonte - div_w
    # Corrente sobre o resistor em serie
    i_res_s = w_res_s / r_diodo
    # Corrente sobre o resistor de carga
    i_res_carga = w_diodo/r_carga
    # Corrente sobre o diodo
    i_diodo = i_res_s - i_res_carga
    # Potencia dissipada sobre o diodo
    pot_diodo = w_diodo * i_diodo

    div_w_entry.delete(0, tk.END)
    div_w_entry.insert(0, str(round(div_w,2))+" V")
    w_res_s_entry.delete(0, tk.END)
    w_res_s_entry.insert(0, str(round(w_res_s,2))+" V")
    i_res_s_entry.delete(0, tk.END)
    i_res_s_entry.insert(0, str(round(i_res_s,2))+" mA")
    i_res_carga_entry.delete(0, tk.END)
    i_res_carga_entry.insert(0, str(round(i_res_carga,2))+" mA")
    i_diodo_entry.delete(0, tk.END)
    i_diodo_entry.insert(0, str(round(i_diodo,2))+" mA")
    pot_diodo_entry.delete(0, tk.END)
    pot_diodo_entry.insert(0, str(round(pot_diodo,2))+" mW")

def open_screen1():
    global freq_entry, rms_entry, res_entry, cap_entry
    global max_volt_entry, min_volt_entry, avg_volt_entry
    global modulo1

    modulo1 = cTK.CTkToplevel(root)
    modulo1.geometry("300x550")
    modulo1.title("Módulo 1")

    cTK.CTkLabel(modulo1, text="Frequência da onda (Hz)").pack()
    freq_entry = cTK.CTkEntry(modulo1)
    freq_entry.pack()

    cTK.CTkLabel(modulo1, text="Tensão rms (V)").pack()
    rms_entry = cTK.CTkEntry(modulo1)
    rms_entry.pack()

    cTK.CTkLabel(modulo1, text="Resistência da carga (kΩ)").pack()
    res_entry = cTK.CTkEntry(modulo1)
    res_entry.pack()

    cTK.CTkLabel(modulo1, text="Valor do capacitor (µF)").pack()
    cap_entry = cTK.CTkEntry(modulo1)
    cap_entry.pack()

    # Output fields
    cTK.CTkLabel(modulo1, text="Resultados").pack(pady=20)
    cTK.CTkLabel(modulo1, text="Tensão máxima (pico)").pack()
    max_volt_entry = cTK.CTkEntry(modulo1)
    max_volt_entry.pack()
    max_volt_entry.bind("<Key>", ignore_input)  

    cTK.CTkLabel(modulo1, text="Tensão mínima").pack()
    min_volt_entry = cTK.CTkEntry(modulo1)
    min_volt_entry.pack()
    min_volt_entry.bind("<Key>", ignore_input)  

    cTK.CTkLabel(modulo1, text="Tensão média").pack()
    avg_volt_entry = cTK.CTkEntry(modulo1)
    avg_volt_entry.pack()
    avg_volt_entry.bind("<Key>", ignore_input)  

    calc_button = cTK.CTkButton(modulo1, text="Calcular", command=calculate)
    calc_button.pack(pady=20)
   
def open_screen2():
    global r_diodo_entry, r_carga_entry, w_fonte_entry, w_diodo_entry
    global div_w_entry, w_res_s_entry, i_res_s_entry, i_res_carga_entry, i_diodo_entry, pot_diodo_entry

    modulo2 = cTK.CTkToplevel(root)
    modulo2.geometry("300x700")
    modulo2.title("Módulo 2")

    cTK.CTkLabel(modulo2, text="Resistência em série ao diodo (kΩ)").pack()
    r_diodo_entry = cTK.CTkEntry(modulo2)
    r_diodo_entry.pack()

    cTK.CTkLabel(modulo2, text="Resistência de carga (kΩ)").pack()
    r_carga_entry = cTK.CTkEntry(modulo2)
    r_carga_entry.pack()

    cTK.CTkLabel(modulo2, text="Tensão da fonte (V)").pack()
    w_fonte_entry = cTK.CTkEntry(modulo2)
    w_fonte_entry.pack()

    cTK.CTkLabel(modulo2, text="Tensão de ruptura do diodo (V)").pack()
    w_diodo_entry = cTK.CTkEntry(modulo2)
    w_diodo_entry.pack()

    # Output fields
    cTK.CTkLabel(modulo2, text="Resultados").pack(pady=20)
    cTK.CTkLabel(modulo2, text="Tensão do divisor de tensão").pack()
    div_w_entry = cTK.CTkEntry(modulo2)
    div_w_entry.pack()
    div_w_entry.bind("<Key>", ignore_input)  

    cTK.CTkLabel(modulo2, text="Tensão sobre o resistor em série").pack()
    w_res_s_entry = cTK.CTkEntry(modulo2)
    w_res_s_entry.pack()
    w_res_s_entry.bind("<Key>", ignore_input)  

    cTK.CTkLabel(modulo2, text="Corrente sobre o resistor em série").pack()
    i_res_s_entry = cTK.CTkEntry(modulo2)
    i_res_s_entry.pack()
    i_res_s_entry.bind("<Key>", ignore_input)  

    cTK.CTkLabel(modulo2, text="Corrente sobre o resistor de carga").pack()
    i_res_carga_entry = cTK.CTkEntry(modulo2)
    i_res_carga_entry.pack()
    i_res_carga_entry.bind("<Key>", ignore_input) 

    cTK.CTkLabel(modulo2, text="Corrente sobre o diodo").pack()
    i_diodo_entry = cTK.CTkEntry(modulo2)
    i_diodo_entry.pack()
    i_diodo_entry.bind("<Key>", ignore_input) 

    cTK.CTkLabel(modulo2, text="Potência dissipada sobre o diodo").pack()
    pot_diodo_entry = cTK.CTkEntry(modulo2)
    pot_diodo_entry.pack()
    pot_diodo_entry.bind("<Key>", ignore_input) 

    calc_button = cTK.CTkButton(modulo2, text="Calcular", command=calculate2)
    calc_button.pack(pady=20)


root = cTK.CTk()
root.title("Cálculos de Eletrônica")
root.geometry("1200x600")
root.resizable(False, False)

title_label = cTK.CTkLabel(root, text="Escolha seu módulo", font=('bold', 20))
title_label.pack(pady=20)

image1 = ImageTk.PhotoImage(Image.open("imgs/circuito1.png"))
image2 = ImageTk.PhotoImage(Image.open("imgs/circuito2.png"))

frame1 = cTK.CTkFrame(root)
frame1.pack(side="left", padx=20, pady=20)

title1 = cTK.CTkLabel(frame1, text="Módulo 1")
title1.pack()

button1 = tk.Button(frame1, image=image1, command=open_screen1)
button1.pack()
button1.config(borderwidth=5, relief="solid")

frame2 = cTK.CTkFrame(root)
frame2.pack(side="left", padx=20, pady=20)

title2 = cTK.CTkLabel(frame2, text="Módulo 2")
title2.pack()

button2 = tk.Button(frame2, image=image2, command=open_screen2)
button2.pack()
button2.config(borderwidth=5, relief="solid")

root.mainloop()
