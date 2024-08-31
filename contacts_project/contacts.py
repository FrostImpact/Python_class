import ast
from ast import literal_eval

def is_letter(char):
    return ('a' <= char <= 'z') or ('A' <= char <= 'Z')

def name_validation(name):
    if len(name) == 0:
        return True
    
    if len(name) < 2:
        return False
        
    else:
        return True

def email_validation(email):
    email_list = list(email)

    if len(email) == 0:
        return True
    if email_list.count("@") != 1:
        return False
    
    at_position = email.index("@")
    dot_position = email.find(".", at_position)
    
    if dot_position == -1:
        return False
    
    if at_position < 2:
        return False
    
    if dot_position - at_position <= 1:
        return False
    
    if not is_letter(email[0]) or not is_letter(email[-1]):
        return False
    
    domain = email[at_position+1:dot_position]
    if not any(is_letter(c) for c in domain):
        return False
    
    return True

def phone_number_validation(phone_number):
    if len(phone_number) == 0:
        return True

    return len(phone_number) == 10 and phone_number.isdigit()

def add_contact():
 
    contact = [["First Name", ""], ["Last Name", ""], ["Email", ""], ["Phone Number", ""]]
    check = 0

    while check < 5:
        while check < 1:
            first_name = input("First name: ")
            if name_validation(first_name):
                contact[0][1] = first_name
                check += 1
            else:
                print("First name must have at least 2 characters.")
                
        while check < 2:
            last_name = input("Last name: ")
            if name_validation(last_name):
                contact[1][1] = last_name
                check += 1
            else:
                print("Last name must have at least 2 characters.")

        while check < 3:
            email = input("Email: ")
            if email_validation(email):
                contact[2][1] = email
                check += 1
            else:
                print("Invalid email format.")

        while check < 4:
            phone_number = input("Phone number: ")
            if phone_number_validation(phone_number):
                contact[3][1] = phone_number
                check += 1
            else:
                print("Phone number must have exactly 10 digits.")
            
        if contact[0][1] == "" and contact[1][1] == "" and contact[2][1] == "" and contact[3][1] == "":
            print("Every parameter cannot be empty.")
            check = 0
        else:
            check += 1

    return contact

def edit_contact(contact_list):
    if not contact_list: 
        print("Contact list is empty.")
        return
    
    view_contacts(contact_list)
    
    contact_number = int(input("Enter the number of the contact you want to edit: "))
    
    for contact in contact_list: #cycles through all contacts in the list
    
        if contact_list.index(contact) == contact_number - 1: 
            print("Contact found. What would you like to edit?")
            print("1 to edit First Name")
            print("2 to edit Last Name")
            print("3 to edit Email")
            print("4 to edit Phone Number")
            choice = int(input("Enter your choice: "))

            if choice == 1:
                new_first_name = input("Enter new first name: ")
                if name_validation(new_first_name):
                    contact[0][1] = new_first_name
                    print("First name updated.")
                else:
                    print("First name must have at least 2 characters.")
            elif choice == 2:
                new_last_name = input("Enter new last name: ")
                if name_validation(new_last_name):
                    contact[1][1] = new_last_name
                    print("Last name updated.")
                else:
                    print("Last name must have at least 2 characters.")
            elif choice == 3:
                new_email = input("Enter new email: ")
                if email_validation(new_email):
                    contact[2][1] = new_email
                    print("Email updated.")
                else:
                    print("Invalid email format.")
            elif choice == 4:
                new_phone_number = input("Enter new phone number: ")
                if phone_number_validation(new_phone_number):
                    contact[3][1] = new_phone_number
                    print("Phone number updated.")
                else:
                    print("Phone number must have exactly 10 digits.")
            else:
                print("Invalid choice.")
            return

    print("Contact not found.")

def view_contacts(contact_list):
    if not contact_list:
        print("You have no contacts.")
        return
    
    # Sort the contact list alphabetically by first name, last name, and email
    contact_list.sort(key=lambda x: (x[0][1], x[1][1], x[2][1]))
    
    # Display contacts
    for i, contact in enumerate(contact_list, start=1):
        print(f"{i}.")
        if contact[0][1]:
            print(f"First name: {contact[0][1]}")
        if contact[1][1]:
            print(f"Last name: {contact[1][1]}")
        if contact[2][1]:
            print(f"Email: {contact[2][1]}")
        if contact[3][1]:
            print(f"Phone number: {contact[3][1]}")
        print()

def delete_contact(contact_list):
    if not contact_list:
        print("Contact list is empty.")
        return
    
    view_contacts(contact_list)
    contact_number = int(input("Enter the number of the contact you want to delete: "))
    
    if 1 <= contact_number <= len(contact_list):
        contact_list.pop(contact_number - 1)
        print("Contact deleted.")
    else:
        print("Invalid contact number.")

def database(contact_list):

    add_cont = open("contacts_database","w")
    add_cont.write(str(contact_list))
    add_cont.close()


def main(): #main function 

    reset = open("contacts_database","r")
    reset_str = reset.read()
    reset_list = ast.literal_eval(reset_str)
    reset.close()

    contact_list = reset_list
    
    while True:

        choice = int(input("What do you want to do? 1 to show list of contacts, 2 to add contact, 3 to edit contact, 4 to delete contact, 0 to stop program: "))
        
        if choice == 1:
            view_contacts(contact_list)
        
        elif choice == 2:
            new_contact = add_contact() #calls function
            contact_list.append(new_contact) #appends what is returned
            
            print("Contact added.")
        
        elif choice == 3:
            edit_contact(contact_list)
        
        elif choice == 4:
            delete_contact(contact_list)
        
        elif choice == 0:
            print("Exiting program.")
            break
        
        else:
            print("Invalid choice. Please try again.")
        
    database(contact_list)
            
main() #create a new function which can write on the contacts database file. Any changes including edit, add or delete should be updated in the contacts database
#read from contacts database, whatever we get is the new master list at the start of the program. write those changes in the contact database. when the user wants to see the contacts list 
#we extract it and present it