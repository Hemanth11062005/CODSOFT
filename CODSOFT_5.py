from tkinter import *

contacts = []

def add_contact():
    name = nameEntry.get()
    phone = phoneEntry.get()
    email = emailEntry.get()
    address = addressEntry.get()
    contacts.append({"Name": name, "Phone": phone, "Email": email, "Address": address})
    update_contact_list()
    
def update_contact_list():
    contact_listbox.delete(0, END)
    for contact in contacts:
        contact_listbox.insert(END, contact["Name"] + "-" + contact["Phone"])

def search_contact():
    search_term = search_entry.get().lower()
    search_results = [contact for contact in contacts if search_term in contact["Name"].lower() or search_term in contact["Phone"]]
    contact_listbox.delete(0, END)
    for contact in search_results:
        contact_listbox.insert(END, contact["Name"] + " - " + contact["Phone"])

def delete_contact():
    selected_index = contact_listbox.curselection()
    if selected_index:
        del contacts[selected_index[0]]
        update_contact_list()
        
window = Tk()
window.title("Contact Management System")

nameLabel = Label(window, text="Name")
nameLabel.grid(row=0, column=0, padx=5, pady=5)

nameEntry = Entry(window)
nameEntry.grid(row=0, column=1, padx=5, pady=5)

phoneLabel = Label(window, text="Phone")
phoneLabel.grid(row=1, column=0, padx=5, pady=5)

phoneEntry = Entry(window)
phoneEntry.grid(row=1, column=1, padx=5, pady=5)

emailLabel = Label(window, text="Email")
emailLabel.grid(row=2, column=0, padx=5, pady=5)

emailEntry = Entry(window)
emailEntry.grid(row=2, column=1, padx=5, pady=5)

addressLabel = Label(window, text="Address")
addressLabel.grid(row=3, column=0, padx=5, pady=5)

addressEntry = Entry(window)
addressEntry.grid(row=3, column=1, padx=5, pady=5)

addButton = Button(window, text="Add Contact", command=add_contact)
addButton.grid(row=4, columnspan=2, padx=5, pady=5)

searchLabel = Label(window, text="Search")
searchLabel.grid(row=5, column=0, padx=5, pady=5)

search_entry = Entry(window)
search_entry.grid(row=5, column=1, padx=5, pady=5)

searchButton = Button(window, text="Search", command=search_contact)
searchButton.grid(row=6, columnspan=2, padx=5, pady=5)

deleteButton = Button(window, text="Delete Contact", command=delete_contact)
deleteButton.grid(row=7, columnspan=2, padx=5, pady=5)

contact_listbox = Listbox(window, width=50)
contact_listbox.grid(row=8, columnspan=2, padx=5, pady=5)

update_contact_list()

window.mainloop()
