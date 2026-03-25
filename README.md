# Jarvage-project.
https://github.com/iitnikhil6388-dot/Jarvage-project.

# 🎙️ Voice Assistant using Python

This project is a simple **Voice Assistant** built using Python. It can recognize voice commands and perform tasks like playing music, searching Wikipedia, opening applications, and sending WhatsApp messages.

---

## 🚀 Features

* 🎤 Voice command recognition
* 🔊 Text-to-speech response
* 🎵 Play random music from YouTube
* ⏰ Tell current time
* 🌐 Open websites like YouTube and Google
* 📖 Search information from Wikipedia
* 💬 Send WhatsApp messages instantly
* 🖥️ Open applications on your system

---

## 🛠️ Technologies Used

* Python
* `pyttsx3` (Text-to-Speech)
* `speech_recognition` (Voice Input)
* `pyautogui` (System automation)
* `wikipedia` (Information retrieval)
* `pywhatkit` (WhatsApp automation)
* `webbrowser` (Open websites)

---

## 📦 Installation

Install the required libraries using pip:

```bash
pip install pyttsx3 SpeechRecognition pyautogui wikipedia pywhatkit pyaudio
```

⚠️ Note:

* If `pyaudio` gives error, install it separately depending on your system.

---

## ▶️ How to Run

```bash
python your_file_name.py
```

After running:

1. Speak a command
2. Assistant will respond and perform the action

---

## 🗣️ Supported Commands

| Command Example            | Action                    |
| -------------------------- | ------------------------- |
| "Hello"                    | Greets user               |
| "Play my favourite music"  | Plays random song         |
| "Say time"                 | Tells current time        |
| "Open YouTube"             | Opens YouTube             |
| "Search Wikipedia [topic]" | Gives info from Wikipedia |
| "Search Google [query]"    | Opens Google search       |
| "Send WhatsApp"            | Sends predefined message  |

---

## ⚙️ Configuration

* Replace phone number in WhatsApp section:

```python
pwk.sendwhatmsg_instantly("+91XXXXXXXXXX","Hello from Nikhil",15,True,2)
```

* Change voice:
# 🎙️ Voice Assistant using Python

This project is a simple **Voice Assistant** built using Python. It can recognize voice commands and perform tasks like playing music, searching Wikipedia, opening applications, and sending WhatsApp messages.

---

## 🚀 Features

* 🎤 Voice command recognition
* 🔊 Text-to-speech response
* 🎵 Play random music from YouTube
* ⏰ Tell current time
* 🌐 Open websites like YouTube and Google
* 📖 Search information from Wikipedia
* 💬 Send WhatsApp messages instantly
* 🖥️ Open applications on your system

---

## 🛠️ Technologies Used

* Python
* `pyttsx3` (Text-to-Speech)
* `speech_recognition` (Voice Input)
* `pyautogui` (System automation)
* `wikipedia` (Information retrieval)
* `pywhatkit` (WhatsApp automation)
* `webbrowser` (Open websites)

---

## 📦 Installation

Install the required libraries using pip:

```bash
pip install pyttsx3 SpeechRecognition pyautogui wikipedia pywhatkit pyaudio
```

⚠️ Note:

* If `pyaudio` gives error, install it separately depending on your system.

---

## ▶️ How to Run

```bash
python your_file_name.py
```

After running:

1. Speak a command
2. Assistant will respond and perform the action

---

## 🗣️ Supported Commands

| Command Example            | Action                    |
| -------------------------- | ------------------------- |
| "Hello"                    | Greets user               |
| "Play my favourite music"  | Plays random song         |
| "Say time"                 | Tells current time        |
| "Open YouTube"             | Opens YouTube             |
| "Search Wikipedia [topic]" | Gives info from Wikipedia |
| "Search Google [query]"    | Opens Google search       |
| "Send WhatsApp"            | Sends predefined message  |

---

## ⚙️ Configuration

* Replace phone number in WhatsApp section:

```python
pwk.sendwhatmsg_instantly("+91XXXXXXXXXX","Hello from Nikhil",15,True,2)
```

* Change voice:

```python
engine.setProperty('voice', voices[1].id)
```

---
***



