#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    file_name = dir(hidden_4)
    for name in file_name:
        if name[:2] != '__':
            print(name)
