import requests
import json
from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk


def update_b_label(event):
    code=b_combobox.get()
    name=cur[code]
    b_label.config(text=name)


def update_t_label(event):
    code=t_combobox.get()
    name=cur[code]
    t_label.config(text=name)


def exchange():
    t_code=t_combobox.get()
    b_code=b_combobox.get()

    if t_code and b_code:
        try:
            response=requests.get(f"https://v6.exchangerate-api.com/v6/571aba74e1bd586f26a2f38b/latest/{b_code}")
            response.raise_for_status()
            data=response.json()
            if t_code in data["conversion_rates"]:
                exchange_rate=data["conversion_rates"][t_code]
                t_name=cur[t_code]
                b_name=cur[b_code]
                mb.showinfo("Курс обмена", f"Курс: {exchange_rate:.2f} {t_name} за 1 {b_name}")
            else:
                mb.showerror("Ошибка!", f"Валюта {t_code} не найдена!")
        except Exception as e:
            mb.showerror("Ошибка!", f"Произошла ошибка: {e}")
    else:
        mb.showwarning("Внимание!", "Введите код валюты!")



'''import pprint

result=requests.get("https://v6.exchangerate-api.com/v6/571aba74e1bd586f26a2f38b/latest/USD")
data=json.loads(result.text)
p=pprint.PrettyPrinter(indent=4)

p.pprint(data)'''

cur={
    "RUB": "Российский рубль",
    "EUR": "Евро",
    "GBP": "Британский фунт стерлингов",
    "JPY": "Японская йена",
    "CNY": "Китайский юань",
    "KZT": "Казахский тенге",
    "UZS": "Узбекский сун",
    "CHF": "Швейцарский франк",
    "AED": "Дирхам ОАЭ",
    "CAD": "Канадский доллар",
    "USD": "Американский доллар"
}

window=Tk()
window.title("Курсы обмена валют")
window.geometry("360x300")

Label(text="Базовая валюта").pack(padx=10, pady=10)
b_combobox=ttk.Combobox(values=list(cur.keys()))
b_combobox.pack(padx=10, pady=10)
b_combobox.bind("<<ComboboxSelected>>", update_b_label)

b_label=ttk.Label()
b_label.pack(padx=10, pady=10)

#Label(text="Выберите код валюты").pack(padx=10, pady=10)
Label(text="Целевая валюта").pack(padx=10, pady=10)
#cur=["RUB", "EUR", "GBR", "JPY", "CNY", "KZT", "UZS", "CHF", "AED", "CAD"]
t_combobox=ttk.Combobox(values=list(cur.keys()))
t_combobox.pack(padx=10, pady=10)
t_combobox.bind("<<ComboboxSelected>>", update_t_label)

'''entry=Entry()
entry.pack(padx=10, pady=10)'''

t_label=ttk.Label()
t_label.pack(padx=10, pady=10)


Button(text="Получить курс обмена", command=exchange).pack(padx=10, pady=10)

window.mainloop()

