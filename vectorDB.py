from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import Pinecone
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

pdf_path = "newly_merged_document.pdf"

def setup_pinecone_index(pdf_path):
    # Load the PDF text
    loader = PyPDFLoader(pdf_path)
    text = loader.load_and_split()

    # Initialize text splitter
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=700,
        chunk_overlap=128
    )
    text_chunks = text_splitter.split_documents(text)

    # Load the embedding model
    embeddings_model = GoogleGenerativeAIEmbeddings(
        model="models/embedding-001"
    )

    # Initialize Pinecone
    pinecone_index = Pinecone.from_documents(
        index_name='new',
        embedding=embeddings_model,
        documents=text_chunks
    )
    
    return pinecone_index



