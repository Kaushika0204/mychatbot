class Chatbox {
    constructor() {
        this.args = {
            openButton: document.querySelector('.chatbox__button'),
            chatBox: document.querySelector('.chatbox__support'),
            sendButton: document.querySelector('.send__button')
        }

        this.state = false;
        this.messages = [];

        this.display();
    }

    display() {
        const { openButton, chatBox, sendButton } = this.args;

        openButton.addEventListener('click', () => this.toggleState(chatBox));
        sendButton.addEventListener('click', () => this.onSendButton(chatBox));

        const node = chatBox.querySelector('input');
        node.addEventListener("keyup", ({ key }) => {
            if (key === "Enter") {
                this.onSendButton(chatBox);
            }
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
        if (text1 === "") {
            return;
        }

        let msg1 = { name: "User", message: text1 };
        this.messages.push(msg1);

        // Send the user input to the server
        fetch('/chat', {
            method: 'POST',
            body: JSON.stringify({ user_input: text1 }),
            headers: {
                'Content-Type': 'application/json'
            },
        })
            .then(response => {
                if (response.ok) {
                    return response.json();
                } else {
                    throw new Error('Network response was not ok');
                }
            })
            .then(data => {
                console.log(data);
                const chatbotResponse = data.chatbot_response;
                let msg2 = { name: "meteori", message: chatbotResponse };
                this.messages.push(msg2);
                this.updateChatText(chatbox);
                textField.value = '';
            })
            .catch(error => {
                console.error('Error:', error);
                // Handle the error gracefully, e.g., display an error message to the user.
                this.updateChatText(chatbox, 'An error occurred. Please try again.');
                textField.value = '';
            });
    }

    updateChatText(chatbox, errorMessage = null) {
        var html = '';
        this.messages.slice().reverse().forEach(function (item) {
            if (item.name === "meteori") {
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
