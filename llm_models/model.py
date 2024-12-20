from langchain_community.chat_models import ChatOpenAI

# OpenAI API 키 설정
OPENAI_API_KEY = "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"

# GPT-4 모델 설정
llm = ChatOpenAI(
    model="gpt-4o",
    temperature=0,
    model_kwargs={"top_p": 0.9},  # top_p 값을 여기에 설정
    openai_api_key=OPENAI_API_KEY
)

# GPT-4 Turbo 모델 설정
closed_llm = ChatOpenAI(
    model="gpt-4", temperature=0, top_p=0, openai_api_key=OPENAI_API_KEY
)

# 동일 모델 다른 설정
solver_llm = ChatOpenAI(
    model="gpt-4o", temperature=0, openai_api_key=OPENAI_API_KEY
)
