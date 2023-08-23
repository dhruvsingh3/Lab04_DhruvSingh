Flight_id = ["AI161E90", "BR161F91", "AI161F99", "VS171E20", "AS171G30", "AI131F49"]
From = ["BLR", "BOM", "BBI", "JLR", "HYD", "HYD"]
To = ["BOM", "BBI", "BLR", "BBI", "JLR", "BOM"]
Price = [5600, 6750, 8210, 5500, 4400, 3499]


class Flights:
    def __init__(self, Flight_id, From, To, Price):
        self.Flight_id = Flight_id
        self.From = From
        self.To = To
        self.Price = Price

    def display(self, lst):
        if len(lst) > 0:
            for i in lst:
                print(
                    "Flight ",
                    Flight_id[i],
                    " is from ",
                    From[i],
                    " to ",
                    To[i],
                    ". And its price is ",
                    Price[i],
                )
        else:
            print("No flights found")

    def tocity(self, Input):
        lst = []
        for i in range(len(To)):
            if To[i] == Input:
                lst.append(i)
        return lst

    def fromcity(self, Input):
        lst = []
        for i in range(len(From)):
            if From[i] == Input:
                lst.append(i)
        return lst

    def fromtocity(self, Input):
        lst = []
        for i in range(len(From)):
            if From[i] == Input[0].upper() and To[i] == Input[1].upper():
                lst.append(i)
        return lst


f = Flights(Flight_id, From, To, Price)
print(
    "Enter your Preferance: \n1. Flights for a particular City\n2. Flights From a city\n3. Flights between two given cities"
)
choice = int(input("Your Preferance: "))
if choice == 1:
    print(
        "Enter the City you want to travel to: \nBLR: Bengaluru\nBOM: Mumbai\nBBI: Bhubaneswar\nHYD: Hyderabad\nJLR: Jabalpur"
    )
    Input = input("Your choice: ").upper()
    lst = f.tocity(Input)
    f.display(lst)
elif choice == 2:
    print(
        "Enter the City you want to travel from: \nBLR: Bengaluru\nBOM: Mumbai\nBBI: Bhubaneswar\nHYD: Hyderabad\nJLR: Jabalpur"
    )
    Input = input("Your choice: ").upper()
    lst = f.fromcity(Input)
    f.display(lst)
elif choice == 3:
    print(
        "Enter the City you want to travel from and to i.e. From to: \nBLR: Bengaluru\nBOM: Mumbai\nBBI: Bhubaneswar\nHYD: Hyderabad\nJLR: Jabalpur"
    )
    Input = input("Your choice: ").split()
    lst = f.fromtocity(Input)
    f.display(lst)
