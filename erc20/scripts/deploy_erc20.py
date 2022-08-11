from brownie import OurToken, network, config
from scripts.helpful_scripts import get_account


def deploy_lottery():
    account = get_account()
    Token = OurToken.deploy({"from": account})
    print(Token.balanceOf(account))


def main():
    deploy_lottery()
