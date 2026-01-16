# define a function.
# This funtion returns response based-chatbot on the user's input


def chatbot_response(user_input):
    # if the user says 'hello'
    if user_input == "hello":
        return "Hi!"
    
    # if the user says 'how are you'
    elif user_input == "how are you":
        return "I am fine, thanks!"
    
    # if the user says 'bye'
    elif user_input == "bye":
        return "Goodbye!"
    
    # if the user enters any other input
    else:
        return "Sorry, I don't understand."
    
    
# Display the chatbot start messages
print("Bot: Hello, I am a simple chatbot")
print("Bot: You ca say 'hello', 'how are you',or 'bye' to exit")


# Use while loop to keep the chatbot running.
while True:

    # Take input from the user
    user_message = input("You:")

    # clean the message(remove extra spaces and convert to lowercase)
    user_message = user_message.strip().lower()

    # Call the function to get the chatbot response
    bot_reply = chatbot_response(user_message)

    # print the chatbot response
    print("Bot:", bot_reply)

    # Stop the loop if user enters 'bye'
    if user_message == "bye":
        break


# Display the chat end meassage
print("Bot: chat ended. Have a nice day!")
