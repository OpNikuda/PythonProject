import pytest
from src.generators import filter_by_currency

@pytest.fixture
def sample_transactions():
    return [
        {
            "operationAmount": {
                "currency": {"code": "USD"}
            },
            "description": "Transaction 1"
        },
        {
            "operationAmount": {
                "currency": {"code": "EUR"}
            },
            "description": "Transaction 2"
        },
        {
            "operationAmount": {
                "currency": {"code": "USD"}
            },
            "description": "Transaction 3"
        }
    ]

def test_filter_by_currency(sample_transactions):
    # Тест на фильтрацию USD
    usd_transactions = list(filter_by_currency(sample_transactions, "USD"))
    assert len(usd_transactions) == 2
    assert all(t["operationAmount"]["currency"]["code"] == "USD" for t in usd_transactions)

def test_no_matching_currency(sample_transactions):
    # Тест на отсутствие валюты
    gbp_transactions = list(filter_by_currency(sample_transactions, "GBP"))
    assert len(gbp_transactions) == 0

def test_empty_input():
    # Тест на пустой ввод
    assert list(filter_by_currency([], "USD")) == []

def test_missing_currency_field():
    # Тест на отсутствие поля currency
    with pytest.raises(KeyError):
        list(filter_by_currency([{"operationAmount": {}}], "USD"))


from src.generators import transaction_descriptions

@pytest.mark.parametrize("transactions,expected", [
    ([{"description": "Test 1"}], ["Test 1"]),
    ([{"description": "A"}, {"description": "B"}], ["A", "B"]),
    ([], []),
])
def test_transaction_descriptions(transactions, expected):
    assert list(transaction_descriptions(transactions)) == expected

def test_missing_description_field():
    with pytest.raises(KeyError):
        next(transaction_descriptions([{"no_description": ""}]))


from src.generators import card_number_generator

@pytest.mark.parametrize("start,end,expected", [
    (1, 1, ["0000 0000 0000 0001"]),
    (1, 3, [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003"
    ]),
    (9999, 10001, [
        "0000 0000 0000 9999",
        "0000 0000 0001 0000",
        "0000 0000 0001 0001"
    ]),
])
def test_card_number_generator(start, end, expected):
    assert list(card_number_generator(start, end)) == expected

def test_edge_cases():
    # Тест на максимальное значение
    last_card = list(card_number_generator(9999999999999999, 9999999999999999))
    assert last_card == ["9999 9999 9999 9999"]

    # Тест на недопустимый диапазон
    with pytest.raises(ValueError):
        list(card_number_generator(-1, 5))

    with pytest.raises(ValueError):
        list(card_number_generator(2, 1))


#######