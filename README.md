# Python project1

This Python script utilizes the GitHub API to list users with read access to a specified GitHub repository. It prompts the user for their GitHub username and Personal Access Token, ensuring secure authentication.

If you have created your own organization on GitHub and own repositories within that organization, you can control access to those repositories by managing collaborators and their permissions. In your case, if you are the only owner, you have full administrative access to the repositories.

## Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/your-repo.git
    cd your-repo
    ```

2. Run the script with the following command:

    ```bash
    python script.py <repo_owner> <repo_name>
    ```

    Replace `<repo_owner>` with the owner of the repository and `<repo_name>` with the name of the repository.

3. Enter your GitHub username when prompted.

4. Use `getpass.getpass` to securely input your Personal Access Token when prompted.
      ```To get Access Token go to GitHub account settings```

     1. Navigate to "Developer settings in git" and then "Personal access tokens."
   
     2. Click on "Generate token."

     3. Fill in the required information and select the scopes (permissions) for your token.

     4.  Click "Generate token."

     Once you've generated the token, copy it immediately. GitHub will not display it again.

5. The script will then list users with read access to the specified repository.

# Explanation Of Code

# Import Libraries

```python
import getpass 
import requests
import sys
```

1.The getpass module is imported to securely input the Personal Access Token without displaying it on the screen.

2.The requests library is imported to make HTTP requests to the GitHub API.

3.The sys module is imported for handling command-line arguments.

# Setting GitHub API URL:

```python
API_URL = "https://api.github.com"
```
This variable holds the base URL for the GitHub API.

# Prompting for User Input:

```python
USERNAME = input("Enter your GitHub username: ")
TOKEN = getpass.getpass("Enter your Personal Access Token: ")
```

The script prompts the user to input their GitHub username and securely input their Personal Access Token using getpass.getpass.

# Defining the Function:

```python
def list_users_with_read_access(repo_owner, repo_name):
```
This function takes two parameters, repo_owner and repo_name, representing the owner and name of the GitHub repository, and lists users with read access to that repository.

# Building the API Endpoint:

```python
endpoint = f"repos/{repo_owner}/{repo_name}/collaborators"
```
The API endpoint is constructed using the provided repository owner and name.

# Sending a GET Request to GitHub API:

```python
response = requests.get(
    f"{API_URL}/{endpoint}",
    auth=(USERNAME, TOKEN)
)
```
The script sends a GET request to the GitHub API using the constructed endpoint and provides authentication using the GitHub username and Personal Access Token.

# Handling the Response:

```python
if response.status_code == 200:
```
Checks if the GET request was successful (status code 200).

# Processing Collaborators:

```python
collaborators = [collaborator['login'] for collaborator in response.json() if collaborator['permissions']['pull']]
```
Extracts the login usernames of collaborators with read access (pull permission) from the API response.

# Displaying the Results:

```python
if collaborators:
    print(f"Users with read access to {repo_owner}/{repo_name}:")
    print("\n".join(collaborators))
else:
    print(f"No users with read access found for {repo_owner}/{repo_name}.")
```
If there are collaborators, it prints their usernames. Otherwise, it notifies that no users with read access were found.

# Handling Errors:

``` python
else:
    print(f"Failed to fetch collaborators. Status code: {response.status_code}")
```
If the GET request was not successful, it prints an error message along with the HTTP status code.

# Main Script Execution:
``` python
if __name__ == "__main__":
```
Checks if the script is being run as the main program.

# Command-Line Argument Validation:
```python
if len(sys.argv) != 3:
    print("Usage: python script.py <repo_owner> <repo_name>")
    sys.exit(1)
```
Ensures that the script is provided with the correct number of command-line arguments (repository owner and name). Prints usage instructions and exits if incorrect.

# Getting Repository Owner and Name from Command-Line Arguments:
```python
Copy code
repo_owner = sys.argv[1]
repo_name = sys.argv[2]
```
Retrieves the repository owner and name from the command-line arguments.

# Calling the Function with Provided Repository Information:
```python

print(f"Listing users with read access to {repo_owner}/{repo_name}...")
list_users_with_read_access(repo_owner, repo_name)
```
Calls the list_users_with_read_access function with the specified repository owner and name, initiating the script's main functionality.


