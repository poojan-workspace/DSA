def print_order (name, chai_type): # PARAMETERS
    print(f"{name} ordered {chai_type} chai")

print_order("Alex", "Lemon") # ARGUMENTS
print_order("Alice", "Ginger")
print_order("Bob", "Mint")

# Example 2:

def fetch_sales():
    print("Fetching sales data now...")

def filter_valid_sales_data():
    print("Filtering valid sales data now...")

def summarize_data():
    print("Summarizing sales data now...")

def generate_report():
    fetch_sales()
    filter_valid_sales_data()
    summarize_data()
    print("Report generated!!")

generate_report()