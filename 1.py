import re

# SQL Analyzer Function
def analyze_query(query):
    select_pattern = r"SELECT\s+(.+)\s+FROM\s+(\w+)(?:\s+WHERE\s+(.+))?"
    match = re.match(select_pattern, query, re.IGNORECASE)
    if match:
        columns = match.group(1)
        table = match.group(2)
        conditions = match.group(3)

        print("Query Analysis:")
        print(f"- Columns: {columns}")
        print(f"- Table: {table}")
        if conditions:
            print(f"- Conditions: {conditions}")
        else:
            print("- Conditions: None")
    else:
        print("Invalid SQL Query. Ensure it follows the SELECT ... FROM ... WHERE structure.")

# Example Queries
print("Query 1:")
analyze_query("SELECT Name, Age FROM Customers WHERE Age > 30;")

print("\nQuery 2:")
analyze_query("SELECT * FROM Students;")

print("\nInvalid Query:")
analyze_query("SELEC Name FROM Customers;")
