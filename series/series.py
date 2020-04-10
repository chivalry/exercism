def slices(series, length):
    if not series:
        raise ValueError('cannot slice empty series')
    if length <= 0:
        raise ValueError('cannot slice into zero length')
    size = len(series)
    if length > size:
        raise ValueError('cannot slice into pieces larger than series length')
    buf = []
    for i in range(size - length + 1):
        buf.append(series[i:i+length])
    return buf
