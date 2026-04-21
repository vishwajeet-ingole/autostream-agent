import json

# Load data
with open("rag_data.json") as f:
    kb = json.load(f)

state = {
    "intent": None,
    "lead": {"name": None, "email": None, "platform": None}
}

def mock_lead_capture(name, email, platform):
    print(f"\nLead captured successfully: {name}, {email}, {platform}")

def detect_intent(text):
    text = text.lower()
    
    # High intent first (priority)
    if any(word in text for word in ["buy", "try", "subscribe", "start", "sign up"]):
        return "high_intent"
    
    # Pricing / product
    elif any(word in text for word in ["price", "pricing", "plan", "cost"]):
        return "pricing"
    
    # Greeting
    elif any(word in text for word in ["hi", "hello", "hey"]):
        return "greeting"
    
    return "other"

def get_pricing():
    return f"""
Basic Plan: {kb['pricing']['basic']}
Pro Plan: {kb['pricing']['pro']}
"""

def chat():
    print("AutoStream AI Agent 🤖")
    
    while True:
        user = input("\nYou: ")
        intent = detect_intent(user)
        state["intent"] = intent
        
        if intent == "greeting":
            print("Agent: Hello! Ask me about pricing or plans.")
        
        elif intent == "pricing":
            print("Agent:", get_pricing())
        
        elif intent == "high_intent":
            print("Agent: Great! Please provide your details.")
            
            if not state["lead"]["name"]:
                state["lead"]["name"] = input("Name: ")
            
            if not state["lead"]["email"]:
                state["lead"]["email"] = input("Email: ")
            
            if not state["lead"]["platform"]:
                state["lead"]["platform"] = input("Platform: ")
            
            mock_lead_capture(
                state["lead"]["name"],
                state["lead"]["email"],
                state["lead"]["platform"]
            )
            break
        
        else:
            print("Agent: Please ask about pricing or plans.")

chat()