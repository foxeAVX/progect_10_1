word = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]



def filter_by_state(word: list[dict[str, any]], state_id: str = "EXECUTED") -> list[dict[str, any]]:
    """функция принимающая словарь, и выдает
     новый список с заданным ключем"""
    word_state = []

    for key in word:
        if key.get("state") == state_id:
            word_state.append(key)
        # print(word_state)
    return word_state


def sort_by_date(inform: list[dict[str, any]], reverse: bool = True) -> list[dict[str, any]]:
    """функция сортировки по дате, словаря"""
    sorted_word_state = sorted(word, key= lambda x: str(x["date"], reverse= reverse)
    return sorted_word_state

#В key=lambda x: x["date"] добавили str(): key=lambda x: str(x["date"]) большенство ошибок пропало

sorted_word_state = sort_by_date(word)

print(filter_by_state(word))
print(sorted_word_state)