def load_txt(path: str) -> list[str]:
    with open(path, "r") as f:
        data = f.read()
        data_list = data.split("\n")

    return data_list
