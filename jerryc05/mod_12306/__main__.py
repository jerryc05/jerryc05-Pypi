def query_city(d_city: str, a_city: str) -> list:
    """Get station info by keyword.

    :param d_city: Keyword of departure city.
    :param a_city: Keyword of arrival city.
    :return: ((ID, CHN NAME), (ID, CHN NAME))
    """

    import jerryc05.mod_12306.station_name
    parse = jerryc05.mod_12306.station_name.parse
    city = d_city.lower()
    r = []
    import operator
    itemgetter = operator.itemgetter
    while len(r) < 2:
        station = None
        while not station or not station[0][0]:
            while not city or not 96 < ord(city[0]) < 123:
                city = input(
                    f'Invalid argument: Expected letters but found {city}, retry: ')
            station = parse(city)
            if not station:
                station = [('', '', '', '--- NO RESULT! ---', '', '')]
            station.sort(key=itemgetter(3))
            print('+-----+--------------------+------+--------------+\n'
                  '| No. |    STATION NAME    | CODE |   CHN NAME   |\n'
                  '+-----+--------------------+------+--------------+')
            for index, item in enumerate(station):
                print(
                    f'| {index + 1:3} | {item[3]:18} | {item[2]:4} '
                    f'| {item[1]:{12 - len(item[1]) + item[1].count(" ")}} |')
            print('+-----+--------------------+------+--------------+')

            if not station[0][0]:
                station = None
                city = input(f'City name "{city}" not found, retry: ')

        __index = int(input('Index number: ')) - 1
        while not 0 <= __index < len(station):
            __index = int(input('Index number invalid, retry: ')) - 1

        __station: tuple = station[__index]
        print('Chosen station name:\n'
              '+-----+--------------------+------+--------------+\n'
              f'| {__index + 1:3} | {__station[3]:18} | {__station[2]:4} '
              f'| {__station[1]:{12 - len(__station[1]) + __station[1].count(" ")}} |\n'
              '+-----+--------------------+------+--------------+\n\n')
        r.append((__station[1], __station[2]))
        city = a_city.lower()
    return r


def main(args: list = None):
    """Main executor of mod_123-7 module.

    :param args: [depart_city, arrive_city, date]
    """

    if not args:
        args = []
    __len_args = len(args)
    if __len_args < 3:
        raise SystemError(f'Missing argument: Expected 3 but found {__len_args}.')

    # todo support more argument
    date = args[2]
    while not len(date) == 10 or not \
            int(date[:4]) > 2018 or not \
            0 < int(date[5:7]) < 13 or not \
            0 < int(date[8:]) < 32:
        if len(date) == 8:
            date = f'{date[:4]}-{date[4:6]}-{date[6:8]}'
        else:
            date = input(f'Date "{date}" invalid, retry: ')
    depart_city, arrive_city = query_city(args[0], args[1])

    import urllib.request
    with urllib.request.urlopen(
            'https://kyfw.12306.cn/otn/leftTicket/query?'
            f'leftTicketDTO.train_date={date}&'
            f'leftTicketDTO.from_station={depart_city[1]}&'
            f'leftTicketDTO.to_station={arrive_city[1]}&'
            'purpose_codes=ADULT'
    ) as r:
        import json
        print('+-------+-------+-------+-------+-------+-------+-------+---------'
              '+---------+------+------+\n'
              '| TRAIN | START |  END  | TOTAL |  VIP  |  1ST  |  2ND  |  SOFT-  '
              '|  HARD-  | HARD | NONE |\n'
              '|  NO.  | TIME: | TIME: | TIME: | CLASS | CLASS | CLASS | SLEEPER '
              '| SLEEPER | SEAT | SEAT |\n'
              '+-------+-------+-------+-------+-------+-------+-------+---------'
              '+---------+------+------+')
        import jerryc05.mod_12306.mod_parser
        ticket_count = jerryc05.mod_12306.mod_parser.ticket_count
        colored_text = jerryc05.mod_12306.mod_parser.colored_text
        train_data: tuple = json.loads(r.read())['data']['result']
        if not train_data:
            train_data = (
                '|||-----|||||-----|-----|-----|||||||||||||||||||||||',)
        for item in train_data:
            train = item.split('|')
            train_no = train[3]
            # from_station_code = train[6]
            # from_station_name = depart_city[0]
            # to_station_code = train[7]
            # to_station_name = arrive_city[0]
            start_time = train[8]
            arrive_time = train[9]
            total_time = train[10]
            vip_class_seat = ticket_count(train[32])
            first_class_seat = ticket_count(train[31])
            second_class_seat = ticket_count(train[30])
            soft_sleeper = ticket_count(train[23])
            hard_sleeper = ticket_count(train[28])
            hard_seat = ticket_count(train[29])
            no_seat = ticket_count(train[26])

            info = f'| {train_no:5} ' \
                f'| {start_time:5} ' \
                f'| {arrive_time:5} ' \
                f'| {total_time:^5} ' \
                f'| {vip_class_seat:^5} ' \
                f'| {first_class_seat:^5} ' \
                f'| {second_class_seat:^5} ' \
                f'| {soft_sleeper:^7} ' \
                f'| {hard_sleeper:^7} ' \
                f'| {hard_seat:^5}' \
                f'| {no_seat:^5}|'

            if not second_class_seat == '\\' and not second_class_seat == '0':
                colored_text(info, 'green', style='bright')

            elif (vip_class_seat == '\\' or vip_class_seat == '0') and \
                    (first_class_seat == '\\' or first_class_seat == '0') and \
                    (second_class_seat == '\\' or second_class_seat == '0') and \
                    (soft_sleeper == '\\' or soft_sleeper == '0') and \
                    (hard_sleeper == '\\' or hard_sleeper == '0') and \
                    (hard_seat == '\\' or hard_seat == '0') and \
                    (no_seat == '\\' or no_seat == '0'):
                colored_text(info, 'red', style='dim')

            else:
                print(info)

        print('+-------+-------+-------+-------+-------+-------+-------+---------'
              '+---------+------+------+')

    # from getpass import getpass
    # print(
    #     f'\nYour password is hidden when typing!\n
    #     Password = {getpass("Type password here (hidden): ")}')

# if __name__ == "__main__":
#     from sys import path
#
#     path.insert(0, '.')
#     main(['beijing', 'xm', '2019-05-03'])
