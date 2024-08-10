def reverse_text(text):
    while text:
        current_character = text[-1]

        yield current_character

        text = text[:-1]


for char in reverse_text("step"):
    print(char, end='')
