import langchain
import langgraph
from pydantic import BaseModel
from langchain_ollama import ChatOllama
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import START, MessagesState, StateGraph
from langchain_core.messages import HumanMessage
from typing import List




system_chat_prompt = """
You are a helpful assistant that remembers information shared in the conversation.
"""

llm = ChatOllama(
    model="mistral",
    temperature=0,
    system_prompt=system_chat_prompt,
)

# Set up the initial graph based on our state definition
graph_builder = StateGraph(state_schema=MessagesState)

# Define the function that calls the model
def call_model(state: MessagesState):
    response = llm.invoke(state["messages"])
    return {"messages": response}

# Add the chatbot function to the app graph as a node called "chatbot"
graph_builder.add_node("chatbot", call_model)

# Define the chatbot node as the app entrypoint
graph_builder.add_edge(START, "chatbot")

# Add memory
memory = MemorySaver()
app = graph_builder.compile(checkpointer=memory)
config = {"configurable": {"thread_id": "abc123"}}

while True:
    message = input("You: ")
    if message.lower() == "exit":
        print("Exiting...")
        break
    response = app.invoke({"messages": [HumanMessage(message)]}, config)
    print("Assistant: ", response["messages"][-1].content)
