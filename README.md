# 🔐 Encrypted Chat Server with GUI Client

A multithreaded C++ chat server with XOR-based message encryption, supporting real-time direct and group messaging. It communicates with a Python-based GUI client over TCP using simple encrypted messages.

## 🚀 Features
- 💬 Individual (DM) messaging using `/msg <username> <message>`
- 👥 Group creation and messaging
- 🔐 Simple XOR encryption for message privacy
- 🧵 Multithreaded server using WinSock and mutex locks
- 🖥️ Python PYQT5 GUI client

## 🛠️ Technologies Used
- **C++** (server-side)
  - WinSock API
  - STL containers, threads, mutex
- **Python** (client-side)
  - PYQT5 for GUI
  - `socket` library for TCP communication

## 📦 Project Structure
```
.
├── Server.exe (compiled output)
├── server.cpp (main server logic)
├── Client-GUI/
│   └── client.py (GUI client)
├── INSTRUCTIONS.txt
└── [Client/] ← (Deprecated: ignore this folder)
```

## ▶️ How to Run

### 🖥️ Server (C++)
1. Open Command Prompt
2. Navigate to the project directory:
   ```bash
   cd path\to\project\x64\Debug
   Server.exe
   ```

### 💻 Client (Python GUI)
1. Open VSCode or any IDE
2. Navigate to `Client-GUI/client.py`
3. Run the file:
   ```bash
   python client.py
   ```

## 💡 Supported Actions

1. **Send Message**
   - Click “Send Message” button
   - Enter:  
     ```
     /msg <username> <message>
     ```
     Example: `/msg Bhawish Hello!!`

2. **Create Group**
   - Click “Create Group”
   - Enter group name and users when prompted

3. **Send Group Message**
   - Click “Group Message”
   - Input prompts and send

## ⚠️ Notes
- The `Client/` folder contains an older console-based prototype — not required anymore.
- Make sure the server is running before launching the client.

## 📸 Demo
Watch the live demo:One thing I absolutely love about university? The projects.
They push you to build something real — and learn so much in the process.
Excited to share a quick demo of the multithreaded C++ chat server I’ve been building!
This project supports:
✅ Encrypted communication using XOR with hex encoding
✅ Individual and group messaging
✅ Real-time user and group list updates
✅ Multithreading with proper mutex protection

Whether you're learning about socket programming or exploring concurrency in C++, this walkthrough might give you a solid head start.

GithubLink: [🔗https://github.com/BhawishKumarLohana/ChatApplication]

🎥 Watch the full demo here: [🔗https://youtu.be/YYSP43V1WGY]
👇 Feedback, questions, and ideas are always welcome!

#cpp #socketprogramming #multithreading #networksecurity #linux #winsock #opensource #projectdemo #programming 

## 📬 Contributions & Feedback
Pull requests, suggestions, or feedback are welcome!
