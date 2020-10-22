from random import randint


class OrganizationClient:
    def __init__(self, api_token):
        self.api_token = api_token

    def request_organization_id(self):
        print("Requesting organization_id...")
        return randint(8_000_000, 9_000_000)


class RepositoryClient:
    def __init__(self, api_token):
        self.api_token = api_token

    def request_repositories_list(self, organization_id):
        print(
            f"Requesting the list of the repositories names "
            f"[organization_id={organization_id}]..."
        )
        return ["django", "nodejs", "flask"]


class GithubClient:
    """This class acts as the Facade, and the others above are
    subsystems.
    """

    def __init__(self, api_token):
        self.organization_client = OrganizationClient(api_token)
        self.repository_client = RepositoryClient(api_token)

    def list_user_repositories(self):
        organization_id = self.organization_client.request_organization_id()
        return self.repository_client.request_repositories_list(
            organization_id
        )
