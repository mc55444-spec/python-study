# sk-4e5dd1a2a40c4dc597c42deb7db521f9 --- deepseek api key

# Please install OpenAI SDK first: `pip3 install openai`

from openai import OpenAI

client = OpenAI(api_key="sk-4e5dd1a2a40c4dc597c42deb7db521f9", base_url="https://api.deepseek.com")

print("welcome to my application!!!!")
print("please input your question:")
content = input()


response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": ""},
        {"role": "user", "content": content},
    ],
    stream=True # 是否开启流式输出，
)

for chunk in response:
    if chunk.choices and chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="", flush=True)
print()  # 换行