from mistralai import Mistral

model = Mistral( api_key="<key>")
response = model.chat.complete(model="mistral-small-2506", messages=[
    {
        "role": "user",
        "content": "You measure my life in hours and I serve you by expiring. I’m quick when I’m thin and slow when I’m fat. The wind is my enemy."
    }
])
print("Response:", response.choices[0].message.content)
