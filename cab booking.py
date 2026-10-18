import random

while True:
    print("\n CAB BOOKING CHATBOT ")
    print("1. Book Ride")
    print("2. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        print("\nChoose Cab Type")
        print("1. Auto - Rs.12/km")
        print("2. Sedan - Rs.18/km")
        print("3. SUV - Rs.25/km")

        cab = input("Enter cab choice: ")

        if cab == "1":
            cab_name = "Auto"
            rate = 12
        elif cab == "2":
            cab_name = "Sedan"
            rate = 18
        elif cab == "3":
            cab_name = "SUV"
            rate = 25
        else:
            print("Invalid cab choice!")
            continue

        print("\n SELECT ROUTE ")
        print("1. Pune Station to Shivajinagar - 5 km")
        print("2. Pune Station to Kothrud - 8 km")
        print("3. Pune Station to Wakad - 10 km")
        print("4. Swargate to Shivajinagar - 5 km")
        print("5. Swargate to Kothrud - 8 km")
        print("6. Swargate to Wakad - 10 km")
        print("7. Hinjawadi to Shivajinagar - 5 km")
        print("8. Hinjawadi to Kothrud - 8 km")
        print("9. Hinjawadi to Wakad - 10 km")

        route = input("Enter route number: ")

        if route == "1":
            source, destination, distance = "Pune Station", "Shivajinagar", 5
        elif route == "2":
            source, destination, distance = "Pune Station", "Kothrud", 8
        elif route == "3":
            source, destination, distance = "Pune Station", "Wakad", 10
        elif route == "4":
            source, destination, distance = "Swargate", "Shivajinagar", 5
        elif route == "5":
            source, destination, distance = "Swargate", "Kothrud", 8
        elif route == "6":
            source, destination, distance = "Swargate", "Wakad", 10
        elif route == "7":
            source, destination, distance = "Hinjawadi", "Shivajinagar", 5
        elif route == "8":
            source, destination, distance = "Hinjawadi", "Kothrud", 8
        elif route == "9":
            source, destination, distance = "Hinjawadi", "Wakad", 10
        else:
            print("Invalid route choice!")
            continue

        fare = distance * rate

        print("\n===== RIDE DETAILS =====")
        print("Cab Type:", cab_name)
        print("Source:", source)
        print("Destination:", destination)
        print("Distance:", distance, "km")
        print("Rate: Rs.", rate, "per km")
        print("Total Fare: Rs.", fare)

        print("\n1. Confirm & Share OTP")
        print("2. Cancel Ride")

        confirm = input("Enter your choice: ")

        if confirm == "1":
            otp = random.randint(1000, 9999)
            print("Your OTP is:", otp)
            print("Cancellation is not allowed after OTP sharing.")
            print("Ride booked successfully!")

        elif confirm == "2":
            print("Ride cancelled successfully. No OTP shared.")

        else:
            print("Invalid choice! Ride cancelled. No OTP shared.")

    elif choice == "2":
        print("Thank you for using Cab Booking Chatbot!")
        break

    else:
        print("Invalid choice! Please select 1 or 2.")