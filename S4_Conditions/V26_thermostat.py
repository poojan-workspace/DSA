device_status = "active"

temperature = 32

if device_status == "active":
    if temperature > 35:
        print(f"High temperature alert!!")
    else:
        print(f"Normal temperature.")
else:
    print(f"Device offline!!")
