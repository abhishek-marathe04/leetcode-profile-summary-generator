from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

from langchain_core.tools import Tool
from langchain.agents import (
    initialize_agent,
)

from common.llm import get_llm
from tools.leetcode import fetch_leetcode_language_info_tool, fetch_leetcode_profile_info_tool

def fetch_leetcode_username(prompt: str):
    print(f'Inside Fetch Leetcode Username  : {prompt}')
    fetch_leetcode_username_prompt = """
        You are a leetcode username extractor. You will receive Query which will have leetcode username mentioned, You need to return only leetcode username. The username is usually a single word or alphanumeric string.

        If no username is present, return "None" otherwise return single text which contains username, Do not return your thought process.

        Query: {query}
        Username:
    """

    llm = get_llm()
    fetch_leetcode_username_prompt_template = PromptTemplate(input_variables=['query'], template=fetch_leetcode_username_prompt)

    chain = fetch_leetcode_username_prompt_template | llm | StrOutputParser()
    
    # information = scrape_linkedin_profile(linkedin_url="https://gist.githubusercontent.com/emarco177/0d6a3f93dd06634d95e46a2782ed7490/raw/78233eb934aa9850b689471a604465b188e761a0/eden-marco.json")
    res = chain.invoke(input={'query': prompt})

    return res


def leetcode_agent_using_zero_shot_react(query: str):
    load_dotenv()
    print(f'Request Received  : {query}')
    leetcode_username = fetch_leetcode_username(prompt=query)

    print(f'leetcode_username for query : {leetcode_username}')

    llm = get_llm()
    
    tools_for_agent = [
        Tool(
            name="GetLeetcodeProfileDetails",
            func=lambda leetcode_username: fetch_leetcode_profile_info_tool(leetcode_username.strip()),
            description="Use this to fetch leetcode profile details of a user. Input should be the username.",
            return_direct=True
        ),
        Tool(
            name="GetProgramingLangaugeStats",
            func=lambda leetcode_username: fetch_leetcode_language_info_tool(leetcode_username.strip()),
            description="Use this to fetch Programing language stats of a user. Input should be the username.",
            return_direct=True
        )
    ]

    # Initialize the agent
    agent = initialize_agent(
        tools=tools_for_agent,
        llm=llm,
        agent="zero-shot-react-description",
        verbose=True
    )

    res = agent.run(query)

    return res

if __name__ == '__main__':
    load_dotenv()

    profile_prompt = '"Get Profile Details": "Get the profile details of username user8162l"'
    langague_prompt = '"Get Profile Details": "Get the profile details of username user8162l"'
    res = leetcode_agent_using_zero_shot_react(query=profile_prompt)

    print(res)
