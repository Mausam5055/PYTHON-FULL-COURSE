import os
import logging
import requests
from flask import Flask, request, jsonify
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(_name_)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Configuration Constants
CONFIG = {
    "WHATSAPP": {
        "API_URL": f"https://graph.facebook.com/v18.0/{os.getenv('WHATSAPP_PHONE_NUMBER_ID')}/messages",
        "ACCESS_TOKEN": os.getenv("WHATSAPP_ACCESS_TOKEN"),
        "VERIFY_TOKEN": os.getenv("WHATSAPP_VERIFY_TOKEN")
    },
    "HUGGINGFACE": {
        "API_KEY": os.getenv("HF_API_KEY"),
        "MODEL_URL": os.getenv("HF_MODEL_URL", "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct")
    }
}

# Helper Functions
def generate_ai_response(prompt: str, max_retries: int = 2) -> str:
    """Generate AI response using Hugging Face model with retry logic"""
    headers = {"Authorization": f"Bearer {CONFIG['HUGGINGFACE']['API_KEY']}"}
    payload = {"inputs": prompt}

    for attempt in range(max_retries):
        try:
            response = requests.post(
                CONFIG['HUGGINGFACE']['MODEL_URL'],
                headers=headers,
                json=payload,
                timeout=15
            )
            response.raise_for_status()
            
            if response.status_code == 200:
                result = response.json()
                if isinstance(result, list) and len(result) > 0:
                    return f"{result[0].get('generated_text', 'I need more coffee to think... ☕')}\n\n- Powered by Mausam Kar's AI Bot 🤖"
                
            logging.error(f"Unexpected HF API response: {response.text}")
            return "Hmm, my AI brain is a bit fuzzy right now. Try again later!"

        except requests.exceptions.RequestException as e:
            logging.error(f"HF API Error (Attempt {attempt + 1}): {str(e)}")
            if attempt == max_retries - 1:
                return "My AI service is currently unavailable. Please try again later!"

    return "Oops! AI service timeout. Let's try that again later."

def process_message(message: str) -> str:
    """Process incoming messages with custom responses"""
    cleaned_msg = message.strip().lower()

    responses = {
        "who created you": "I was engineered into existence by Mausam Kar! 🚀",
        "your creator": "The brilliant mind behind me is Mausam Kar! 🌟",
        "hello": "Hello! How can I assist you today? 😊",
        "hi": "Hi there! What can I do for you?",
        "help": "I'm here to help! Ask me anything or share what you need assistance with."
    }

    for key in responses:
        if key in cleaned_msg:
            return responses[key]
    
    return generate_ai_response(message)

def send_whatsapp_message(recipient: str, message: str) -> dict:
    """Send message through WhatsApp Cloud API with proper error handling"""
    headers = {
        "Authorization": f"Bearer {CONFIG['WHATSAPP']['ACCESS_TOKEN']}",
        "Content-Type": "application/json"
    }

    payload = {
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": recipient,
        "type": "text",
        "text": {"body": message}
    }

    try:
        response = requests.post(
            CONFIG['WHATSAPP']['API_URL'],
            json=payload,
            headers=headers,
            timeout=10
        )
        response.raise_for_status()
        return response.json()

    except requests.exceptions.RequestException as e:
        logging.error(f"WhatsApp API Error: {str(e)}")
        return {"status": "error", "message": str(e)}

# Webhook Endpoints
@app.route("/webhook", methods=["GET"])
def verify_webhook():
    """Verify webhook subscription"""
    if request.args.get("hub.mode") == "subscribe" and \
       request.args.get("hub.verify_token") == CONFIG['WHATSAPP']['VERIFY_TOKEN']:
        return request.args.get("hub.challenge"), 200
    return "Verification failed", 403

@app.route("/webhook", methods=["POST"])
def handle_incoming_messages():
    """Handle incoming WhatsApp messages"""
    try:
        data = request.get_json()
        entry = data["entry"][0]
        changes = entry["changes"][0]
        value = changes["value"]
        
        if "messages" in value:
            message = value["messages"][0]
            if message["type"] == "text":
                sender = message["from"]
                text_body = message["text"]["body"]
                
                logging.info(f"Received message from {sender}: {text_body}")
                response_text = process_message(text_body)
                send_whatsapp_message(sender, response_text)
                
        return jsonify({"status": "success"}), 200

    except Exception as e:
        logging.error(f"Webhook processing error: {str(e)}")
        return jsonify({"status": "error", "message": str(e)}), 500

# Run the application
if _name_ == "_main_":
    app.run(
        host="0.0.0.0",
        port=int(os.getenv("PORT", 5000)),
        debug=os.getenv("FLASK_DEBUG", "false").lower() == "true"
    )