"import time
from datetime import datetime

# Admin Credentials
admins = [
    {"username": "admin", "password": "password"}
]

# Initial Emergency Contacts
emergency_contacts = [
    {"name": "Fire Department", "number": "123-4567", "type": "Fire", "priority": 1},
    {"name": "Barangay Police", "number": "234-5678", "type": "Police", "priority": 1},
    {"name": "Medical Team", "number": "345-6789", "type": "Medical", "priority": 2},
    {"name": "Traffic Unit", "number": "456-7890", "type": "Traffic", "priority": 3}
]

# Network Path for Simulation
network_path = [
    "Barangay Router",
    "Control Center",
    "Target Emergency Unit"
]

# Greeting & Loader 
def loading_animation(message):
    print(f"{message}", end="", flush=True)
    for _ in range(3):
        time.sleep(0.5)
        print(".", end="", flush=True)
    print("\n")

# Admin Login 
def login_admin():
    print("\n--- Administrator Login ---")
    username = input("Username: ").strip()
    password = input("Password: ").strip()

    for admin in admins:
        if admin["username"] == username and admin["password"] == password:
            print("Log In Successful, Welcome Admin!")  
            return True

    print("Invalid credentials. Access denied.")
    return False

# View Contacts 
def view_contacts():
    print("\n--- Emergency Contacts ---")
    if not emergency_contacts:
        print("No contacts available.")
        return

    sorted_list = sorted(emergency_contacts, key=lambda x: x["priority"])
    for i, contact in enumerate(sorted_list):
        print(f"[{i + 1}] {contact['name']} | {contact['type']} | {contact['number']} | Priority: {contact['priority']}")

# Trace a Call
def trace_call(contact):
    print(f"\nTracing call to: {contact['name']}")
    for i, hop in enumerate(network_path):
        print(f"[{i + 1}] Passing through {hop}...")
        time.sleep(1)
    print(f"{contact['name']} successfully notified!\n")

# Simulate Call from All
def simulate_call():
    view_contacts()
    if not emergency_contacts:
        return
    try:
        choice = int(input("\nEnter the number of the contact to call: ")) - 1
        if 0 <= choice < len(emergency_contacts):
            trace_call(emergency_contacts[choice])
        else:
            print("Invalid selection.")
    except:
        print("Invalid input.")

# Search by Service Type
def search_contact():
    service_types = {
        "1": "Fire",
        "2": "Police",
        "3": "Medical",
        "4": "Traffic"
    }

    print("\nAvailable Service Types:")
    for key, value in service_types.items():
        print(f"{key}. {value}")

    choice = input("Enter the number of the service type to search: ").strip()
    selected_type = service_types.get(choice)

    if not selected_type:
        print("Invalid selection.")
        return

    results = [c for c in emergency_contacts if c["type"] == selected_type]

    if results:
        print(f"\nContacts for '{selected_type}':")
        for i, contact in enumerate(results):
            print(f"[{i + 1}] {contact['name']} | {contact['number']}")

        simulate = input("Do you want to simulate a call to a contact? (y/n): ").lower()
        if simulate == 'y':
            if len(results) == 1:
                trace_call(results[0])
            else:
                try:
                    call_choice = int(input("Enter the number of the contact to call: ")) - 1
                    if 0 <= call_choice < len(results):
                        trace_call(results[call_choice])
                    else:
                        print("Invalid number selection.")
                except:
                    print("Invalid input.")
    else:
        print("No contacts found for that service.")

# Admin Functions
def add_contact():
    print("\n--- Add New Contact ---")
    name = input("Name: ")
    number = input("Contact Number: ")
    contact_type = input("Type (Fire, Police, etc.): ").capitalize()
    try:
        priority = int(input("Priority (1 = High, 3 = Low): "))
    except:
        print("Invalid priority.")
        return

    contact = {
        "name": name,
        "number": number,
        "type": contact_type,
        "priority": priority
    }
    emergency_contacts.append(contact)
    print("Contact added successfully!")

def delete_contact():
    view_contacts()
    try:
        idx = int(input("Enter the number of the contact to delete: ")) - 1
        removed = emergency_contacts.pop(idx)
        print(f"Removed: {removed['name']}")
    except:
        print("Invalid selection.")

def edit_contact():
    view_contacts()
    try:
        idx = int(input("Enter the number of the contact to edit: ")) - 1
        contact = emergency_contacts[idx]
    except:
        print("Invalid selection.")
        return

    print("\nLeave field blank to keep current value.")
    name = input(f"New name ({contact['name']}): ") or contact['name']
    number = input(f"New number ({contact['number']}): ") or contact['number']
    contact_type = input(f"New type ({contact['type']}): ") or contact['type']
    try:
        priority_input = input(f"New priority ({contact['priority']}): ")
        priority = int(priority_input) if priority_input else contact['priority']
    except:
        print("Invalid priority. Keeping old value.")
        priority = contact['priority']

    emergency_contacts[idx] = {
        "name": name,
        "number": number,
        "type": contact_type,
        "priority": priority
    }
    print("Contact updated!")

# Menus 
def admin_menu():
    while True:
        print("\nAdministrator Menu:")
        print("1. View All Contacts")
        print("2. Add New Contact")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Logout")

        choice = input("Choose an option: ")
        if choice == '1':
            view_contacts()
        elif choice == '2':
            add_contact()
        elif choice == '3':
            edit_contact()
        elif choice == '4':
            delete_contact()
        elif choice == '5':
            print("Logging out of Admin Menu...")
            break
        else:
            print("Invalid option.")

def resident_menu():
    while True:
        print("\nResident Menu:")
        print("1. View All Contacts")
        print("2. Search Contact by Service")
        print("3. Simulate a Call")
        print("4. Back")

        choice = input("Choose an option: ")
        if choice == '1':
            view_contacts()
        elif choice == '2':
            search_contact()
        elif choice == '3':
            simulate_call()
        elif choice == '4':
            print("Logging out of Resident Menu...")
            break
        else:
            print("Invalid option.")

# Main Function
def main():
    current_hour = datetime.now().hour
    if 5 <= current_hour < 12:
        time_greeting = "Good morning"
    elif 12 <= current_hour < 18:
        time_greeting = "Good afternoon"
    elif 18 <= current_hour < 22:
        time_greeting = "Good evening"
    else:
        time_greeting = "It's late, but we're here to help!"

    print("--------------------------------------------")
    print("Welcome to BarangayAlert: Emergency System")
    print("--------------------------------------------")
    print(f"{time_greeting}! How can we assist you today?\n")

    while True:
        print("Are you an Administrator or a Resident?")
        print("1. Administrator")
        print("2. Resident")
        print("3. Exit")

        role = input("Enter your choice (1/2/3): ").strip()

        if role == '1':
            if login_admin():
                print("\nAccess granted. Opening Administrator Menu...")
                loading_animation("Loading")
                admin_menu()
        elif role == '2':
            print("\nAccessing Resident Menu...")
            loading_animation("Loading")
            resident_menu()
        elif role == '3':
            print("\nThank you for using BarangayAlert. Stay safe!")
            break
        else:
            print("Invalid selection. Please try again.")

# Run the program
if __name__ == "__main__":
    main()"
    
