text = ""
while True:
    line = ""
    print("Choose a formatter:")
    formatter = input()
    if formatter == "!help":
        print("Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line")
        continue
    elif formatter == "!done":
        break
    elif formatter == "plain":
        line = input("Text:")
        text += f"{line} "
    elif formatter == "bold":
        line = input("Text:")
        line = f"**{line}** "
        text += line
    elif formatter == "italic":
        line = input("Text:")
        line = f"*{line}* "
        text += line
    elif formatter == "header":
        level = int(input('Level:>'))
        while not 1 <= level <= 6:
            level = int(input('The level should be within the range of 1 to 6.\nLevel:>'))
        line = input("Text:")
        line = f"{'#'*level} {line} "
        text += line
    elif formatter == "link":
        label = input('Label:>')
        url = input('URL:>')
        line = f"[{label}]({url}) "
        text += line
    elif formatter == "inline-code":
        line = input("Text:")
        line = f"`{line}` "
        text += line
    elif formatter == "new-line":
        text += "\n"
    elif formatter == "unordered-list":
        rows = int(input('Number of rows:>'))
        while rows <= 0:
            rows = int(input('The numbers of rows should be greater than zero\nNumber of rows:>'))
        for i in range(1, rows + 1):
            row = input(f'Row #{i}:>')
            text += f'* {row}\n'
    elif formatter == "ordered-list":
        rows = int(input('Number of rows:>'))
        while rows <= 0:
            rows = int(input('The numbers of rows should be greater than zero\nNumber of rows:>'))
        for i in range(1, rows + 1):
            row = input(f'Row #{i}:>')
            text += f'{i}.{row}\n'
    else:
        print("Unknown formatting type or command")
        continue
    print(text)
    with open("output.md","w") as f: f.writelines(text)
