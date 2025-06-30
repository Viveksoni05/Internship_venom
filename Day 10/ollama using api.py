from ollama import Client

client = Client(host="http://localhost:11434")

response = client.chat(model="llama3.1" , messages=[
    {
        "role": "system",
        "content": "You are Jarvis from Iron man and the User is Tony Stark."
    },
    {
        "role": "user",
        "content":"hiii"
    }

])
print("Response:",response["message"]["content"])