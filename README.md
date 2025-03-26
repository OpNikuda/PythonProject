# Маскировка номеров карт и счетов

## Описание проекта

Этот проект представляет собой набор функций на Python для маскировки номеров банковских карт и счетов.  Он предоставляет простые и удобные инструменты для защиты конфиденциальной информации, оставляя видимыми только необходимые части номера. Подходит для использования в финансовых приложениях, системах обработки платежей и других областях, где требуется безопасное отображение информации о банковских реквизитах.

## Установка

1.  **Клонируйте репозиторий:**

    ```bash
    git clone https://github.com/ваш_логин/имя_вашего_репозитория.git  # Замените на вашу ссылку
    ```

2.  **Перейдите в директорию проекта:**

    ```bash
    cd имя_вашего_репозитория
    ```

3.  **Создайте и активируйте виртуальное окружение (рекомендуется):**

    ```bash
    python -m venv .venv
    source .venv/bin/activate  # Linux/macOS
    .venv\Scripts\activate  # Windows
    ```

4.  **Установите зависимости:**

    ```bash
    pip install pytest
    ```
    (В этом проекте pytest используется для тестов.)

## Использование

В проекте представлены следующие функции:

*   `mask_card_number(card_number)`: Маскирует номер карты, оставляя видимыми только последние 4 цифры (формат: '**********XXXX').  Требует, чтобы `card_number` состоял только из цифр.
*   `mask_account_number(account_number)`: Маскирует номер счета, оставляя открытыми первые и последние 4 цифры (формат: 'XXXX********XXXX'). Требует, чтобы `account_number` состоял только из цифр.
*   `mask_account_card(payment_info)`: Определяет, является ли `payment_info` номером карты или счетом, и применяет соответствующую маскировку. Если длина `payment_info` <= 16, считается номером карты; иначе - номером счета.  Требует, чтобы `payment_info` состоял только из цифр.  Генерирует `ValueError` при невалидном формате номера.

Примеры использования:

```python
from src.masking_functions import mask_card_number, mask_account_number, mask_account_card

card_number = "1234567890123456"
masked_card = mask_card_number(card_number)
print(f"Замаскированный номер карты: {masked_card}")  # Вывод: ************3456

account_number = "12345678901234567890"
masked_account = mask_account_number(account_number)
print(f"Замаскированный номер счета: {masked_account}") # Вывод: 1234**********90

payment_info = "1234567890123456"
masked_payment = mask_account_card(payment_info)
print(f"Замаскированная платежная информация: {masked_payment}") # Вывод: ************3456

try:
    invalid_payment = "abc1234"
    masked_invalid = mask_account_card(invalid_payment)
except ValueError as e:
    print(f"Ошибка: {e}") # Вывод: Ошибка: Неверный формат номера.
```

# 🏦 Генераторы для работы с банковскими данными

Модуль `generators` предоставляет инструменты для обработки транзакций и генерации финансовых данных.

## 📦 Установка

```bash
pip install -e .
```

## 🛠 Модуль `generators`

### 🔎 `filter_by_currency(transactions, currency)`
Фильтрует транзакции по валюте операций.

**Аргументы:**
| Параметр | Тип | Описание |
|----------|-----|----------|
| `transactions` | `List[Dict]` | Список транзакций |
| `currency` | `str` | Код валюты (например, "USD") |

**Возвращает:**
- `Iterator[Dict]` - генератор транзакций в указанной валюте

**Пример:**
```python
from generators import filter_by_currency

transactions = [
    {
        "id": 1,
        "operationAmount": {
            "amount": "100.00",
            "currency": {"code": "USD"}
        }
    },
    {
        "id": 2,
        "operationAmount": {
            "amount": "200.00",
            "currency": {"code": "EUR"}
        }
    }
]

# Получаем только USD-транзакции
for transaction in filter_by_currency(transactions, "USD"):
    print(transaction["id"])  # Выведет: 1
```

### 📝 `transaction_descriptions(transactions)`
Извлекает описания транзакций.

**Пример:**
```python
from generators import transaction_descriptions

data = [
    {"description": "Payment for services"},
    {"description": "Money transfer"}
]

descriptions = transaction_descriptions(data)
print(next(descriptions))  # "Payment for services"
```

### 💳 `card_number_generator(start, end)`
Генерирует номера карт в формате `XXXX XXXX XXXX XXXX`.

**Пример генерации 5 номеров:**
```python
from generators import card_number_generator

for card in card_number_generator(1, 5):
    print(card)

# 0000 0000 0000 0001
# 0000 0000 0000 0002
# ... 
# 0000 0000 0000 0005
```

## 🧪 Тестирование
```bash
pytest --cov=generators tests/
```

## Лицензия
Nikonorov.M
