from pydantic import BaseModel, Field
from typing import Annotated, Literal
from langgraph.graph.message import add_messages

class AgentSchema(BaseModel):
    message : Annotated[list, add_messages] = Field(..., description="List of messages to be processed by the agent.")
    user_ques : str = Field(..., description="List of curated user questions.")
    prompt_query_context : str = Field(..., description="A detailed prompt with SQL DB context that will help agent to generate SQL query.")
    is_safe : Literal["Yes", "No"] = Field(..., description="Whether the query is safe or not.")
    generated_sql_query : str = Field(..., description="Generated SQL query.")
    sql_query_execution_result : str = Field(..., description="SQL query execution result.")
    final_answer : str = Field(..., description="Final answer.")