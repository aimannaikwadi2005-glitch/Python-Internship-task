

from abc import ABC, abstractmethod


# Parent class
class Passenger(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def get_discount(self):
        pass


# Child class
class RegularPassenger(Passenger):
    def get_discount(self):
        return 0


# Child class
class StudentPassenger(Passenger):
    def get_discount(self):
        return 10


# Flight class
class Flight:
    def __init__(self, code, airline, source, destination, seats, fare):
        self.code = code
        self.airline = airline
        self.source = source
        self.destination = destination
        self.seats = seats
        self.fare = fare

    def display(self):
        print(self.code, self.airline, self.source, self.destination,
              self.seats, self.fare)


# Booking class
class Booking:
    def __init__(self, booking_id, flight, passenger, tickets):
        self.booking_id = booking_id
        self.flight = flight
        self.passenger = passenger
        self.tickets = tickets

        self.subtotal = flight.fare * tickets
        self.discount = self.subtotal * passenger.get_discount() / 100
        self.total = self.subtotal - self.discount

    def display(self):
        print("\nBooking ID:", self.booking_id)
        print("Passenger:", self.passenger.name)
        print("Age:", self.passenger.age)
        print("Passenger Type:", type(self.passenger).__name__)
        print("Flight:", self.flight.code)
        print("Route:", self.flight.source, "to", self.flight.destination)
        print("Tickets:", self.tickets)
        print("Base fare per ticket: Rs.", self.flight.fare)
        print("Subtotal: Rs.", self.subtotal)
        print("Discount: Rs.", self.discount)
        print("Final amount: Rs.", self.total)


# Main system class
class FlightBookingSystem:
    def __init__(self):
        self.flights = [
            Flight("PN101", "CloudJet", "Pune", "Delhi", 20, 4000),
            Flight("MB202", "SkyAir", "Mumbai", "Bengaluru", 15, 3500),
            Flight("PH303", "SkyWings", "Pune", "Hyderabad", 25, 3000)
        ]

        self.bookings = []
        self.booking_number = 1001

    # Display flights
    def display_flights(self):
        print("\nCode Airline Source Destination Seats Fare")
        for flight in self.flights:
            flight.display()

    # Find flight
    def find_flight(self, code):
        for flight in self.flights:
            if flight.code.lower() == code.lower():
                return flight
        return None

    # Validate booking details
    def validate_booking(self, flight, name, age, tickets):
        if flight is None:
            print("Invalid flight code!")
            return False

        if name.strip() == "":
            print("Passenger name cannot be blank!")
            return False

        if age <= 0:
            print("Age must be greater than zero!")
            return False

        if tickets <= 0:
            print("Tickets must be greater than zero!")
            return False

        if tickets > flight.seats:
            print("Not enough seats available!")
            return False

        return True

    # Calculate fare
    def calculate_fare(self, flight, passenger, tickets):
        subtotal = flight.fare * tickets
        discount = subtotal * passenger.get_discount() / 100
        total = subtotal - discount

        print("Subtotal: Rs.", subtotal)
        print("Discount: Rs.", discount)
        print("Final amount: Rs.", total)

    # Book a flight
    def book_flight(self):
        self.display_flights()

        code = input("Enter flight code: ").strip()
        flight = self.find_flight(code)

        name = input("Enter passenger name: ").strip()

        try:
            age = int(input("Enter age: "))
            passenger_type = input(
                "Passenger type (Regular/Student): "
            ).strip().lower()
            tickets = int(input("Enter number of tickets: "))
        except ValueError:
            print("Invalid input! Age and tickets must be numbers.")
            return

        if not self.validate_booking(flight, name, age, tickets):
            print("Booking failed. No seats have been changed.")
            return

        if passenger_type == "student":
            passenger = StudentPassenger(name, age)
        elif passenger_type == "regular":
            passenger = RegularPassenger(name, age)
        else:
            print("Invalid passenger type!")
            return

        self.calculate_fare(flight, passenger, tickets)

        # Change seats only after successful validation
        flight.seats -= tickets

        booking = Booking(
            "BK" + str(self.booking_number),
            flight,
            passenger,
            tickets
        )

        self.bookings.append(booking)
        self.booking_number += 1

        print("\nBooking confirmed!")
        booking.display()

    # View latest booking
    def view_booking(self):
        if len(self.bookings) == 0:
            print("No bookings available.")
        else:
            self.bookings[-1].display()

    # Main menu
    def run(self):
        while True:
            print("\nWelcome to CloudJet Air Booking")
            print("1. View Flights")
            print("2. Book Flight")
            print("3. View Booking")
            print("4. Exit")

            choice = input("Enter choice: ")

            if choice == "1":
                self.display_flights()
            elif choice == "2":
                self.book_flight()
            elif choice == "3":
                self.view_booking()
            elif choice == "4":
                print("Thank you for using CloudJet Air Booking!")
                break
            else:
                print("Invalid choice! Please try again.")


# Create object and run program
system = FlightBookingSystem()
system.run()
