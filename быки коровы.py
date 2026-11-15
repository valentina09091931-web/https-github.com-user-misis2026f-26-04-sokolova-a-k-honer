import tkinter as tk
from tkinter import ttk, messagebox
import random
secret=""
attempts=0
history=[]
def generate_secret(length=4):
    digits=list("0123456789")
    random.shuffle(digits)
    if digits[0]=="0":
        for i in range(1, len(digits)):
            if digits[i]!=0:
                digits[0], digits[i]=digits[i], digits[0]
                break
    return "".join(digits[:length])
def count_bulls_cows(guess, target):
    bulls=sum(1 for i in range(len(target)) if guess[i]==target[i])
    cows=sum(1 for d in guess if d in target)-bulls
    return bulls, cows
def new_game():
    global secret, attempts, history
    length=int(length_var.get())
    secret=generate_secret(length)
    attempts=0
    history.clear()
    info_label.config(text=f" загадал {length}-значное число с уникальными цифрами")
    attempts_label.config(text="Попыток 0")
    history_box.delete("1.0", tk.END)
    guess_entry.focus()
    check_button.config(state="normal")
    guess_entry.config(state="normal")
def check_guess(event=None):
    global attempts
    raw=guess_entry.get().strip()
    length=len(secret)
    if not raw:
        messagebox.showwarning("Внимание", "ВВедите число!")
        return
    if not raw.isdigit():
        messagebox.showerror("Ошибка", "Только цифры, без букв и пробелов")
        guess_entry.delete(0, tk.END)
        return
    if len(raw)!=length:
        messagebox.showwarning("Внимание",f"Нужно ровно {length} цифр")
        return
    if len(set(raw))!=length:
        messagebox.showwarning("Внимание","Цифры не должны повторяться")
        return
    attempts=attempts+1
    bulls, cows= count_bulls_cows(raw, secret)
    attempts_label.config(text=f"Попыток: {attempts}")
    history_box.insert(tk.END, f"{attempts:>2}. {raw} →  🐂 {bulls}  🐄 {cows}\n")
    history_box.see(tk.END)
    if bulls==length:
        info_label.config(text=f"Победа! Число было{secret}", foreground="green")
        check_button.config(state="disabled")
        guess_entry.config(state="disabled")
        messagebox.showinfo("Победа!",
                            f"Вы угадали число {secret}!\nПопыток: {attempts}")
        return
    guess_entry.delete(0,tk.END)
    guess_entry.focus()
root=tk.Tk()
root.title("Быки и коровы")
root.geometry("440x560")
root.resizable(False, False)
main=ttk.Frame(root,padding=20)
main.pack(fill="both", expand=True)
ttk.Label(main, text="🐂🐄 Быки и коровы",
          font=("Arial", 16, "bold")).pack(pady=(0,15))
top_frame=ttk.Frame(main)
top_frame.pack(fill="x",pady=(0,10))
ttk.Label(top_frame, text="Длина числа:").pack(side="left")
length_var=tk.StringVar(value="4")
length_combo=ttk.Combobox(top_frame, textvariable=length_var,
                          values=["3","4","5"], state="readonly", width=5)
length_combo.pack(side="left", padx=(10,0))
ttk.Button(top_frame,text="Новая игра",command=new_game).pack(side="right")
info_label=ttk.Label(main,text="Нажмите <Новая игра>",font=("Arial",10))
info_label.pack(pady=(0,5))
attempts_label=ttk.Label(main, text="Попыток 0",font=("Arial",10))
attempts_label.pack(pady=(0,10))
input_frame=ttk.Frame(main)
input_frame.pack(fill="x",pady=(0,10))
guess_entry=ttk.Entry(input_frame,font=("Courier",14),justify="center")
guess_entry.pack(side="left",fill="x",expand=True,padx=(0,5))
guess_entry.bind("<Return>", check_guess)
check_button=ttk.Button(input_frame,text="Проверить",command=check_guess)
check_button.pack(side="left")
ttk.Label(main,text="История:").pack(anchor="w")
history_box=tk.Text(main,height=15,font=("Courier",11),state="normal")
history_box.pack(fill="both",expand=True)
ttk.Label(main,text="🐂 — цифра на своём месте    🐄 — цифра есть, но не там",
          font=("Arial",9),foreground="blue").pack(pady=(10,0))
new_game()
root.mainloop()
