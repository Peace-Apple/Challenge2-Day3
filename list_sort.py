def list_sort(lista):

    even = []
    odd = []
    characters = []
    my_dictionary = dict()
    if not isinstance(lista, list):
        return 'Invalid Input'

    if not lista:
        my_dictionary['evens'] = even
        my_dictionary['odds'] = odd
        my_dictionary['chars'] = characters
        return my_dictionary

    for p in lista:

        if isinstance(p, int):
            if p % 2 == 0:
                even.append(p)

            else:
                odd.append(p)

        elif isinstance(p, str):
            characters.append(p)

    my_dictionary['evens'] = sorted(even)
    my_dictionary['odds'] = sorted(odd)
    my_dictionary['chars'] = sorted(characters)
    return my_dictionary


print(list_sort([1, 3, 5, 'a', 'b']))