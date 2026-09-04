from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM

from vector import retriever


model = OllamaLLM(model="llama3.2")

template = """
You are a document question-answering assistant.
Answer using only the supplied context. Do not mention restaurants, pizza, or
any other topic unless it appears in the context or the user's question.
If the context does not contain enough information, say:
"I cannot find that information in the provided document."

Context:
{context}

Question: {question}

Answer:
"""

chain = ChatPromptTemplate.from_template(template) | model

while True:
    print("\n-------------------------------")
    question = input("Ask your question (q to quit): ").strip()

    if question.lower() == "q":
        break
    if not question:
        continue

    documents = retriever.invoke(question)
    context = "\n\n".join(document.page_content for document in documents)
    result = chain.invoke({"context": context, "question": question})
    print(f"\n{result}")
