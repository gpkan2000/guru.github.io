# Load package for making HTTP API requests
import requests

# Configure Mailgun API credentials (replace with your actual values)
api_key = "your-mailgun-api-key"
domain = "your-mailgun-domain"

# Get email details from user
to = input("To email: ")
subject = input("Subject: ")
message = input("Message: ")

# Send email via Mailgun API using HTTP POST request
response = requests.post(f"https://api.mailgun.net/v3/{domain}/messages",
    auth=("api", api_key),  # HTTP Basic authentication
    data={"from": f"sender@{domain}", "to": to, "subject": subject, "text": message})

# Check response status and display result to user
print("✅ Email sent!" if response.status_code == 200 else "❌ Failed")

