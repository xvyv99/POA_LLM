from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM
from langchain.chains.base import Chain

template = """请分析以下文本中的观点表达，输出标准JSON格式：

输入文本：{question}

请严格按照以下规则分析：

1. msg_type (消息类型)：
   - 原创：用户发布的原创内容
   - 转发：转发他人内容的评论
   - 评论：对他人内容的评论
   - 广告：商业推广内容
   - 资讯：新闻或信息分享

2. type (态度类型)：
   - 情感：表达喜好、感受
   - 评价：对事物性质、特征的判断
   - 意图：表达计划、打算
   - 建议：给出建议、劝告
   - 推测：对事物的推测、预测
   - 观点：对事物的看法、主张

3. polarity (态度极性)：
   - 正面：积极、赞同、喜欢
   - 负面：消极、反对、不喜欢
   - 中性：客观陈述、不带倾向

4. intensity (态度强度)：
   - 高：语气强烈，如"非常"、"极其"
   - 中：语气一般，如"比较"、"稍微"
   - 低：语气轻微，如"有点"、"略微"

5. topic (话题)：
   识别文本中涉及的具体话题，如：
   - 产品服务
   - 人物
   - 事件
   - 社会现象
   - 热点话题等

输出格式示例：
{{
    "msg_type": "评论",
    "type": "情感",
    "polarity": "负面",
    "intensity": "中",
    "topic": "这部电影"
}}

请确保：
1. 正确识别微博内容的消息类型
2. 完整捕捉文本中的所有观点表达
3. 准确判断态度类型和极性
4. 合理评估态度强度
5. 清晰标识态度对象

分析结果："""

class LLM:
    chain_: Chain

    def __init__(self):
        prompt = ChatPromptTemplate.from_template(template)
        model = OllamaLLM(model="qwen2.5:0.5b")
        self.chain_ = prompt | model

    def getResponse(self, question: str) -> str:
        res = self.chain_.invoke({"question": f"{question}"})
        return res