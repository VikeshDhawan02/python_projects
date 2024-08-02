import re

# Predefined patterns and responses
patterns = {
    r'.*weather.*today.*': 'The weather today is sunny with a high of 25°C.',
    r'.*weather.*tomorrow.*': 'Tomorrow, expect partly cloudy skies with a high of 28°C.',
    r'.*temperature.*today.*': 'Today, the temperature is 25°C.',
    r'.*temperature.*tomorrow.*': 'Tomorrow, the temperature will reach a high of 28°C.',
    r'.*good morning.*': 'Good morning! How can I help you today?',
    r'.*good afternoon.*': 'Good afternoon! How can I assist you?',
    r'.*good evening.*': 'Good evening! What can I do for you?',
    r'.*bye.*': 'Goodbye! Have a great day!'
}

def chatbot_response(user_input):
    # Check each pattern for a match and return the corresponding response
    for pattern, response in patterns.items():
        if re.match(pattern, user_input, re.IGNORECASE):
            return response
    # If no match is found, provide a default response
    return "I'm sorry, I don't understand your question."

# Main chat loop
print("Chatbot: Hello! How can I assist you today?")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Chatbot: Goodbye! Have a great day!")
        break
    response = chatbot_response(user_input)
    print("Chatbot:", response)
