morse_letters = {
    'a': '._',
    'b': '_...',
    'c': '_._.',
    'd': '_..',
    'e': '.',
    'f': '.._.',
    'g': '__.',
    'h': '....',
    'i': '..',
    'j': '.___',
    'k': '_._',
    'l': '._..',
    'm': '__',
    'n': '_.',
    'o': '___',
    'p': '.__.',
    'q': '__._',
    'r': '._.',
    's': '...',
    't': '_',
    'u': '.._',
    'v': '..._',
    'w': '.__',
    'x': '_.._',
    'y': '_.__',
    'z': '__..',
    ' ': '/',
    '1': '.____',
    '2': '..___',
    '3': '...__',
    '4': '...._',
    '5': '.....',
    '6': '_....',
    '7': '__...',
    '8': '___..',
    '9': '____.',
    '0': '_____',
}
print("Enter text which you want to translate to morse code (Type '*end' to exit the program):")
text = input().lower()
while text != '*end':
    morse = ''
    check = False
    for i in text:
        if i not in morse_letters:
            check = True
            morse = morse + i
        else:
            morse = morse + morse_letters[i]
    if check:
        print('You have used characters which do not have a morse equivalent and were therefore unconverted')
    print(f"Your converted text is:\n{morse}\nEnter what else you would like to convert (Type '*end' to exit the program):")
    text = input().lower()
print('Gooddbye')