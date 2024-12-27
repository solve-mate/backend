from langchain_openai.chat_models import ChatOpenAI  # ChatOpenAI로 변경
from langchain.prompts import ChatPromptTemplate  # 챗 모델에 맞는 프롬프트 템플릿
from langchain.schema.runnable import RunnableSequence  # RunnableSequence 사용
import os
from dotenv import load_dotenv

# 환경 변수 로드
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# OpenAI Chat 모델 객체 초기화
llm = ChatOpenAI(
    openai_api_key=OPENAI_API_KEY,
    model="gpt-3.5-turbo",  # 챗 모델 사용
    temperature=0.7,
    max_tokens=300,
)

# 챗 프롬프트 템플릿 정의
prompt = ChatPromptTemplate.from_template(template="문제를 읽어줘: {question}")

# RunnableSequence 사용
qa_chain = prompt | llm  # 프롬프트와 LLM을 파이프처럼 연결


def get_gpt_response(question: str) -> str:
    """질문에 대한 LangChain 기반 응답 생성"""
    return qa_chain.invoke({"question": question})
