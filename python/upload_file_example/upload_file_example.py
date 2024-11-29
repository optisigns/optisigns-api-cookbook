import requests
import json
import os

# URLs for GraphQL server and file upload API
graphql_url = "https://graphql-gateway.optisigns.com/graphql"
upload_url = "https://api2.transloadit.com/assemblies"  # File upload endpoint

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
        resp = requests.post(graphql_url, json=graphql_query, headers=headers)
        resp.raise_for_status()  # Raise an error for HTTP codes >= 400

        return resp.json()
    except requests.RequestException as e:
        print(f"Error sending GraphQL request: {e}")
        
        # Log response content if available
        if hasattr(e, 'response') and e.response is not None:
            print("Response Status Code:", e.response.status_code)
            print("Response Content:", e.response.text)
        
        return None

def get_upload_options():
    """
    Fetches upload options from the GraphQL server.
    :return: Upload options or None in case of errors
    """
    graphql_query = {
        "query": """
        query {
            getFileUploadOptions
        }
        """
    }
    resp = graphql_request(graphql_query)
    return resp.get('data', {}).get('getFileUploadOptions') if resp else None



def upload_file(upload_opts, file_path):
    """
    Uploads a file to the specified upload URL.
    :param upload_opts: Upload options containing params and signature
    :param file_path: Path to the file to be uploaded
    :return: Response data or None in case of errors
    """
    print("uploadFile started...")
    try:
        # Serialize params with consistent formatting
        serialized_params = json.dumps(upload_opts['params'], separators=(',', ':'))

        # Ensure file exists
        if not os.path.exists(file_path):
            print("Error: File not found.")
            return None

        # Prepare multipart form data
        with open(file_path, 'rb') as file:
            form_data = {
                'params': (None, serialized_params),
                'signature': (None, upload_opts.get('signature')),
                'file': (os.path.basename(file_path), file, 'application/octet-stream')
            }

            # Perform the POST request
            resp = requests.post(
                upload_url,
                files=form_data,  # Correctly structured multipart data
                headers={}  # Let requests handle the headers
            )
            resp.raise_for_status()  # Raise an error for HTTP codes >= 400

            print("Upload successful")
            return resp.json()
    except requests.RequestException as e:
        print(f"Error uploading file: {e}")
        if hasattr(e, 'response') and e.response is not None:
            print("Response content:", e.response.text)
        return None

def add_file_asset(assembly):
    """
    Creates a file asset in the system using the uploaded file's metadata.
    :param assembly: Assembly object returned from the upload API
    :return: Created asset or None in case of errors
    """
    if not assembly:
        return None

    assembly_id = assembly.get('assembly_id')
    upload_item = assembly.get('uploads', [{}])[0]

    payload = {
        "type": "file",
        "originalFileName": upload_item.get('name'),
        "processId": assembly_id,
        "status": "converting",
        "path": None  # File path; None indicates Home directory, e.g., '/Demo'
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
    return resp.get('data', {}).get('saveAsset') if resp else None

# Main execution flow
if __name__ == "__main__":
    print("started....")
    upload_options = get_upload_options()  # Fetch upload options

    file_path = "os-logo.png"  # e.g., /Users/files/this-week-promo.png

    if upload_options:
        assembly = upload_file(upload_options, file_path)  # Upload the file
        if assembly:
            asset = add_file_asset(assembly)  # Save the uploaded file as an asset
            print("created asset: ", asset)