# Load built-in SQLite database package
import sqlite3

# Connect to database file (creates file if it doesn't exist)
# Note: demo.db comes pre-populated with 11 sample users for demonstration
conn = sqlite3.connect("demo.db")
cursor = conn.cursor()

# Create table structure if it doesn't already exist
cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)")

# First, show existing users in the database
print("📊 Current Users in Database:")
existing_users = cursor.execute("SELECT * FROM users").fetchall()
if existing_users:
    for row in existing_users:
        print(f"ID: {row[0]} | Name: {row[1]} | Age: {row[2]}")
else:
    print("No users in database yet.")

print("\nLet's add a new user!")

# Get new user data from input
name = input("Name: ")
age = int(input("Age: "))

# Insert new user data using safe parameterized query
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))

# Permanently save changes to database file
conn.commit()

# Show updated list of all users
print("\n📊 All Users After Adding New User:")
for row in cursor.execute("SELECT * FROM users"):
    print(f"ID: {row[0]} | Name: {row[1]} | Age: {row[2]}")

# Close database connection and release resources
conn.close()
