if __name__ == "__main__":
    import emoji

    text = input("Napiš text: ")
    print(emoji.emojize(text.lower(), language="alias"))