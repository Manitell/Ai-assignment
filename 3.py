import sqlite3

# Function to execute and validate SQL query
def execute_and_validate(query):
    try:
        # Create a temporary SQLite database
        conn = sqlite3.connect(":memory:")
        cursor = conn.cursor()

        # Setup a sample database schema
        cursor.execute("CREATE TABLE Customers (ID INT, Name TEXT, Age INT, City TEXT);")
        cursor.execute("INSERT INTO Customers VALUES (1, 'Alice', 25, 'London');")
        cursor.execute("INSERT INTO Customers VALUES (2, 'Bob', 30, 'Paris');")
        cursor.execute("INSERT INTO Customers VALUES (3, 'Charlie', 35, 'New York');")

        # Execute user query
        cursor.execute(query)
        result = cursor.fetchall()

        print("Query Executed Successfully!")
        print("Output:")
        for row in result:
            print(row)

    except sqlite3.Error as e:
        print("SQL Error:", e)
    finally:
        conn.close()

# Example Query
print("Example Query 1:")
execute_and_validate("SELECT Name, Age FROM Customers WHERE Age > 25;")

print("\nExample Query 2:")
execute_and_validate("SELECT City FROM Customers WHERE ID < 3;")

print("\nExample Query with Error:")
execute_and_validate("SELEC Name FROM Customers;")  # Intentional typo in SQL syntax
