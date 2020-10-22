from unittest.mock import Mock, MagicMock, patch

import pytest

from ..classes import OrganizationClient, RepositoryClient, GithubClient


def test_organization_client(organization_client, api_token):
    assert organization_client.api_token == api_token


@patch("facade.classes.randint")
@patch("builtins.print")
def test_request_organization_id(print_mock, random_mock, organization_client,
                                 organization_id):
    random_mock.return_value = organization_id

    organization_id_returned = organization_client.request_organization_id()

    assert organization_id_returned == organization_id
    print_mock.assert_called_once_with("Requesting organization_id...")


def test_repository_client(repository_client, api_token):
    assert repository_client.api_token == api_token


@patch("builtins.print")
def test_request_repositories_list(print_mock, repository_client, api_token,
                                   organization_id):
    repositories_list = repository_client.request_repositories_list(
        organization_id
    )

    assert repositories_list == ["django", "nodejs", "flask"]
    print_mock.assert_called_once_with(
        "Requesting the list of the repositories names "
        "[organization_id=8923019]..."
    )


@patch("facade.classes.RepositoryClient")
@patch("facade.classes.OrganizationClient")
def test_github_client(organization_constructor_mock,
                       repository_constructor_mock, api_token):
    organization_client_mock = MagicMock()
    repository_client_mock = MagicMock()

    organization_constructor_mock.return_value = organization_client_mock
    repository_constructor_mock.return_value = repository_client_mock

    github_client = GithubClient(api_token)

    assert github_client.organization_client == organization_client_mock
    assert github_client.repository_client == repository_client_mock
    organization_constructor_mock.assert_called_once_with(api_token)
    repository_constructor_mock.assert_called_once_with(api_token)


def test_list_user_repositories(github_client, organization_id):
    organization_client_mock = Mock()
    organization_client_mock.request_organization_id = Mock(
        return_value=organization_id
    )

    repositories = ["rails", "spring", "jboss"]

    repository_client_mock = Mock()
    repository_client_mock.request_repositories_list = Mock(
        return_value=repositories
    )

    github_client.organization_client = organization_client_mock
    github_client.repository_client = repository_client_mock

    repositories_returned = github_client.list_user_repositories()

    assert repositories_returned == repositories
    organization_client_mock.request_organization_id.assert_called_once_with()
    repository_client_mock.request_repositories_list.assert_called_once_with(
        organization_id
    )
