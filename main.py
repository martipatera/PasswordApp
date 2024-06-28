import tkinter as tk
import random
import os
import tkinter.font as tkFont
#both passwords should be 16 char long!!!

filename = "MyPasswords.txt"


def Main():
    
    
    for buttons in window.winfo_children():
        buttons.destroy()
    showmypasswords = tk.Button(window, text="My Passwords", height=5, width=20, command=MyPasswords)
    showmypasswords.pack(pady=50)

    charactersandnumbers = tk.Button(window, text="Generete Characters and Numbers", height=5, width=20, command=CharactersAndNumbers)
    charactersandnumbers.pack(pady=50)

    charactersandsymbols = tk.Button(window, text="Generate Characters, Numbers\n and Symbols", height=5, width=20, command=CharactersNumbersAndSymbols)
    charactersandsymbols.pack(pady=50)

def MyPasswords():
    global text
    linescount = 0
        
    for buttons in window.winfo_children():
        buttons.destroy()
        
    text_box = tk.Text(window, wrap='word', height=5, width=50, font=myfont, bg="#ffffff", fg="#000000")
    text_box.pack(pady=250)
    
    mainmenubutton = tk.Button(window, text="Main Menu",command=Main, height=5, width=50)
    mainmenubutton.pack()
        
        
    if os.path.exists(filename):
        if os.path.getsize(filename) == 0:
            text = tk.Label(window, text="No Passwords Yet!")
            text.pack()

        else:
            with open(filename, "r") as file:
                text_box.delete("1.0", tk.END)
                for index, line in enumerate(file):
                    linescount += 1
                    passwords = line.strip()
                    text_box.config(height=linescount, padx= 10, pady=10)
                    
                    
                    if index == 0:
                        text_box.insert(tk.END, passwords)
                        
                        
                    else:
                        text_box.insert(tk.END,"\n"+passwords)
 
    else:
        with open(filename, "w") as file:
            pass
      

def CharactersAndNumbers():
    
    
    for buttons in window.winfo_children():
        buttons.destroy()
    
    
    passwordname = tk.Text(window, width=30,height=1 ,bg="#ffffff", highlightbackground="#000000", highlightthickness=1,fg="#000000", font=myfont)
    passwordname.pack(pady=50)
    
    genereatepassword = tk.Button(window, text="Generate", width=25, height=5, command=GeneratePasswordNums)
    genereatepassword.pack()
    
    mainmenubutton = tk.Button(window, text="Main Menu",command=Main, width=50, height=5)
    mainmenubutton.pack()
    
 

def CharactersNumbersAndSymbols():
    
    
    for buttons in window.winfo_children():
        buttons.destroy()
    
    passwordname = tk.Text(window, width=30,height=1, bg="#ffffff", highlightbackground="#000000", highlightthickness=1, fg="#000000",font=myfont)
    passwordname.pack(pady=50)
    
    genereatepassword = tk.Button(window, text="Generate", width=25, height=5, command=GeneratePasswordSym)
    genereatepassword.pack()
    
    mainmenubutton = tk.Button(window, text="Main Menu",command=Main, width=50, height=5)
    mainmenubutton.pack()
    
 
def GeneratePasswordNums():
    for buttons in window.winfo_children():
        buttons.destroy()
        
    password = ""
    for i in range(1, 17):
        randomnumber = random.randrange(len(charectersandnumbers))
        password = password + charectersandnumbers[randomnumber]
    with open (filename, "a") as file:
        file.writelines(password+ "\n")
        
    
    
    mainmenubutton = tk.Button(window, text="Main Menu",command=Main, height=5, width=50)
    mainmenubutton.pack()
    
    password_box = tk.Text(window,height=1,width=50,font=myfont, bg="#ffffff", fg="#000000")
    password_box.pack(pady=50)
    password_box.delete("1.0", tk.END)
    password_box.insert(tk.END,password)
    password = ""
    
    
    
    
    
    
def GeneratePasswordSym():
    for buttons in window.winfo_children():
        buttons.destroy()
    
    
    password = "" 
    for i in range(1, 17):
        randomnumber = random.randrange(len(charactersnumberssymbols))
        password = password + charactersnumberssymbols[randomnumber]
    
       
    with open (filename, "a") as file:
        file.writelines(password + "\n")
        
    mainmenubutton = tk.Button(window, text="Main Menu",command=Main, height=5, width=50)
    mainmenubutton.pack()   
    
    password_box = tk.Text(window,height=1,width=50,font=myfont, bg="#ffffff", fg="#000000")
    password_box.pack(pady=50)
    password_box.delete("1.0", tk.END)
    password_box.insert(tk.END,password)
    password = ""
    
    
    
    






charectersandnumbers = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                    '1', '2', '3', '4', '5', '6', '7', '8', '9', '0','1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

charactersnumberssymbols = ['!', '"', '#', '$', '%', '&', '\'', '(', ')', '*', '+', ',', '-', '.', '/',
                        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', '@',
                        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
                        'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                        '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~',
                        'a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
                        'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



    

window = tk.Tk() #vytvori zakladni okno
window.title("Password App")
window.attributes('-fullscreen', True)
myfont = tkFont.Font(family="Ariel", size= 15)


Main()
window.mainloop()
    



