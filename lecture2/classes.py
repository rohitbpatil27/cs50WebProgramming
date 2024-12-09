class Flight():

    def __init__(self, capacity):
        self.capacity =capacity
        self.passenger = []


    def add_passenger(self, name):
        if not self.check_capacity():
            return False
        self.passenger.append(name)
        return True

    def check_capacity(self):
        return self.capacity - len(self.passenger)            


f = Flight (4)

people = ["Rohit", "Estaa", "Namrata", "Viaan"]


for name in people:
    if f.add_passenger(name):
        print(f"{name} got a seat in flight")
    else:
        print(f"{name} didnt get a seat in flight")




















































# class Point ():
#     def __init__(self, input1, input2):
#         self.x = input1
#         self.y = input2

# p = Point(2, 8)
# print(p.x)
# print(p.y)


