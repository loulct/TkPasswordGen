import random
import string
from tkinter import (
    BooleanVar,
    Button,
    Checkbutton,
    Entry,
    Frame,
    IntVar,
    Spinbox,
    StringVar,
    Tk,
)


class Interface(Frame):
    """ """

    def __init__(self, window, **kwargs):
        """ """
        Frame.__init__(self, window, **kwargs)

        self.length_default = IntVar(value=16)
        self.length = Spinbox(window, from_=0, to=26, textvariable=self.length_default)
        self.length.pack()

        self.check_digits = BooleanVar()
        self.check_digits.set(True)
        self.check_lowercase = BooleanVar()
        self.check_lowercase.set(True)
        self.check_uppercase = BooleanVar()
        self.check_uppercase.set(True)
        self.check_special = BooleanVar()
        self.check_special.set(False)

        self.digits = Checkbutton(
            window,
            text="Digits [ 0 1 2 3 4 5 6 7 8 9 ]",
            variable=self.check_digits,
            onvalue=True,
            offvalue=False,
        )
        self.digits.pack()
        self.lowercase = Checkbutton(
            window,
            text="Lowercase letters [ a b c ... x y z ]",
            variable=self.check_lowercase,
            onvalue=True,
            offvalue=False,
        )
        self.lowercase.pack()
        self.uppercase = Checkbutton(
            window,
            text="Uppercase letters [ A B C ... X Y Z ]",
            variable=self.check_uppercase,
            onvalue=True,
            offvalue=False,
        )
        self.uppercase.pack()
        self.special = Checkbutton(
            window,
            text="Special characters [ ~ ! @ # $ % ^ & * ( ) - _ = + [ ] { } ; : , . < > / ? | ]",
            variable=self.check_special,
            onvalue=True,
            offvalue=False,
        )
        self.special.pack()
        self.generate_btn = Button(window, text="Generate", command=self.generate)
        self.generate_btn.pack()
        self.value = StringVar()
        self.output = Entry(window, textvariable=self.value, width=30)
        self.output.pack()

    def generate(self):
        """ """
        password = []
        chars = []

        if self.check_digits.get():
            chars.append(string.digits)
        if self.check_lowercase.get():
            chars.append(string.ascii_lowercase)
        if self.check_uppercase.get():
            chars.append(string.ascii_uppercase)
        if self.check_special.get():
            chars.append(string.punctuation)

        if len(chars) > 0:
            for index in range(int(self.length.get())):
                password.append(random.choice(chars[random.randint(0, len(chars) - 1)]))

            self.value.set("".join(password))


window = Tk()
window.title("Password generator")
interface = Interface(window)
interface.mainloop()
