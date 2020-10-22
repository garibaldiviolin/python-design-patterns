from .classes import GithubClient


github_client = GithubClient("0df15beb54bcd215fbe20323246a9ebb")
user_repositories = github_client.list_user_repositories()
print(f"User repositories: {user_repositories}")
