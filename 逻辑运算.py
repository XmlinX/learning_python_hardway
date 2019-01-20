def not_empty(s):
    return s and s.strip()


a = list(filter(not_empty, ['A', '', 'B', None, 'C', '  ']))
print(a)