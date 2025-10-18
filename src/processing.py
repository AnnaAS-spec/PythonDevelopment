from typing import List, Dict


def filter_by_state(data: List[Dict], state: str = "EXECUTED") -> List[Dict]:
    """
    Возвращает новый список словарей, содержащий только те элементы,
    у которых значение по ключу 'state' соответствует указанному.

    """
    return [item for item in data if item.get("state") == state]
