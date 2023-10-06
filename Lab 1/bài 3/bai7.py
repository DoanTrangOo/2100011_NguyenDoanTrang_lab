string = 'geeksforgeeks_is_best'
words = string.split('_')
capitalized_words = [word.title() for word in words]
result = ''.join(capitalized_words)
print(result)
