from pydantic import BaseModel, Field
from typing import Annotated

class AgentSchema(BaseModel):
    message : Annotated[list,add] = Field(..., description="List of messages to be processed by the agent.")
