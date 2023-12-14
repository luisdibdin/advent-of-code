def load_trebuchet_txt():
    with open("advent-of-code/01/trebuchet.txt", "r") as f:
        data = f.read()
        data_list = data.split("\n")

    return data_list


if __name__ == "__main__":
    trebuchet_txt = load_trebuchet_txt()
