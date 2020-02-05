class OrderedSet(object):
    def __init__(self, some_iterable):
        self.container = []
        for item in some_iterable:
            if item not in self.container:
                self.container.append(item)

    def __repr__(self):
        return self.container.__repr__()

    def __str__(self):
        return self.container.__str__()

    def __iter__(self):
        for item in self.container:
            yield item


if __name__ == "__main__":
    ordered_words = ["these", "are", "words", "in", "an", "order"]
    print(*OrderedSet(ordered_words))
    print(*set(ordered_words))
    print(*OrderedSet(["repeated", "words", "are", "not", "repeated"]))

