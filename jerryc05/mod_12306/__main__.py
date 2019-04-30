def query_city(city: str) -> tuple:
    '''return (ID, CHN NAME)'''

    from jerryc05.mod_12306.station_name import parse
    city = city.lower()
    while not city or not 96 < ord(city[0]) < 123:
        print(f'Invalid argument: Expected letters but found {city}.')
        return ()

    station = parse(city)
    if not station:
        station = [('', '', '', '--- NO RESULT! ---', '', '')]
    station.sort(key=lambda x: x[3])
    print('''\
+-----+--------------------+-----+--------------+
| NO. |    STATION NAME    | ID: |   CHN NAME   |
+-----+--------------------+-----+--------------+\
''')
    for index, item in enumerate(station):
        print(
            f'| {index:3} | {item[3]:18} | {item[2]:3} | {item[1]:{12-len(item[1])+item[1].count(" ")}} |')
    print('''\
+-----+--------------------+-----+--------------+\
''')

    if not station[0][0]:
        return query_city(input(f'City name "{city}" not found, retry: '))

    index_chosen = int(input('Index number: '))
    while not 0 <= index_chosen < len(station):
        index_chosen = int(input('Index number invalid, retry: '))
    __result = (station[index_chosen][1], station[index_chosen][2])
    return __result


def main(args=[]):
    '''param: args =  [depart_city, arrive_city, date]'''

    __len_args = len(args)
    if __len_args < 3:
        print(f'Missing argument: Expected 3 but found {__len_args}.')
        return

    # todo support more argument
    depart_city, arrive_city, date = \
        query_city(args[0]), query_city(args[1]), args[2]

    from urllib import request
    with request.urlopen(
        'https://kyfw.12306.cn/otn/leftTicket/query?'
        f'leftTicketDTO.train_date={date}'
        f'&leftTicketDTO.from_station={depart_city[1]}'
        f'&leftTicketDTO.to_station={arrive_city[1]}'
        f'&purpose_codes=ADULT'
    ) as r:
        import json
        for item in json.loads(r.read().decode('utf-8'))['data']['result']:
            train = item.split('|')
            train_no = train[3]
            # from_station_code = train[6]
            # from_station_name = depart_city[0]
            # to_station_code = train[7]
            # to_station_name = arrive_city[0]
            start_time = train[8]
            arrive_time = train[9]
            total_time = train[10]
            first_class_seat = train[31] or '--'
            second_class_seat = train[30] or '--'
            soft_sleep = train[23] or '--'
            hard_sleep = train[28] or '--'
            hard_seat = train[29] or '--'
            no_seat = train[26] or '--'

            info = (f'车次:{train_no}\t出发时间:{start_time}\t到达时间:{arrive_time}\t消耗时间:{total_time}\t座位情况：\t 一等座：「{first_class_seat}」 \t二等座：「{second_class_seat}」\t软卧：「{soft_sleep}」\t硬卧：「{hard_sleep}」\t硬座：「{hard_seat}」\t无座：「{no_seat}」\n\n')

            print(info)

    # from getpass import getpass
    # print(
    #     f'\nYour password is hidden when typing!\nPassword = {getpass("Type password here (hidden): ")}')


if __name__ == "__main__":
    from sys import path
    path.insert(0, '.')
    main(['beij', 'fz', '2019-05-02'])
