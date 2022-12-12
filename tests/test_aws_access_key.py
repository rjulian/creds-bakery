#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
import creds_bakery.aws_user_access_key as aws_user_access_key

test_object= aws_user_access_key.AwsAccessKey()

def test_access_key_formatted_correctly():
    random_access_key = test_object.generate_access_key_random()
    assert "AKIA" in random_access_key
    assert len(random_access_key) == 20

def test_secret_access_key_formatted_correctly():
    random_secret_key = test_object.generate_secret_access_key()
    print(random_secret_key)
    assert len(random_secret_key) == 41