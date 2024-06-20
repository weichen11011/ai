# 參考老師的 https://github.com/ccc112b/py2cs/blob/master/03-%E4%BA%BA%E5%B7%A5%E6%99%BA%E6%85%A7/A4-groq/hello/groqChat.py
import os
import sys
from groq import Groq



language = sys.argv[1].lower()
if (language == 'ch'):
    question = " ".join(sys.argv[2:]) + "請用中文回答"
elif (language == 'en'):
    question = " ".join(sys.argv[2:]) + "請用英文回答"
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
