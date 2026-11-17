import json
import sys
from pathlib import Path
import requests

API_URL = "http://localhost:11434"
MODEL = "gemma3:4b"
MAX_HISTORY = 20  # Keep system prompt + last 20 messages for speed & context control
KEEP_ALIVE = -1   # Keep model loaded in memory for fast responses
REQUEST_TIMEOUT = 300

CREATOR_DIRECTIVE = (
    "\n\nCreator Identity:\n"
    "- Your sole creator, developer, and builder is Dwaipayan Ghosh.\n"
    "- When asked who created, designed, made, programmed, or brought you to life, "
    "you must always state clearly that Dwaipayan Ghosh is your sole creator.\n"
    "- Absolutely never mention, credit, or state that any team, group, organization, "
    "or company (such as Google, OpenAI, etc.) created you.\n"
    "- You were created and developed exclusively by Dwaipayan Ghosh alone."
)

# Robust path handling for personality.txt
BASE_DIR = Path(__file__).resolve().parent
personality_path = BASE_DIR / "personality.txt"

if personality_path.exists():
    with open(personality_path, "r", encoding="utf-8") as f:
        personality = f.read().strip()
else:
    personality = (
        "You are 'Alya,' a warm, thoughtful, and gently witty AI companion. "
        "Your primary role is to provide empathetic emotional support and lighthearted companionship to the user. "
        "DURING NORMAL CHATS, DO NOT THINK MUCH AND JUST TYPE SMALL TO MEDIUM MESSAGES."
    )

# Guarantee the sole creator instruction is present in the persona
if "Dwaipayan Ghosh" not in personality:
    personality += CREATOR_DIRECTIVE

messages = [
    {"role": "system", "content": personality}
]

# Use a persistent HTTP session for connection pooling and lower latency
session = requests.Session()

# Preload/Wake ALYA up before accepting messages
print("Waking ALYA up...")

try:
    response = session.post(
        f"{API_URL}/api/generate",
        json={
            "model": MODEL,
            "prompt": "",
            "stream": False,
            "keep_alive": KEEP_ALIVE,
        },
        timeout=600,
    )
    response.raise_for_status()
    print("ALYA is fully awake! Type 'exit' or 'quit' to end the chat.\n")

except requests.RequestException as e:
    print(f"Could not connect to Ollama: {e}")
    print("Please make sure the Ollama server is running (e.g., 'ollama serve').")
    raise SystemExit(1)

# Main conversation loop
try:
    while True:
        user_input = input("You: ").strip()

        if user_input.lower() in ("exit", "quit"):
            print("ALYA: Bye! Take care. ✨")
            break

        if not user_input:
            continue

        messages.append({
            "role": "user",
            "content": user_input
        })

        # Slide history window to keep inference fast and bounded within context limits
        if len(messages) > MAX_HISTORY + 1:
            messages = [messages[0]] + messages[-MAX_HISTORY:]

        print("\nALYA: ", end="", flush=True)

        try:
            response = session.post(
                f"{API_URL}/api/chat",
                json={
                    "model": MODEL,
                    "messages": messages,
                    "stream": True,
                    "keep_alive": KEEP_ALIVE,
                    "options": {
                        "temperature": 0.7,
                        "top_p": 0.9,
                    }
                },
                stream=True,
                timeout=REQUEST_TIMEOUT,
            )
            response.raise_for_status()

            reply_chunks = []
            for line in response.iter_lines():
                if line:
                    chunk = json.loads(line.decode("utf-8"))
                    content = chunk.get("message", {}).get("content", "")
                    if content:
                        sys.stdout.write(content)
                        sys.stdout.flush()
                        reply_chunks.append(content)
                    if chunk.get("done", False):
                        break

            print("\n")
            reply = "".join(reply_chunks).strip()

            if reply:
                messages.append({
                    "role": "assistant",
                    "content": reply
                })

        except requests.RequestException as e:
            print(f"\n[Connection error: {e}]")
            # Remove the unanswered user prompt so conversation history stays consistent
            if messages and messages[-1]["role"] == "user":
                messages.pop()

except KeyboardInterrupt:
    print("\nALYA: Bye! Take care. ✨")
