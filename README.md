# AutoStream AI Agent

This project is a conversational AI agent built for a fictional SaaS product AutoStream.

## Features
- Intent detection (greeting, pricing, high-intent)
- RAG-based responses using local JSON knowledge base
- Lead capture system with mock API call
- Multi-turn conversation handling

## How to Run
1. Install Python 3.9+
2. Run:
   python app.py

## Architecture
This project uses a simple state-based conversational flow.
Intent detection is rule-based, while RAG is implemented using a local JSON file.

The agent transitions through:
Greeting → Pricing → High Intent → Lead Capture

State is stored in a Python dictionary to maintain conversation memory.

## WhatsApp Integration
This agent can be integrated using WhatsApp Business API with webhooks.

Incoming messages are received on a backend server, processed by the agent, and responses are sent back via API.

User sessions can be tracked using phone numbers to maintain conversation state.
