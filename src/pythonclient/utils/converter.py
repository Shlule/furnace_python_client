def snake_to_pascal(mystring: str):
    words = mystring.split('_')
    return ''.join(word.capitalize() for word in words)

def pascal_to_snake(mystring: str):
    snake_case = ''
    for i, char in enumerate(mystring):
        if char.isupper() and i != 0:
            snake_case += '_'
        snake_case += char.lower()
    return snake_case
