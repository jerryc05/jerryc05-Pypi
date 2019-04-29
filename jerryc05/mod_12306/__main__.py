def main(args: list = []):
    from getpass import getpass
    print(
        f'\nYour password is hidden when typing!\nPassword = {getpass("Type password here (hidden): ")}')


if __name__ == "__main__":
    main()
