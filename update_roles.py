import os
import requests

# Get environment variables
SECRET_TOKEN = os.getenv('SECRET_TOKEN')
ORG_NAME = 'Test_poc_env'
REPO_NAME = 'teams_and_role'
TEAM_NAME = 'admin'
ROLE = 'Read'

# Set up request headers
headers = {
    'Authorization': f'token {SECRET_TOKEN}',
    'Accept': 'application/vnd.github.v3+json'
}

# Get the team ID
team_url = f'https://api.github.com/orgs/{ORG_NAME}/teams/{TEAM_NAME}'
response = requests.get(team_url, headers=headers)
team_id = response.json().get('id')

if team_id:
    # Update the team's role
    update_url = f'https://api.github.com/teams/{team_id}/repos/{ORG_NAME}/{REPO_NAME}'
    data = {
        'permission': ROLE
    }
    response = requests.put(update_url, headers=headers, json=data)

    if response.status_code == 204:
        print(f'Successfully updated the role to {ROLE} for the team {TEAM_NAME} in the repo {REPO_NAME}')
    else:
        print(f'Failed to update role: {response.json()}')
else:
    print(f'Team {TEAM_NAME} not found')
