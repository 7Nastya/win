def del_duplicates(duplicate_list):
    result = []
    for elem in duplicate_list:
        if elem not in result:
            result.append(elem)
    return result


t = [{"key1": "value1"}, {"k1": "v1", "k2": "v2", "k3": "v3"}, {}, {}, {"key1": "value1"}, {"key1": "value1"},
     {"key2": "value2"}]

print(del_duplicates(t))
