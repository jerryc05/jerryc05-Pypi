def main():
    class Flight():
        def __init__(self,
                     d_city: str,
                     a_city: str,
                     d_date: str = None,
                     a_date: str = None,
                     web_page: str = None):
            self.d_city = d_city     # departure city
            self.a_city = a_city     #   arrival city
            self.d_date = d_date     # departure date
            self.a_date = a_date     #   arrival date
            self.web_page = web_page #    detail webpage

    class BaseCrawler():
        def __init__(self, engine: str, flight: Flight):
            self._engine = engine # crawler type
            self._flight = flight #  flight data
            self.is_round_trip = True if flight.a_date else False

        def search(self, result: tuple):
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

        def search(self, result: list):
            d_city = self._get_airport(self._flight.d_city)
            a_city = self._get_airport(self._flight.a_city)
            import urllib.parse as u_parse
            quote=u_parse.quote
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
                i=u_read.index(b'request.open(')
                u_read=u_read[i+21:u_read.index(b', true')].replace(b"' + fl + '", b'&is=1').replace(b"' + ul",b'&ul=0')
                print(f'https://vacation.hotwire.com{u_read.decode()}')
                # request.open('GET', '/Flight-Search-Paging?c=

            # 'https://vacation.hotwire.com/Flights-Search?'
            # 'trip=roundtrip'
            # '&leg1=from:Washington, DC, United States (WAS),to:Los Angeles, CA, United States (LAX),departure:06/03/2019TANYT'
            # '&leg2=from:Los Angeles, CA, United States (LAX),to:Washington, DC, United States (WAS),departure:06/06/2019TANYT'
            # '&passengers=adults:1,children:0,seniors:0,infantinlap:Y'
            # '&options=cabinclass:economy'
            # '&mode=search'
            # '&origref=vacation.hotwire.com'

            # https://vacation.hotwire.com/Flights-Search?trip=roundtrip&leg1=from%3AWashington%2C%20DC%2C%20United%20States%20(WAS)%2Cto%3ALos%20Angeles%2C%20CA%2C%20United%20States%20(LAX)%2Cdeparture%3A06%2F01%2F2019TANYT&leg2=from%3ALos%20Angeles%2C%20CA%2C%20United%20States%20(LAX)%2Cto%3AWashington%2C%20DC%2C%20United%20States%20(WAS)%2Cdeparture%3A06%2F02%2F2019TANYT&passengers=adults%3A1%2Cchildren%3A0%2Cseniors%3A0%2Cinfantinlap%3AY&options=cabinclass%3Aeconomy&mode=search&origref=vacation.hotwire.com

            # 'https://vacation.hotwire.com/Flights-Search?'
            # 'tmid=22041369292'
            # '&trip=OneWay'
            # '&leg1=from:WAS,to:LAX,departure:05/31/2019TANYT'
            # '&passengers=children:0,adults:1,seniors:0,infantinlap:Y'
            # '&options=sortby:price'
            # '&mode=search'
            # '&paandi=true'

            # https://vacation.hotwire.com/Flight-Search-Paging?c=4277bc33-7857-4adf-8376-3c2a1db7e3cf&is=1&sp=asc&cz=200&cn=0&ul=0

    HotWireCrawler(Flight('was', 'lax', '06/03/2019', '06/06/2019')).search([])


if __name__ == "__main__":
    try:
        main()
    except OSError as e:
        print(e)