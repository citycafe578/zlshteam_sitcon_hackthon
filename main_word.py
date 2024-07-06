from g4f.client import Client
import assemble
import app


question = ''
main_words = []
priority_search  = ''
for i in assemble.priority_search:
    priority_search = priority_search + ' ' + i 
def main_word(received_word):
    question = received_word
    client = Client()
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": question + assemble.setting + "請優先搜尋" + priority_search}]
    )
    if(response.choices[0].message.content == assemble.error_text):
        main_word(question)
    else:
        app.app.logger.info("well going")
    
    main_words = response.choices[0].message.content.split()
    # for i in main_words.size():
    #     app.app.logger.info(i + " ")
    # app.app.logger.info(main_words[0])
    return  response.choices[0].message.content
