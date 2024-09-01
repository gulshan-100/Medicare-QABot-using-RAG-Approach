document.addEventListener('DOMContentLoaded', () => {
    const chatbox = document.getElementById('chatbox');
    const questionInput = document.getElementById('question');
    const sendBtn = document.getElementById('send-btn');
    const clearChatBtn = document.getElementById('clear-chat');
    const downloadChatBtn = document.getElementById('download-chat');

    function addMessage(text, isUser) {
        const messageDiv = document.createElement('div');
        messageDiv.classList.add('message');
        messageDiv.classList.add(isUser ? 'user-message' : 'bot-message');
        messageDiv.innerHTML = text.replace(/\n/g, '<br>'); // Replace newlines with <br> for HTML formatting
        chatbox.appendChild(messageDiv);
        chatbox.scrollTop = chatbox.scrollHeight;
    }

    function addLoadingIndicator() {
        const loadingDiv = document.createElement('div');
        loadingDiv.classList.add('loading');
        // You might want to add some actual loading spinner CSS to the .loading class
        chatbox.appendChild(loadingDiv);
        chatbox.scrollTop = chatbox.scrollHeight;
        return loadingDiv;
    }

    async function askQuestion() {
        const question = questionInput.value.trim();
        if (question) {
            addMessage(question, true);
            questionInput.value = '';
            questionInput.focus();

            const loadingIndicator = addLoadingIndicator();

            try {
                const response = await fetch('/ask', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({question: question})
                });

                chatbox.removeChild(loadingIndicator);

                if (response.ok) {
                    const data = await response.json();
                    addMessage(data.answer || 'No response from the server.', false);
                } else {
                    addMessage('Error: ' + response.statusText, false);
                }
            } catch (error) {
                console.error('Error:', error);
                chatbox.removeChild(loadingIndicator);
                addMessage('Sorry, an error occurred while processing your question.', false);
            }
        }
    }

    sendBtn.addEventListener('click', askQuestion);
    questionInput.addEventListener('keypress', (event) => {
        if (event.key === 'Enter') {
            askQuestion();
        }
    });

    clearChatBtn.addEventListener('click', () => {
        chatbox.innerHTML = ''; // Clear chat messages
    });

    downloadChatBtn.addEventListener('click', () => {
        const chatContent = chatbox.innerText; // Get the plain text content
        const blob = new Blob([chatContent], { type: 'text/plain;charset=utf-8' });
        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = 'chat.txt';
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
    });
});
