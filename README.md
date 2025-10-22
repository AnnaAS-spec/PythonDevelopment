# Виджет банковских операций клиента

## Описание проекта
Проект представляет собой набор функций для обработки и отображения банковских операций клиента.  
Функционал включает:
- фильтрацию операций по статусу (`state`);
- сортировку операций по дате;
- форматирование даты в читаемый вид;
- подготовку данных для отображения в пользовательском интерфейсе (виджете);
- заготовку для интеграции с внешними API (например, Roistat и AmoCRM).

Проект написан на **Python 3** и оформлен по стандартам **PEP 8**, включая аннотацию типов и docstrings.

---

## Цель проекта
Создать модуль для обработки данных о банковских операциях, который можно использовать:
- в веб-приложениях (например, в личном кабинете клиента);
- в API-интерфейсах;
- в учебных проектах по Python.

---

## Установка

1. Убедитесь, что установлен Python 3.8 или выше:
   ```bash
   python --version
   ```

2. Склонируйте или скачайте репозиторий:
   ```bash
   git clone https://github.com/username/bank-widget.git
   cd bank-widget
   ```

3. Установите зависимости (если появятся):
   ```bash
   pip install -r requirements.txt
   ```

---

## Структура проекта

```
bank_widget/
│
├── utils/
│   ├── filters.py         # Функции для фильтрации и сортировки операций
│   ├── formatters.py      # Преобразование даты и маскировка данных
│   ├── api_client.py      # Работа с API (Roistat, AmoCRM)
│
├── main.py                # Основной модуль приложения
├── tests/                 # Тесты
└── README.md              # Описание проекта
```

---

## Основные функции

### `filter_by_state(data: list[dict], state: str = 'EXECUTED') -> list[dict]`
Фильтрует список операций по ключу `state`.

**Пример:**
```python
from utils.filters import filter_by_state

operations = [
    {"id": 1, "state": "EXECUTED"},
    {"id": 2, "state": "CANCELED"},
]
print(filter_by_state(operations))
# [{'id': 1, 'state': 'EXECUTED'}]
```

---

### `sort_by_date(data: list[dict], reverse: bool = True) -> list[dict]`
Сортирует операции по полю `date` в порядке возрастания или убывания.

**Пример:**
```python
from utils.filters import sort_by_date

operations = [
    {"id": 1, "date": "2024-01-05T12:00:00"},
    {"id": 2, "date": "2023-12-31T08:30:00"},
]
print(sort_by_date(operations))
# [{'id': 1, 'date': '2024-01-05T12:00:00'}, {'id': 2, 'date': '2023-12-31T08:30:00'}]
```

---

### `get_date(date_str: str) -> str`
Преобразует дату из формата ISO `"2024-03-11T02:26:18.671407"`  
в человекочитаемый вид `"11.03.2024"`.

**Пример:**
```python
from utils.formatters import get_date

print(get_date("2024-03-11T02:26:18.671407"))
# 11.03.2024
```

---

### `mask_account(account_number: str) -> str`
Маскирует номер счёта или карты для безопасного отображения.

**Пример:**
```python
from utils.formatters import mask_account

print(mask_account("1234567890123456"))
# **** 3456
```

---

### `get_operations_from_api(token: str, url: str) -> list[dict]`
(для интеграции с внешними системами, например Roistat или AmoCRM)

Получает данные через API и возвращает список операций.

**Пример:**
```python
from utils.api_client import get_operations_from_api

data = get_operations_from_api(token="YOUR_TOKEN", url="https://api.example.com/operations")
print(data)
```

---

## Пример комплексного использования

```python
from utils.filters import filter_by_state, sort_by_date
from utils.formatters import get_date

operations = [
    {"id": 1, "state": "EXECUTED", "date": "2024-02-10T10:00:00"},
    {"id": 2, "state": "CANCELED", "date": "2024-02-09T09:00:00"},
]

executed = filter_by_state(operations)
sorted_executed = sort_by_date(executed)

for op in sorted_executed:
    print(f"Операция {op['id']} от {get_date(op['date'])}")
```

**Вывод:**
```
Операция 1 от 10.02.2024
```

---

## Тестирование

Запустить встроенные тесты можно так:
```bash
pytest tests/
```

Или проверить doctest:
```bash
python -m doctest utils/*.py
```

---

## Используемые технологии

- **Python 3.8+**
- **datetime**
- **requests**
- **pytest**
- **PEP 8 / PEP 257** (docstrings)

---

## Автор
**Анна Саушева**  
Python-разработчик (учебный проект по обработке банковских операций)  
2025 год  

---

## Идеи для развития
- Добавить визуализацию данных в виде веб-виджета (Flask/FastAPI).
- Реализовать подключение к банковскому API.
- Добавить кэширование данных.
- Создать пользовательский интерфейс для фильтрации и поиска.
