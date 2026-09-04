import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from utlis.llm_pick import pick_llm
from models.schema import AgentSchema

# ------------------------------------ AI Agent Code ------------------------------------ #

def curate_question(state: AgentSchema) -> AgentSchema:  
    return state
    user_q
  




