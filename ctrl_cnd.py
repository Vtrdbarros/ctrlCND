import tkinter as tk
import estadual
import threading




class FederalOptionsDialog:
    def __init__(self):
        self.dialog = tk.Tk()
        self.dialog.title("Opções Federais/Trabalhistas")
        self._create_buttons()
        self.dialog.mainloop()

    def _create_buttons(self):
        options = ["CND-RFB", "Situação fiscal", "CND TRABALHISTA", "FGTS"]
        for option in options:
            btn = tk.Button(self.dialog, text=option, command=lambda opt=option: self.on_option_click(opt), width=20, height=2)
            btn.pack(pady=10)

    def on_option_click(self, option):
        print(f"Federal option '{option}' selected")

class EstadualOptionsDialog:
    def __init__(self):
        self.dialog = tk.Tk()
        self.dialog.title("Opções Estaduais")
        self._create_buttons()
        self.dialog.mainloop()

    def _create_buttons(self):
        options = ["Consulta Irregularidades","Certidão Regularidade Fiscal", "Certidao Negativa Narrativa DebitoFiscal"]
        for option in options:
            btn = tk.Button(self.dialog, text=option, command=lambda opt=option: self.on_option_click(opt), width=20, height=2)
            btn.pack(pady=10)
    def on_option_click(self, option):
        print(f"Estadual option '{option}' selected")

class MainDialog:
    def __init__(self):
        self.dialog = tk.Tk()
        self.dialog.title("Escolha a opção")
        self._create_buttons()
        self.dialog.protocol("WM_DELETE_WINDOW", self.on_close)
        self.dialog.mainloop()

    def _create_buttons(self):
        options = ["Federal/Trabalhista", "Estadual", "Municipal"]
        for option in options:
            btn = tk.Button(self.dialog, text=option, command=lambda opt=option: self.on_option_click(opt), width=20, height=2)
            btn.pack(pady=10)

    def on_option_click(self, option):
        if option == "Federal/Trabalhista":
            FederalOptionsDialog()
        elif option == "Estadual":
            thread = threading.Thread(target=estadual.open_efisco_website_in_subprocess)
            thread.start()
            print(f"Opção '{option}' clicada, iniciando webscraping para efisco...")
            self.dialog.destroy()
            EstadualOptionsDialog()
            
        else:
            print(f"Opção '{option}' clicada!")

    def on_close(self):
        self.dialog.destroy()
    def destroy(self):
        self.dialog.destroy()

if __name__ == "__main__":
    MainDialog()