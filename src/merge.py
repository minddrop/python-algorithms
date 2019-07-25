def merge(arr):
    if len(arr) < 2:
        return arr
    n = int(len(arr) / 2)
    l = merge(arr[:n])
    r = merge(arr[n:])
    return merge_list(l, r)


def merge_list(l, r):
    result = []
    while l or r:
        if not l:
            while r:
                result.append(r.pop(0))
            return result
        if not r:
            while l:
                result.append(l.pop(0))
            return result
        if l[0] <= r[0]:
            result.append(l.pop(0))
        else:
            result.append(r.pop(0))
    return result
