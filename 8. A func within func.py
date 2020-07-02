def display(str):
    def message():
        return 'How are you '

    result = message() + str
    return result


print(display('Nids'))
