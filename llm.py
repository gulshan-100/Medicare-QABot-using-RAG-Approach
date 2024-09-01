from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_community.vectorstores import Pinecone
from dotenv import load_dotenv, find_dotenv
from langchain.chains import RetrievalQA  
from langchain_groq import ChatGroq

load_dotenv(find_dotenv())

# Initialize the Groq model
groq_model = ChatGroq(
    model="llama3-70b-8192"
)

def create_qa_chain():
    # Load the embedding model
    embedding_model = GoogleGenerativeAIEmbeddings(
        model="models/embedding-001"
    )

    # Initialize Pinecone with existing index
    knowledge = Pinecone.from_existing_index(
        index_name="new",
        embedding=embedding_model
    )

    # Create and return the RetrievalQA chain
    qa_chain = RetrievalQA.from_chain_type(
        llm=groq_model,
        chain_type="stuff",
        retriever=knowledge.as_retriever()
    )
    
    return qa_chain



