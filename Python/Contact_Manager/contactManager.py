contacts = []

print("Contact Management System")

def add_contact():
    name = input("Enter name of Contact: ")
    phoneNo = input("Enter Mobile Number of Contact: ")
    emailId = input("Enter E-mail Id of Contact: ")

    contact = {
        "name": name,
        "phoneNo": phoneNo,
        "emailId": emailId
    }

    contacts.append(contact)

    print("Contact added successfully!")

def view_contacts():
    if len(contacts) == 0:
        print("No contacts found.")
        return

    print("\n----- Contacts -----")

    for i, contact in enumerate(contacts, start=1):
        print(f"\nContact {i}")
        print(f"Name: {contact['name']}")
        print(f"Phone: {contact['phoneNo']}")
        print(f"Email: {contact['emailId']}")

def edit_contact():
    if len(contacts) == 0:
        print("No contacts found.")
        return

    view_contacts()

    choice = int(input("\nEnter contact number to edit: "))

    if choice >= 1 and choice <= len(contacts):

        contact = contacts[choice - 1]

        print("\nEnter new details:")

        name = input("Enter name: ")
        phoneNo = input("Enter Mobile Number: ")
        emailId = input("Enter E-mail Id: ")

        contact["name"] = name
        contact["phoneNo"] = phoneNo
        contact["emailId"] = emailId

        print("Contact updated successfully!")

    else:
        print("Invalid contact number.")

def delete_contact():
    if len(contacts) == 0:
        print("No contacts found.")
        return

    view_contacts()

    choice = int(input("\nEnter contact number to delete: "))

    if choice >= 1 and choice <= len(contacts):
        deleted_contact = contacts.pop(choice - 1)

        print(
            f"{deleted_contact['name']} "
            "has been deleted successfully!"
        )
    else:
        print("Invalid contact number.")

while True:

    print("\n----- Contact Management System -----")
    print("1. Add New Contact")
    print("2. Delete Existing Contact")
    print("3. Edit Existing Contact")
    print("4. View All Contacts")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact()

    elif choice == "2":
        delete_contact()

    elif choice == "3":
        edit_contact()

    elif choice == "4":
        view_contacts()

    elif choice == "5":
        print("Exiting Contact Management System...")
        break

    else:
        print("Invalid choice. Please try again.")