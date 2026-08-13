import os

from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_text_splitters import RecursiveCharacterTextSplitter 
from langchain_community.document_loaders import PyPDFLoader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_core.prompts import ChatPromptTemplate

# --------------------------------------------------
# 1. Load environment variables
# --------------------------------------------------

load_dotenv()

# Disable Chroma telemetry
os.environ["ANONYMIZED_TELEMETRY"] = "False"


# --------------------------------------------------
# 2. Initialize LLM
# --------------------------------------------------

llm_model = ChatOpenAI(
    base_url="https://openrouter.ai/api/v1",
    model="openrouter/free",
    api_key=os.environ["OPENROUTER_API_KEY"],
)


# --------------------------------------------------
# 3. Initialize embedding model
# --------------------------------------------------

embedding_model = HuggingFaceEmbeddings(
    model_name="BAAI/bge-small-en-v1.5"
)


# --------------------------------------------------
# 4. Create text splitter
# --------------------------------------------------

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100, 
)


# --------------------------------------------------
# 5. Load PDF
# --------------------------------------------------

pdf_loader = PyPDFLoader("./data/Trupti_Resume.pdf")

loaded_pdf = pdf_loader.load()


# --------------------------------------------------
# 6. Split PDF into chunks
# --------------------------------------------------

chunks = splitter.split_documents(loaded_pdf)

print(f"Total chunks created: {len(chunks)}")


# --------------------------------------------------
# 7. Create Chroma vector database
# --------------------------------------------------

chroma_db = Chroma.from_documents(
    documents=chunks,
    embedding=embedding_model,
    persist_directory="./rag_basic_chroma_db",
)


# --------------------------------------------------
# 8. Create prompt
# --------------------------------------------------

prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
You are a helpful AI assistant that answers questions
based only on the provided context.

Rules:
1. Use only the provided context.
2. If the answer cannot be found in the context, say:
   "I couldn't find that information in the document."
3. Do not summarize the entire document unless explicitly asked.
4. Answer the user's specific question directly.
"""
    ),
    (
        "human",
        """
Context:
{context}

User question:
{query}
"""
    ),
])


# --------------------------------------------------
# 9. Create chain
# --------------------------------------------------

chain = prompt | llm_model


# --------------------------------------------------
# 10. Chat loop
# --------------------------------------------------

print("\nAI: Hi, how can I help you with your document?")
print("Type 'exit' to quit.\n")


while True:

    user_ques = input("Human: ").strip()

    if user_ques.lower() == "exit":
        print("AI: Goodbye!")
        break

    if not user_ques:
        continue


    # --------------------------------------------------
    # 11. Retrieve relevant documents
    # --------------------------------------------------

    documents = chroma_db.similarity_search(
        user_ques,
        k=3
    )


    # --------------------------------------------------
    # 12. Convert Documents into plain text
    # --------------------------------------------------

    context = "\n\n".join(
        document.page_content
        for document in documents
    )


    # --------------------------------------------------
    # 13. Generate answer
    # --------------------------------------------------

    response = chain.invoke({
        "query": user_ques,
        "context": context,
    })


    # --------------------------------------------------
    # 14. Display answer
    # --------------------------------------------------

    print("\nAI:", response.content)
    print()