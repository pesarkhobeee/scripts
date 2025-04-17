# Local AI Agent for Markdown Files

A local AI agent that uses LlamaIndex, FAISS, and Ollama to provide intelligent search and question answering over your markdown files.

## Overview

This project creates a local AI agent that:
- Loads markdown files from a specified directory
- Creates vector embeddings using HuggingFace embeddings
- Stores these embeddings in a FAISS vector database
- Provides both raw retrieval and LLM-powered responses to your queries
- Uses Ollama to run LLMs locally on your machine

## Requirements

- Python 3.13+
- [Ollama](https://ollama.ai/) installed with the llama3.2 model
- Dependencies listed in `pyproject.toml`

## Installation

1. Make sure you have [Ollama](https://ollama.ai/) installed and the llama3.2 model downloaded:
   ```
   ollama pull llama3.2
   ```

2. Clone this repository:
   ```
   git clone https://github.com/yourusername/local-ai-agent-for-markdown-files.git
   cd local-ai-agent-for-markdown-files
   ```

## Usage

1. Place your markdown files in the `docs` directory.

2. Run the application:
   ```
   uv run main.py
   ```

3. Enter your query when prompted.

4. The application will display:
   - Raw retrieval results showing the closest matches from your documents
   - An LLM-powered response that answers your query based on the content

## Storage

The vector index is automatically saved to the `./storage` directory for future use.

## Example

The repository comes with sample markdown files in the `docs` directory to get you started.
