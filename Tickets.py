class Ticket:
    count = int(2000)
    tickets_resolved = 0
    tickets_to_solve = 0

    def __init__(self, Ticket_creator, Staff_id, Email_address, Description, Response, Ticket_status):
        Ticket.count += 1
        self.Ticket_creator = Ticket_creator
        self.Staff_id = Staff_id
        self.Email = Email_address
        self.Description = Description
        self.Response = Response
        self.Ticket_status = Ticket_status
        self.Status = True

    def resolve_ticket(self, Response):
        self.Response = Response
        self.Status = True
        Ticket.tickets_resolved += 1
        Ticket.tickets_to_solve -= 1

    def display_ticket(self):
        # ------->>>>>> print ticket info<<<<<<<<----------
        print(f"Ticket Number:, {self.Ticket_number}\n"
              f"Ticket Creator: {self.Ticket_creator}\n"
              f"Staff ID:, {self.Staff_id}\n"
              f"Email Address:, {self.Email_address}\n"
              f"Description:, {self.Description}\n"
              f"Response:, {self.Response}\n"
              f"Ticket Status:, {self.Status}\n")
