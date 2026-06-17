import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from ticket_manager import load_tickets, save_tickets, add_ticket, close_ticket, get_open_tickets


def test_load_tickets(tmp_path):
    tickets_file = tmp_path / "tickets.json"
    sample = [{"id": 1, "title": "Test ticket", "status": "open"}]
    tickets_file.write_text(json.dumps(sample))

    os.chdir(tmp_path)
    import ticket_manager
    original = ticket_manager.TICKETS_FILE
    ticket_manager.TICKETS_FILE = str(tickets_file)

    result = load_tickets()
    assert len(result) == 1
    assert result[0]["title"] == "Test ticket"

    ticket_manager.TICKETS_FILE = original


def test_load_tickets_empty(tmp_path):
    os.chdir(tmp_path)
    import ticket_manager
    original = ticket_manager.TICKETS_FILE
    ticket_manager.TICKETS_FILE = str(tmp_path / "nonexistent.json")

    result = load_tickets()
    assert result == []

    ticket_manager.TICKETS_FILE = original


def test_add_ticket():
    tickets = []
    ticket = add_ticket(tickets, "Fix login bug")

    assert ticket["id"] == 1
    assert ticket["title"] == "Fix login bug"
    assert ticket["status"] == "open"
    assert len(tickets) == 1


def test_add_multiple_tickets():
    tickets = []
    add_ticket(tickets, "First task")
    second = add_ticket(tickets, "Second task")

    assert second["id"] == 2
    assert len(tickets) == 2


def test_close_ticket():
    tickets = []
    add_ticket(tickets, "Bug to fix")
    result = close_ticket(tickets, 1)

    assert result is not None
    assert result["status"] == "closed"


def test_close_nonexistent_ticket():
    tickets = []
    add_ticket(tickets, "Some task")
    result = close_ticket(tickets, 999)

    assert result is None


def test_get_open_tickets():
    tickets = []
    add_ticket(tickets, "Open task")
    add_ticket(tickets, "Another open task")
    add_ticket(tickets, "Will be closed")
    close_ticket(tickets, 3)

    open_tickets = get_open_tickets(tickets)
    assert len(open_tickets) == 2
    assert all(t["status"] == "open" for t in open_tickets)


def test_save_and_load(tmp_path):
    import ticket_manager
    original = ticket_manager.TICKETS_FILE
    ticket_manager.TICKETS_FILE = str(tmp_path / "test_tickets.json")

    tickets = []
    add_ticket(tickets, "Saved ticket")
    save_tickets(tickets)

    loaded = load_tickets()
    assert len(loaded) == 1
    assert loaded[0]["title"] == "Saved ticket"

    ticket_manager.TICKETS_FILE = original
