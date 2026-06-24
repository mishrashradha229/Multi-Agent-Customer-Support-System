import os

from llm.gemini import ask_llm as gemini_llm
from llm.groq_llm import ask_llm as groq_llm


DEFAULT_PROVIDER = os.getenv(

    "LLM_PROVIDER",

    "gemini"

).lower()


def ask_llm(prompt, provider=None):

    provider = (provider or DEFAULT_PROVIDER).lower()

    if provider == "groq":

        return groq_llm(prompt)

    return gemini_llm(prompt)