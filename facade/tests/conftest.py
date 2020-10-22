from ..classes import OrganizationClient, RepositoryClient, GithubClient

import pytest


@pytest.fixture
def api_token():
    return "23cf84f4abcd4ad9fad6d5b0294c66b4"


@pytest.fixture
def organization_id():
    return 8_923_019


@pytest.fixture
def organization_client(api_token):
    return OrganizationClient(api_token)


@pytest.fixture
def repository_client(api_token):
    return RepositoryClient(api_token)


@pytest.fixture
def github_client(api_token):
    return GithubClient(api_token)
