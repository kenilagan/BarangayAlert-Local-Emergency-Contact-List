import time

# admin
admin_credentials = {
    "admin": "admin"
}

# In-memory contacts list
emergency_contacts = [
    {"name": "Fire Department", "number": "123-4567", "type": "Fire", "priority": 1},
    {"name": "Barangay Police", "number": "234-5678", "type": "Police", "priority": 1},
    {"name": "Medical Team", "number": "345-6789", "type": "Medical", "priority": 2},
    {"name": "Traffic Unit", "number": "456-7890", "type": "Traffic", "priority": 3}
]

# Simulated call path
network_path = ["Barangay Router", "Control Center", "Target Emergency Unit"]

def view_contacts():
    print("\n--- Emergency Contacts ---")
    if not emergency_contacts:
        print("No contacts available.")
        return
    sorted_list = sorted(emergency_contacts, key=lambda x: x["priority"])
    for i, contact in enumerate(sorted_list):
        print(f"[{i + 1}] {contact['name']} | {contact['type']} | {contact['number']} | Priority: {contact['priority']}")

def trace_call(contact):
    print(f"\nTracing call to: {contact['name']}")
    for i, hop in enumerate(network_path):
        print(f"[{i + 1}] Passing through {hop}...")
        time.sleep(1)
    print(f"{contact['name']} successfully notified!\n")

def search_contact():
    service_types = {
        "1": "Fire",
        "2": "Police",
        "3": "Medical",
        "4": "Traffic",
        "5": "Local Official"
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

        simulate = input("Do you want to simulate a call to this contact? (y/n): ").lower()
        if simulate == 'y':
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

def call_by_name():
    name = input("Enter the name of the contact to call: ").strip()
    found = next((c for c in emergency_contacts if c["name"].lower() == name.lower()), None)
    if found:
        trace_call(found)
    else:
        print("Contact not found.")

def add_contact():
    print("\n--- Add New Contact ---")
    name = input("Name: ")
    number = input("Contact Number: ")
    contact_type = input("Type (Fire, Police, Medical, Traffic, Local Official): ").capitalize()
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

def login_admin():
    print("\n--- Admin Login ---")
    username = input("Username: ").strip().lower()
    password = input("Password: ").strip()

    if username == "admin" and password == "admin":
        print("Login successful! Welcome, Admin!")
        return True
    else:
        print("Invalid credentials. Access denied.")
        return False

def resident_menu():
    while True:
        print("\nResident Menu:")
        print("1. View All Contacts")
        print("2. Search Contact by Service")
        print("3. Simulate Call by Name")
        print("4. Logout")

        choice = input("Choose an option: ")
        if choice == '1':
            view_contacts()
        elif choice == '2':
            search_contact()
        elif choice == '3':
            call_by_name()
        elif choice == '4':
            break
        else:
            print("Invalid option.")

def admin_menu():
    while True:
        print("\nAdministrator Menu:")
        print("1. Add New Contact")
        print("2. Edit Contact")
        print("3. Delete Contact")
        print("4. View All Contacts")
        print("5. Logout")

        choice = input("Choose an option: ")
        if choice == '1':
            add_contact()
        elif choice == '2':
            edit_contact()
        elif choice == '3':
            delete_contact()
        elif choice == '4':
            view_contacts()
        elif choice == '5':
            break
        else:
            print("Invalid option.")

def main():
    while True:
        print("\n==== BarangayAlert: Emergency Contact System ====")
        print("1. Login as Administrator")
        print("2. Login as Resident")
        print("3. Exit")

        role = input("Choose your role: ")

        if role == '1':
            if login_admin():
                admin_menu()
        elif role == '2':
            resident_menu()
        elif role == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid selection.")

if __name__ == "__main__":
    main()
