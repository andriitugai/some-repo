def deep_flatten(seq):
    result = []

    def chain(seq):
        nonlocal result

        try:
            for elem in seq:
                if isinstance(elem, str):
                    result.append(elem)
                    return
                chain(elem)
        except TypeError:
            result.append(seq)

    chain(seq)
    return result

if __name__ == '__main__':
    lst_s = [1, [2, "Hello"], [4, [5, 6]]]
    print(deep_flatten(lst_s))

