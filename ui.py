import tkinter as tk

class Application(tk.Frame):

    def chamar_algoritmo_genetico(self):
        print('a')

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.grid()
        self.create_widget()

    def create_widget(self):
        self.instruction = tk.Label(self,text = "City", font = "22")
        self.instruction.grid(row = 0, column=0)
        self.city = tk.Entry(self)
        self.city.grid(row = 0, column = 1)
        self.instruction = tk.Label(self,text = "Population", font = "22")
        self.instruction.grid(row = 1, column=0)
        self.population = tk.Entry(self)
        self.population.grid(row = 1, column = 1)
        self.button1 = tk.Button(self, text="Submit")
        self.button1.event_add(self.chamar_algoritmo_genetico())
        self.button1.grid()

root = tk.Tk()
root.title("Traveller")
root.geometry("320x180")
app = Application(master=root)
app.mainloop()