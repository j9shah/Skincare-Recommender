"""
The following functions use tkinter to create a GUI that the user can interact with
"""
def get_category_input() -> str:
    """
    Gets the type of product that should be recommended from the user, using a dropdown menu
    """
    # initializing GUI
    category_window = tk.Tk()
    category_window.title("Skincare Reccomender")
    category_window.geometry("500x500")  # changes the size

    label = tk.Label(text="What kind of products would you like reccomended?")
    label.pack()

    category_options = [  # sample ones for now
        "Serum",
        "Moisturizer",
        "Sunscreen",
        "Toner",
        "Masks",
        "Eyecreams",
        "Cleansers"
    ]
    # option that is chosen by the user
    clicked = tk.StringVar(category_window)
    # initial text
    clicked.set("Serum")
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
    """
    Gets the type of skin type the user has
    This function has similar structure to get_product_input()
    """
    skin_type_window = tk.Tk()
    skin_type_window.title("Skincare Reccomender")
    skin_type_window.geometry("500x500")
    label = tk.Label(text="What's your skin type?")
    label.pack()
    skin_type_options = ["Dry", "Oily", "Combination"]
    clicked = tk.StringVar(skin_type_window)
    clicked.set("Dry")
    drop = tk.OptionMenu(skin_type_window, clicked, *skin_type_options)
    drop.pack()
    submit_button = tk.Button(skin_type_window, text='Next', command=skin_type_window.destroy)
    submit_button.pack()
    skin_type_window.mainloop()
    return clicked.get()


def get_budget_input() -> int:
    """
    Gets the user's budget
    """
    budget_window = tk.Tk()
    budget_window.title("Skincare Reccomender")
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
    clicked.set("$50")
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


def get_output() -> None:
    """
    Displays the output for the user
    """
    output_window = tk.Tk()
    output_window.title("Skincare Reccomender")
    output_window.geometry("500x500")
    label = tk.Label(text="We've found some products that might be g")
    label.pack()
    skin_type_options = ["Dry", "Oily", "Combination"]
    clicked = tk.StringVar(skin_type_window)
    clicked.set("Dry")
    drop = tk.OptionMenu(skin_type_window, clicked, *skin_type_options)
    drop.pack()
    submit_button = tk.Button(skin_type_window, text='Next', command=skin_type_window.destroy)
    submit_button.pack()
    skin_type_window.mainloop()
    return clicked.get()