import json
import os

TICKETS_FILE = "tickets.json"


def load_tickets():
    if not os.path.exists(TICKETS_FILE):
        return []
    with open(TICKETS_FILE, "r") as f:
        return json.load(f)


def save_tickets(tickets):
    with open(TICKETS_FILE, "w") as f:
        json.dump(tickets, f, indent=2)


def get_next_id(tickets):
    if not tickets:
        return 1
    return max(t["id"] for t in tickets) + 1


def add_ticket(tickets, title):
    ticket = {
        "id": get_next_id(tickets),
        "title": title,
        "status": "open",
    }
    tickets.append(ticket)
    return ticket


def close_ticket(tickets, ticket_id):
    for ticket in tickets:
        if ticket["id"] == ticket_id:
            ticket["status"] = "closed"
            return ticket
    return None


def get_open_tickets(tickets):
    return [t for t in tickets if t["status"] == "open"]
