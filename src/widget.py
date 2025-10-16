from datetime import datetime
from masks import get_mask_card_number
from masks import get_mask_account


def mask_account_card(data: str) -> str:
    """
    Определяет тип (карта или счёт) и возвращает строку
    с замаскированным номером.

    Args:
        data (str): Строка с типом и номером (например,
            "Visa Platinum 7000792289606361" или
            "Счет 73654108430135874305").

    Returns:
        str: Строка с тем же типом и замаскированным номером.
    """
    # Разделяем строку на слова
    parts = data.split()
    number = parts[-1]  # последний элемент — это номер
    name = " ".join(parts[:-1])  # всё до номера — название

    if name.lower().startswith("счет"):
        masked = get_mask_account(number)
    else:
        masked = get_mask_card_number(number)

    return f"{name} {masked}"


def get_date(date_str: str) -> str:
    """
    Преобразует дату из формата ISO в формат ДД.ММ.ГГГГ.

    Args:
        date_str (str): Дата в формате "YYYY-MM-DDTHH:MM:SS.mmmmmm",
                        например "2024-03-11T02:26:18.671407".

    Returns:
        str: Дата в формате "ДД.ММ.ГГГГ", например "11.03.2024".

    Examples:
        >>> get_date("2024-03-11T02:26:18.671407")
        '11.03.2024'
    """
    dt = datetime.fromisoformat(date_str)  # превращаем ISO строку в datetime
    return dt.strftime("%d.%m.%Y")  # форматируем в нужный вид
