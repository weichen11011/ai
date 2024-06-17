import os
import sys
from groq import Groq

while True:
    language = sys.argv[1].lower()
    question = " ".join(sys.argv[2:])
    print(f"選擇的語言：{language}")
    print("問題：", question)

    client = Groq(
        api_key="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",
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": question,
            }
        ],
        model="llama3-8b-8192",
    )

    print(chat_completion.choices[0].message.content)
