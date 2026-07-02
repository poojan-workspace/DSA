'''
IndexError, KeyError, NameError, ZeroDivisionError, TypeError
'''


chai_menu = {"Masala": 30, "Ginger": 40}

# This will raise a KeyError as the Elaichi key is not present in the dictionary.
# chai = chai_menu["Elaichi"]

# print("Hello chai code")

# How to handle it? >> Try except


try:
    chai = chai_menu["Elaichi"]
except Exception as error:
    print("This key is not present in the dictionary", error)

print("Hello chai code")


# Complex Try and Expect:

def serve_chai(flavor):

    try:
        print(f"Serving {flavor} chai...")

        if flavor == "unknown":
            raise ValueError("The flavor does not exist.")
        
    except ValueError as e:
        print("Error: ", e)

    else:
        print(f"Your {flavor} chai is ready!")

    # No matter what outcomes comes from either "try" or "except" clause, "finally" will always run
    finally:
        print("Next customer...")


serve_chai("masala")
serve_chai("unknown")
