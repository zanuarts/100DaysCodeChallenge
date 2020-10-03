def solution(s):
    newStr = ''
    for char in s:
        if char == char.upper():
            newStr += ' ' + char
        else:
            newStr += char
    return newStr

solution("helloWorld") # "hello World"
solution("camelCase") # "camel Case"
solution("breakCamelCase") # "break Camel Case"