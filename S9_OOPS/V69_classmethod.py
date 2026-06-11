'''
@classmethod: this is used to have more than one constructors technically.
'''


class ChaiOrder:

    def __init__(self, tea_type, sweetness, size):
        self.tea_type = tea_type
        self.sweetness = sweetness
        self.size = size

    @classmethod
    def from_dict(cls, order_dict):
        return cls(
            order_dict["tea_type"],
            order_dict["sweetness"],
            order_dict["size"]
        )
    
    @classmethod
    def from_string(cls, order_string):
        tea_type, sweetness, size = order_string.split("-")
        return cls(tea_type, sweetness, size)
    
order1 = ChaiOrder.from_dict({"tea_type": "Masala", "sweetness": "2", "size": "Regular"})
order2 = ChaiOrder.from_string("Ginger-4-Large")
order3  = ChaiOrder("Lemon", "1", "Large")

print(order1.__dict__)
print(order2.__dict__)
print(order3.__dict__)