import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import *
from tkinter import PhotoImage
from PIL import Image, ImageTk
from functools import partial

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
window.title("Doominos")
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
Checkout = ttk.Frame(notebook, style="Custom.TFrame")

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
notebook.add(Checkout, text="Checkout")
notebook.pack(expand=True, fill="both")

# adding a confirmation dialog when closing the window
def on_closing():
    if messagebox.askokcancel("Exit the program",
                             "Are you sure you want to exit?"):
        window.destroy()
window.protocol("WM_DELETE_WINDOW", on_closing)

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

def switch_to_checkout():
    notebook.select(Checkout)

# Dictionary to store the cart items
cart = {}

# Create a label for the cart tab
Cart_label = tk.Label(Cart, text="Your Cart", font=("Arial", 24),
                        bg=button_color_active, fg=fg_color)
Cart_label.pack(pady=20)

# Create a listbox for the cart display in the cart tab
cart_display = tk.Listbox(Cart, width=50, height=20, bg=bg_color, fg=fg_color)
cart_display.pack(pady=20)

# Function to add items to the cart
def add_to_cart(item_name, quantity):
    try:
        quantity = int(quantity)  # Ensure quantity is an integer
        if quantity <= 0:
            messagebox.showerror("Error", "Quantity must be at least 1")
            return
        current_quantity = cart.get(item_name, 0)
        if current_quantity + quantity > 100:  # Check if quantity exceeds 100
            messagebox.showerror("Error", "Quantity cannot exceed 100")
            return
        cart[item_name] = current_quantity + quantity
        messagebox.showinfo("Added to Cart",
         f"{quantity} x {item_name} added to cart")
        update_cart_display()  # Refresh the cart display after adding an item
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid quantity")

# Function to update the cart display
def update_cart_display():
    global cart_display, discounted_price
    # Clear the cart display
    cart_display.delete(0, tk.END)

    # Add items from the cart to the display
    total_price = 0
    for item_name, quantity in cart.items():
        if quantity > 0:
            # Fetch the price from the price dictionary
            item_price = price.get(item_name,
                                    0) if "Free" not in item_name else 0
            total_price += item_price * quantity
            cart_display.insert(
                tk.END, 
                f"{item_name} x {quantity} = ${item_price:.2f} = ${item_price 
                * quantity:.2f}"
                )

    # Add the discounted price if applicable
    if 'discounted_price' in globals() and discounted_price is not None:
        cart_display.insert(tk.END,
         f"Total after discount: ${discounted_price:.2f}")
        
    # Add the total price to the display
    cart_display.insert(tk.END, f"Total: ${total_price:.2f}")

    

update_cart_display()

# Adding content to the Homepage tab that has buttons to switch between tabs
Homepage_label = tk.Label(Homepage, text="Welcome to Doominos",
                           font=("Arial", 24), bg=button_color_active,
                             fg=fg_color)
Homepage_label.pack(pady=20)

button_to_deals = tk.Button(Homepage, text="Deals", command=switch_to_deals,
                             bg=button_color, fg=fg_color)
button_to_deals.pack(pady=10)

button_to_pizza = tk.Button(Homepage, text="Pizza", command=switch_to_pizza,
                             bg=button_color, fg=fg_color)
button_to_pizza.pack(pady=10)

button_to_sides = tk.Button(Homepage, text="Sides", command=switch_to_sides,
                             bg=button_color, fg=fg_color)
button_to_sides.pack(pady=10)

button_to_drinks_desserts = tk.Button(Homepage, text="Drinks And Desserts",
                                       command=switch_to_drinks_desserts,
                                         bg=button_color, fg=fg_color)
button_to_drinks_desserts.pack(pady=10)

view_cart_button = tk.Button(Homepage, text="View Cart",
                              command=switch_to_cart, bg=button_color,
                                fg=fg_color)
view_cart_button.pack(pady=10)

# Adding ways to switch back to the homepage from each tab
button_to_homepage = tk.Button(Pizza, text="Back to Homepage",
                                command=switch_to_homepage, bg=button_color,
                                  fg=fg_color)
button_to_homepage.pack(pady=10)

button_to_homepage = tk.Button(Sides, text="Back to Homepage",
                                command=switch_to_homepage, bg=button_color,
                                  fg=fg_color)
button_to_homepage.pack(pady=10)

button_to_homepage = tk.Button(Drinksdesserts, text="Back to Homepage",
                                command=switch_to_homepage, bg=button_color,
                                  fg=fg_color)
button_to_homepage.pack(pady=10)

button_to_homepage = tk.Button(Deals, text="Back to Homepage",
                                command=switch_to_homepage, bg=button_color,
                                  fg=fg_color)
button_to_homepage.pack(pady=10)

button_to_homepage = tk.Button(Cart, text="Continue Shopping",
                                command=switch_to_homepage, bg=button_color,
                                  fg=fg_color)
button_to_homepage.pack(pady=10)


# dictionary to select the quantity of the items
quantity_selectors = []

# Function to create quantity selector
def create_quantity_selector(parent, item_name):
    frame = tk.Frame(parent, bg=bg_color)
    frame.pack(pady=10)

    label = tk.Label(frame, text=item_name, font=("Arial", 16), bg=bg_color,
                      fg=fg_color)
    label.pack(side=tk.LEFT)

    quantity_var = tk.IntVar(value=1)
    quantity_entry = tk.Entry(frame, textvariable=quantity_var, width=5)
    quantity_entry.pack(side=tk.LEFT)

    button = tk.Button(frame, text="Add to Cart", command=lambda:
                        add_to_cart(item_name, quantity_var.get()),
                          bg=button_color, fg=fg_color)
    button.pack(side=tk.LEFT)

    quantity_selectors.append(quantity_var)

# Dictionary to store the deals
deals = {
    "Deal 1": "Buy 1 Pizza, Get 1 Free",
    "Deal 2": "20% Off on Orders Above $50",
    "Deal 3": "Free Sides with Any Pizza",
    "Deal 4": "Buy 2 Desserts, Get 1 Free",
    "Deal 5": "Free Drink with Any 2 Pizzas"
}

# Adding the deals to the Deals tab
Deals_label = tk.Label(Deals, text="Deals", font=("Arial", 24),
                        bg=button_color_active, fg=fg_color)
Deals_label.pack(pady=20)

# Storing the menu items in a dictionary
Pizza_label = tk.Label(Pizza, text="Pizza Menu", font=("Arial", 24),
                        bg=button_color_active, fg=fg_color)
Pizza_label.pack(pady=20)

Sides_label = tk.Label(Sides, text="Sides Menu", font=("Arial", 24),
                        bg=button_color_active, fg=fg_color)
Sides_label.pack(pady=20)

Desserts_label = tk.Label(Drinksdesserts, text="Desserts Menu",
                           font=("Arial", 24), bg=button_color_active,
                            fg=fg_color)
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
        label = tk.Label(parent, text=f"{deal}: {description}",
                          font=("Arial", 16), bg=bg_color, fg=fg_color)
        label.pack(pady=10)

# Adding the deals to the Deals tab
create_deal_labels(deals, Deals)
Deals_label.pack(pady=20)

# Adding spinboxes for the quantity of each item in the pizza menu
for item_name, item_price in pizza_menu:
    # Create a frame for each item
    item_frame = tk.Frame(Pizza, bg=bg_color)
    item_frame.pack(pady=10)

    # Display the item name and price
    item_label = tk.Label(item_frame, text=f"{item_name}: {item_price}",
                           font=("Arial", 16), bg=bg_color, fg=fg_color)
    item_label.pack(side=tk.LEFT, padx=10)

    # Create a spinbox for quantity
    quantity_spinbox = tk.Spinbox(item_frame, from_=0, to=10, width=5,
                                   bg=button_color, fg=fg_color,
                                   validate="key",
                                    validatecommand=(
                                        window.register(lambda v: v.isdigit()),
                                         '%P'))
    quantity_spinbox.pack(side=tk.LEFT, padx=10)
    quantity_selectors.append((item_name, quantity_spinbox))

    # Create an add-to-cart button
    add_to_cart_button = tk.Button(
        item_frame,
        text="Add to Cart",
        command=lambda item=item_name, spinbox=quantity_spinbox:
          add_to_cart(item, int(spinbox.get())),
        bg=button_color,
        fg=fg_color
    )
    add_to_cart_button.pack(side=tk.LEFT, padx=10)

# Adding spinboxes for the quantity of each item in the sides menu
for item_name, item_price in sides_menu:  # Renamed 'price' to 'item_price'
    # Create a frame for each item
    item_frame = tk.Frame(Sides, bg=bg_color)
    item_frame.pack(pady=10)

    # Display the item name and price
    item_label = tk.Label(item_frame, text=f"{item_name}: {item_price}",
                           font=("Arial", 16), bg=bg_color, fg=fg_color)
    item_label.pack(side=tk.LEFT, padx=10)

    # Create a spinbox for quantity
    quantity_spinbox = tk.Spinbox(item_frame, from_=0, to=10, width=5,
                                   bg=button_color, fg=fg_color,
                                   validate="key", validatecommand=(
                                    window.register(lambda v: v.isdigit()),
                                     '%P'))
    quantity_spinbox.pack(side=tk.LEFT, padx=10)
    quantity_selectors.append((item_name, quantity_spinbox))

    # Create an add-to-cart button
    add_to_cart_button = tk.Button(
        item_frame,
        text="Add to Cart",
        command=lambda item=item_name, spinbox=quantity_spinbox:
          add_to_cart(item, int(spinbox.get())),
        bg=button_color,
        fg=fg_color
    )
    add_to_cart_button.pack(side=tk.LEFT, padx=10)

# Adding spinboxes for the quantity of each item in the desserts menu
for item_name, item_price in Desserts_menu:
    # Create a frame for each item
    item_frame = tk.Frame(Drinksdesserts, bg=bg_color)
    item_frame.pack(pady=10)

    # Display the item name and price
    item_label = tk.Label(item_frame, text=f"{item_name}: {item_price}",
                           font=("Arial", 16), bg=bg_color, fg=fg_color)
    item_label.pack(side=tk.LEFT, padx=10)

    # Create a spinbox for quantity
    quantity_spinbox = tk.Spinbox(item_frame, from_=0, to=10, width=5,
                                   bg=button_color, fg=fg_color,
                                   validate="key", 
                                   validatecommand=(
                                    window.register(lambda v: v.isdigit()), 
                                    '%P'))
    quantity_spinbox.pack(side=tk.LEFT, padx=10)
    quantity_selectors.append((item_name, quantity_spinbox))

    # Create an add-to-cart button
    add_to_cart_button = tk.Button(
        item_frame,
        text="Add to Cart",
        command=lambda item=item_name, spinbox=quantity_spinbox: add_to_cart(
            item, int(spinbox.get())
            ),
        bg=button_color,
        fg=fg_color
    )
    add_to_cart_button.pack(side=tk.LEFT, padx=10)

# Adding the drinks menu heading
Drinks_label = tk.Label(Drinksdesserts, text="Drinks Menu", font=("Arial", 24),
                         bg=button_color_active, fg=fg_color)
Drinks_label.pack(pady=20)

# Adding spinboxes for the quantity of each item in the drinks menu
for item_name, item_price in Drinks_menu:
    # Create a frame for each item
    item_frame= tk.Frame(Drinksdesserts, bg=bg_color)
    item_frame.pack(pady=10)

    # Display the item name and price
    item_label = tk.Label(item_frame, text=f"{item_name}: {item_price}",
                           font=("Arial", 16), bg=bg_color, fg=fg_color)
    item_label.pack(side=tk.LEFT, padx=10)

    # create a spinbox for quantity
    quantity_spinbox = tk.Spinbox(item_frame, from_=0, to=10, width=5,
                                   bg=button_color, fg=fg_color,
                                   validate="key", validatecommand=(
                                    window.register(lambda v: v.isdigit()),
                                     '%P'))
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

# Function to allow selecting of sides if given free sides as a part of a deal
def show_selection(deal_name, options):
    # Create a new window for deals selection
    selection = tk.Toplevel(window)
    selection.title("Select Your Free Item")
    selection.geometry("400x300")
    selection.config(bg=bg_color)
    
    # Create a label for the selection
    freeitem_label = tk.Label(selection, text="Select Your Free Item:",
                         font=("Arial", 16), bg=bg_color, fg=fg_color)
    freeitem_label.pack(pady=10)

    # Create a listbox for the selection
    selection_listbox = tk.Listbox(selection, font="Arial",
                         bg=bg_color, fg=fg_color)
    for item_name, item_price in zip(
        options, [price.get(item, 0) for item in options]
        ):
        selection_listbox.insert(tk.END, f"{item_name}: {item_price}")
        selection_listbox.pack(pady=10)

    # Create a function to confirm selection
    def confirm_selection(selection, listbox):
        selected_items = listbox.curselection()
        if not selected_items:
            messagebox.showerror("Error", "Please select an item")
            return
        
        # Get the selected item
        selected_item = listbox.get(selected_items[0])
        item_name = selected_item.split(":")[0].strip()
        
        # Add the selected item to the cart
        cart[f"{item_name} (Free)"] = cart.get(f"{item_name} (Free)", 0) + 1
        messagebox.showinfo("Selection Confirmed", f"{item_name} "
        "added to cart\n"
        f"Total amount saved: {calculate_savings(deal_name)} "
        f"with {deal_name}")
        update_cart_display()  # Refresh the cart display after selection
        
        # Close the selection window
        selection.destroy()

    # Create a confirm button
    confirm_button = tk.Button(selection, text="Confirm Selection",
                                 command=lambda: confirm_selection(
                                      selection, selection_listbox),
                                 bg=button_color, fg=fg_color)
    confirm_button.pack(pady=10)


# Creating a unique selection menu based on the deal selected

sides_options = [
    item[0] for item in sides_menu
]

desserts_options = [
    item[0] for item in Desserts_menu
]

pizza_options = [
    item[0] for item in pizza_menu
]

drinks_options = [
    item[0] for item in Drinks_menu
]



applied_deals = set()  # A set to keep track of applied deals

# Function to display how much is saved with the deal applied
savings = 0.0  # Variable to store savings amount
def calculate_savings(deal_name):
    global savings
    if deal_name == "Deal 1":
        # Buy 1 Pizza, Get 1 Free
        savings = price.get(item_name, item_price) if item_name in price else 0
    elif deal_name == "Deal 2":
        # 20% Off on Orders Above $50
        total_price = sum(price.get(item_name, 0) * quantity for item_name,
         quantity in cart.items() if "Free" not in item_name)
        savings = total_price * 0.20 if total_price >= 50 else 0
    elif deal_name == "Deal 3":
        # Free Sides with Any Pizza
        savings = price.get(item_name, item_price) if item_name in price else 0
    elif deal_name == "Deal 4":
        # Buy 2 Desserts, Get 1 Free
        savings = price.get(item_name, item_price) if item_name in price else 0
    elif deal_name == "Deal 5":
        # Free Drink with Any 2 Pizzas
        savings = price.get(item_name, item_price) if item_name in price else 0
    else:
        savings = 0.0

def show_savings(deal_name, savings):
    messagebox.showinfo("Deal Savings",
                         f"You saved ${savings:.2f} with {deal_name}!")

# Function to prevent applying multiple deals at once while applying the deals
def apply_deal(deal_name):
    global applied_deals
    # Check if the deal is already applied
    if deal_name in applied_deals:
        messagebox.showerror("Deal Already Applied", f"{deal_name} is "
        "already applied to your cart")
        return

    # Apply the deal based on its name
    if deal_name == "Deal 1":
        # Buy 1 Pizza, Get 1 Free
        applied = False
        for item_name in cart.keys():
            if item_name in price and item_name in [
                item[0] for item in pizza_menu
                ]:
                options = pizza_options
                show_selection(deal_name, options)
                messagebox.showinfo("Deal Applied", "Deal 1 applied: Buy 1 "
                "Pizza, Get 1 Free")
                applied_deals.add(deal_name)  # Mark the deal as applied
                applied = True
                break
        if not applied:
            messagebox.showerror("Deal Not Applicable", "You must have a "
            "pizza in your cart to apply Deal 1")

    elif deal_name == "Deal 2":
        # 20% Off on Orders Above $50
        total_price = sum(price.get(item_name, 0) * quantity for item_name,
         quantity in cart.items() if "Free" not in item_name)
        if total_price >= 50:
            discount = total_price * 0.20
            global discounted_price
            discounted_price = total_price - discount
            messagebox.showinfo("Deal Applied",
             f"Deal 2 applied: 20% off! You saved: ${discount:.2f}.")
            cart_display.delete(0, tk.END)
            cart_display.insert(tk.END,
             f"Total after discount: ${discounted_price:.2f}")
            applied_deals.add(deal_name)  # Mark the deal as applied
        else:
            messagebox.showerror("Deal Not Applicable", "Total order must "
            "be above $50 to apply Deal 2")

    elif deal_name == "Deal 3":
        # Free Sides with Any Pizza
        applied = False
        for item_name in cart.keys():
            if item_name in price and item_name in [
                item[0] for item in pizza_menu
                ]:
                options = sides_options
                show_selection(deal_name, options)
                messagebox.showinfo("Deal Applied", "Deal 3 applied: Free "
                "Sides with Any Large Pizza")
                applied_deals.add(deal_name)  # Mark the deal as applied
                applied = True
                break
        if not applied:
            messagebox.showerror("Deal Not Applicable", "You must have a "
            "pizza in your cart to apply Deal 3")

    elif deal_name == "Deal 4":
        # Buy 2 Desserts, Get 1 Free
        dessert_count = sum(cart.get(item[0], 0) for item in Desserts_menu)
        if dessert_count >= 2:
            options = desserts_options
            show_selection(deal_name, options)
            messagebox.showinfo("Deal Applied", "Deal 4 applied: Buy 2 "
            "Desserts, Get 1 Free")
            applied_deals.add(deal_name)
        else:
            messagebox.showerror("Deal Not Applicable", "You must have at "
            "least 2 desserts in your cart to apply Deal 4")

    elif deal_name == "Deal 5":
        # Free Drink with Any 2 Pizzas
        pizza_count = sum(cart.get(item[0], 0) for item in pizza_menu)
        if pizza_count >= 2:
            options = drinks_options
            show_selection(deal_name, options)
            messagebox.showinfo("Deal Applied", "Deal 5 applied: Free Drink "
            "with Any 2 Pizzas")
            applied_deals.add(deal_name)
        else:
            messagebox.showerror("Deal Not Applicable", "You must have at "
            "least 2 pizzas in your cart to apply Deal 5")

# Refresh the cart display after applying a deal
    update_cart_display()

# Adding buttons to apply each of the deals
for deal_name in deals.keys():
    deal_button = tk.Button(Deals, text=f"Apply {deal_name}",
                            command=partial(apply_deal, deal_name),
                            bg=button_color, fg=fg_color)
    deal_button.pack(pady=5)

# Creating a checkout button in the cart tab
def checkout():
    if not cart:
        messagebox.showerror("Empty Cart", "Your cart is empty!")
        return
    total_price = sum(price.get(item_name, 0) * quantity for item_name,
     quantity in cart.items() if "Free" not in item_name)
    if 'discounted_price' in globals() and discounted_price is not None:
        total_price = discounted_price
    if messagebox.askyesno("Checkout",
     "Would you like to proceed with the checkout your total is "
     f"${total_price:.2f}?"):
        messagebox.showinfo("Checkout Successful", "Thank you for your order!")
    switch_to_checkout()

# Adding a checkout button to the cart tab
checkout_button = tk.Button(Cart, text="Checkout",
                             command=checkout, bg=button_color,
                               fg=fg_color)
checkout_button.pack(pady=20)

# Adding the checkout tab content
Checkout_label = tk.Label(Checkout, text="Checkout",
                            font=("Arial", 24), bg=button_color_active,
                             fg=fg_color)
Checkout_label.pack(pady=20)

# Adding instructions for the checkout tab
Checkout_instructions = tk.Label(Checkout,
    text="Please review your order and proceed to payment.",
    font=("Arial", 16), bg=bg_color, fg=fg_color)
Checkout_instructions.pack(pady=10)

# Adding a back button to the checkout tab
back_to_cart_button = tk.Button(Checkout, text="Back to Cart",
                                 command=switch_to_cart, bg=button_color,
                                   fg=fg_color)
back_to_cart_button.pack(pady=10)

# Adding payment methods
payment_methods = [
    "Please select", "Credit Card", "Debit Card", "PayPal", "Cash on Delivery"
    ]

# Adding a label for payment methods
payment_label = tk.Label(Checkout, text="Payment Methods",
                          font=("Arial", 18), bg=bg_color, fg=fg_color)
payment_label.pack(pady=10)

# Adding a dropdown menu for payment methods
payment_var = tk.StringVar(value=payment_methods[0])
payment_dropdown = tk.OptionMenu(Checkout, payment_var,
                                   *payment_methods)
payment_dropdown.config(bg=button_color, fg=fg_color)
payment_dropdown.pack(pady=10)

# Adding a confirm payment button
def confirm_payment():
    selected_method = payment_var.get()
    messagebox.showinfo("Payment Confirmed",
     f"Your payment method {selected_method} has been confirmed.")
    

# Function to format expiration date
def format_expiration_date(event, expiration_date_entry):
    # Get the current value of the entry
    current_value = expiration_date_entry.get()

    # Automatically insert '/' after the second character
    if len(current_value) == 2 and not current_value.endswith('/'):
        expiration_date_entry.insert(2, '/')

# Creating a window to enter the payment details for card
def enter_payment_details_card():
    payment_window = tk.Toplevel(window)
    payment_window.title("Enter Payment Details")
    payment_window.geometry("400x300")
    payment_window.config(bg=bg_color)

    # Adding a label for payment details
    payment_details_label = tk.Label(payment_window,
        text="Enter your payment details:", font=("Arial", 16),
        bg=bg_color, fg=fg_color)
    payment_details_label.pack(pady=10)

    # Adding an entry for card number
    card_number_label = tk.Label(payment_window, text="Card Number:",
                                  font=("Arial", 14), bg=bg_color,
                                  fg=fg_color)
    card_number_label.pack(pady=5)
    card_number_entry = tk.Entry(payment_window, width=20)
    card_number_entry.pack(pady=5)

    # Adding an entry for expiration date
    expiration_date_label = tk.Label(payment_window,
        text="Expiration Date (MM/YY):", font=("Arial", 14),
        bg=bg_color, fg=fg_color)
    expiration_date_label.pack(pady=5)
    expiration_date_entry = tk.Entry(payment_window, width=20)
    expiration_date_entry.pack(pady=5)
    expiration_date_entry.bind("<KeyRelease>",
     lambda event: format_expiration_date(event, expiration_date_entry))

    # Adding an entry for CVV
    cvv_label = tk.Label(payment_window, text="CVV:", font=("Arial", 14),
                          bg=bg_color, fg=fg_color)
    cvv_label.pack(pady=5)
    cvv_entry = tk.Entry(payment_window, width=20, show='*')
    cvv_entry.pack(pady=5)

    # Adding a confirm button
    confirm_button = tk.Button(payment_window, text="Confirm",
                                command=lambda: [messagebox.askyesno(
                                    "Payment Details Entered",
                                    "Your payment details have been entered"
                                    " successfully."
                                    " Would you like to proceed?"), 
                                    payment_window.destroy()],
                                bg=button_color, fg=fg_color)
    confirm_button.pack(pady=10)

# Adding a variable to store the PayPal email entry
paypal_email_entry = ""

# Adding a button to enter payment details for PayPal
def enter_payment_details_paypal():
    global paypal_email_entry
    payment_window = tk.Toplevel(window)
    payment_window.title("Enter Payment Details")
    payment_window.geometry("400x300")
    payment_window.config(bg=bg_color)

    # Adding a label for PayPal details
    paypal_label = tk.Label(payment_window,
        text="Enter your PayPal email:", font=("Arial", 16),
        bg=bg_color, fg=fg_color)
    paypal_label.pack(pady=10)

    # Adding an entry for PayPal email
    paypal_email_entry = tk.Entry(payment_window, width=30)
    paypal_email_entry.pack(pady=10)
    
    # Adding a confirm button
    confirm_button = tk.Button(payment_window, text="Confirm",
                                command=lambda: [store_paypal_email(), 
                                messagebox.showinfo("Payment Details Entered",
                                    "Your PayPal email has been entered"
                                    " successfully."),
                                    payment_window.destroy()],
                                bg=button_color, fg=fg_color)
    confirm_button.pack(pady=10)

# Function to store the payment details for paypal email
def store_paypal_email():
    global paypal_email_entry, paypal_email
    paypal_email = paypal_email_entry.get()
    if not paypal_email:
        messagebox.showerror("Error", "Please enter a valid PayPal email")
        return

# Adding a button to enter payment details for cash
def enter_payment_details_cash():
    payment_window = tk.Toplevel(window)
    payment_window.title("Cash on Delivery")
    payment_window.geometry("700x300")
    payment_window.config(bg=bg_color)

    # Adding a label for cash payment
    cash_label = tk.Label(payment_window,
        text="You have selected Cash on Delivery.\n"
        " Please note that change is available only to the nearest dollar.",
         font=("Arial", 16),
        bg=button_color_active, fg=fg_color)
    cash_label.pack(pady=10)

    # Adding a confirm button
    confirm_button = tk.Button(payment_window, text="Confirm",
                                command=lambda: [messagebox.askyesno(
                                    "Payment Method Confirmed",
                                    "Your payment method has been confirmed"
                                    " successfully.\n"
                                    "Would you like to proceed?"),
                                    payment_window.destroy()],
                                bg=button_color, fg=fg_color)
    confirm_button.pack(pady=10)

# Adding a button to enter payment details based on the selected method
def enter_payment_details():
    selected_method = payment_var.get()
    if selected_method == "Credit Card" or selected_method == "Debit Card":
        enter_payment_details_card()
    elif selected_method == "PayPal":
        enter_payment_details_paypal()
    elif selected_method == "Cash on Delivery":
        enter_payment_details_cash()
    else:
        messagebox.showerror("Error", "Please select a valid payment method")
        
# Adding a button to enter payment details
enter_payment_details_button = tk.Button(Checkout,
    text="Enter Payment Details", command=enter_payment_details,
    bg=button_color, fg=fg_color)
enter_payment_details_button.pack(pady=10)

# Function to finish the order
def finish_order():
    if not cart:
        messagebox.showerror("Empty Cart", "Your cart is empty!")
        return
    total_price = sum(price.get(item_name, 0) * quantity for item_name,
     quantity in cart.items() if "Free" not in item_name)

    if 'discounted_price' in globals() and discounted_price is not None:
        total_price = discounted_price
    selected_method = payment_var.get()
    message = "Your order has been placed successfully!\n"
    message += f"Total: ${total_price:.2f}\n"
    message += f"Payment Method: {selected_method}\n"

    if selected_method == "PayPal":
        message += f"PayPal Email: {paypal_email}\n"
    message += "Thank you for ordering from Doominos!"
    validate_details = messagebox.askokcancel("Order Placed", message)
    if validate_details == False:
        return
    else:
        messagebox.showinfo("Order Confirmation", "Your order has been "
        "placed successfully!")
        window.destroy()  # Close the window after finishing the order
        messagebox.showinfo("Thank You",
         "Thank you for ordering from Doominos!")

# Adding a button to finish the order
finish_order_button = tk.Button(Checkout, text="Finish Order",
                             command=finish_order, bg=button_color,
                               fg=fg_color)
finish_order_button.pack(pady=100)

# Adding the logo
logo = Image.open("logo.jpg") 
logo = logo.resize((125, 125))
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo, bg=bg_color)
logo_label.pack()
logo_label.place(x=0, y=23)

window.mainloop()
