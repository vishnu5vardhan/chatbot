document.addEventListener('DOMContentLoaded', function() {
    addMessage('Bot', 'Good afternoon! How could I help you?');
    document.getElementById('send-button').addEventListener('click', sendMessage);
    document.getElementById('user-input').addEventListener('keydown', function(event) {
        if (event.key === 'Enter') {
            sendMessage();
        }
    });
});

function addMessage(sender, text) {
    const messagesContainer = document.getElementById('messages');
    const messageContainer = document.createElement('div');
    messageContainer.className = `message-container ${sender.toLowerCase()}-message`;

    const avatar = document.createElement('div');
    avatar.className = `${sender.toLowerCase()}-avatar`;
    avatar.textContent = sender === 'Bot' ? 'B' : 'U';

    const messageBubble = document.createElement('div');
    messageBubble.className = 'message-bubble';
    messageBubble.textContent = text;

    const timestamp = document.createElement('div');
    timestamp.className = 'message-timestamp';
    timestamp.textContent = new Date().toLocaleTimeString();

    messageBubble.appendChild(timestamp);
    messageContainer.appendChild(avatar);
    messageContainer.appendChild(messageBubble);
    messagesContainer.appendChild(messageContainer);
    messagesContainer.scrollTop = messagesContainer.scrollHeight;
}

function sendMessage() {
    const userInput = document.getElementById('user-input').value;
    if (userInput.trim() === '') return;

    addMessage('You', userInput);
    document.getElementById('user-input').value = '';

    // Send the user input to the backend and handle the response
    fetch('/get-response', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ query: userInput }),
    })
    .then(response => response.json())
    .then(data => {
        const botResponse = data.response;
        addMessage('Bot', botResponse);
    })
    .catch(error => {
        console.error('Error:', error);
        addMessage('Bot', 'Sorry, something went wrong!');
    });
}
