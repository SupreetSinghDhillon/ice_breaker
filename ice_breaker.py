from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import JsonOutputParser
from langchain_ollama import ChatOllama
from linkedin import scrape_linkedin_profile

if __name__ == "__main__":
    summary_template = """
    Given the following information about a person:

    {information}

    Respond with a JSON object with the following keys:
    - "summary": a short summary of the person
    - "facts": a list of two interesting facts about the person
    """

    information = """
    Bhupinder "Bindy" Singh Johal (14 January 1971 – 20 December 1998) was an Indo-Canadian gangster from Vancouver, British Columbia, Canada. 
    A self-confessed drug trafficker, he was known for his outspoken nature, blatant disregard for authority and his longtime rivalry with former mentors Ranjit Cheema and rival Punjabi Mafia faction led by the Dosanjh brothers and Robbie Kandola.
    On 20 December 1998, Johal was fatally shot in the back of the head at a crowded nightclub in Vancouver.
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    # llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    # llm = ChatOpenAI(temperature=0, model_name="gpt-4")
    llm = ChatOllama(model="llama2", temperature=0)
    parser = JsonOutputParser()

    chain = summary_prompt_template | llm | parser

    result = chain.invoke({"information": information})

    # print(result)

    print("Summary:", result["summary"])
    print("Facts:", result["facts"])
