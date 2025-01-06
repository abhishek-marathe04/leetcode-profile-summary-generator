import requests
import json

def create_payload_for_profile_details(username):
    query = """
    query userProblemsSolved($username: String!) {
      allQuestionsCount {
        difficulty
        count
      }
      matchedUser(username: $username) {
        problemsSolvedBeatsStats {
          difficulty
          percentage
        }
        submitStatsGlobal {
          acSubmissionNum {
            difficulty
            count
          }
        }
      }
    }
    """
    variables = {"username": username}
    payload = {
        "query": query,
        "variables": variables
    }
    return json.dumps(payload)

def fetch_leetcode_profile_details(username: str):

    url = "https://leetcode.com/graphql/"

    payload=create_payload_for_profile_details(username)
    headers = {
        'Content-Type': 'application/json',
        'Cookie': 'csrftoken=5Gu3YF4TquK8xs192vLBajbzFKyxktvwAZkOeBf1VQmI4NLuVLoo6hEdK8CLMbup'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return response.json()

def create_payload_for_langauge_stats(username):
    query = """
    query languageStats($username: String!) {
        matchedUser(username: $username) {
            languageProblemCount {
            languageName
            problemsSolved
            }
        }
    }
    """
    variables = {"username": username}
    payload = {
        "query": query,
        "variables": variables
    }
    return json.dumps(payload)

def fetch_leetcode_language_stats(username: str):

    url = "https://leetcode.com/graphql/"

    payload=create_payload_for_langauge_stats(username)
    headers = {
        'Content-Type': 'application/json',
        'Cookie': 'csrftoken=5Gu3YF4TquK8xs192vLBajbzFKyxktvwAZkOeBf1VQmI4NLuVLoo6hEdK8CLMbup'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return response.json()