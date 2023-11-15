from flask import Flask, render_template
from flask_socketio import SocketIO, join_room, leave_room, send

app = Flask(__name__)
socketio = SocketIO(app)

class ChatRoomsManager:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(ChatRoomsManager, cls).__new__(cls)
            cls._instance.rooms = {}
        return cls._instance

chat_rooms_manager = ChatRoomsManager()

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('join')
def handle_join(data):
    username = data['username']
    room = data['room']

    join_room(room)

    if room not in chat_rooms_manager.rooms:
        chat_rooms_manager.rooms[room] = set()

    chat_rooms_manager.rooms[room].add(username)

    socketio.emit('update_users', {'users': list(chat_rooms_manager.rooms[room])}, room=room)

@socketio.on('leave')
def handle_leave(data):
    username = data['username']
    room = data['room']

    leave_room(room)
    chat_rooms_manager.rooms[room].remove(username)

    socketio.emit('update_users', {'users': list(chat_rooms_manager.rooms[room])}, room=room)

@socketio.on('message')
def handle_message(data):
    username = data['username']
    room = data['room']
    message = data['message']

    send({'username': username, 'message': message}, room=room)

if __name__ == '__main__':
    socketio.run(app, debug=True)
