from langchain_openai import ChatOpenAI, ChatAnthropic
from dotenv import load_dotenv
load_dotenv()

def pick_llm(Level: str):

    """ 
    Picks the appropriate LLM based on the user's level of the question 
    
    Args :
      level(str) : The level of the question, can be easy, medium or hard.

    Returns :
      The name of llm to be used.
    """

    if Level.lower() == "low":
        return ChatAnthropic()(Model="claude-2", temperature=0)
    elif Level.lower() == "medium":
        return ChatOpenAI(temperature=0.9, model_name="gpt-3.5-turbo")
    elif Level.lower() == "high":
        return ChatOpenAI(temperature=0.9, model_name="gpt-4")
    else:
        raise ValueError(f"Invalid level: {Level}")

    return pick_llm

llm_obj = pick_llm("low")
print(llm_obj.invoke("hello"))