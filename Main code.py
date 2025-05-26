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
window.title("Pizza House")
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
Cart = ttk.Frame(notebook, style="Custom.TFrame")

# Define the style for the notebook
style=ttk.Style()
style.configure("Custom.TFrame", background=bg_color)

# Add tabs to the notebook
notebook.add(Homepage, text="Homepage")
notebook.add(Deals, text="Deals")
notebook.add(Pizza, text="Pizza")
notebook.add(Sides, text="Sides")
notebook.add(Drinksdesserts, text="Drinks And Desserts")
notebook.add(Cart, text="Cart")
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

def switch_to_cart():
    notebook.select(Cart)

# dictionary to store the cart items
cart = {}

# Create a listbox for the cart display in the cart tab
cart_display = tk.Listbox(Cart, width=50, height=20, bg=bg_color, fg=fg_color)
cart_display.pack(pady=20)

# Function to add items to the cart
def add_to_cart(item_name, quantity):
    if quantity <= 0:
        messagebox.showerror("Error", "Quantity must be at least 1")
        return
    cart[item_name] = cart.get(item_name, 0) + quantity
    messagebox.showinfo("Added to Cart", f"{quantity} x {item_name} added to cart")

# Function to update the cart display
def update_cart_display():
    global cart_display
    # Clear the cart display
    cart_display.delete(0, tk.END)

    # Add items from the cart to the display
    total_price = 0
    for item_name, quantity in cart.items():
        if quantity > 0:
            price = next(price for item, price in (pizza_menu + sides_menu + 
            Desserts_menu + Drinks_menu) if item == item_name)
            total_price += price * quantity
            cart_display.insert(tk.END, f"{item_name} x {quantity} = ${price:.2f} = ${price * quantity:.2f}")
        
    # Add the total price to the display
    cart_display.insert(tk.END, f"Total: ${total_price:.2f}")

    

update_cart_display()

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
Deals_label.pack(pady=20)

# Storing the menu items in a dictionary
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
price = {
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

# Adding the deals to the Deals tab
create_deal_labels(deals, Deals)
Deals_label.pack(pady=20)

# Adding spinboxes for the quantity of each item in the pizza menu
for item_name, price in pizza_menu:
    # Create a frame for each item
    item_frame= tk.Frame(Pizza, bg=bg_color)
    item_frame.pack(pady=10)

    # Display the item name and price
    item_label = tk.Label(item_frame, text=f"{item_name}: {price}", font=("Arial", 16), bg=bg_color, fg=fg_color)
    item_label.pack(side=tk.LEFT, padx=10)

    # create a spinbox for quantity
    quantity_spinbox = tk.Spinbox(item_frame, from_=0, to=10, width=5, bg=button_color, fg=fg_color)
    quantity_spinbox.pack(side=tk.LEFT, padx=10)
    quantity_selectors.append((item_name, quantity_spinbox))
    # create an add to cart button
    add_to_cart_button = tk.Button(
        item_frame,
        text="Add to Cart", 
        command=lambda item=item_name, spinbox=quantity_spinbox: 
        add_to_cart(item, int(spinbox.get())), bg=button_color, 
        fg=fg_color
        )
    add_to_cart_button.pack(side=tk.LEFT, padx=10)
# Adding spinboxes for the quantity of each item in the sides menu
for item_name, price in sides_menu:
    # Create a frame for each item
    item_frame= tk.Frame(Sides, bg=bg_color)
    item_frame.pack(pady=10)

    # Display the item name and price
    item_label = tk.Label(item_frame, text=f"{item_name}: {price}", font=("Arial", 16), bg=bg_color, fg=fg_color)
    item_label.pack(side=tk.LEFT, padx=10)

    # create a spinbox for quantity
    quantity_spinbox = tk.Spinbox(item_frame, from_=0, to=10, width=5, bg=button_color, fg=fg_color)
    quantity_spinbox.pack(side=tk.LEFT, padx=10)
    quantity_selectors.append((item_name, quantity_spinbox))
    # create an add to cart button
    add_to_cart_button = tk.Button(
        item_frame,
        text="Add to Cart", 
        command=lambda item=item_name, spinbox=quantity_spinbox: 
        add_to_cart(item, int(spinbox.get())), bg=button_color, 
        fg=fg_color
        )
    add_to_cart_button.pack(side=tk.LEFT, padx=10)
# Adding spinboxes for the quantity of each item in the desserts menu
for item_name, price in Desserts_menu:
    # Create a frame for each item
    item_frame= tk.Frame(Drinksdesserts, bg=bg_color)
    item_frame.pack(pady=10)

    # Display the item name and price
    item_label = tk.Label(item_frame, text=f"{item_name}: {price}", font=("Arial", 16), bg=bg_color, fg=fg_color)
    item_label.pack(side=tk.LEFT, padx=10)

    # create a spinbox for quantity
    quantity_spinbox = tk.Spinbox(item_frame, from_=0, to=10, width=5, bg=button_color, fg=fg_color)
    quantity_spinbox.pack(side=tk.LEFT, padx=10)
    quantity_selectors.append((item_name, quantity_spinbox))
    # create an add to cart button
    add_to_cart_button = tk.Button(
        item_frame,
        text="Add to Cart", 
        command=lambda item=item_name, spinbox=quantity_spinbox: 
        add_to_cart(item, int(spinbox.get())), bg=button_color, 
        fg=fg_color
        )
    add_to_cart_button.pack(side=tk.LEFT, padx=10)

# Adding the drinks menu heading
Drinks_label = tk.Label(Drinksdesserts, text="Drinks Menu", font=("Arial", 24), bg=bg_color, fg=fg_color)
Drinks_label.pack(pady=20)
# Adding spinboxes for the quantity of each item in the drinks menu
for item_name, price in Drinks_menu:
    # Create a frame for each item
    item_frame= tk.Frame(Drinksdesserts, bg=bg_color)
    item_frame.pack(pady=10)

    # Display the item name and price
    item_label = tk.Label(item_frame, text=f"{item_name}: {price}", font=("Arial", 16), bg=bg_color, fg=fg_color)
    item_label.pack(side=tk.LEFT, padx=10)

    # create a spinbox for quantity
    quantity_spinbox = tk.Spinbox(item_frame, from_=0, to=10, width=5, bg=button_color, fg=fg_color)
    quantity_spinbox.pack(side=tk.LEFT, padx=10)
    quantity_selectors.append((item_name, quantity_spinbox))
    # create an add to cart button
    add_to_cart_button = tk.Button(
        item_frame,
        text="Add to Cart", 
        command=lambda item=item_name, spinbox=quantity_spinbox: 
        add_to_cart(item, int(spinbox.get())), bg=button_color, 
        fg=fg_color
        )
    add_to_cart_button.pack(side=tk.LEFT, padx=10)

# Function to remove items from the cart
def remove_from_cart(item_name):
    if item_name in cart:
        del cart[item_name]
        messagebox.showinfo("Removed from Cart", f"{item_name} removed from cart")
    else:
        messagebox.showerror("Error", f"{item_name} not found in cart")

# Button to remove items from the cart
remove_button = tk.Button(window, text="Remove from Cart", command=lambda: remove_from_cart(item_name), bg=button_color, fg=fg_color)

# Adding a button to view the cart
def view_cart():
    cart_items = "\n".join([f"{item}: {quantity}" for item, quantity in cart.items()])
    if cart_items != "":
        messagebox.showinfo("Cart", cart_items)
    else:
        messagebox.showinfo("Cart", "Your cart is empty")

view_cart_button = tk.Button(window, text="View Cart", command=view_cart, bg=button_color, fg=fg_color)
view_cart_button.pack(pady=10)


# Adding the logo
logo = Image.open("logo.jpg") 
logo = logo.resize((125, 125))
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo, bg=bg_color)
logo_label.pack()
logo_label.place(x=0, y=23)

window.mainloop()