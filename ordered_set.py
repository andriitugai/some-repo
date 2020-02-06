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

    def __eq__(self, other):
        if not (isinstance(other, OrderedSet) or isinstance(other, set)):
            # don't attempt to compare against unrelated types
            return NotImplemented

        if isinstance(other, set):
            return other == set(self)
        else:
            if len(self) != len(other):
                return False
            return all(x == y for x, y in zip(self, other))

    def add(self, item):
        if item not in self.container:
            self.container.append(item)

    def discard(self, item):
        if item in self.container:
            self.container.remove(item)

    def __len__(self):
        return len(self.container)

    def __getitem__(self, i):
        return self.container[i]


if __name__ == "__main__":
    ordered_words = ["these", "are", "words", "in", "an", "order"]
    print(*OrderedSet(ordered_words))
    print(*set(ordered_words))
    print(*OrderedSet(["repeated", "words", "are", "not", "repeated"]))

    words = OrderedSet(["hello", "hello", "how", "are", "you"])
    words.add("doing")
    print(*words)

    words.discard("Python!")
    words.discard("are")
    print(*words)

    # print({"0", "1", "2"} == OrderedSet(["2", "1", "0"]))

    print(OrderedSet([1, 2, 3]) == OrderedSet([1, 2, 3]))
    print(OrderedSet([1, 2, 3]) == OrderedSet([1, 2, 3, 4]))
    print(OrderedSet([1, 2, 3, 4]) == OrderedSet([1, 2, 3]))
    print(OrderedSet([1, 3, 2]) == OrderedSet([1, 2, 3]))

    print(OrderedSet(["how", "are", "you"]) == OrderedSet(["how", "you", "are"]))
    print(OrderedSet(["how", "are", "you"]) == {"how", "you", "are"})
    print(OrderedSet(["how", "are", "you"]) == ["how", "are", "you"])

    print(words[1], words[-1])

