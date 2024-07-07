from openai import OpenAI
import assemble
import app
import os
from PIL import Image
import pytesseract

api_key = assemble.ai_api 
client = OpenAI(api_key = api_key)
main_idea = ''

def receive(message):
    completion = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "assistant", "content": assemble.setting},
            {"role": "user", "content": message + "請優先搜尋" + assemble.priority_search}
        ]
    )
    ans = str(completion.choices[0].message)
    main_idea = ask_idea(ans)
    return ans, main_idea

def img_receive(img_id):
    img_path = f"images\\{img_id}.jpg"
    img = Image.open(img_path)
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    text = pytesseract.image_to_string(img, lang='eng')
    if os.path.exists(img_path):
        os.remove(img_path)
        img_path = ''
    completion = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "assistant", "content": assemble.setting},
            {"role": "user", "content": text + "請優先搜尋" + assemble.priority_search}
        ]
    )
    ans = str(completion.choices[0].message)
    main_idea = ask_idea(ans)
    return ans, main_idea

def ask_idea(ans):
    completion = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "assistant", "content": assemble.setting},
            {"role": "user", "content": ans + "請問這題的核心觀念是什麼，用最簡單的文字回答，用繁體中文" + assemble.priority_search}
        ]
    )
    main_idea = str(completion.choices[0].message)
    main_idea = main_idea.replace("ChatCompletionMessage(content='", "")
    main_idea = main_idea.replace("', role='assistant', function_call=None, tool_calls=None)", "")
    main_idea = main_idea.replace("\n", "%0D%0A")
    app.app.logger.info("Main Idea:", main_idea)
    return main_idea
