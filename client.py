import google.generativeai as genai

# Configure the API key
genai.configure(api_key="")

# Pick a Gemini model (like gemini-1.5-flash for speed, or gemini-1.5-pro for reasoning)
model = genai.GenerativeModel("gemini-1.5-flash")

# Send a chat-style message
chat = model.start_chat()
response = chat.send_message("What is coding?")

print(response.text)
