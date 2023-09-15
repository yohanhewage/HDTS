from Tickets import Ticket
#------------------ >>>>>>>>>>>>>Menu maker<<<<<<<<<<<<----------------------------------------
def menuLoad(menu):
    count = 1

    for z in menu:
        print(f"{count}. {z}")
        count += 1

    print(f"0. EXIT")

    choice = input("Enter Choice Number: ")

    if choice.isnumeric():
        choice = int(choice)

        if choice in range(0, count):
            answer = choice
        else:
            print("Error: Number out of RANGE.")
            answer = 99
    else:
        print("Error: Input NOT a number.")
        answer = 99

    return answer

def create_ticket():C
 #------->>>>>>>>> Ticket info<<<<<<<<<<<<<-----------------

Ticket_creator = input("Enter ticket creator: ")
Staff_id = input("Enter staff ID: ")
Email_address = input("Enter email address: ")
Description = input("Enter description: ")
Response = input("Enter response:")
Ticket_status = input("Ticket status:")



ticket = Ticket(Ticket_creator, Staff_id, Email_address, Description, Response, Ticket_status )

#return ticket

def resolve_ticket(ticket):
    response = input("Enter response: ")
    ticket.resolve_ticket(Response)



tickets = []

#------------Responding to Tickets ------------------------------------>


while True:
    menu = ["Create Ticket", "Resolve Ticket", "Display Ticket Statistics","Printing tickets"]
    choice = menuLoad(menu)

    if choice == 1:
        ticket = create_ticket()
        tickets.append(ticket)
        print("\nTicket created successfully.")

    elif choice == 2:
        ticket_number = Ticket.ticket_count
        found = False

        for Ticket in Tickets:
            if Ticket.ticket_number == Ticket.ticket_count:
                resolve_ticket(ticket)
                found = True
                print("\nTicket resolved successfully.")
                break

        if not found:
            print("\nTicket number not found.")

    elif choice == 3:
        print(f"\nDisplay Ticket Statistics \n"
            # f"Ticket number:  { Ticket.ticket_count}\n"
             f"Tickets Created: {Ticket.tickets_to_solve}\n"
             f"Tickets Resolved: {Ticket.tickets_resolved}\n"
             f"Tickets To Solve: {Ticket.tickets_to_solve}\n")

    elif choice == 4:
       # tickets.append(ticket)
        for ticket in tickets:
         print(f"Printing Tickets: \n"
               f"Ticket number:  { Ticket.ticket_count}\n"
               f"Ticket Creator: {ticket.ticket_creator}\n"
               f"Staff ID: {ticket.staff_id}\n"
               f"Email Address: {ticket.email_address}\n"
               f"Description: {ticket.description}\n"
               f"Response: {ticket.response}\n"
               f"Ticket Status: {ticket.status}\n")

    elif choice == 5:
        # password change
        print()

#------------------- generate the password---------------

    def generate_password(self, ):

        new_password = "";

#----------------------- first two characters of Staff_id

        new_password = self.staff_id[0:2];

#----------- + first 3 characters of Creator_name

        new_password += self.Ticket_creator[0:3];

        return new_password;

   # elif choice == 0:

       # break
#---------------->>>>>>EXIT<<<<<<<<<<<-----------------




