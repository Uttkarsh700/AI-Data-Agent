from langchain_openai import ChatOpenAI, ChatAnthropic
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
import os

load_dotenv()

def pick_llm(Level: str):

    """
    Picks the appropriate LLM based on the user's level of the question.

    Args:
        Level (str): low, medium or high

    Returns:
        LLM object
    """

    if Level.lower() == "low":
        return ChatAnthropic(
            model="claude-opus-4-6",
            temperature=0,
            api_key=os.getenv("AGENTROUTER_API_KEY"),
            base_url="https://agentrouter.org"
        )

    elif Level.lower() == "medium":
        return ChatOpenAI(
            model="gpt-5.5",
            temperature=0.9,
            api_key=os.getenv("AGENTROUTER_API_KEY"),
            base_url="https://agentrouter.org/v1"
        )

    elif Level.lower() == "high":
        return ChatOpenAI(
            model="gpt-5.5",
            temperature=0.9,
            api_key=os.getenv("AGENTROUTER_API_KEY"),
            base_url="https://agentrouter.org/v1"
        )

    else:
        raise ValueError(f"Invalid level: {Level}")


llm_obj = pick_llm("low")

response = llm_obj.invoke("hello")

print(response.content)