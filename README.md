# Medicare-QABot-using-RAG-Approach
**Project Overview**
This chatbot uses a RAG approach to provide informative responses based on a knowledge base stored in a vector database. It combines the power of language models with efficient information retrieval to generate accurate and contextually relevant answers.

**Screenshot**
![Sreenshot](https://github.com/gulshan-100/Medicare-QABot-using-RAG-Approach/blob/main/Screenshot.png)

**Features**
* PDF document ingestion and processing
* Text chunking and embedding
* Vector storage using Pinecone
* Integration with Google's Generative AI for embeddings
* Use of Groq's LLM for text generation
* Flask-based web API
* Simple HTML/CSS/JS frontend for user interaction

**Technology Stack**
* Backend: Python, Flask
* Frontend: HTML, CSS, JavaScript
* Language Models: Google Generative AI (for embeddings) & Groq (llama3-70b-8192 model for text generation)
* Vector Database: Pinecone
* Text Processing: LangChain

**Project Structure**
* vectordb.py: Handles PDF ingestion, text splitting, and Pinecone index setup
* llm.py: Sets up the language model and QA chain
* app.py: Flask application for serving the API
* templates/index.html* : Frontend HTML file
* static/: Directory for CSS and JS files (not shown in provided code)

**Setup and Installation**

1. Clone the repository:
    ```
    git clone https://github.com/gulshan-100/Medicare-QABot-using-RAG-Approach.git
    cd  Medicare-QABot-using-RAG-Approach
    ```
2. Install required dependencies:
   ```
    pip install -r requirements.txt
   ```
3. Set up environment variables: Create a .env file in the project root and add the following:
   ```
    GOOGLE_API_KEY=<your-google-api-key>
    PINECONE_API_KEY=<your-pinecone-api-key>
    GROQ_API_KEY=<your-groq-api-key>
   ```
4. Run the Application:
   ```
    python app.py
   ```
**Usage**
1. Start the Flask Application:
    ```python app.py```
2. Open a web browser and navigate to http://localhost:5000 to access the chatbot interface.
3. Enter your questions in the provided input field and receive answers from the chatbot.

**FrontEnd**
The frontend is a simple HTML page with CSS styling and JavaScript for handling user interactions. It sends questions to the backend API and displays the responses.

**Demo Video**
[Project Demo](https://github.com/gulshan-100/Medicare-QABot-using-RAG-Approach/blob/main/Demo_video.mp4)]

