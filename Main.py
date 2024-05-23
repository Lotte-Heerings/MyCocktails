from Applicatie import Applicatie
from CocktailDB import CocktailDB
import tkinter as tk


root = tk.Tk()
cocktail_db = CocktailDB()
applicatie = Applicatie(cocktail_db, root)
root.mainloop()
