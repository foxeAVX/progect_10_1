def get_date(data: str) -> str:
    """Функция принимает дату и время в формате ГГГГ-ММ-ДД... и выводит дату в формате ДД.ММ.ГГГГ"""
    return f"{data[8:10]}.{data[5:7]}.{data[:4]}"


# print(get_date(str(x)))
