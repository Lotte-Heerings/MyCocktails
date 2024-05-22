from Applicatie import Applicatie
from CocktailDB import CocktailDB
import tkinter as tk


# window = tk.Tk()
#
# greeting = tk.Label(text="PR")
# greeting.pack()
# window.mainloop()
root = tk.Tk()
cocktail_db = CocktailDB()
applicatie = Applicatie(cocktail_db, root)
#applicatie.uitvoeren()
root.mainloop()
