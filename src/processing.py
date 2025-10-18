from datetime import datetime
from typing import List, Dict


def filter_by_state(data: List[Dict], state: str = "EXECUTED") -> List[Dict]:
    """
    Возвращает новый список словарей, содержащий только те элементы,
    у которых значение по ключу 'state' соответствует указанному.

    """
    return [item for item in data if item.get("state") == state]


def sort_by_date(data: List[Dict], reverse: bool = True) -> List[Dict]:
    """
    Возвращает новый список словарей, отсортированный по дате (ключ 'date').

    """
    return sorted(
        data,
        key=lambda x: datetime.fromisoformat(x["date"]),
        reverse=reverse
    )
