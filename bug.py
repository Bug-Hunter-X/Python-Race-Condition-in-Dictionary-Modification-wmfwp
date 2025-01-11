def function_with_uncommon_bug(data):
    # Assume data is a list of dictionaries
    result = {}
    for item in data:
        key = item['key']
        if key not in result:
            result[key] = []
        result[key].append(item['value'])
    return result

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

result = function_with_uncommon_bug(data)
print(result) # Expected output: {'a': [1, 2], 'b': [3]}

# The bug is subtle and can be difficult to spot.
# It arises from a common error while creating the dictionary
# There might be a race condition if multiple threads try to access and modify the same dictionary concurrently
# The solution is to use a thread-safe data structure like defaultdict from collections module instead of plain dict