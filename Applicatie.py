from tkinter import *
from tkinter import messagebox


class Applicatie:
    def __init__(self, cocktail_db, master):
        self.cocktail_db = cocktail_db
        self.master = master
        master.title("Hoofdmenu")
        self.label = Label(master, text="Invulveld")
        self.label.pack()
        self.entry = Entry(master)
        self.entry.pack()
        self.button1 = Button(master, text="Zoeken op ingrediënt", command=self._zoek_op_ingredient)
        self.button1.pack()
        self.button2 = Button(master, text="Krijg een random cocktail", command=self._get_random_cocktail)
        self.button2.pack()
        self.button3 = Button(master, text="Krijg details van een specifieke cocktail",
                              command=self._get_cocktail_details)
        self.button3.pack()
        self.button4 = Button(master, text="Afsluiten", command=master.quit)
        self.button4.pack()

    def _zoek_op_ingredient(self):
        ingredient = self.entry.get()
        if len(ingredient) == 0:
            messagebox.showwarning("Invul error", "Geen input gekregen. Controleer het invulveld.")
            return
        cocktails = self.cocktail_db.zoek_op_ingredient(ingredient)
        if cocktails:
            cocktail_list = ""
            for cocktail in cocktails:
                cocktail_list += cocktail["strDrink"] + "\t|"
            messagebox.showinfo(f"Cocktails met {ingredient}:", cocktail_list)
        else:
            messagebox.showwarning("Naam error", "Cocktails niet gevonden. Controleer het ingrediënt.")

    def _get_random_cocktail(self):
        cocktail = self.cocktail_db.get_random_cocktail()
        cocktail_naam = cocktail["strDrink"]
        messagebox.showinfo("Random cocktail", cocktail_naam)
        response = messagebox.askyesno("Meer details?", "Wil je meet details van deze cocktail?")
        if response:
            self._get_cocktail_details(cocktail_naam)

    def _get_cocktail_details(self, cocktail_naam = None):
        if cocktail_naam is None:
            cocktail_naam = self.entry.get()
        if len(cocktail_naam) == 0:
            messagebox.showwarning("Invul error", "Geen input gekregen. Controleer het invulveld.")
            return

        cocktail = self.cocktail_db.get_cocktail_details(cocktail_naam)
        if cocktail:
            for drink in cocktail:
                messagebox.showinfo("Details",
                                    "Naam: " + drink["strDrink"] + "\n"
                                    "Categorie: " + drink["strCategory"] + "\n"
                                    "Glas: " + drink["strGlass"] + "\n"
                                    "Instructies: " + drink["strInstructions"] + "\n"
                                    "Ingrediënten: " + drink["strIngredient1"] + "\n"
                                    "Afbeelding URL: " + drink["strDrinkThumb"])
        else:
            messagebox.showwarning("Naam error", "Cocktail details niet gevonden. "
                                                 "Controleer de ingevoerde naam.")
