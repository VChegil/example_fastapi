import pytest
from app.fss import add, multiply, BankAccount, InsufficientFunds

@pytest.fixture
def zero_bankaccount():
    return BankAccount()

@pytest.fixture
def bank_account():
    return BankAccount(50)
# @pytest.mark.parametrize("num1, num2, expected",[
#     (3, 2, 5),
#     (7, 1, 8),
#     (12, 4, 16)
# ])
# def test_add(num1, num2, expected):
#     print("tess")
#     assert add(num1, num2) == expected


def test_bank_set_initial_count(bank_account):

    assert bank_account.balance == 50


def test_bank_default_amount(zero_bankaccount):
    assert zero_bankaccount.balance == 0


def test_withdraw(bank_account):

    bank_account.withdraw(20)
    assert bank_account.balance == 30

def test_diposit(bank_account):

    bank_account.deposit(10)
    assert bank_account.balance == 60


def test_collect_intrest(bank_account):
    bank_account.collect_interest()
    assert round(bank_account.balance, 6) == 55


@pytest.mark.parametrize("deposited, withdrew, expected",[
    (200, 100, 100),
    (50, 10, 40),
    (1200, 200, 1000)
])
def test_bank_transaction(zero_bankaccount, deposited, withdrew, expected):
    zero_bankaccount.deposit(deposited)
    zero_bankaccount.withdraw(withdrew)
    assert zero_bankaccount.balance == expected


def test_insufficient_funds(zero_bankaccount):
    with pytest.raises(InsufficientFunds):
        zero_bankaccount.withdraw(100)
