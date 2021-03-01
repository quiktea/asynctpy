async def clean_string(string : str):
    chars = ["+"]
    for char in chars:
        string = string.replace(char, "")

    return string