# tests network mode against sepolia

import os
import subprocess
import sys
import time

import pytest
import requests
from eth_account import Account

import boa
from boa.network import NetworkEnv

PKEY = os.environ["SEPOLIA_PKEY"]
SEPOLIA_URI = os.environ["SEPOLIA_ENDPOINT"]


# run all tests with testnet
@pytest.fixture(scope="module", autouse=True)
def sepolia_env():
    with boa.swap_env(NetworkEnv(SEPOLIA_URI)):
        boa.env.add_account(Account.from_key(PKEY))
        yield
