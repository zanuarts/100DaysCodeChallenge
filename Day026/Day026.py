def kebabize(string):
    result = ''
    text = ''.join([i for i in string if not i.isdigit()])
    if len(text) == 0:
        return result
    res = text[0].lower() + text[1:] 
    for char in res:
        if char == char.upper():
            result += '-' + char.lower()
        else:
            result += char.lower()
    return result

# "Basic tests"
kebabize('myCamelCasedString') # 'my-camel-cased-string'
kebabize('myCamelHas3Humps') # 'my-camel-has-humps'
kebabize('SOS') # 's-o-s'
kebabize('42') # ''
kebabize('CodeWars') # 'code-wars'