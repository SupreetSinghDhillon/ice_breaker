import os
import requests
from dotenv import load_dotenv

load_dotenv


def scrape_linkedin_profile(linkedin_profile_url: str, mock: bool = False):
    """scrape information from LinkedIn profiles,
    Manually scrape the information from the LinkedIn profile"""

    if mock:
        linkedin_profile_url = "https://gist.githubusercontent.com/emarco177/859ec7d786b45d8e3e3f688c6c9139d8/raw/5eaf8e46dc29a98612c8fe0c774123a7a2ac4575/eden-marco-scrapin.json"
        response = requests.get(
            linkedin_profile_url,
            timeout=10,
        )

    else:
        api_endpoint = "http://nubela.co/proxycurl/api/v2/linkedin"
        header_dic = { "Authorization" : f'Bearer {os.getenv("PROXYCURL_API_KEY")}' }
        response = requests.get(
            api_endpoint,
            headers=header_dic,
            params={"url": linkedin_profile_url},
            timeout=10,
        )

    data = response.json()
    # data = {
    #     k: v
    #     for k, v in data.items()
    #     if v not in ([], "", "", None) and k not in ["certifications"]
    # }

    return data


if __name__ == "__main__":
    print(
        scrape_linkedin_profile(
            linkedin_profile_url="https://www.linkedin.com/in/kellyboyi/", mock=True
        )
    )
