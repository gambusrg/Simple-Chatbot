# Simple LangChain Chatbot

## Project Overview

This project implements a simple chatbot using LangChain and LangGraph frameworks with the Mistral language model via Ollama. The chatbot maintains conversation history and can remember information shared during the conversation.

## Features

- Interactive command-line interface
- Persistent memory between messages
- Integration with local Ollama LLM server
- Simple and extendable architecture using LangGraph

## Prerequisites

- Python 3.8+
- Ollama installed and running locally with the Mistral model

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/simple-langchain-chatbot.git
   cd simple-langchain-chatbot
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install langchain langgraph langchain-ollama pydantic
   ```

4. Ensure Ollama is installed and the Mistral model is downloaded:
   ```bash
   ollama pull mistral
   ```

## Usage

1. Run the chatbot:
   ```bash
   python main.py
   ```

2. Start chatting with the bot. Type your messages and press Enter.

3. Type "exit" to end the conversation.

## How It Works

The chatbot uses a simple LangGraph architecture:

1. User input is captured from the command line
2. The input is converted to a LangChain message format
3. The message is processed through a graph that:
   - Maintains conversation history using MemorySaver
   - Sends the conversation to the LLM for processing
   - Returns the LLM's response
4. The assistant's response is displayed to the user

## Code Structure

```
main.py          # Main application file with the chatbot implementation
```

## Customization

### Changing the LLM Model

To use a different model, modify the `llm` definition:

```python
llm = ChatOllama(
    model="llama2",  # Change to another available model
    temperature=0,
    system_prompt=system_chat_prompt,
)
```

### Modifying System Prompt

Adjust the system prompt to change the chatbot's personality or capabilities:

```python
system_chat_prompt = """
You are a helpful assistant specialized in technical support for programming questions.
"""
```

## Extending the Project

You can extend this basic implementation by:

1. Adding more nodes to the graph for more complex processing
2. Implementing tools for web search, calculation, etc.
3. Creating a web interface using a framework like Flask or FastAPI
4. Adding structured output handling for specific tasks

## License

[Your License Here]

## Acknowledgments

- [LangChain](https://github.com/langchain-ai/langchain) - For the LLM interaction framework
- [LangGraph](https://github.com/langchain-ai/langgraph) - For the state management and flow control
- [Ollama](https://ollama.ai/) - For providing easy access to local LLMs
