from langchain_groq import ChatGroq
from core.config import GROQ_API_KEY, MODEL_NAME

_llm = None

def get_llm():

    global _llm

    if _llm is None:
        _llm = ChatGroq(
            groq_api_key=GROQ_API_KEY,
            model_name=MODEL_NAME
        )

    return _llm