import json


FILE_NAME = "contacts.json"


def load_contacts():
    """Load contacts from the JSON file."""

    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        print("Warning: contacts.json is invalid or empty.")
        return []


def save_contacts():
    """Save contacts to the JSON file."""

    try:
        with open(FILE_NAME, "w") as file:
            json.dump(contacts, file, indent=4)

    except OSError:
        print("Error: Could not save contacts.")


def add_contact():
    """Add a new contact."""

    print("\n----- Add Contact -----")

    name = input("Enter name of Contact: ").strip()
    phoneNo = input("Enter Mobile Number of Contact: ").strip()
    emailId = input("Enter E-mail Id of Contact: ").strip()

    if name == "":
        print("Name cannot be empty.")
        return

    contact = {
        "name": name,
        "phoneNo": phoneNo,
        "emailId": emailId
    }

    contacts.append(contact)

    save_contacts()

    print("Contact added successfully!")


def view_contacts():
    """Display all contacts."""

    if len(contacts) == 0:
        print("\nNo contacts found.")
        return

    print("\n----- Contacts -----")

    for i, contact in enumerate(contacts, start=1):
        print(f"\nContact {i}")
        print(f"Name    : {contact['name']}")
        print(f"Phone   : {contact['phoneNo']}")
        print(f"Email   : {contact['emailId']}")


def delete_contact():
    """Delete a contact."""

    if len(contacts) == 0:
        print("\nNo contacts found.")
        return

    view_contacts()

    try:
        choice = int(input("\nEnter contact number to delete: "))

        if choice >= 1 and choice <= len(contacts):

            deleted_contact = contacts.pop(choice - 1)

            save_contacts()

            print(
                f"\n{deleted_contact['name']} "
                "has been deleted successfully!"
            )

        else:
            print("Invalid contact number.")

    except ValueError:
        print("Please enter a valid number.")


def edit_contact():
    """Edit an existing contact."""

    if len(contacts) == 0:
        print("\nNo contacts found.")
        return

    view_contacts()

    try:
        choice = int(input("\nEnter contact number to edit: "))

        if choice >= 1 and choice <= len(contacts):

            contact = contacts[choice - 1]

            print("\n----- Edit Contact -----")

            name = input(
                f"Enter name [{contact['name']}]: "
            ).strip()

            phoneNo = input(
                f"Enter Mobile Number [{contact['phoneNo']}]: "
            ).strip()

            emailId = input(
                f"Enter E-mail Id [{contact['emailId']}]: "
            ).strip()

            # Keep old value if user presses Enter
            if name != "":
                contact["name"] = name

            if phoneNo != "":
                contact["phoneNo"] = phoneNo

            if emailId != "":
                contact["emailId"] = emailId

            save_contacts()

            print("\nContact updated successfully!")

        else:
            print("Invalid contact number.")

    except ValueError:
        print("Please enter a valid number.")


def main():
    """Main program."""

    global contacts

    contacts = load_contacts()

    print("\n================================")
    print("   Contact Management System")
    print("================================")

    while True:

        print("\n----- Menu -----")
        print("1. Add Contact")
        print("2. Delete Contact")
        print("3. Edit Contact")
        print("4. View Contacts")
        print("5. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            add_contact()

        elif choice == "2":
            delete_contact()

        elif choice == "3":
            edit_contact()

        elif choice == "4":
            view_contacts()

        elif choice == "5":
            print("\nThank you for using Contact Management System!")
            break

        else:
            print("\nInvalid choice. Please select 1-5.")


main()