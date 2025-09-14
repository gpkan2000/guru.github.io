import requests    # For making web requests (used in later parts)
import json       # For handling JSON data (used in later parts)
import psycopg2

# Database Configuration
DB_HOST = "aws-0-ap-south-1.pooler.supabase.com"
DB_PORT = 6543
DB_DATABASE = "postgres"
DB_USER = "postgres.ntqronyjnvuvqhbhpudn"
DB_PASSWORD = "RbUL1wu88gGuuDJ"

"""Get all student data from Supabase"""
print("📊 Getting student profiles...")
    
conn = psycopg2.connect(host=DB_HOST, port=DB_PORT, database=DB_DATABASE, user=DB_USER, password=DB_PASSWORD)
cursor = conn.cursor()
    
cursor.execute("""
        SELECT * 
        FROM linkedin_profiles 
        ORDER BY id
    """)
    
results = cursor.fetchall()
# Print each row
print("Printing all rows:")
for row in results:
  print(row)
print("----------------end of print --------------------")    
conn.close()
    

