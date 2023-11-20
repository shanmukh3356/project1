import getpass  # Import getpass for secure password 
import requests
import sys

# GitHub API URL
API_URL = "https://api.github.com"

# Prompt the user for GitHub username and personal access token
USERNAME = input("Enter your GitHub username: ")

#input getpass.getpass to input the token securely without displaying it on the screen.
TOKEN = getpass.getpass("Enter your Personal Access Token: ")

# Function to list users with read access to the repository
def list_users_with_read_access(repo_owner, repo_name):
    endpoint = f"repos/{repo_owner}/{repo_name}/collaborators"

    # Send a GET request to the GitHub API with authentication
    response = requests.get(
        f"{API_URL}/{endpoint}",
        auth=(USERNAME, TOKEN)
    )

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        collaborators = [collaborator['login'] for collaborator in response.json() if collaborator['permissions']['pull']]

        # Display the list of collaborators with read access
        if collaborators:
            print(f"Users with read access to {repo_owner}/{repo_name}:")
            print("\n".join(collaborators))
        else:
            print(f"No users with read access found for {repo_owner}/{repo_name}.")
    else:
        print(f"Failed to fetch collaborators. Status code: {response.status_code}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <repo_owner> <repo_name>")
        sys.exit(1)

    repo_owner = sys.argv[1]
    repo_name = sys.argv[2]

    print(f"Listing users with read access to {repo_owner}/{repo_name}...")
    list_users_with_read_access(repo_owner, repo_name)
