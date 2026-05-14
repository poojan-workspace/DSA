'''
Dictionary can be used to avoid multiple if-else or match-case statements.

This code is highly scalable becuase we can put whatever coupon in "users" dict,
but it will only get the discount if its present in "coupons" dict.

'''


users = [
    {"id": 1, "total": 100, "coupon": "P20"},
    {"id": 2, "total": 200, "coupon": "P40"},
    {"id": 3, "total": 80, "coupon": "F10"}
]

coupons = {
    "P40": (0.4, 0),
    "P20": (0.2, 0),
    "F10": (0, 10)
}

for user in users:
    percent, fixed = coupons.get(user["coupon"], (0, 0))

    discount = user["total"] * percent + fixed

    print(f"{user["id"]} paid {user["total"]} and got a discount of {discount} for next visit.") 