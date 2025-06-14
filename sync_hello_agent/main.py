import os
from dotenv import load_dotenv
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel
from agents.run import RunConfig
import asyncio
import chainlit as cl


load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

if not gemini_api_key:
    raise ValueError("Error: GEMINI_API_KEY not found in .env file. Add your Gemini API key to proceed.")

external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

config = RunConfig(
    model=model,
    tracing_disabled=True
)


agent: Agent = Agent(name="Assistant", instructions="You are a helpful assistant", model=model)

@cl.on_chat_start
async def start():
    await cl.Message(
        content="Hello! I'm your AI assistant powered by Gemini. How can I help you today?",
    ).send()

@cl.on_message
async def main(message: cl.Message):
    # Get AI response
    response = Runner.run_sync(agent, message.content, run_config=config)
    
    # Send the response
    await cl.Message(
        content=response.final_output,
    ).send()
