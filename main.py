from groq import Groq
from api_key import client

system_prompt = "Act like a mentor and give short answers."
messages = [{"role": "system", "content": system_prompt}]

while True:
    user_prompt = input("Prompt: ")

    # Break the loop if the user types 'stop'
    if user_prompt.lower() == "stop":
        print("Chat ended.")
        break

    messages.append({"role": "user", "content": user_prompt})
    response = client.chat.completions.create(
        messages=messages,
        model="llama-3.3-70b-versatile",
    )

    reply = response.choices[0].message.content
    print(reply)

    messages.append({"role": "assistant", "content": reply})
