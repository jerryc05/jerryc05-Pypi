def main(args: list = []):
    from jerryc05.mod_12306.train_station import parse
    keyword: str = args[0].lower() if args else ''
    while not keyword or not 96 < ord(keyword[0]) < 123:
        keyword = input('Keywords for train station? ').lower()

    station: list = parse(keyword)
    station.sort(key=lambda x: x[3])
    print('+----------------+-----+------+---------+')
    print('|  STATION NAME  |     |  ID  |   CHN   |')
    print('+----------------+-----+------+---------+')
    for x in station:
        print(f'| {x[3]:14} | {x[2]:3} | {x[5]:4} | {x[1]:{8-len(x[1])+x[1].count(" ")}}|')
        # print(
        #     f'| {x[3]:14} | {x[2]:3} | {x[5]:4} | {x[1].replace(" ", chr(12288)):{chr(12288)}<4}  |')

    print('+----------------+-----+------+---------+')

    # from getpass import getpass
    # print(
    #     f'\nYour password is hidden when typing!\nPassword = {getpass("Type password here (hidden): ")}')


if __name__ == "__main__":
    main()
