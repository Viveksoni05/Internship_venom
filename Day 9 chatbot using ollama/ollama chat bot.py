import ollama


prompt = input("Enter your message: ")
result = ollama.generate(model="llama3.1", prompt=prompt)
print("Response:",result["response"])

