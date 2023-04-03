"""
CSC111 Course Project: Sephora Beauty Matchmaker
This file is Copyright (c) 2023 Vivian Feng, Cailyn Kim, Jainam Shah, and Jennifer Tan.

The following functions use tkinter to create a GUI simulation that the user can interact with and use.
"""
import tkinter as tk  # add to requirements.txt later
from typing import Optional
import initialize
import network


def get_category_input() -> str:
    """Gets the type of product that should be recommended from the user, using a dropdown menu
    """
    # initializing GUI
    category_window = tk.Tk()
    category_window.title("Sephora Recommender")
    category_window.geometry("500x500")  # changes the size

    label = tk.Label(text="What kind of products would you like recommended?")
    label.pack()

    category_options = initialize.pass_category_list()
    # option that is chosen by the user
    clicked = tk.StringVar(category_window)
    # initial text
    clicked.set(category_options[0])
    # creating the dropdown menu
    drop = tk.OptionMenu(category_window, clicked, *category_options)
    drop.pack()
    # submit button, closes the window when clicked
    submit_button = tk.Button(category_window, text='Next', command=category_window.destroy)
    submit_button.pack()
    category_window.mainloop()

    # gets the submitted option
    return clicked.get()


def get_skin_type_input() -> str:
    """Gets the type of skin type the user has
    This function has similar structure to get_product_input()
    """
    skin_type_window = tk.Tk()
    skin_type_window.title("Sephora Recommender")
    skin_type_window.geometry("500x500")
    label = tk.Label(text="What's your skin type?")
    label.pack()
    skin_type_options = ["dry", "oily", "combination"]
    clicked = tk.StringVar(skin_type_window)
    clicked.set(skin_type_options[0])
    drop = tk.OptionMenu(skin_type_window, clicked, *skin_type_options)
    drop.pack()
    submit_button = tk.Button(skin_type_window, text='Next', command=skin_type_window.destroy)
    submit_button.pack()
    skin_type_window.mainloop()
    return clicked.get()


def get_budget_input() -> int:
    """Gets the user's budget
    """
    budget_window = tk.Tk()
    budget_window.title("Sephora Recommender")
    budget_window.geometry("500x500")
    label = tk.Label(text="What's your budget? Choose an amount in $.")
    label.pack()
    budget_options = [
        "$50",
        "$100",
        "$150",
        "$200+"
    ]
    clicked = tk.StringVar(budget_window)
    clicked.set(budget_options[0])
    drop = tk.OptionMenu(budget_window, clicked, *budget_options)
    drop.pack()
    submit_button = tk.Button(budget_window, text='Next', command=budget_window.destroy)
    submit_button.pack()
    budget_window.mainloop()
    if clicked.get() == "$50":
        return 50
    elif clicked.get() == "$100":
        return 100
    elif clicked.get() == "$150":
        return 150
    else:
        return 200


def get_brand_input() -> Optional[str]:
    """Gets a specific brand that the user wants to search for
    If the user chooses to search for any brand, returns None
    """
    brand_window = tk.Tk()
    brand_window.title("Sephora Recommender")
    brand_window.geometry("500x500")
    label = tk.Label(text="Finally, is there a brand you're looking for?")
    label.pack()
    brand_options = initialize.pass_brands_list()
    brand_options.insert(0, "All brands")
    clicked = tk.StringVar(brand_window)
    clicked.set("All brands")
    drop = tk.OptionMenu(brand_window, clicked, *brand_options)
    drop.pack()
    submit_button = tk.Button(brand_window, text='Search for skincare!', command=brand_window.destroy)
    submit_button.pack()
    brand_window.mainloop()
    if clicked.get() == "All brands":
        return None
    else:
        return clicked.get()


def get_output(recommended_products: list[network.Product]) -> None:
    """
    Displays the recommended products for the user
    """
    output_window = tk.Tk()
    output_window.title("Sephora Recommender")
    output_window.geometry("500x500")
    label = tk.Label(text="We've found some products that you might like:")
    label.pack()
    for product in recommended_products:
        tk.Label(text=product.brand + ", " + product.name + ", $" + str(product.price)).pack()
    submit_button = tk.Button(output_window, text='Done', command=output_window.destroy)
    submit_button.pack()
    output_window.mainloop()


if __name__ == '__main__':
    import python_ta

    python_ta.check_all(config={
        'max-line-length': 120,
        'extra-imports': ['tkinter', 'initialize', 'network'],
    })
