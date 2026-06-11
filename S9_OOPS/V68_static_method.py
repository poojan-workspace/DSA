'''
@staticmethods are used when we directly want to access properties and methods of a class without creating an object.
'''


class StripText:

    @staticmethod
    def stripText(text):
        return [item.strip() for item in text.split(",")]
# split(",") spearates the values from whereevr the commas are found
# strip() removes the spaces from the string

raw = " water , honey ,  milk,   ginger ,  sugar"

# Simple way of creating an object reference for the class and call the method inside
obj = StripText()
print(obj.stripText(raw))

# @staticmethod: no need of creating an obj for the class
cleaned_text = StripText.stripText(raw)
print(cleaned_text)