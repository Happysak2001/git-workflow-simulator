from ticket_manager import load_tickets, save_tickets, add_ticket, close_ticket, get_open_tickets


def show_menu():
    print("\n=== Ticket Manager ===")
    print("1. Show open tickets")
    print("2. Add a new ticket")
    print("3. Close a ticket")
    print("4. Show all tickets")
    print("5. Exit")
    return input("\nChoose an option: ")


def display_tickets(tickets, label="Tickets"):
    if not tickets:
        print(f"\nNo {label.lower()} found.")
        return
    print(f"\n--- {label} ---")
    for t in tickets:
        status = "[OPEN]" if t["status"] == "open" else "[CLOSED]"
        print(f"  #{t['id']} {status} {t['title']}")


def main():
    tickets = load_tickets()

    while True:
        choice = show_menu()

        if choice == "1":
            display_tickets(get_open_tickets(tickets), "Open Tickets")

        elif choice == "2":
            title = input("Enter ticket title: ")
            if title.strip():
                ticket = add_ticket(tickets, title.strip())
                save_tickets(tickets)
                print(f"Created ticket #{ticket['id']}: {ticket['title']}")
            else:
                print("Title cannot be empty.")

        elif choice == "3":
            display_tickets(get_open_tickets(tickets), "Open Tickets")
            try:
                ticket_id = int(input("Enter ticket ID to close: "))
                result = close_ticket(tickets, ticket_id)
                if result:
                    save_tickets(tickets)
                    print(f"Closed ticket #{result['id']}: {result['title']}")
                else:
                    print(f"Ticket #{ticket_id} not found.")
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "4":
            display_tickets(tickets, "All Tickets")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()
