class Chai:
    def __init__(self, sweetness, milk_level):
        self.sweetness = sweetness
        self.milk_level = milk_level

    def sip():
        print("sipping")
    
    def add_sugar(self, amount):
        self.amount=amount

my_chai = Chai(sweetness=3, milk_level=2)

my_chai.add_sugar(1)

my_chai.sip()
