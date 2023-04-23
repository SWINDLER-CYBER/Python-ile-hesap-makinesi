import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Hesap Makinesi")

        # hesap makinesi ekranı
        self.display = tk.Entry(master, width=25, font=('Arial', 16))
        self.display.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        # sayı tuşları
        self.buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]
        
        # tuşları yerleştir
        for i, symbol in enumerate(self.buttons):
            row = i // 4 + 1
            column = i % 4
            button = tk.Button(master, text=symbol, width=5, font=('Arial', 16),
                               command=lambda symbol=symbol: self.add_to_display(symbol))
            button.grid(row=row, column=column, padx=5, pady=5)

    def add_to_display(self, symbol):
        if symbol == '=':
            # hesaplamayı yap
            try:
                result = str(eval(self.display.get()))
            except:
                result = 'Geçersiz işlem'
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, result)
        else:
            # ekrana sembol ekle
            self.display.insert(tk.END, symbol)

root = tk.Tk()
app = Calculator(root)
root.mainloop()
