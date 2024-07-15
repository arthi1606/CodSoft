class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}, Address: {self.address}"

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print("Contact added.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            for i, contact in enumerate(self.contacts, start=1):
                print(f"{i}. {contact.name} - {contact.phone}")

    def search_contact(self, search_term):
        found_contacts = [contact for contact in self.contacts if search_term.lower() in contact.name.lower() or search_term in contact.phone]
        if not found_contacts:
            print("No contacts found.")
        else:
            for contact in found_contacts:
                print(contact)

    def update_contact(self, index, updated_contact):
        if 0 <= index < len(self.contacts):
            self.contacts[index] = updated_contact
            print("Contact updated.")
        else:
            print("Invalid contact index.")

    def delete_contact(self, index):
        if 0 <= index < len(self.contacts):
            self.contacts.pop(index)
            print("Contact deleted.")
        else:
            print("Invalid contact index.")

def display_menu():
    print("\nContact Book Application")
    print("1. View Contacts")
    print("2. Add Contact")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

def get_contact_details():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    return Contact(name, phone, email, address)

def main():
    contact_book = ContactBook()

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            contact_book.view_contacts()
        elif choice == '2':
            contact = get_contact_details()
            contact_book.add_contact(contact)
        elif choice == '3':
            search_term = input("Enter name or phone number to search: ")
            contact_book.search_contact(search_term)
        elif choice == '4':
            contact_book.view_contacts()
            try:
                index = int(input("Enter the contact number to update: ")) - 1
                updated_contact = get_contact_details()
                contact_book.update_contact(index, updated_contact)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif choice == '5':
            contact_book.view_contacts()
            try:
                index = int(input("Enter the contact number to delete: ")) - 1
                contact_book.delete_contact(index)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif choice == '6':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
