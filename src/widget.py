def mask_account_card(account_card: str) -> str:
    """Принимает на вход номер карты или счет и возврощает с скрытым номером"""
    list_account_card = account_card.split(" ")
    if len(list_account_card[-1]) == 16:
        if len(list_account_card) == 3:
            card_number_masks = list_account_card[-1]
            card_number_masks = (
                card_number_masks[:4]
                + " "
                + card_number_masks[4:6]
                + "** **** "
                + card_number_masks[-4:]
            )
            return " ".join(list_account_card[:2]) + " " + card_number_masks
        else:
            card_number_masks = list_account_card[-1]
            card_number_masks = (
                card_number_masks[:4]
                + " "
                + card_number_masks[4:6]
                + "** **** "
                + card_number_masks[-4:]
            )
            return " ".join(list_account_card[:1]) + " " + card_number_masks
    elif len(list_account_card[-1]) == 20:
        mask_account = "**" + list_account_card[-1][-4:]
        return " ".join(list_account_card[:1]) + " " + mask_account


def get_date(data: str) -> str:
    """Функция принимает дату и время в формате ГГГГ-ММ-ДД... и выводит дату в формате ДД.ММ.ГГГГ"""
    return f"{data[8:10]}.{data[5:7]}.{data[:4]}"
