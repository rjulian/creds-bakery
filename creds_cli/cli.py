#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This is the entry point for the command-line interface (CLI) application.

It can be used as a handy facility for running the task from a command line.

.. note::

    To learn more about Click visit the
    `project website <http://click.pocoo.org/5/>`_.  There is also a very
    helpful `tutorial video <https://www.youtube.com/watch?v=kNke39OZ2k0>`_.

    To learn more about running Luigi, visit the Luigi project's
    `Read-The-Docs <http://luigi.readthedocs.io/en/stable/>`_ page.

.. currentmodule:: creds_cli.cli
.. moduleauthor:: rjulian <richard@rjulian.net>
"""
import json
import logging
import click
from .__init__ import __version__
from .aws_user_access_key import AwsAccessKey
from .github import Github
from .gcp_service_account import GcpServiceAccount

LOGGING_LEVELS = {
    0: logging.NOTSET,
    1: logging.ERROR,
    2: logging.WARN,
    3: logging.INFO,
    4: logging.DEBUG,
}  #: a mapping of `verbose` option counts to logging levels


class Info:
    """An information object to pass data between CLI functions."""

    def __init__(self):  # Note: This object must have an empty constructor.
        """Create a new instance."""
        self.verbose: int = 0


# pass_info is a decorator for functions that pass 'Info' objects.
#: pylint: disable=invalid-name
pass_info = click.make_pass_decorator(Info, ensure=True)


# Change the options to below to suit the actual options for your task (or
# tasks).
@click.group()
@click.option("--verbose", "-v", count=True, help="Enable verbose output.")
@pass_info
def cli(info: Info, verbose: int):
    """Run creds_cli."""
    # Use the verbosity count to determine the logging level...
    if verbose > 0:
        logging.basicConfig(
            level=LOGGING_LEVELS[verbose]
            if verbose in LOGGING_LEVELS
            else logging.DEBUG
        )
        click.echo(
            click.style(
                f"Verbose logging is enabled. "
                f"(LEVEL={logging.getLogger().getEffectiveLevel()})",
                fg="yellow",
            )
        )
    info.verbose = verbose


@cli.group()
@pass_info
def aws(_: Info):
    """Generate credentials for AWS services."""


@aws.command()
@pass_info
def user_access_keys(info: Info):
    """Create mock response for create aws access keys."""
    info.aws_access_keys = AwsAccessKey()
    access_keys_payload = info.aws_access_keys.generate_create_aws_access_key_payload()
    print(json.dumps(access_keys_payload, indent=4))

@cli.group()
@pass_info
def github(_: Info):
    """Generate credentials for github."""

@github.command()
@pass_info
def personal_access_token(info: Info):
    """Create mock classic github PAT"""
    info.github = Github()
    github_pat = info.github.personal_access_token_payload()
    print(json.dumps(github_pat,indent=4))

@cli.group()
@pass_info
def gcp(_: Info):
    """Generate credentials for Google Cloud Platform services"""

@gcp.command()
@pass_info
def service_account_credentials(info: Info):
    """Create mock service account tokens"""
    info.gcp_service_account = GcpServiceAccount()
    gcp_service_accounts_payload = info.gcp_service_account.generate_service_account_payload()
    print(json.dumps(gcp_service_accounts_payload, indent=4))

@cli.command()
def version():
    """Get the library version."""
    click.echo(click.style(f"{__version__}", bold=True))
