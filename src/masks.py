def get_mask_card_number(card_number: str) -> str:
    """
    Возвращает замаскированный номер банковской карты.

    Отображаются первые 6 и последние 4 цифры, остальная часть
    заменяется звездочками. Формат результата: XXXX XX** **** XXXX.

    Args:
        card_number (str): Номер банковской карты в виде строки из 16 цифр.

    Returns:
        str: Замаскированный номер карты.
    """
    first = card_number[:6]
    last = card_number[-4:]
    masked_middle = "** ****"
    masked = f"{first[:4]} {first[4:6]}{masked_middle} {last}"
    return masked


def get_mask_account(account_number: str) -> str:
    """
    Возвращает замаскированный номер банковского счёта.

    Отображаются только последние 4 цифры, перед ними ставятся две
    звездочки. Формат результата: **XXXX.

    Args:
        account_number (str): Номер банковского счёта в виде строки.

    Returns:
        str: Замаскированный номер счёта.
    """
    last = account_number[-4:]
    return f"**{last}"


# Примеры работы
print(get_mask_card_number("7000792289606361"))  # 7000 79** **** 6361
print(get_mask_account("73654108430135874305"))  # **4305
