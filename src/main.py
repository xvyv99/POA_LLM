from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM

template = """Question: {question}

Answer: Let's think step by step."""

prompt = ChatPromptTemplate.from_template(template)

model = OllamaLLM(model="qwen2.5:7b")

chain = prompt | model

print(chain.invoke({"question": "请判断以下文本的观点倾向，真诚的认为遇上你是我的缘，仅需要回答正面与负面即可"}))