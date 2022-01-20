def most_frequent(sentence):
    d = {}
    for ch in sentence:
        if ch not in d:
            d[ch] = 0
        d[ch] += 1
    items = sorted(d.items(), key=lambda kv: kv[+1], reverse=False)
    items = sorted(items, key=lambda kv: kv[+1], reverse=True)
    for k, v in items:
        print(k, v)

most_frequent('Mississippi')
