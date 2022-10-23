from decimal import Decimal
from brownie import network, config, accounts, MockV3Aggregator
from web3 import Web3

LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local2"]

DECIAMLS = 8
STARTING_PRCE = 200000000


def get_account():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        # == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def deploy_mocks():
    print(f"The active network is {network.show_active()}")
    print("Deploying Mocks...")
    # 200000000000000000000
    if len(MockV3Aggregator) <= 0:
        # mock_aggregator = MockV3Aggregator.deploy(18, Web3.toWei(2000, "ether"), {"from": account})
        MockV3Aggregator.deploy(DECIAMLS, STARTING_PRCE, {"from": get_account()})
        price_feed_address = MockV3Aggregator[-1].address
        print("Mocks deployed!")


# to add a new account type brwonie accounts new freecodecamp-accounts to use it type accounts.load("freecodecamp-accounts")
# continuation fro serious accounts only you use this h
# dont use your real private key in main net in .env
# arrange means you arre arranging act meaning you are doing what you like assert means writhing what you expected
# if you want to test only one thing brownie test -k test_updating_storage brownie test --pd
# t
# if anything is under development like ganache we it is in development and anything under ethereum brownie is going yo keep
# track of them brownie knows that infura is a thing and can directly connect with it connecting infura with testnet
# brownie networks list
# brownie console
# it will start again from the begining
# to ass a new gnanche blockchin yo brownie networks add Ethereum ganache-local2 host=http://127.0.0.1:7545 chainid=5777
# remove previous cd - cd ..
# if len(MockV3Aggregator) <= 0:
# mock_aggregator = MockV3Aggregator.deploy(18, Web3.toWei(2000, "ether"), {"from": account})
# MockV3Aggregator.deploy(DECIAMLS, STARTING_PRCE, {"from": get_account()})
# price_feed_address = MockV3Aggregator[-1].address
# print("Mocks deployed!")
