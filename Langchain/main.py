from langchain_groq import ChatGroq

# Initialize the Groq chat model
# We're using LLaMA 3 70B model, which is one of the latest available on Groq
llm = ChatGroq(
    model="llama3-70b-8192",
    temperature=0.3,
    max_tokens=500,
)

# Generate the response using LangChain's invoke method
response = llm.invoke("What are the 7 wonders of the world?")
print(f"Response: {response.content}")