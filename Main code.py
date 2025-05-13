import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import *
from tkinter import PhotoImage
from PIL import Image, ImageTk

# Variables for the colors of the GUI
bg_color = "white"
fg_color = "black"
button_color = "lightblue"
button_color_hover = "lightgreen"
button_color_active = "blue"
button_color_active_hover = "green"

# Create the main window
window=tk.Tk()
window.geometry("1200x1000")
window.title("Pizza Ordering System")
window.config(bg="#f0f0f0")

# Create a Notebook widget
notebook = ttk.Notebook(window)

# Create frames for each tab
Homepage = ttk.Frame(notebook)
Pizza = ttk.Frame(notebook)
Sides = ttk.Frame(notebook)
Drinksdesserts = ttk.Frame(notebook)

# Add tabs to the notebook
notebook.add(Homepage, text="Homepage")
notebook.add(Pizza, text="Pizza")
notebook.add(Sides, text="Sides")
notebook.add(Drinksdesserts, text="Drinks And Desserts")
notebook.pack(expand=True, fill="both")

# Functions for switching between tabs
def switch_to_pizza():
    notebook.select(Pizza)

def switch_to_sides():
    notebook.select(Sides)

def switch_to_drinks_desserts():
    notebook.select(Drinksdesserts)

def switch_to_homepage():
    notebook.select(Homepage)

# Adding content to the Homepage tab that will have buttons to switch between tabs
button_to_pizza = tk.Button(Homepage, text="Pizza", command=switch_to_pizza, bg=button_color, fg=fg_color)
button_to_pizza.pack(pady=10)

button_to_sides = tk.Button(Homepage, text="Sides", command=switch_to_sides, bg=button_color, fg=fg_color)
button_to_sides.pack(pady=10)

button_to_drinks_desserts = tk.Button(Homepage, text="Drinks And Desserts", command=switch_to_drinks_desserts, bg=button_color, fg=fg_color)
button_to_drinks_desserts.pack(pady=10)


# Adding ways to switch back to the homepage from each tab
button_to_homepage = tk.Button(Pizza, text="Back to Homepage", command=switch_to_homepage, bg=button_color, fg=fg_color)
button_to_homepage.pack(pady=10)

button_to_homepage = tk.Button(Sides, text="Back to Homepage", command=switch_to_homepage, bg=button_color, fg=fg_color)
button_to_homepage.pack(pady=10)

button_to_homepage = tk.Button(Drinksdesserts, text="Back to Homepage", command=switch_to_homepage, bg=button_color, fg=fg_color)
button_to_homepage.pack(pady=10)

# Adding the menu items
Pizza_label = tk.Label(Pizza, text="Pizza Menu", font=("Arial", 24), bg=bg_color, fg=fg_color)

pizza_menu = [
    ("Margherita", "$11.99"),
    ("Pepperoni Classic", "$14.99"),
    ("Buffalo Chicken", "$17.99"),
    ("Vegeterian Delight", "$16.00"),
    ("Meat Lovers", "$19.99"),
    ("Hawaiian", "$16.40")
]

for item, price in pizza_menu:
    label = tk.Label(Pizza, text=f"{item}: {price}", font=("Arial", 16), bg=bg_color, fg=fg_color)
    label.pack(pady=10)
# Adding the logo
logo = Image.open("logo.jpg") 
logo = logo.resize((125, 125))
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo, bg=bg_color)
logo_label.pack()
logo_label.place(x=0, y=23)

window.mainloop()
