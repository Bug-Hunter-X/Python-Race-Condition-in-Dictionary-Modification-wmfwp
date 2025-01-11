from collections import defaultdict
def function_with_uncommon_bug_solution(data):
    # Use defaultdict to avoid race conditions
    result = defaultdict(list)
    for item in data:
        key = item['key']
        result[key].append(item['value'])
    return dict(result)

data = [{
    'key': 'a',
    'value': 1
},
{
    'key': 'a',
    'value': 2
},
{
    'key': 'b',
    'value': 3
}]

result = function_with_uncommon_bug_solution(data)
print(result) # Expected output: {'a': [1, 2], 'b': [3]}