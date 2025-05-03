from langchain_community.tools.tavily_search import TavilySearchResults

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.tools import Tool
from langchain.agents import ( AgentExecutor, create_react_agent )
from langchain import hub
# from tools.tools import get_profile_url_tavily


def get_profile_url_tavily(name: str):
    """Search for LinkedIn or Twitter Profile page"""

    search = TavilySearchResults()
    res = search.run(f"{name}")
    return res


def lookup(name:str) -> str:
    llm = ChatOpenAI(temperature=0, model_name="gpt-4o-mini")
    template = """given the full name {name} I want you to return the LinkedIn profile URL of the person, your answer should contain only the URL."""

    prompt = PromptTemplate(
        input_variables=["name"], template=template
    )

    tools_for_agent = [
        Tool(
            name="Crawl Google 4 linkedin profile page",
            func=get_profile_url_tavily,
            description="Search for LinkedIn profile page",
        )
    ]

    react_prompt = hub.pull("hwchase17/react")

    agent = create_react_agent(llm=llm, tools=tools_for_agent, prompt=react_prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools_for_agent, verbose=True)

    result = agent_executor.invoke(input = {"input": prompt.format(name=name)})

    linkedin_profile_url = result["output"]
    return linkedin_profile_url



if __name__ == "__main__":
    name = "Supreet DHillon SFU"
    linkedin_profile_url = lookup(name)
    print(linkedin_profile_url)





