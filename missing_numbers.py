def missing_num(listb):

    missing_number = list()
    sorted_list = sorted(listb)
    upper = sorted_list[-1]
    lower = sorted_list[0]
    if len(sorted_list) == 0:
        return "invalid input"
    if not isinstance(listb, list):
        return 'only lists are accepted'
    for p in range(lower, upper):
        if p not in listb:
            missing_number.append(p)

    return missing_number


if __name__ == '__main__':
    listb = [1, 2, 4, 5, 6, 7, 8, 10, 12]
    print(missing_num(listb))
