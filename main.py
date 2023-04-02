"""
CSC111 Course Project: Skincare Reccomender
Vivian Feng, Cailyn Kim, Jainam Shah, Jennifer Tan
"""
import tkinter as tk  # add to requirements.txt later


# the following functions use tkinter to get input from the user
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


# def get_skin_type_input() -> str:
#     """
#     Gets the type of skin type the user has
#     This function has similar structure to get_product_input()
#     """
#     skin_type_window = tk.Tk()
#     skin_type_window.title("Skincare Reccomender")
#     skin_type_window.geometry("500x500")
#
#     label = tk.Label(text="What's your skin type?")
#     label.pack()
#
#     skin_type_options = [
#         "Serum",
#         "Moisturizer",
#         "Sunscreen",
#         "Toner",
#         "Masks",
#         "Eyecreams",
#         "Cleansers"
#     ]
#     # option that is chosen by the user
#     clicked = tk.StringVar(product_window)
#     # initial text
#     clicked.set("Serum")
#     # creating the dropdown menu
#     drop = tk.OptionMenu(product_window, clicked, *product_options)
#     drop.pack()
#     # submit button, closes the window when clicked
#     submit_button = tk.Button(product_window, text='Next', command=product_window.destroy)
#     submit_button.pack()
#     product_window.mainloop()
#
#     # gets the submitted option
#     return clicked.get()





if __name__ == '__main__':
    # Loading in csv files
    product = get_category_input()
