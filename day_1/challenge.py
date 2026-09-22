"""A question none of the three systems was designed for."""
from day_1.workflow import workflow
from day_1.agent import agent
 
QUESTION = "I can pay Rs. 30,000. Which two courses can I take together within this budget?"
 
print("Q:", QUESTION)
print("\nWorkflow :", workflow(QUESTION))
print("\nAgent    :", agent(QUESTION))
