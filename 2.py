import sqlite3

def provide_feedback(query):
    try:
        conn = sqlite3.connect(":memory:")
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE Students (ID INT, Name TEXT, Score INT);")
        cursor.execute("INSERT INTO Students VALUES (1, 'John', 85);")
        cursor.execute("INSERT INTO Students VALUES (2, 'Jane', 92);")

        cursor.execute(query)
        results = cursor.fetchall()
        print("Correct Query! Results:")
        for row in results:
            print(row)
    except sqlite3.OperationalError as e:
        if "syntax" in str(e):
            print("Feedback: Syntax Error! Check your SELECT, FROM, or WHERE syntax.")
        elif "no such table" in str(e):
            print("Feedback: Table name is incorrect.")
        else:
            print(f"SQL Error: {e}")
    finally:
        conn.close()

# Correct Query
print("Feedback Example 1:")
provide_feedback("SELECT Name, Score FROM Students WHERE Score > 90;")

# Query with Syntax Error
print("\nFeedback Example 2:")
provide_feedback("SELEC Name FROM Students;")

# Query with Wrong Table
print("\nFeedback Example 3:")
provide_feedback("SELECT * FROM Studentss;")
