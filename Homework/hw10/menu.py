from waitlist import Waitlist
class Menu:
    """A class representing the menu for the restaurant reservation program"""

    def __init__(self):
        """Initialize the menu with the waitlist object"""
        self.waitlist = Waitlist()

    def run(self):
        """Print the main menu"""
        print("Welcome to the Restaurant Reservation System!")
        print("==============================================")
        print("Please select an option:")
        print("1. Add a customer to the waitlist")
        print("2. Seat the next customer")
        print("3. Change the time of a customer's reservation")
        print("4. Peek at the next customer")
        print("5. Print the reservation list")
        print("6. Quit")
        print("")
        while True:
            
            choice = input("Enter your choice (1-6): ")
            print("*************************************************")
            #Each one of these options should call a method from Waitlist class 
            if choice == "1":
                #TODO """Add a customer to the waitlist"""
                name = input("Enter customer name: ")
                time = input("Enter reservation time (in format HH:MM): ")
                self.waitlist.add_customer(name, time)
                print(f"{name} has been added to the waitlist at {time}.")


            elif choice == "2":
                #TODO"""Seat the next customer"""
                customer = self.waitlist.seat_customer()
                if customer:
                    print(f"{customer[0]} has been seated with reservation time {customer[1]}")
                else:
                    print("There are no customers on the waitlist.")


            elif choice == "3":
                #TODO"""Change the time of a customer's reservation"""
                name = input("Enter customer name: ")
                new_time = input("Enter new reservation time (in format HH:MM): ")
                if self.waitlist.change_reservation(name, new_time):
                    print(f"{name}'s reservation time has been changed to {new_time}.")
                else:
                    print(f"{name} was not found on the waitlist.")

            elif choice == "4":
                #TODO"""Peek at the next customer"""
                customer = self.waitlist.peek()
                if customer:
                    print(f"The next customer is {customer[0]} with reservation time {customer[1]}.")
                else:
                    print("There are no customers on the waitlist.")

            elif choice == "5":
                #TODO"""Print the waitlist"""
                self.waitlist.print_reservation_list()
            elif choice == "6":
                """exit the program at any time"""
                print("Thank you for using the Restaurant Reservation System!")
                break
            else:
                print("Invalid choice. Try again.")
    

s = Menu()
s.run()

