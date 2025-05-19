import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import *
from tkinter import PhotoImage
from PIL import Image, ImageTk

# Variables for the colors of the GUI
bg_color = "black"
fg_color = "white"
button_color = "red"
button_color_hover = "lightgreen"
button_color_active = "blue"
button_color_active_hover = "green"

# Create the main window
window=tk.Tk()
window.geometry("1200x1000")
window.title("Discount Dominos")
window.config(bg="#000000")

# Create a Notebook widget
notebook = ttk.Notebook(window)

# Create frames for each tab
Homepage = ttk.Frame(notebook, style="Custom.TFrame")
Deals = ttk.Frame(notebook, style="Custom.TFrame")
Pizza = ttk.Frame(notebook, style="Custom.TFrame")
Sides = ttk.Frame(notebook, style="Custom.TFrame")
Deals = ttk.Frame(notebook, style="Custom.TFrame")
Drinksdesserts = ttk.Frame(notebook, style="Custom.TFrame")

# Define the style for the notebook
style=ttk.Style()
style.configure("Custom.TFrame", background=bg_color)

# Add tabs to the notebook
notebook.add(Homepage, text="Homepage")
notebook.add(Deals, text="Deals")
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

def switch_to_deals():
    notebook.select(Deals)

# Adding content to the Homepage tab that will have buttons to switch between tabs
Homepage_label = tk.Label(Homepage, text="Welcome to the Discount Dominos", font=("Arial", 24), bg=button_color_active, fg=fg_color)
Homepage_label.pack(pady=20)

button_to_deals = tk.Button(Homepage, text="Deals", command=switch_to_deals, bg=button_color, fg=fg_color)
button_to_deals.pack(pady=10)

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

button_to_homepage = tk.Button(Deals, text="Back to Homepage", command=switch_to_homepage, bg=button_color, fg=fg_color)
button_to_homepage.pack(pady=10)

# dictionary to store the cart items
cart = {}

# Function to add items to the cart
def add_to_cart(item_name, quantity):
    if quantity <= 0:
        messagebox.showerror("Error", "Quantity must be at least 1")
        return
    cart[item_name] = cart.get(item_name, 0) + quantity
    messagebox.showinfo("Added to Cart", f"{quantity} x {item_name} added to cart")

# dictionary to select the quantity of the items
quantity_selectors = []

# Function to create quantity selector
def create_quantity_selector(parent, item_name):
    frame = tk.Frame(parent, bg=bg_color)
    frame.pack(pady=10)

    label = tk.Label(frame, text=item_name, font=("Arial", 16), bg=bg_color, fg=fg_color)
    label.pack(side=tk.LEFT)

    quantity_var = tk.IntVar(value=1)
    quantity_entry = tk.Entry(frame, textvariable=quantity_var, width=5)
    quantity_entry.pack(side=tk.LEFT)

    button = tk.Button(frame, text="Add to Cart", command=lambda: add_to_cart(item_name, quantity_var.get()), bg=button_color, fg=fg_color)
    button.pack(side=tk.LEFT)

    quantity_selectors.append(quantity_var)

# Dictionary to store the deals
deals = {
    "Deal 1": "Buy 1 Pizza, Get 1 Free",
    "Deal 2": "20% Off on Orders Above $50",
    "Deal 3": "Free Sides with Any Large Pizza",
    "Deal 4": "Buy 2 Desserts, Get 1 Free",
    "Deal 5": "Free Drink with Any Pizza Order"
}

# Adding the deals to the Deals tab
Deals_label = tk.Label(Deals, text="Deals", font=("Arial", 24), bg=bg_color, fg=fg_color)

# Adding the menu items
Pizza_label = tk.Label(Pizza, text="Pizza Menu", font=("Arial", 24), bg=bg_color, fg=fg_color)
Pizza_label.pack(pady=20)

Sides_label = tk.Label(Sides, text="Sides Menu", font=("Arial", 24), bg=bg_color, fg=fg_color)
Sides_label.pack(pady=20)

Desserts_label = tk.Label(Drinksdesserts, text="Desserts Menu", font=("Arial", 24), bg=bg_color, fg=fg_color)
Desserts_label.pack(pady=20)


pizza_menu = [
    ("Margherita", "$11.99"),
    ("Pepperoni Classic", "$14.99"),
    ("Buffalo Chicken", "$17.99"),
    ("Vegeterian Delight", "$16.00"),
    ("Meat Lovers", "$19.99"),
    ("Hawaiian", "$16.40")
]

sides_menu = [
    ("Curly Fries", "$3.99"),
    ("Garlic Bread", "$4.99"),
    ("Cheesy Bread", "$5.99"),
    ("Chicken Wings", "$8.99"),
    ("Salad", "$6.99"),
]

Desserts_menu = [	
    ("Classic Tiramisu", "$11.50"),
    ("Chocolate Lava Cake", "$13.50"),
    ("Cannoli", "$9.99"),
    ("New York Cheesecake", "$11.50"),
    ("Zeppole (Italian Doughnuts)", "$9.99"),
    ("Gelato", "$13.99")
]
Drinks_menu = [
    ("Italian Soda", "$7.50"),
    ("Limoncello", "$5.95"),
    ("Sprite", "$4.50"),
    ("Coke", "$4.50")
]

# dictionary to store the menu prices
menu_prices = {
    "Margherita": 11.99,
    "Pepperoni Classic": 14.99,
    "Buffalo Chicken": 17.99,
    "Vegeterian Delight": 16.00,
    "Meat Lovers": 19.99,
    "Hawaiian": 16.40,
    "Curly Fries": 3.99,
    "Garlic Bread": 4.99,
    "Cheesy Bread": 5.99,
    "Chicken Wings": 8.99,
    "Salad": 6.99,
    "Classic Tiramisu": 11.50,
    "Chocolate Lava Cake": 13.50,
    "Cannoli": 9.99,
    "New York Cheesecake": 11.50,
    "Zeppole (Italian Doughnuts)": 9.99,
    "Gelato": 13.99,
    "Italian Soda": 7.50,
    "Limoncello": 5.95,
    "Sprite": 4.50,
    "Coke": 4.50
}

# Function to create labels for deals
def create_deal_labels(deals, parent):
    for deal, description in deals.items():
        label = tk.Label(parent, text=f"{deal}: {description}", font=("Arial", 16), bg=bg_color, fg=fg_color)
        label.pack(pady=10)

# Function to create labels for menu items
def create_menu_labels(menu, parent):
    for item, price in menu:
        label = tk.Label(parent, text=f"{item}: {price}", font=("Arial", 16), bg=bg_color, fg=fg_color)
        label.pack(pady=10)
create_menu_labels(pizza_menu, Pizza)
create_menu_labels(sides_menu, Sides)
create_menu_labels(Desserts_menu, Drinksdesserts)
create_menu_labels(deals.items(), Deals)

Drinks_label = tk.Label(Drinksdesserts, text="Drinks Menu", font=("Arial", 24), bg=bg_color, fg=fg_color)
Drinks_label.pack(pady=20)

create_menu_labels(Drinks_menu, Drinksdesserts)

# Adding spinboxes for quantity selection
for item in pizza_menu:
    create_quantity_selector(Pizza, item[0])

# Adding the logo
logo = Image.open("logo.jpg") 
logo = logo.resize((125, 125))
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo, bg=bg_color)
logo_label.pack()
logo_label.place(x=0, y=23)

window.mainloop()