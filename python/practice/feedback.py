# Create an infinite loop to continuously collect feedback
while True:
    # Get feedback text from user
    feedback = input("Enter feedback (or 'exit'): ")
    
    # Check if user wants to exit the program
    if feedback.lower() == 'exit': 
        break
    
    # Get rating from user
    rating = input("Rate 1-5: ")
    
    # Open file in append mode and write the feedback data
    with open("feedback.txt", "a") as f:
        f.write(f"Rating: {rating}/5 | {feedback}\n")
    
    # Confirm to user that data was saved
    print("Feedback saved! 📝")
