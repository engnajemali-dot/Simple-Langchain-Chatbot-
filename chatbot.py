import os
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

# Load environment variables
load_dotenv()

# Initialize model
llm = ChatOpenAI(
    model="gpt-4.1-mini",
    temperature=0.7
)

# Load system prompt
with open("prompts/system_prompt.txt", "r") as file:
    system_prompt = file.read()

# Conversation memory
chat_history = [
    SystemMessage(content=system_prompt)
]

print("\n🤖 AI Chatbot Started!")
print("Type 'exit' to quit.\n")

while True:
    
    # User input
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("\n👋 Goodbye!")
        break

    # Add user message to memory
    chat_history.append(
        HumanMessage(content=user_input)
    )

    # Get AI response
    response = llm.invoke(chat_history)

    # Print response
    print(f"\nAI: {response.content}\n")

    # Save AI response to memory
    chat_history.append(
        AIMessage(content=response.content)
    )
