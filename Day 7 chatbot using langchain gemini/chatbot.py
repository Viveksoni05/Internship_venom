from langchain_google_genai import ChatGoogleGenerativeAI

Lim = ChatGoogleGenerativeAI(model="gemini-2.0-flash", api_key="<key>")

while True:
    question = input("Ask a question (or type 'exit' to quit): ")

    if question.lower() == 'exit':
        print("Goodbye!")
        break

    response = Lim.invoke(question)
    print("Response:", response.content)
