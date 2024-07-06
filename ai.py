from openai import OpenAI
import assemble

api_key = assemble.ai_api 
client = OpenAI(api_key = api_key)
def receive(message):
    completion = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "assistant", "content": assemble.setting},
            {"role": "user", "content": message + "請優先搜尋" + assemble.priority_search}
        ]
    )

    return str(completion.choices[0].message)

