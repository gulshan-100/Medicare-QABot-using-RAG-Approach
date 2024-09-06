from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_community.vectorstores import Pinecone
from dotenv import load_dotenv, find_dotenv
from langchain.chains import RetrievalQA
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate

load_dotenv(find_dotenv())

# Initialize the Groq model
groq_model = ChatGroq(
    model="llama3-70b-8192",
    temperature=0.0
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

    # Define a custom prompt template
    prompt_template = """Use the following pieces of context to answer the question of user in 
    detail at the end. Solve the user query in best way possible in detailed manner. If you don't know the answer, just say that you don't know, don't try 
    to make up an answer.

    {context}

    Question: {question}
    Answer:"""

    PROMPT = PromptTemplate(
        template=prompt_template, input_variables=["context", "question"]
    )

    # Create and return the RetrievalQA chain with the custom prompt
    qa_chain = RetrievalQA.from_chain_type(
        llm=groq_model,
        chain_type="stuff",
        retriever=knowledge.as_retriever(),
        return_source_documents=True,
        chain_type_kwargs={"prompt": PROMPT}
    )
    
    return qa_chain
