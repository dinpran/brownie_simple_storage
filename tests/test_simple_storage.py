from tkinter import S
from brownie import SimpleStorage, accounts


def test_deploy():
    # Arrange
    # locating account
    account = accounts[0]
    # Act
    # deploying simplestorage and then calling the function wee can call any function and then comparing it
    simple_storage = SimpleStorage.deploy({"from": account})
    starting_value = simple_storage.retrieve()
    expected = 0
    # Assert
    # seeing whether what we expected are correct or wrong
    assert starting_value == expected


# brownie test -k test_updating_storage


def test_updating_storage():
    # Arrange
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})
    # Act
    expected = 15
    simple_storage.store(expected, {"from": account})
    h = simple_storage.store(expected, {"from": account})
    h.wait(1)
    # Assert
    assert expected == simple_storage.retrieve()


# brownie networks list

# it is like the rpc code http:/5777 like that and it works with everything in whivh infura is written
# export WEB3_INFURA_PROJECT_ID = 1eecd61a1b8f4686bb1794aacb2bd2b5
