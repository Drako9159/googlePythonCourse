def to_seconds(hours, minutes, seconds):
    return hours * 3600 + minutes * 60 + seconds

print("Welcome to this time converter")
cont = "y"
while cont == "y":
    hours = int(input("Enter the number of hours: "))
    minutes = int(input("Enter the number of minutes: "))
    seconds = int(input("Enter the number of seconds: "))
    print("That's {} seconds.".format(to_seconds(hours, minutes, seconds)))
    cont = input("Do you want to do another conversion? (y/n): ")
    print()

print("Goodbye!")