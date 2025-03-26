
# 🏦 Банковские инструменты

Проект предоставляет набор инструментов для работы с банковскими данными, включая маскировку реквизитов и обработку транзакций.

## 📦 Установка

1. Клонируйте репозиторий:
```bash
git clone https://github.com/ваш_логин/имя_репозитория.git
cd имя_репозитория
```
Установите зависимости:
```
bash
Copy
pip install -r requirements.txt
```
🔐 Модуль маскировки данных
Функции
```
mask_card_number(card_number: str) -> str
```

# Маскирует номер карты, оставляя последние 4 цифры.
## Пример:
```
python
Copy
mask_card_number("1234567890123456")  # "************3456"
mask_account_number(account_number: str) -> str
```

# Маскирует номер счета, оставляя первые и последние 4 цифры.
## Пример:
```
python
Copy
mask_account_number("12345678901234567890")  # "1234**********7890"
mask_account_card(payment_info: str) -> str
```

# Автоматически определяет тип реквизитов и применяет соответствующую маскировку.

## Пример:
```
python
Copy
mask_account_card("1234567890123456")  # "************3456"
mask_account_card("12345678901234567890")  # "1234**********7890"
```
# 🛠 Модуль generators
Функции
```
filter_by_currency(transactions: list, currency: str) -> Iterator[dict]
```

# Фильтрует транзакции по валюте.
## Пример:
```
python
Copy
for transaction in filter_by_currency(transactions, "USD"):
    print(transaction["id"])
transaction_descriptions(transactions: list) -> Iterator[str]
```

# Извлекает описания транзакций.
## Пример:
```
python
Copy
for desc in transaction_descriptions(transactions):
    print(desc)
card_number_generator(start: int, end: int) -> Iterator[str]
```

# Генерирует номера карт в заданном диапазоне.
## Пример:
```
python
Copy
for card in card_number_generator(1, 5):
    print(card)  # "0000 0000 0000 0001", ..., "0000 0000 0000 0005"
```
# 🧪 Тестирование
Запуск всех тестов:
```
bash
Copy
pytest --cov=src --cov=generators --cov-report=term-missing
```
# Проверка стиля кода:
```
bash
Copy
flake8 src/ generators/
```
# 📜 Лицензия
MIT © Nikonorov.M

