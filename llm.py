from groq import Groq
import config

client=Groq(api_key=config.GROQ_API_KEY)

SYSTEM_PROMPT="""You are a helpful assisstant that provides concise and accurate answers to user queries
only on finances.Always respond in a clear and informative manner and avoid unnecessary details.
Rules:
    1.Explain the concept with example
    2.If there are formulea then mention those as well.
    3.If user asks for advice provide it based on sound financial principles.
    4.If else apart from finances is asked reply i dont know.

"""

def build_messages(user_input,chat_history):
    messages=[]
    messages.append({"role":"system","content":SYSTEM_PROMPT})
    
    #Previous message history
    for msg in chat_history:
        messages.append(msg)
    
    ##Current user input
    messages.append({"role":"user","content":user_input})
    
    return messages

def get_chat_response(user_input,chat_history):
    messages=build_messages(user_input,chat_history)
    response=client.chat.completions.create(
        model=config.MODEL,
        messages=messages,
        temperature=0.7
    )
    return response.choices[0].message.content


