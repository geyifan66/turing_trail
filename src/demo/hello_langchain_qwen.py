from langchain_qwq import ChatQwQ

apikey = 'sk-4002be77e85a4f5e86880895dbbd60f2'
base_url='https://dashscope.aliyuncs.com/compatible-mode/v1'

import os
os.environ["DASHSCOPE_API_KEY"] = apikey
os.environ["DASHSCOPE_API_BASE"] = base_url

evn =  os.getenv("DASHSCOPE_API_KEY")
print(evn)

model = ChatQwQ(model="qwq-plus")
response = model.invoke("Hello, how are you?")
content = response.content
print(content)

# 访问模型推理内容
reasoning = response.additional_kwargs.get("reasoning_content", "")
print(f"Response: {content}")
print(f"Reasoning: {reasoning}")