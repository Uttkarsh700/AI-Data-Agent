import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utlis.llm_pick import pick_llm
from models.schema import AgentSchema

# ------------------------------------ AI Agent Code ------------------------------------ #

def curate_question(state: AgentSchema) -> AgentSchema:  

    user_question = state.user_question # Bcz this is a pydantic model object

    llm = pick_llm("low") #pick the appropraite LLM based on the level of the question.

    response = llm.invoke(f"curate the following question: {user_question}.")

    state.curated_ques = response
    return state


def prompt_query_context(state: AgentSchema) -> AgentSchema:

    curate_question = state.curated_ques 
  




