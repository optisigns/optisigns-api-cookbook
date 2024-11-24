import requests
import json
import os

# URLs for GraphQL server and file upload API
graphql_url = "https://graphql-gateway.optisigns.com/graphql"

# Retrieve API key from the environment variable
api_key = os.getenv("OPTISIGNS_API_KEY")  # Use OPTISIGNS_API_KEY from the environment

if not api_key:
    raise ValueError("Environment variable OPTISIGNS_API_KEY is not set.")


def graphql_request(graphql_query):
    """
    Helper function to send GraphQL requests.
    :param graphql_query: The GraphQL query or mutation object
    :return: Response data or None in case of errors
    """
    headers = {
        "Authorization": f"Bearer {api_key}"  # Include API key in the request headers
    }
    try:
        print("Sending GraphQL request...")
        print("Request Headers:", headers)
        print("Request Payload:", json.dumps(graphql_query, indent=2))  # Log GraphQL query
        
        resp = requests.post(graphql_url, json=graphql_query, headers=headers)
        resp.raise_for_status()  # Raise an error for HTTP codes >= 400

        # Log the response if successful
        print("GraphQL Response:", json.dumps(resp.json(), indent=2))
        return resp.json()
    except requests.RequestException as e:
        print(f"Error sending GraphQL request: {e}")
        
        # Log response content if available
        if hasattr(e, 'response') and e.response is not None:
            print("Response Status Code:", e.response.status_code)
            print("Response Content:", e.response.text)
        
        return None

def create_website_asset(asset_name, url):
    """
    Creates a website asset in the system using the provided asset name and URL.
    :param asset_name: Name of the asset (e.g., "Website App 1")
    :param url: URL of the website (e.g., "https://www.optisigns.com/")
    :return: Created asset or None in case of errors
    """
    payload = {
        "type": "web",  # Asset type: website
        "subType": "static",
        "path": None,  # File path; None indicates Home directory
        "webLink": url,  # Website link
        "originalFileName": asset_name,  # Asset name
        "fileType": "web",  # File type
        "webType": "website"  # Web type
    }

    graphql_query = {
        "query": """
        mutation saveAsset($payload: AssetInput!, $teamId: String){
            saveAsset(payload: $payload, teamId: $teamId){
                _id,
                type,
                originalFileName,
                createdAt,
                status,
                lastUpdatedDate,
                teamId,
                path
            }
        }
        """,
        "variables": {
            "teamId": "1",  # Default team ID
            "payload": payload
        }
    }

    resp = graphql_request(graphql_query)
    if resp:
        print("GraphQL Response:", json.dumps(resp, indent=2))
    return resp.get('data', {}).get('saveAsset') if resp else None

# Main execution flow
if __name__ == "__main__":
    print("started....")
    asset_name = "Website App 1"
    url = "https://www.optisigns.com/product/engage"
    
    print("Creating website asset...")
    website_asset = create_website_asset(asset_name, url)
    if website_asset:
        print("Created Website Asset:", website_asset)
    else:
        print("Failed to create website asset. Check logs for details.")
