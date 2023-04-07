while True:
    print("Choose a formatter:")
    formatter = input()
    if formatter == "!help":
        print("Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line")
        continue
    elif formatter == "!done":
        break
    else:
        print("Unknown formatting type or command")
        continue