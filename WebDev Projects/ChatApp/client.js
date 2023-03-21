const socket = io('http://localhost:8000')

const form=document.getElementById('send-container')
const msgIN = document.getElementById('msgID')
const messageContainer = document.querySelector(".container")

const append =(message, position)=>{
    const msgElement = document.createElement('div');
    msgElement.innerText=message;
    msgElement.classList.add('message')
    msgElement.classList.add(position)
    messageContainer.append(msgElement)
}

const name = prompt("Enter your name to join!");
socket.emit('new-user-joined', name);

socket.on('user-joined', name =>{
    append(`${name} has joined the chat`, 'right')
})