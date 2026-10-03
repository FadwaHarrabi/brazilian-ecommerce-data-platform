from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from Vector import retriever
from data_profiling import all_profiles,candidates



# turn what you already computed into plain text
profiles_combined = "\n\n".join(f"Table: {name}\n{text}" for name, text in all_profiles.items())

relationship_text = "\n".join(
    f"{table_a}.{col_a} <-> {table_b}.{col_b} (overlap: {ratio})"
    for table_a, col_a, table_b, col_b, ratio in candidates
)

llm=OllamaLLM(model="llama3.2")
template = """
You are a data engineer analyzing a relational dataset.

Here are the column profiles for each table:
{profiles}

Here are candidate relationships found by comparing overlapping values between columns:
{relationships}

Based on this evidence, explain:
1. What each table most likely represents in the business
2. Which of the candidate relationships are real foreign key relationships, and which look like coincidental overlaps
3. The overall entity structure of this dataset, in plain language
"""
prompt=ChatPromptTemplate.from_template(template)
chain=prompt | llm
while True:
    question=input("Ask your question (q to quit): ")
    if question == "q":
        break
    output=retriever.invoke(question)
    result = chain.invoke({
        "profiles": profiles_combined,
        "relationships": relationship_text
    })
    print(result)
