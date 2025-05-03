# from dotenv import load_dotenv
# from langchain.prompts.prompt import PromptTemplate
# from langchain_openai import ChatOpenAI
# from langchain_ollama import ChatOllama
# from langchain_core.output_parsers import StrOutputParser
# from third_parties.linkedin import scrape_linkedin_profile
# from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent
# from output_parsers import summary_parser

# def ice_break_with(name: str) -> str:
#     linkedin_username = linkedin_lookup_agent(name=name)
#     linkedin_data = scrape_linkedin_profile(linkedin_profile_url=linkedin_username, mock=True)

#     summary_template = """
#     given the information {information} about a person I want you to create:
#     1. A short summary
#     2. two interesting facts about them

#     \n{format_instructions}
#     """

#     summary_prompt_template = PromptTemplate(
#         input_variables=["information"], template=summary_template,
#         partial_variables={"format_instructions": summary_parser.get_format_instructions()}
#     )

#     # llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
#     llm = ChatOllama(model="llama3.2")
#     # llm = ChatOllama(model="gpt-3.5-turbo")

#     chain = summary_prompt_template | llm | summary_parser
#     linkedin_data =  scrape_linkedin_profile(
#             linkedin_profile_url="https://www.linkedin.com/in/kellyboyi/",
#             mock=True
#         )
#     res = chain.invoke(input={"information": linkedin_data})

#     print(res)



# if __name__ == "__main__":
#     load_dotenv()

#     print("IceBreaker Enter")

#     ice_break_with("Supreet Dhillon LoadMinds")


from langchain_core.prompts import PromptTemplate 
from langchain_openai import ChatOpenAI   

if __name__ == "__main__":
    print("Hello Langchain")

    summary_template = """
    given the information {information} about a person I want you to create:
    1. A short summary
    2. two interesting facts about them
    """

    information = """
    Bhupinder "Bindy" Singh Johal (14 January 1971 – 20 December 1998) was an Indo-Canadian gangster from Vancouver, British Columbia, Canada. 
    A self-confessed drug trafficker,[3] he was known for his outspoken nature, blatant disregard for authority and his longtime rivalry with former mentors Ranjit Cheema and rival Punjabi Mafia faction led by the Dosanjh brothers and Robbie Kandola.
    [4] On 20 December 1998, Johal was fatally shot in the back of the head at a crowded nightclub in Vancouver.[5]"""

    summary_prompt_template = PromptTemplate(input_variables=["information"], template=summary_template)
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

    chain = summary_prompt_template | llm

    res = chain.invoke(input={"information": information})

    print(res)




