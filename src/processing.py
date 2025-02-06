word = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
 {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
 {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
 {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]


def filter_by_state(word: list[dict[str, any]], state_id: str = "EXECUTED") -> list[dict[str, any]]:

    word_state_exe=[]
    word_state_can=[]
    word_state=[]

    for key in word:
        if key.get("state") == state_id:
            word_state.append(key)
        # print(word_state)
    return word_state


print(filter_by_state(word))


    # for i in word:
    #     # print(i)
    #     for key, value in i.items():
    #         if value=='EXECUTED':
    #             word_state_exe.append(i)
    #         elif value=='CANCELED':
    #             word_state_can.append(i)
    # return word_state_can

    # word_state = word_state_exe + word_state_can
    # return word_state

#     for key, value in word:
#         print(key)
#         # if value=='EXECUTED':
#         #     print(word)
#         # else:
#         #     print("....")
#
#
# # print(f"{x[1]}")
#
# print(filter_by_state(word))

# x=1
#
# def xxx(x):
#     i='x'+'y'
#     return i
#
# print(xxx(x))

def sort_by_date(inform: list[dict[str, any]], reverse: bool = True) -> list[dict[str,any]]:
    sorted_word_state = sorted(word, key= lambda x: x["date"], reverse= reverse)
    return sorted_word_state

sorted_word_state = sort_by_date(word)

print(sorted_word_state)