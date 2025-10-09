def read_text_file(filename):
    try:
        with open(filename) as file:
            text = file.readlines()
            for texts in text:
                print(texts)
    except FileNotFoundError as error:
        print(f'File not found: {error}')