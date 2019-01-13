from tkinter import *
from time import *

fields=("Subject", "Message")

emails=[]

#get the entries in the field
def fetch(entries):
    for entry in entries:
        field=entry[0]
        text=entry[1].get()
        print('%s: "%s"' % (field, text))

#Enter the entries to the console
def makeform(root, field):
    entries=[]
    for field in fields:
        row=Frame(root)
        label=Label(row, width=30, text=field, anchor='w')
        entry=Entry(row)
        row.pack()
        label.pack()
        entry.pack()
        entries.append((field, entry))
    return entries

#Send function
def send():
    pass

def decrypt():
    pass



##class Email:
##    def __init__(self):
##        self.message=message
##        self.sender=sender

        
        
        
    
class Window(Frame):

    # Define settings upon initialization. Here you can specify
    def __init__(self, master=None):
        
        # parameters that you want to send through the Frame class. 
        Frame.__init__(self, master)   

        #reference to the master widget, which is the tk window                 
        self.master = master

        #with that, we want to then run init_window, which doesn't yet exist
        self.init_window()

    #Creation of init_window
    def init_window(self):

        # changing the title of our master widget      
        self.master.title("GUI")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        # creating a menu instance
        menu = Menu(self.master)
        self.master.config(menu=menu)

        # create the file object)
        file = Menu(menu)

        # adds a command to the menu option, calling it exit, and the
        # command it runs on event is client_exit

        #added "file" to our menu
        menu.add_command(label="Send", command=send)

        # create the file object)
        edit = Menu(menu)

        # adds a command to the menu option, calling it exit, and the
        # command it runs on event is client_exit


        #added "file" to our menu
        menu.add_cascade(label="Mail", command=byteMails)


    def client_exit(self):
        exit()
        

if __name__ == '__main__':
   root = Tk()

   root.geometry("200x150")

   #creation of an instance
   app = Window(root)
    
   ents = makeform(root, fields)
   root.bind('<Return>', (lambda event, e=ents: fetch(e)))   
   b1 = Button(root, text='Show', command=(lambda e=ents: fetch(e)))
   b1.pack(side=LEFT, padx=5, pady=5)
   b2 = Button(root, text='Quit', command=root.quit)
   b2.pack(side=LEFT, padx=5, pady=5)
   root.mainloop()
