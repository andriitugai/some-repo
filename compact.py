class compact(object):
    
    RETURNED = object()

    def __init__(self, lst):
        self.lst = lst

    def __iter__(self):
        return self

    def __next__(self):
        prev_value = object()
        while True:
            val = next(self.lst)
            if prev_value is object or val != prev_value:
                prev_value = val
                return val

    def __call__(self):
        prev_value = object()
        result = []

        for item in self.lst:
            if prev_value is object or item != prev_value:
                result.append(item)
            else:
                continue

            prev_value = item
        return result 
            
    def __str__(self):
        prev_value = object()
        result = []

        for item in self.lst:
            if prev_value is object or item != prev_value:
                result.append(item)
            else:
                continue

            prev_value = item

        return str(result)
    
    def __repr__(self):
        prev_value = object()
        result = []

        for item in self.lst:
            if prev_value is object or item != prev_value:
                result.append(item)
            else:
                continue

            prev_value = item

        return str(result)


print(compact([1,1,1]))