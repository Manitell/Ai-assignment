import sqlite3

# Function to validate and execute SQL query
def validate_query(query):
    try:
        # Create an in-memory database
        conn = sqlite3.connect(':memory:')
        cursor = conn.cursor()
        
        # Sample table setup
        cursor.execute("CREATE TABLE Customers (Name TEXT, Age INT, City TEXT);")
        cursor.execute("INSERT INTO Customers VALUES ('Alice', 25, 'London');")
        cursor.execute("INSERT INTO Customers VALUES ('Bob', 30, 'Paris');")
        
        # Execute user query
        cursor.execute(query)
        result = cursor.fetchall()
        
        # Print successful output
        print("Query Executed Successfully!")
        print("Output:", result)
    except Exception as e:
        # Print error message
        print("Error:", e)
    finally:
        conn.close()

# Example Query Input
query = "SELECT Name, Age FROM Customers WHERE Age > 25;"
validate_query(query)
