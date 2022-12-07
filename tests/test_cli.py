#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
.. currentmodule:: test_cli
.. moduleauthor:: rjulian <richard@rjulian.net>

This is the test module for the project's command-line interface (CLI)
module.
"""
# fmt: off
import creds_bakery.cli as cli
from creds_bakery import __version__
# fmt: on
from click.testing import CliRunner, Result


# To learn more about testing Click applications, visit the link below.
# http://click.pocoo.org/5/testing/


def test_version_displays_library_version():
    """
    Arrange/Act: Run the `version` subcommand.
    Assert: The output matches the library version.
    """
    runner: CliRunner = CliRunner()
    result: Result = runner.invoke(cli.cli, ["version"])
    assert (
        __version__ in result.output.strip()
    ), "Version number should match library version."


def test_verbose_output():
    """
    Arrange/Act: Run the `version` subcommand with the '-v' flag.
    Assert: The output indicates verbose logging is enabled.
    """
    runner: CliRunner = CliRunner()
    result: Result = runner.invoke(cli.cli, ["-v", "version"])
    assert (
        "Verbose" in result.output.strip()
    ), "Verbose logging should be indicated in output."


def test_aws_group_displays_valid_message():
    """Command group AWS displays help information"""
    runner: CliRunner = CliRunner()
    result: Result = runner.invoke(cli.cli, ["aws"])
    print(result.output.strip())
    assert "Generate mock credentials for AWS service" in result.output.strip()


def test_aws_user_access_keys_displays_valid_message():
    """Command for user access keys shows correct fields"""
    runner: CliRunner = CliRunner()
    result: Result = runner.invoke(cli.cli, ["aws", "user-access-keys"])
    print(result.output.strip())
    assert "AccessKey" in result.output.strip()
    assert "AccessKeyId" in result.output.strip()
    assert "SecretAccessKey" in result.output.strip()


def test_gcp_group_displays_valid_message():
    """Command group for GCP displays help information"""
    runner: CliRunner = CliRunner()
    result: Result = runner.invoke(cli.cli, ["gcp"])
    print(result.output.strip())
    assert (
        "Generate mock credentials for Google Cloud Platform services"
        in result.output.strip()
    )


def test_gcp_service_account_credentials_displays_valid_message():
    """Command for GCP service account creds shows correct fields"""
    runner: CliRunner = CliRunner()
    result: Result = runner.invoke(cli.cli, ["gcp", "service-account-credentials"])
    print(result.output.strip())
    assert "project_id" in result.output.strip()
    assert "private_key" in result.output.strip()
    assert "client_id" in result.output.strip()


def test_oracle_group_displays_valid_message():
    """Command group for Oracle Cloud displays help information"""
    runner: CliRunner = CliRunner()
    result: Result = runner.invoke(cli.cli, ["oracle-cloud"])
    print(result.output.strip())
    assert (
        "Generates mock credentials for Oracle Cloud Infrastructure"
        in result.output.strip()
    )


def test_oracle_cloud_user_auth_token_displays_valid_message():
    """Command for Oracle user auth token shows correct fields"""
    runner: CliRunner = CliRunner()
    result: Result = runner.invoke(cli.cli, ["oracle-cloud", "user-auth-token"])
    print(result.output.strip())
    assert "OCID" in result.output.strip()
    assert "AuthToken" in result.output.strip()


def test_github_group_displays_valid_message():
    """Command group for Github displays help information"""
    runner: CliRunner = CliRunner()
    result: Result = runner.invoke(cli.cli, ["github"])
    print(result.output.strip())
    assert "Generate mock credentials for Github" in result.output.strip()


def test_github_pat_displays_valid_message():
    """Command for Github personal access token shows correct fields"""
    runner: CliRunner = CliRunner()
    result: Result = runner.invoke(cli.cli, ["github", "personal-access-token"])
    print(result.output.strip())
    assert "UserName" in result.output.strip()
    assert "PersonalAccessToken" in result.output.strip()
