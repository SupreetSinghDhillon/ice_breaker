from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import JsonOutputParser
from langchain_ollama import ChatOllama
from third_parties.linkedin import scrape_linkedin_profile
from tools.tools import get_profile_url_tavily
from agents.linkedin_lookup_agent import lookup
from output_parsers import summary_parser

def ice_break_with(name: str) -> str:
    linkedin_url = lookup(name = name)
   
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url=linkedin_url, mock=True)

    summary_template = """
    Given the following information about a person:

    {information}

    Respond with a JSON object with the following keys:
    - "summary": a short summary of the person
    - "facts": a list of two interesting facts about the person
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], 
        template=summary_template,
        partial_variables={"format_instructions": summary_parser.get_format_instructions()}
    )

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    parser = JsonOutputParser()

    chain = summary_prompt_template | llm | summary_parser
    result = chain.invoke({"information": linkedin_data})

    return result
    

if __name__ == "__main__":

    name = "Eden Marco"
    result = ice_break_with(name)
    print(result)
    print (result.summary)
    print (result.facts)
