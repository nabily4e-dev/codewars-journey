def find_needle(haystack):
    for i in range(len(haystack)):
        if haystack[i] == "needle":
            return f"found the needle at position {i}"
    return "needle not found"

# def find_needle(haystack):
#     for i, result in enumerate(haystack):
#         if result == 'needle':
#             return 'found the needle at position ' + str(i)
#     return 'needle not found!'

# def find_needle(haystack):
#     try:
#         index = haystack.index('needle')
#         return 'found the needle at position ' + str(index)
#     except:
#         return 'needle not found!'

# def find_needle(haystack):
#     indices = [i for i, result in enumerate(haystack) if result == 'needle']
#     if indices:
#         return 'found the needle at position ' + str(indices[0])
#     else:
#         return 'needle not found'
    
# def find_needle(haystack):
#     try:
#         index = next(i for i, element in enumerate(haystack) if element == "needle")
#         return "found the needle at position " + str(index)
#     except StopIteration:
#         return "needle not found"


############
############

haystack = ["hay", "hay", "needle", "hay", "hay"]
print(find_needle(haystack))  # Output: "found the needle at position 2"

haystack = ["hay", "hay", "hay", "hay"]
print(find_needle(haystack))  # Output: "needle not found"

haystack = []
print(find_needle(haystack))  # Output: "needle not found"

haystack = ["needle"]
print(find_needle(haystack))  # Output: "found the needle at position 0"

haystack = ["hay", "needle"]
print(find_needle(haystack))  # Output: "found the needle at position 1"