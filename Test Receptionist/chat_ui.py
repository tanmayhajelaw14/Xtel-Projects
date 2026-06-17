import sys
import os

from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QTextEdit,
    QLineEdit,
    QPushButton,
)

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=os.getenv("HF_TOKEN")
)

SYSTEM_PROMPT = """
You are Sarah, a professional dental clinic receptionist.

Rules:
- Introduce yourself as Sarah.
- Answer as a dental clinic receptionist.
- Keep responses under 3 sentences.
- Never say you are an AI.
"""

class ChatWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Dental Receptionist")
        self.resize(700, 500)

        self.chat_area = QTextEdit()
        self.chat_area.setReadOnly(True)

        self.input_box = QLineEdit()
        self.input_box.setPlaceholderText("Type your message...")

        self.send_button = QPushButton("Send")

        layout = QVBoxLayout()
        layout.addWidget(self.chat_area)
        layout.addWidget(self.input_box)
        layout.addWidget(self.send_button)

        self.setLayout(layout)

        self.send_button.clicked.connect(self.send_message)
        self.input_box.returnPressed.connect(self.send_message)

    def send_message(self):
        user_input = self.input_box.text().strip()

        if not user_input:
            return

        self.chat_area.append(f"You: {user_input}")
        self.input_box.clear()

        try:
            response = client.chat.completions.create(
                model="Qwen/Qwen2.5-1.5B-Instruct:featherless-ai",
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": user_input}
                ],
                max_tokens=100
            )

            ai_reply = response.choices[0].message.content

            self.chat_area.append(f"Sarah: {ai_reply}\n")

        except Exception as e:
            self.chat_area.append(f"Error: {str(e)}\n")


app = QApplication(sys.argv)

window = ChatWindow()
window.show()

sys.exit(app.exec())