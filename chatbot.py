from groq import Groq

client = Groq(api_key="your_api_key_here")

messages = [
    {
        "role": "system",
        "content": "You are a friendly customer service assistant for Tasty Bites Restaurant. Help customers with table reservations, menu questions, and special offers. Menu includes: Grilled Chicken $12, Beef Burger $10, Veggie Pizza $9, Pasta $8, Fish and Chips $11. Special offer: 20% off on Tuesdays. Opening hours: Monday to Sunday 10am to 11pm. Reservations can be made by calling 0711111111. You are warm, friendly and helpful."
    }
]

print("Welcome to Tasty Bites Restaurant! How can I help you today?")
print("Type 'quit' to exit.")
print()

while True:
    user_input = input("Customer: ")
    
    if user_input.lower() == "quit":
        print("Thank you for choosing Tasty Bites. Goodbye!")
        break
    
    messages.append({"role": "user", "content": user_input})
    
    chat = client.chat.completions.create(
        messages=messages,
        model="llama-3.3-70b-versatile",
    )
    
    response = chat.choices[0].message.content
    print("Assistant:", response)
    print()
    
    messages.append({"role": "assistant", "content": response})
