def get_mask_account(pin_account: str) -> str:
    """Функция
    get_mask_account
     принимает на вход номер счета в виде числа и возвращает маску номера по правилу
    **XXXX"""

    pin_mask_account = "**" + pin_account[2:]
    return pin_mask_account


def get_mask_card_number(card_number: str) -> str:
    """Функция get_mask_card_number принимает на вход номер
    карты в виде числа и возвращает маску номера по правилу
    XXXX XX** **** XXXX
    """

    card_number = card_number[:4] + " " + card_number[4:6] + "** **** " + card_number[-4:]
    return card_number


