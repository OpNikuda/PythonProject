def filter_by_currency(transactions: list[dict], currency: str) -> filter:
    """
    Фильтрует транзакции по заданной валюте и возвращает итератор

    :param transactions: Список словарей с транзакциями
    :param currency: Код валюты для фильтрации (например, "USD")
    :return: Итератор по транзакциям в указанной валюте
    """
    return filter(lambda x: x["operationAmount"]["currency"]["code"] == currency, transactions)


def transaction_descriptions(transactions):
    """
    Генератор, который возвращает описания транзакций по очереди

    :param transactions: Список словарей с транзакциями
    :yield: Описание транзакции (поле "description")
    """
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start: int, end: int):
    """
    Генератор номеров банковских карт в формате XXXX XXXX XXXX XXXX

    :param start: Начальный номер (от 1)
    :param end: Конечный номер (до 9999999999999999)
    :yield: Номер карты в формате строки
    """
    for number in range(start, end + 1):
        # Преобразуем число в 16-значную строку с ведущими нулями
        num_str = f"{number:016d}"
        # Разбиваем на группы по 4 цифры
        yield f"{num_str[:4]} {num_str[4:8]} {num_str[8:12]} {num_str[12:16]}"


#