from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever

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
    question = input("Ask your question (q to quit): ")
    print("\n\n")
    if question.lower() == "q":
        break

    stats = retriever.invoke(question)
    result = chain.invoke({
        "stats": stats,
        "question": question})

    print(result)

# Response without any kind of context:
# In a high-pressure situation like that, I'd say it's all about finding the right balance between creativity and reliability.
# Considering the options, I'd choose... LeBron James!

# LeBron has consistently shown his ability to make game-winning shots, take over games, and dominate opponents with his athleticism and skillset.
# With 3 seconds on the clock, he's got the speed, agility, and court vision to create space and get an open look at the basket.

# Plus, his experience in clutch situations is unmatched. He's been in this spot many times before and has come out on top.
# I trust LeBron to make a play that will give his team a chance to win.

# Of course, other great options like Steph Curry, Kevin Durant, or James Harden could also be considered, but LeBron's well-rounded game and
# clutch gene make him my top choice in this scenario!


# Response after setup is complete:
# +-------------------------------------------------+
# Ask your question (q to quit): Who is most likely to score from 3



# Based on the provided stats, Stephen Curry appears to be the player with the highest 3-point shooting percentage (40.2%) among the listed players.
# However, we need to consider other factors such as the number of 3-point attempts.

# Let's compare the 3-point shot metrics:

# * Stephen Curry: 3P% = 40.2, 3PA = not explicitly mentioned
# * Luka Dončić: 3P% = 36.8, 3PA = not explicitly mentioned
# * Anthony Edwards: 3P% = 39.5, 3PA = not explicitly mentioned

# To make a more accurate assessment, we would need to know the number of 3-point attempts for each player.
# Without this information, it's difficult to say who is most likely to score from 3.

# However, if I had to make an educated guess based on the available data, Stephen Curry's high 3P% might suggest that he could be a good candidate
# to score from 3, but we would need more context.


# +-------------------------------------------------+
