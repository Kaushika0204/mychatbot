class Chatbox {
    constructor() {
        this.args = {
            openButton: document.querySelector('.chatbox__button'),
            chatBox: document.querySelector('.chatbox__support'),
            sendButton: document.querySelector('.send__button')
        };

        this.state = false;
        this.messages = [];
        this.intents = [];

        this.display();
        this.loadResponses();
        this.toggleState(this.args.chatBox);
    }

    display() {
        const { openButton, chatBox, sendButton } = this.args;

        openButton.addEventListener('click', () => this.toggleState(chatBox));
        sendButton.addEventListener('click', () => this.onSendButton(chatBox));

        const node = chatBox.querySelector('input');
        node.addEventListener('keyup', ({ key }) => {
            if (key === 'Enter') {
                this.onSendButton(chatBox);
            }
        });
    }

    loadResponses() {
        fetch('bot.json')
            .then((response) => response.json())
            .then((data) => {
                this.intents = data.intents;
            })
            .catch((error) => {
                console.error('Error loading responses:', error);
            });
    }

    toggleState(chatbox) {
        this.state = !this.state;

        // Show or hide the box
        if (this.state) {
            chatbox.classList.add('chatbox--active');
        } else {
            chatbox.classList.remove('chatbox--active');
        }
    }

    onSendButton(chatbox) {
        var textField = chatbox.querySelector('input');
        let text1 = textField.value;
        if (text1 === '') {
            return;
        }

        let msg1 = { name: 'User', message: text1 };
        this.messages.push(msg1);

        // Process user input and get a response
        const chatbotResponse = this.getChatbotResponse(text1);
        let msg2 = { name: 'meteori', message: chatbotResponse };
        this.messages.push(msg2);
        this.updateChatText(chatbox);
        textField.value = '';
    }

    getChatbotResponse(userInput) {
        userInput = userInput.toLowerCase();
    
        for (const intent of this.intents) {
            for (const pattern of intent.patterns) {
                if (userInput.includes(pattern.toLowerCase())) {
                    // Generate a random index within the responses array
                    const randomIndex = Math.floor(Math.random() * intent.responses.length);
                    return intent.responses[randomIndex];
                }
            }
        }
    
        return "I'm sorry, I don't understand. Can you please rephrase your question?";
    }
    
    

    updateChatText(chatbox, errorMessage = null) {
        var html = '';
        this.messages.slice().reverse().forEach(function (item) {
            if (item.name === 'meteori') {
                html += '<div class="messages__item messages__item--visitor">' + item.message + '</div>';
            } else {
                html += '<div class="messages__item messages__item--operator">' + item.message + '</div>';
            }
        });

        const chatmessage = chatbox.querySelector('.chatbox__messages');
        chatmessage.innerHTML = html;

        // If an error message is provided, display it.
        if (errorMessage) {
            chatmessage.innerHTML += '<div class="messages__item messages__item--operator">' + errorMessage + '</div>';
        }
    }
}

const chatbox = new Chatbox();