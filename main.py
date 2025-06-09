from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

model = OllamaLLM(model="llama3.2")

template = """
You are an expert in answering questions about NBA player stats

Here are some relevant stats: {stats}

Here is the question to answer: {question}
"""
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

while True:
    print("\n\n+-------------------------------------------------+")
    question = input("Ask your question (q to quit)")
    print("\n\n")
    if question.lower() == "q":
        break


result = chain.invoke({
    "stats": [],
    "question": "Which player would you give the ball to with 3 seconds on the clock?"})

print(result)

# Response:
# In a high-pressure situation like that, I'd say it's all about finding the right balance between creativity and reliability.
# Considering the options, I'd choose... LeBron James!

# LeBron has consistently shown his ability to make game-winning shots, take over games, and dominate opponents with his athleticism and skillset.
# With 3 seconds on the clock, he's got the speed, agility, and court vision to create space and get an open look at the basket.

# Plus, his experience in clutch situations is unmatched. He's been in this spot many times before and has come out on top.
# I trust LeBron to make a play that will give his team a chance to win.

# Of course, other great options like Steph Curry, Kevin Durant, or James Harden could also be considered, but LeBron's well-rounded game and
# clutch gene make him my top choice in this scenario!
