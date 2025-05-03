from langchain_community.tools.tavily_search import TavilySearchResults


def get_profile_url_tavily(name: str):
    """Search for LinkedIn or Twitter Profile page"""

    search = TavilySearchResults()
    res = search.run(f"{name}")
    return res

if __name__ == "__main__":
    name = "What is the weather at SFU Burnaby right now in degree celsius ?"
    linkedin_profile_url = get_profile_url_tavily(name)
    print(linkedin_profile_url)
