import requests
import json


# curl -X 'POST' \
#   'https://api.getodin.ai/project/search' \
#   -H 'accept: application/json' \
#   -H 'X-API-KEY: 45d56382-9229-4fbd-a9af-931498e1f416' \
#   -H 'X-API-SECRET: JBA2gA+d3+sC93wNJ4oChVomefLeVgQpm9sBUx4B3e8=' \
#   -H 'Content-Type: application/json' \
#   -d '{
#   "project_id": "040ece4f7b184cf4a7c512",
#   "query": "I get 1003 web socket error",
#   "document_keys": [],
#   "hybrid_search_lambda": 0.1,
#   "score_threshold": 0.1,
#   "kw_fuzzy_threshold": 80,
#   "kw_curve_multihit": false,
#   "metadata_filters": {},
#   "max_results": 20,
#   "full_content_words_limit": 200,
#   "metadata_weighting": 0.2,
#   "remove_duplicates": false,
#   "page": 1,
#   "debug": false,
#   "generate_ai_summary": false,
#   "search_by_titles": false,
#   "group_on_backend": false,
#   "multihit_weighting": 0.2,
#   "add_bonus_from_full_content": false,
#   "bonus_from_full_content_threshold": 0.5,
#   "bonus_from_full_content_size": 0.2
# }'

# Load secrets from JSON file
with open('secrets.json') as f:
    secrets = json.load(f)

api_key = secrets['api_key']
api_secret = secrets['api_secret']

# Headers with secret/key
headers = {
    "Content-Type": "application/json",
    #"Content-Type": "multipart/form-data",
    "accept": "application/json",
    "X-API-KEY": api_key,
    "X-API-SECRET": api_secret
    }

def getApiResponse(api_url, payload, method):

    # Send the POST request
    if method == "POST":
        response = requests.post(api_url, headers=headers, json=payload)
        #response = requests.post(api_url, headers=headers, files=payload)
    elif method == "GET":
        response = requests.get(api_url, headers=headers, json=payload)
    return response
# Optional: Query parameters
# params = {
#     "param1": "value1",
#     "param2": "value2"
# }

# Send the request
#response = requests.get(api_url, headers=headers, params=params)
def searchKB():
    api_url = "https://api.getodin.ai/project/search"
    payload = {
      "project_id": "040ece4f7b184cf4a7c512",
      "query": "I get 1003 web socket error",
      "document_keys": [],
      "hybrid_search_lambda": 0.1,
      "score_threshold": 0.1,
      "kw_fuzzy_threshold": 80,
      "kw_curve_multihit": False,
      "metadata_filters": {},
      "max_results": 20,
      "full_content_words_limit": 200,
      "metadata_weighting": 0.2,
      "remove_duplicates": False,
      "page": 1,
      "debug": False,
      "generate_ai_summary": False,
      "search_by_titles": False,
      "group_on_backend": False,
      "multihit_weighting": 0.2,
      "add_bonus_from_full_content": False,
      "bonus_from_full_content_threshold": 0.5,
      "bonus_from_full_content_size": 0.2
    }
    response = getApiResponse(api_url, payload, "POST")
    # Check for success
    if response.status_code == 200:
        data = response.json()

        # Querying specific keys from JSON
        # Example: extract nested values
        try:
            result_1 = data.get("matches")
            print(data['results']['matches'][0]['similarity_score'])
            matches=data['results']['matches']
            for match in matches:
                print(match['similarity_score'], match['search_score'], match['metadata']['key'], match['metadata']['url'])
            #print(result_1[0]["similarity_score"])
            result_2 = data["nestedKey"]["subKey"]
            print("Key1:", result_1)
            print("Nested -> subKey:", result_2)
        except KeyError as e:
            print("Key not found:", e)
    else:
        print(f"Request failed with status code {response.status_code}: {response.text}")


def Chat_1():
    api_url = "https://api.getodin.ai/chat/message"
    payload =  {
    "project_id" : (None , "040ece4f7b184cf4a7c512"),
    "message" : (None, "I get 1003 web socket error")
    }

    response = getApiResponse(api_url, payload, "POST")
    # Check for success
    if response.status_code == 200:
        data = response.json()
        print(data)
        # Querying specific keys from JSON
        # Example: extract nested values
        try:
            result_1 = data.get("matches")
            print(data['results']['matches'][0]['similarity_score'])
            matches=data['results']['matches']
            for match in matches:
                print(match['similarity_score'], match['search_score'], match['metadata']['key'], match['metadata']['url'])
            print(result_1[0]["similarity_score"])
            result_2 = data["nestedKey"]["subKey"]
            print("Key1:", result_1)
            print("Nested -> subKey:", result_2)
        except KeyError as e:
            print("Key not found:", e)
    else:
        print(f"Request failed with status code {response.status_code}: {response.text}")

def Chat():
    api_url = "https://api.getodin.ai/chat/message"
    # payload = {
    #   "message": "I get 1003 web socket error",
    #   "project_id": "040ece4f7b184cf4a7c512",
    #   "chat_id": "6eb26df252204f35acef17",
    #   "is_test": False,
    #   "ai_response":True,
    #   "agent_type": "chat_agent",
    #   "agent_id": "default_kb_agent",
    #   "is_regenerating":False}
    payload =  {
        "message": "I get 1003 web socket error",
        "project_id": "040ece4f7b184cf4a7c512",
        "chat_id": "6eb26df252204f35acef17",
        "document_keys": [
            "string"
        ],
        "google_search": False,
        "is_test": False,
        "personality_name": "string",
        "return_message": False,
        "ai_response": True,
        "model_name": "gpt-4o-mini",
        "agent_type": "chat_agent",
        "chat_name": "string",
        "agent_id": "string",
        "personality_id": "string",
        "use_knowledgebase": True,
        "is_regenerating": False,
        "message_id": "string",
        "ui_form": {},
        "format_instructions": "normal",
        "ignore_chat_history": False,
        "example_json": "string",
        "is_teams_bot": False,
        "sent_from_automator": False,
        "skip_stream": False,
        "request_metadata": {},
        "artifact": {
            "highlighted_code": {
                "start": 0,
                "end": 0,
                "language": "Python"
            },
            "highlighted_text": {
                "content": "string",
                "markdown_blocks": [
                    "string"
                ]
            },
            "artifact": {
                "current_index": 0,
                "contents": [
                    {
                        "index": 0,
                        "type": "text",
                        "title": "string",
                        "full_markdown": "string"
                    },
                    {
                        "index": 0,
                        "type": "code",
                        "title": "string",
                        "language": "string",
                        "code": "string"
                    }
                ]
            },
            "next": "string",
            "language": "English",
            "artifact_length": "short",
            "regenerate_with_emojis": True,
            "reading_level": "Beginner",
            "add_comments": True,
            "add_logs": True,
            "port_language": "Python",
            "fix_bugs": True,
            "custom_quick_action_id": "string"
        }
    }

    response = getApiResponse(api_url, payload, "POST")
    # Check for success
    if response.status_code == 200:
        data = response.json()
        print(data)
        # Querying specific keys from JSON
        # Example: extract nested values
        try:
            result_1 = data.get("matches")
            print(data['results']['matches'][0]['similarity_score'])
            matches=data['results']['matches']
            for match in matches:
                print(match['similarity_score'], match['search_score'], match['metadata']['key'], match['metadata']['url'])
            print(result_1[0]["similarity_score"])
            result_2 = data["nestedKey"]["subKey"]
            print("Key1:", result_1)
            print("Nested -> subKey:", result_2)
        except KeyError as e:
            print("Key not found:", e)
    else:
        print(f"Request failed with status code {response.status_code}: {response.text}")
#Chat_1()
searchKB()