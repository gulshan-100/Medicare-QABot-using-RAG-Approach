from flask import Flask, request, jsonify, render_template
from llm import create_qa_chain

app = Flask(__name__)

qa = create_qa_chain()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    question = request.json.get('question', '').strip()
    if not question:
        return jsonify({'answer': "No question provided."}), 400

    try:
        print(f"Received question: {question}") 
        answer = qa.invoke(question).get("result")
        print(f"Generated answer: {answer}")  
        if not answer:
            answer = "No answer found."
    except Exception as e:
        print(f"Error: {str(e)}")
        answer = "Sorry, I encountered an error while processing your question."

    return jsonify({'answer': answer})

if __name__ == '__main__':
    app.run(debug=True)