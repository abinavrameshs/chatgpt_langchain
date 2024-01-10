
# %%

from langchain.prompts import MessagesPlaceholder, HumanMessagePromptTemplate, ChatPromptTemplate
from langchain.memory import ConversationBufferMemory

prompt = ChatPromptTemplate(
    input_variables= ['content','messages'],
    messages=[
        MessagesPlaceholder(variable_name="messages"),
        HumanMessagePromptTemplate.from_template("{content}")
    ]
)

# %%

from langchain.chat_models import ChatOpenAI 
from langchain.chains import LLMChain
from langchain.memory import FileChatMessageHistory
from dotenv import load_dotenv

load_dotenv()
# %%

chat = ChatOpenAI()

# %%

memory = ConversationBufferMemory(
    memory_key = "messages",
    return_messages = True,
    chat_memory=FileChatMessageHistory("messages.json")
)


# %%
chain = LLMChain(
    llm=chat, 
    prompt=prompt,
    memory=memory
)

# %%
c = 1
while c<3 : 
    content = input(">>>")
    #print(content)
    result = chain(
        inputs={'content': content}
    )
    print(result['text'])
    c=c+1
# %%
