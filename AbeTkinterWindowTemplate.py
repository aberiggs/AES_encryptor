#Author: Abe "N0wh3r3" Riggs; Version: 1.0
from tkinter import *

class EncryptorProgram():
    def __init__(self):
        window = Tk()
        window.title("Encryption GUI ~ By N0wh3r3")
        window.configure(background='#303030')
        window.geometry('768x500')
        window.resizable(width=False, height=False)
        title = Label(window, text="GUI Encryptor", background='#303030', font="helvetica 30 bold")
        title.pack()

        warning = Label(text="WARNING: All spaces in passwords will be deleted!", \
                                    font="Times 20 bold", fg='#eeee41', background='#303030')
        warning.place(x=85, y=180)

        password_text = Label(text="Password", background='#303030', \
                                  font="helvetica 20 italic underline")
        password_text.place(x=325,y=115)

        encrypt_button = Button(text="Encrypt", font="helvetica 20", \
                                height=3, width=10, command=lambda: \
                                self.encrypt_trigger())
        encrypt_button.place(x=50, y=250)

        decrypt_button = Button(text="Decrypt", font="helvetica 20", \
                                height=3, width=10, command=lambda: \
                                self.decrypt_trigger())
        decrypt_button.place(x=560, y=250)

        self.pass_entry = Entry(window, show="x", font="times 15")
        self.pass_entry.place(x=280, y=150)

        window.mainloop()

    def encrypt_trigger(self):
        password = self.pass_entry.get()
        if password != "":
            print("STARTING ENCRYPTION")
            password = password.replace(" ", "")
            print("WITH PASSWORD:", end=" ")
            var = 1
            for i in range(int(len(password)/2)+1):
                print("*", end="")
                if var < len(password):
                    print(password[var], end="")
                    var = var+2
            print()

        else:
            print("Invalid Password")

    def decrypt_trigger(self):
        password = self.pass_entry.get()
        if password != "":
            password = password.replace(" ", "")
            print("STARTING DECRYPTION")
            print("WITH PASSWORD:", end=" ")
            var = 1
            for i in range(int(len(password)/2)+1):
                print("*", end="")
                if var < len(password):
                    print(password[var], end="")
                    var = var+2
            print()

        else:
            print("Invalid Password")

def main():
    program_instance = EncryptorProgram()
    

main()
