from brownie import accounts, config, SimpleStorage, network

# import os


def deploy_simple_storage():
    # account = accounts[0]
    account = get_account()
    # print(account)
    # print(accounts[0])
    simple_storage = SimpleStorage.deploy({"from": account})
    stored_value = simple_storage.retrieve()
    transaction = simple_storage.store(35, {"from": account})
    transaction.wait(1)
    updated_stored_value = simple_storage.retrieve()
    print(updated_stored_value)
    print(stored_value)
    # print(account)
    # accountg = accounts.add(config["wallets"]["from_key"])
    # print(accountg)
    # print(account)
    # brownie accounts new freecodecamp-account
    print(simple_storage)


def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def main():
    deploy_simple_storage()


"""
from brownie import accounts, config, SimpleStorage, network


def deploy_simple_storage():
    account = get_account()
    simple_storage = SimpleStorage.deploy({"from": account})
    stored_value = simple_storage.retrieve()
    print(stored_value)
    transaction = simple_storage.store(15, {"from": account})
    transaction.wait(1)
    updated_stored_value = simple_storage.retrieve()
    print(updated_stored_value)


def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def main():
    deploy_simple_storage()
"""
from brownie import accounts, SimpleStorage, networks, config


def h():
    account = get_account()
    simple_storage = SimpleStorage.deploy({"from": account})
    k = simple_storage.retreive()
    print(k)
    print(simple_storage)
    ggg = SimpleStorage.store(15, {"from": account})
    v = simple_storage.retrive()
    pritn(v)


def j():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])
