from pydoc import cli
from re import M
from brownie import FundMe, accounts, network, config, MockV3Aggregator
from scripts.helpful_scripts import (
    deploy_mocks,
    # get_account,
    # LOCAL_BLOCKCHAIN_ENVIRONMENTS,
)
from web3 import Web3

# network allows us to interact with different networks

LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local2"]

DECIAMLS = 8
STARTING_PRCE = 200000000000


def deploy_fund_me():
    def get_account():
        if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
            # == "development":
            return accounts[0]
        else:
            return accounts.add(config["wallets"]["from_key"])

    account = get_account()
    # you can also import os write it as account = accounts.add(os.getenv("PRIVATE_KEY"))

    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        #!= "development":
        # networks.show_active() tells you what chain it is using like rinkeby or mainnet or kovan
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
    else:
        print(f"The active network is {network.show_active()}")
        print("Deploying Mocks...")
        # 200000000000000000000
        if len(MockV3Aggregator) <= 0:
            # mock_aggregator = MockV3Aggregator.deploy(18, Web3.toWei(2000, "ether"), {"from": account})
            MockV3Aggregator.deploy(DECIAMLS, STARTING_PRCE, {"from": account})
            # MockV3Aggregator.deploy(DECIAMLS, Web3.toWei(2000, "ether"), {"from": account})
        price_feed_address = MockV3Aggregator[-1].address
        print("Mocks deployed!")

    # you are adding fundme to blockchain by doing FundMe.deploy({from: account means from whom you are demploying from})
    # anytime you are deploying you should do {from.....}
    # brownie is intellegent to know whether it is a call or transaction here brownie knows that we are making a state change
    # brownie knows wheter it is a view or transaction

    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify"),
        # publish_source=config["networks"][network.show_active()]["verify"] you can write like this also but you will geterror
    )
    # transaction = simple_storage.store(15, {"from":account})
    # transaction.wait
    print(f"Huzzah, your contract has been deployed to {fund_me.address}")
    print(accounts[0])
    return fund_me


def main():
    deploy_fund_me()
