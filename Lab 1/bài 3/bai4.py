str = 'Geeks123For123Geeks'
print(str.translate({ord(i): None for i in '123'}))
