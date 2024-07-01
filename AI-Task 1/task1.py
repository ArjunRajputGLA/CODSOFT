

#! CHATBOT WITH RULE-BASED RESPONSES

#? Build a simple chatbot that responds to user inputs based on predefined rules. Use if-else statements or pattern matching techniques to identify user queries and provide appropriate responses. This will give you a basic understanding of natural language processing and conversation flow.

import random
from datetime import datetime

jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "What do you get when you cross a snowman and a vampire? Frostbite.",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "Why don't programmers like nature? It has too many bugs.",
    "Why do cows have hooves instead of feet? Because they lactose.",
    "Why did the bicycle fall over? Because it was two-tired.",
    "What do you call fake spaghetti? An impasta.",
    "How do you organize a space party? You planet.",
    "Why was the math book sad? Because it had too many problems.",
    "Why don't skeletons fight each other? They don't have the guts."
]

advice_list = [
    "Always believe in yourself and stay positive!",
    "Keep learning and growing every day.",
    "Take breaks and take care of your mental health.",
    "Stay curious and keep exploring.",
    "Never be afraid to ask for help.",
    "Balance is key. Don't overwork yourself.",
    "Practice gratitude and appreciate the little things.",
    "Stay hydrated and eat healthy.",
    "Exercise regularly to keep your body and mind healthy.",
    "Stay true to yourself and your values."
]

quotes = [
    "The best way to predict the future is to create it. - Peter Drucker",
    "Life is 10% what happens to us and 90% how we react to it. - Charles R. Swindoll",
    "The only limit to our realization of tomorrow is our doubts of today. - Franklin D. Roosevelt",
    "Do not wait to strike till the iron is hot; but make it hot by striking. - William Butler Yeats",
    "Whether you think you can or you think you can't, you're right. - Henry Ford",
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Success is not the key to happiness. Happiness is the key to success. - Albert Schweitzer",
    "Your time is limited, so don't waste it living someone else's life. - Steve Jobs",
    "Success usually comes to those who are too busy to be looking for it. - Henry David Thoreau",
    "Don't watch the clock; do what it does. Keep going. - Sam Levenson"
]

def calculate(expression):
    try:
        return eval(expression)
    except:
        return "Sorry, I can't calculate that."

def chatbot():
    print("\nHello! I'm a simple rule-based chatbot. How can I help you today?")
    
    user_name = input("\nEnter your username: ")
    
    while True:
        user_input = input(f"{user_name}: ").lower()
        
        if "hello" in user_input or "hi" in user_input:
            if user_name:
                print(f"Chatbot: Hello, {user_name}! How can I assist you today?")
            else:
                print("Chatbot: Hello! How can I assist you today?")
        elif "how are you" in user_input:
            print("Chatbot: I'm just a bunch of code, but I'm doing great! How about you?")
        elif "your name" in user_input:
            print("Chatbot: I don't have a name. I'm a simple rule-based chatbot created to assist you.") 
        elif "weather" in user_input:
            print("Chatbot: I can't check the weather right now, but you can use a weather app or website for that.")
        elif "time" in user_input or "date" in user_input:
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            current_date = now.strftime("%Y-%m-%d")
            print(f"Chatbot: The current time is {current_time} and today's date is {current_date}.")
        elif "joke" in user_input or "another one" in user_input:
            print(f"Chatbot: {random.choice(jokes)}")
        elif "advice" in user_input:
            print(f"Chatbot: {random.choice(advice_list)}")
        elif "quote" in user_input:
            print(f"Chatbot: {random.choice(quotes)}")
        elif "calculate" in user_input:
            expression = user_input.replace("calculate", "").strip()
            result = calculate(expression)
            print(f"Chatbot: The result is {result}.")
        elif "bye" in user_input or "exit" in user_input:
            print("Chatbot: Goodbye! Have a great day!")
            break
        else:
            print("Chatbot: I'm sorry, I don't understand that. Can you please rephrase?")

chatbot() 