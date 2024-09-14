import streamlit as st
import os
import google.generativeai as ggi
from dotenv import load_dotenv


load_dotenv(".env")
fetcheed_api_key = os.getenv("API_KEY")
ggi.configure(api_key=fetcheed_api_key)

model = ggi.GenerativeModel("gemini-pro")
chat = model.start_chat()

def pricing_logic(user_input):
    # Set the price range
    min_price = 100
    max_price = 200

    # Calculate the discount or counteroffer
    if user_input < min_price:
        return f"Sorry, our minimum price is ${min_price}."
    elif user_input > max_price:
        return f"We can offer you a discount of 10% off the list price of ${max_price}."
    else:
        return f"We can meet you at ${user_input}."
    
st.title("Negotiation Chatbot")

# Initialize the chatbot conversation
conversation = []

# Create a text input for the user
user_input = st.text_input("Enter your desired price:")

# Handle the user input
if user_input:
    # Append the user input to the conversation
    conversation.append(user_input)

    # Generate a response using the pricing logic and Gemini Pro model
    response = pricing_logic(int(user_input))
    content_response = chat.send_message(user_input, stream=True)
    content_response.resolve()
    response_text = content_response.text




    # Append the response to the conversation
    conversation.append(response)

    # Display the conversation
    st.write(conversation)