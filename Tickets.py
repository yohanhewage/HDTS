class Ticket:
    count = int(2000)


    def __init__(self, Ticket_creator, Staff_id, Email, Description, Response, Ticket_status):
        Ticket.count += 1
        self.Ticket_creator = Ticket_creator
        self.Staff_id = Staff_id
        self.Email = Email
        self.Description = Description
        self.Response = Response
        self.Ticket_status = Ticket_status
        self.vStatus = True