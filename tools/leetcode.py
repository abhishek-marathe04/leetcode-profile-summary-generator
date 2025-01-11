from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

from common.llm import get_llm
from third_parties.leetcode import fetch_leetcode_profile_details, fetch_leetcode_language_stats



def fetch_leetcode_profile_info_tool(username: str):

    summary_template = """
        You will be give leetcode profile information in json format about a person
        Remember, in json summary given to you, allQuestionsCount key contains all questions available on leetcode, it doesn't represent user's attempted questions, 
        matchedUser has all the information that is particular to use
        matchedUser.problemsSolvedBeatsStats contains percentages of solved problems by that user difficuly wise and 
        matchedUser.submitStatsGlobal conatins number of questions user attempted across difficulties

        considering all this information here is json summary of leetcode profile {information} about a person, now create :
        1. a short summary
        2. what is their skill in solving easy, medium and hard problems and what is their success rate
        3. rate their programming level from 1 to 10 and describe what they should do to improve


    """
    
    llm = get_llm()
    leetcode_profile_api_response = fetch_leetcode_profile_details(username=username)
    summary_prompt_template = PromptTemplate(template=summary_template, input_variables=['information'])

    chain = summary_prompt_template | llm | StrOutputParser()
    
    # information = scrape_linkedin_profile(linkedin_url="https://gist.githubusercontent.com/emarco177/0d6a3f93dd06634d95e46a2782ed7490/raw/78233eb934aa9850b689471a604465b188e761a0/eden-marco.json")
    res = chain.invoke(input={'information': leetcode_profile_api_response})

    return res


def fetch_leetcode_language_info_tool(username: str):

    langauge_stats_template = """
        You will be give leetcode language statistics information in json format about a person
        Remember, in json summary given to you, there will be programming langague name along with problem solved in that programming language

        considering all this information here is json summary of leetcode profile {information} about a person, now create :
        1. a short summary
        2. which all langauges they have solved leetcode problems in
        3. which is their favourite langague


    """
    
    llm = get_llm()
    leetcode_langauge_api_response = fetch_leetcode_language_stats(username=username)
    summary_prompt_template = PromptTemplate(template=langauge_stats_template, input_variables=['information'])

    chain = summary_prompt_template | llm | StrOutputParser()
    
    # information = scrape_linkedin_profile(linkedin_url="https://gist.githubusercontent.com/emarco177/0d6a3f93dd06634d95e46a2782ed7490/raw/78233eb934aa9850b689471a604465b188e761a0/eden-marco.json")
    res = chain.invoke(input={'information': leetcode_langauge_api_response})

    return res