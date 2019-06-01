def main():
    import dataclasses

    @dataclasses.dataclass
    class Flight:
        d_city: str           # departure city
        a_city: str           #   arrival city
        d_time_or_date: str   # departure time or departure date
        a_time_or_r_date: str #   arrival time or   arrival date

    class BaseCrawler():
        def __init__(self, engine: str, flight: Flight):
            self._engine = engine # crawler type
            self._flight = flight #  flight data
            self.is_round_trip = True if flight.a_time_or_r_date else False

        def search(self):
            raise NotImplementedError

        def parse(self, result: bytes) -> list:
            raise NotImplementedError

    class HotWireCrawler(BaseCrawler):
        def __init__(self, flight: Flight):
            super().__init__('HotWire', flight)

        def _get_airport(self, keyword: str) -> str:
            url = (f'https://vacation.hotwire.com/api/v4/typeahead/{keyword}?'
                   'callback=' #cb_1559365750262_117481'
                   '&client=Flights.Search'
                    # '&siteid=30031'
                   '&guid=' #5d8c12dfa64e4e3a8eb269aed9392c7e'
                   '&lob=FLIGHTS'
                   '&locale=en_US'
                    # '&expuserid=-1'
                    # '&regiontype=95'
                    # '&ab='
                    # '&dest=false'
                    '&maxresults=9'
                   '&features=uta_client%7Cnearby_airport%7Cta_hierarchy'
                    # '&format=jsonp'
                    # '&device=Desktop'
                    # '&browser=Chrome'
                    # '&personalize=false'
                   ) # yapf: disable
            import urllib.request as u_req
            with u_req.urlopen(url) as u_open:
                u_read: bytes = u_open.read()[1:-1]
                import json
                options: dict = json.loads(u_read)['sr']
                print(
                    '+---+------------------------------------------------------------------------+\n'
                    '| # | Airpot/City Name                                                       |\n'
                    '+---+------------------------------------------------------------------------+'
                )
                last_search_names = []
                for index, option in enumerate(options):
                    _ = option['regionNames']['lastSearchName']
                    last_search_names.append(_)
                    print(f"| {index+1} | {_:70} |")
                print(
                    '+---+------------------------------------------------------------------------+'
                )
                choice = -1
                while not 0 <= choice <= 9:
                    choice = int(input("Select airport/city #: ")) - 1
                return last_search_names[choice]
            raise SystemError(
                "Network access failed! Remote: vacation.hotwire.com")

        def search(self):
            d_city = self._get_airport(self._flight.d_city)
            a_city = self._get_airport(self._flight.a_city)
            import urllib.parse as u_parse
            quote = u_parse.quote
            url = (
                r'https://vacation.hotwire.com/Flights-Search?'
                f'trip={"roundtrip" if self.is_round_trip else "OneWay"}'
                f'&leg1={quote(f"from:{d_city},to:{a_city},departure:{self._flight.d_date}ANYT")}'
                f'&leg2={quote(f"from:{a_city},to:{d_city},departure:{self._flight.a_date}ANYT")}'
                f'&passengers={quote("children:0,adults:1,seniors:0,infantinlap:Y")}'
                f'&options={quote("sortby:price")}'
                r'&mode=search')
            import urllib.request as u_req
            with u_req.urlopen(url) as u_open:
                u_read: bytes = u_open.read()
                # print(u_read)
                # print('\n\n\n')
                _ = u_read.index(b'request.open(')
                u_read = u_read[_ + 21:u_read.index(b', true')].replace(
                    b"' + fl + '", b'&is=1').replace(b"' + ul", b'&ul=0')
                with u_req.urlopen(
                        f'https://vacation.hotwire.com{u_read.decode()}'
                ) as u_open:
                    # u_read: bytes = u_open.read()
                    with open('hotwire.json', 'wb') as f:
                        f.write(u_open.read())

        def parse(self, result: bytes) -> list:
            exit()

    HotWireCrawler(Flight('was', 'lax', '06/03/2019', '06/06/2019')).search()


if __name__ == "__main__":
    try:
        main()
    except OSError as e:
        print(e)