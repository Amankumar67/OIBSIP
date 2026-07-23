"""
===========================================
SecurePass Pro
Advanced Password Generator GUI
Developed by Aman Kumar
===========================================
"""


import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk


from config import *

from generator import generate_password
from strength import check_password_strength
from validator import validate_inputs
from clipboard import copy_password
from history import PasswordHistory



class SecurePassApp:


    def __init__(self, root):

        self.root = root


        # Window Settings

        self.root.title(APP_TITLE)

        self.root.geometry(
            f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}"
        )

        self.root.resizable(
            False,
            False
        )

        self.root.configure(
            bg=BG_COLOR
        )



        # History Object

        self.history = PasswordHistory()



        # Variables

        self.length_value = tk.IntVar(
            value=DEFAULT_PASSWORD_LENGTH
        )


        self.uppercase_var = tk.BooleanVar(
            value=True
        )


        self.lowercase_var = tk.BooleanVar(
            value=True
        )


        self.number_var = tk.BooleanVar(
            value=True
        )


        self.symbol_var = tk.BooleanVar(
            value=True
        )


        self.ambiguous_var = tk.BooleanVar(
            value=False
        )


        self.password_var = tk.StringVar()


        self.show_password_var = tk.BooleanVar(
            value=False
        )



        # Create Menu

        self.create_menu()


       



        # Create GUI

        self.create_widgets()





    # =========================
    # Menu Bar
    # =========================


    def create_menu(self):


        menubar = tk.Menu(
            self.root
        )



        # File Menu

        file_menu = tk.Menu(
            menubar,
            tearoff=0
        )



        file_menu.add_command(

            label="Clear History",

            command=self.clear_history

        )



        file_menu.add_separator()



        file_menu.add_command(

            label="Exit",

            command=self.exit_app

        )



        menubar.add_cascade(

            label="File",

            menu=file_menu

        )




        # Help Menu


        help_menu = tk.Menu(

            menubar,

            tearoff=0

        )



        help_menu.add_command(

            label="About",

            command=self.show_about

        )



        menubar.add_cascade(

            label="Help",

            menu=help_menu

        )



        self.root.config(

            menu=menubar

        )





    # =========================
    # GUI Widgets
    # =========================


    def create_widgets(self):


        title = tk.Label(

            self.root,

            text="🔐 SecurePass Pro",

            font=TITLE_FONT,

            bg=BG_COLOR,

            fg=TEXT_COLOR

        )


        title.pack(

            pady=15

        )



        subtitle = tk.Label(

            self.root,

            text="Secure Cryptographic Password Generator",

            font=LABEL_FONT,

            bg=BG_COLOR,

            fg=SUBTEXT_COLOR

        )


        subtitle.pack()



        self.main_frame = tk.Frame(

            self.root,

            bg=FRAME_COLOR

        )


        self.main_frame.pack(

            padx=25,

            pady=15,

            fill="both",

            expand=True

        )



        # Password Length


        tk.Label(

            self.main_frame,

            text="Password Length",

            font=LABEL_FONT,

            bg=FRAME_COLOR,

            fg=TEXT_COLOR

        ).pack(

            pady=5

        )



        self.length_slider = tk.Scale(

            self.main_frame,

            from_=MIN_PASSWORD_LENGTH,

            to=MAX_PASSWORD_LENGTH,

            orient="horizontal",

            variable=self.length_value,

            command=self.update_length,

            length=350,

            bg=FRAME_COLOR,

            fg=TEXT_COLOR,

            highlightthickness=0

        )


        self.length_slider.pack()



        self.length_label = tk.Label(

            self.main_frame,

            text=f"Length: {DEFAULT_PASSWORD_LENGTH}",

            font=LABEL_FONT,

            bg=FRAME_COLOR,

            fg=SUBTEXT_COLOR

        )


        self.length_label.pack()



        # Options


        options_frame = tk.Frame(

            self.main_frame,

            bg=FRAME_COLOR

        )


        options_frame.pack(

            pady=10

        )



        options = [

            ("Uppercase Letters", self.uppercase_var),

            ("Lowercase Letters", self.lowercase_var),

            ("Numbers", self.number_var),

            ("Symbols", self.symbol_var),

            ("Exclude Ambiguous", self.ambiguous_var)

        ]



        for text, var in options:


            tk.Checkbutton(

                options_frame,

                text=text,

                variable=var,

                font=LABEL_FONT,

                bg=FRAME_COLOR,

                fg=TEXT_COLOR,

                selectcolor=ENTRY_BG

            ).pack(

                anchor="w"

            )


                    # =========================
        # Password Display
        # =========================


        self.password_entry = tk.Entry(

            self.main_frame,

            textvariable=self.password_var,

            font=PASSWORD_FONT,

            justify="center",

            bg=ENTRY_BG,

            fg=TEXT_COLOR,

            width=30,

            show="*"

        )


        self.password_entry.pack(

            pady=10

        )



        # =========================
        # Show Password Checkbox
        # =========================


        self.show_password_check = tk.Checkbutton(

            self.main_frame,

            text="Show Password",

            variable=self.show_password_var,

            command=self.toggle_password,

            font=LABEL_FONT,

            bg=FRAME_COLOR,

            fg=TEXT_COLOR,

            selectcolor=ENTRY_BG

        )


        self.show_password_check.pack()



        # =========================
        # Generate Button
        # =========================


        tk.Button(

            self.main_frame,

            text="Generate Password",

            font=BUTTON_FONT,

            bg=PRIMARY_COLOR,

            fg="white",

            command=self.generate

        ).pack(

            pady=5

        )



        # =========================
        # Strength Label
        # =========================


        self.strength_label = tk.Label(

            self.main_frame,

            text="Strength: --",

            font=LABEL_FONT,

            bg=FRAME_COLOR,

            fg=TEXT_COLOR

        )


        self.strength_label.pack()



        # =========================
        # Strength Progress Bar
        # =========================


        self.strength_bar = ttk.Progressbar(

            self.main_frame,

            length=300,

            mode="determinate",

            maximum=100

        )


        self.strength_bar.pack(

            pady=5

        )



        # =========================
        # Copy Button
        # =========================


        tk.Button(

            self.main_frame,

            text="Copy Password",

            font=BUTTON_FONT,

            command=self.copy

        ).pack(

            pady=5

        )



        # =========================
        # History Section
        # =========================


        tk.Label(

            self.main_frame,

            text="Recent Passwords",

            font=LABEL_FONT,

            bg=FRAME_COLOR,

            fg=TEXT_COLOR

        ).pack()



        self.history_box = tk.Listbox(

            self.main_frame,

            width=35,

            height=5

        )


        self.history_box.pack()



            # =========================
    # Application Functions
    # =========================


    def exit_app(self):

        answer = messagebox.askyesno(

            "Exit",

            "Are you sure you want to exit?"

        )


        if answer:

            self.root.destroy()





    def show_about(self):

        messagebox.showinfo(

            "About SecurePass Pro",

            """
SecurePass Pro

Version: 1.0


Developed by:
Aman Kumar


Technology:

Python
Tkinter
Secrets Module
Pyperclip


Secure Cryptographic Password Generator

© 2026
"""

        )





    def update_length(self, value):

        self.length_label.config(

            text=f"Length: {value}"

        )





    def toggle_password(self):


        if self.show_password_var.get():


            self.password_entry.config(

                show=""

            )


        else:


            self.password_entry.config(

                show="*"

            )





    def generate(self):


        try:


            valid, msg = validate_inputs(

                self.length_value.get(),

                self.uppercase_var.get(),

                self.lowercase_var.get(),

                self.number_var.get(),

                self.symbol_var.get()

            )



            if not valid:


                messagebox.showerror(

                    "Validation Error",

                    msg

                )


                return





            password = generate_password(

                self.length_value.get(),

                self.uppercase_var.get(),

                self.lowercase_var.get(),

                self.number_var.get(),

                self.symbol_var.get(),

                self.ambiguous_var.get()

            )




            # Display Password

            self.password_var.set(password)




            # Strength Check

            strength = check_password_strength(password)



            self.strength_label.config(

                text=f"Strength: {strength['label']}",

                fg=strength["color"]

            )



            score = strength["score"]



            percentage = int(

                (score / 7) * 100

            )



            self.strength_bar["value"] = percentage





            # Auto Copy

            copy_password(password)





            # History Save

            self.history.add_password(password)


            self.update_history()





            messagebox.showinfo(

                "Success",

                "Password generated and copied!"

            )




        except Exception as e:


            messagebox.showerror(

                "Error",

                str(e)

            )







    def copy(self):


        password = self.password_var.get()



        if not password:


            messagebox.showwarning(

                "Warning",

                "Generate password first!"

            )


            return




        success, msg = copy_password(password)




        if success:


            messagebox.showinfo(

                "Copied",

                msg

            )


        else:


            messagebox.showerror(

                "Error",

                msg

            )







    def update_history(self):


        self.history_box.delete(

            0,

            tk.END

        )



        for password in self.history.get_history():


            self.history_box.insert(

                tk.END,

                password

            )







    def clear_history(self):


        self.history.clear_history()



        self.history_box.delete(

            0,

            tk.END

        )



        messagebox.showinfo(

            "History",

            "Password history cleared!"

        )





# =========================
# Application Start
# =========================


if __name__ == "__main__":


    root = tk.Tk()


    app = SecurePassApp(root)


    root.mainloop()