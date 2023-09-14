class Ticket:
    count = int(2000)
    tickets_resolved = 0
    tickets_to_solve = 0

    def __init__(self, Ticket_creator, Staff_id, Email, Description, Response, Ticket_status):
        Ticket.count += 1
        self.Ticket_creator = Ticket_creator
        self.Staff_id = Staff_id
        self.Email = Email
        self.Description = Description
        self.Response = Response
        self.Ticket_status = Ticket_status
        self.Status = True

    def resolve_ticket(self, Response):
        self.Response = Response
        self.Status = True
        Ticket.tickets_resolved += 1
        Ticket.tickets_to_solve -= 1
