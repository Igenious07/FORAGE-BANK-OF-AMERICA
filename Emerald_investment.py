import requests

# GitHub Personal Access Token
token = "YOUR_GITHUB_TOKEN"
# Repository information
username = "your-username"
repository = "your-repository"
file_path = "path/to/file.txt"

# API URL
url = f"https://api.github.com/repos/{username}/{repository}/contents/{file_path}"

# Headers
headers = {
    "Authorization": f"token {token}",
    "Accept": "application/vnd.github.v3+json"
}

# First, get the file's SHA
response = requests.get(url, headers=headers)
if response.status_code == 200:
    file_sha = response.json()["sha"]
    
    # Now delete the file
    delete_data = {
        "message": "Delete file programmatically",
        "sha": file_sha,
        "branch": "main"
    }
    
    delete_response = requests.delete(url, headers=headers, json=delete_data)
    
    if delete_response.status_code == 200:
        print("File deleted successfully!")
    else:
        print(f"Error deleting file: {delete_response.status_code}")
        print(delete_response.json())
else:
    print(f"Error getting file info: {response.status_code}")
    print(response.json())
