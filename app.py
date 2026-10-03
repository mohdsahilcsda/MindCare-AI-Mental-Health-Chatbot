from flask import Flask, render_template_string, request, jsonify
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
from datetime import datetime

app = Flask(__name__)

# Load DialoGPT model
MODEL_NAME = "microsoft/DialoGPT-small"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>MindCare AI Chatbot</title>

    <style>
        body {
            font-family: Arial, sans-serif;
            background: #eaf4f4;
            text-align: center;
            padding: 30px;
        }

        .chatbox {
            background: white;
            max-width: 550px;
            margin: auto;
            padding: 25px;
            border-radius: 12px;
        }

        #messages {
            height: 350px;
            overflow-y: auto;
            text-align: left;
            border: 1px solid #ddd;
            padding: 15px;
            margin-bottom: 15px;
        }

        input {
            width: 65%;
            padding: 10px;
        }

        button {
            padding: 10px 15px;
            background: #168b80;
            color: white;
            border: none;
            cursor: pointer;
        }
    </style>
</head>

<body>

<div class="chatbox">

    <h2>MindCare AI Chatbot</h2>

    <p>Share what's on your mind.</p>

    <div id="messages"></div>

    <input id="userInput" placeholder="Type your message...">

    <button onclick="sendMessage()">Send</button>

    <p>
        <small>
            This chatbot provides general emotional support
            and is not a replacement for professional care.
        </small>
    </p>

</div>

<script>

async function sendMessage() {

    const input = document.getElementById("userInput");
    const message = input.value.trim();

    if (!message) {
        return;
    }

    const box = document.getElementById("messages");

    box.innerHTML +=
        "<p><b>You:</b> " +
        escapeHTML(message) +
        "</p>";

    input.value = "";

    const response = await fetch("/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            message: message
        })
    });

    const data = await response.json();

    box.innerHTML +=
        "<p><b>MindCare AI:</b> " +
        escapeHTML(data.reply) +
        "</p>";

    box.scrollTop = box.scrollHeight;
}


function escapeHTML(text) {

    return text.replace(/[&<>"']/g, char => ({
        "&": "&amp;",
        "<": "&lt;",
        ">": "&gt;",
        '"': "&quot;",
        "'": "&#39;"
    }[char]));

}

</script>

</body>
</html>
"""

def save_chat_log(user_message, bot_response):
    with open("chat_logs.txt", "a", encoding="utf-8") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        file.write(f"Time: {timestamp}\n")
        file.write(f"User: {user_message}\n")
        file.write(f"Bot: {bot_response}\n")
        file.write("-" * 50 + "\n")
def generate_reply(message):

    text = message.lower()
        # Basic NLP safety filter
    unsafe_words = [
        "abuse",
        "hate",
        "kill",
        "violence"
    ]

    if any(word in text for word in unsafe_words):
        return (
            "I want to keep this conversation supportive and safe. "
            "If you are dealing with a serious or immediate problem, "
            "please reach out to a trusted person or a qualified professional."
        )

    # Basic supportive responses
    if any(word in text for word in [
        "stressed", "stress", "worried", "anxious"
    ]):
        return (
            "It sounds like your studies are putting some pressure on you. "
            "Taking a short break and talking to someone you trust may help. "
            "Would you like to tell me what is making your studies stressful?"
        )

    if any(word in text for word in [
        "sad", "lonely", "upset"
    ]):
        return (
            "I'm sorry you're having a difficult time. "
            "You don't have to handle everything alone. "
            "Would you like to share what's been bothering you?"
        )

    if any(word in text for word in [
        "hello", "hi", "hey"
    ]):
        return (
            "Hello! I'm MindCare AI. "
            "I'm here to listen. How are you feeling today?"
        )

    # Transformer response for other messages
    new_input = tokenizer.encode(
        message + tokenizer.eos_token,
        return_tensors="pt"
    )

    with torch.no_grad():

        output = model.generate(
            new_input,
            max_length=min(new_input.shape[1] + 60, 1024),
            pad_token_id=tokenizer.eos_token_id,
            do_sample=True,
            temperature=0.7,
            top_p=0.9
        )

    reply = tokenizer.decode(
        output[:, new_input.shape[-1]:][0],
        skip_special_tokens=True
    ).strip()

    if not reply:
        reply = (
            "Thank you for sharing that. "
            "Would you like to tell me more about how you are feeling?"
        )

    return reply


@app.route("/")
def home():
    return render_template_string(HTML)


@app.route("/chat", methods=["POST"])
def chat():

    data = request.get_json()
    message = data.get("message", "").strip()

    if not message:
        return jsonify({
            "reply": "Please enter a message."
        })

    reply = generate_reply(message)

    save_chat_log(message, reply)

    return jsonify({"reply": reply})


if __name__ == "__main__":
    app.run(debug=True)