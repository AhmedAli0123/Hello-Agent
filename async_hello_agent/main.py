import os
import chainlit as cl
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

# Load Gemini API key
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY not found in environment variables")

genai.configure(api_key=api_key)

# Configure Gemini model
model = genai.GenerativeModel("gemini-2.0-flash")

@cl.on_chat_start
async def on_chat_start():
    # Initialize empty chat history
    cl.user_session.set("chat_history", [])

@cl.on_message
async def on_message(message: cl.Message):
    try:
        history = cl.user_session.get("chat_history")
        
        # Format the user message
        user_message = {"role": "user", "parts": [message.content]}
        history.append(user_message)
        
        # Create chat session with history
        chat = model.start_chat(history=history)
        
        # Generate response
        response = chat.send_message(message.content)
        
        if not response.text:
            await cl.Message(content="I apologize, but I couldn't generate a response. Please try again.").send()
            return
            
        # Add model's response to history
        model_message = {"role": "model", "parts": [response.text]}
        history.append(model_message)
        
        # Update the session with new history
        cl.user_session.set("chat_history", history)
        
        # Send response back to user
        await cl.Message(content=response.text).send()
        
    except Exception as e:
        await cl.Message(content=f"An error occurred: {str(e)}").send()