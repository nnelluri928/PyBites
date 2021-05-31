def flatten(items):
    for item in items:
        if not isinstance(item,(list,tuple)):
            yield item
        else:
            yield from flatten(item)


items = [1,[2,3,[]],[4,[5,[6,7,8],9],10]]

print(list(flatten(items)))