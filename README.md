# jerryc05 - PyPI Repo

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/8ad023960ef448ebaecd41219072297f)](https://app.codacy.com/app/jerryc05/jerryc05-Pypi?utm_source=github.com&utm_medium=referral&utm_content=jerryc05/jerryc05-Pypi&utm_campaign=Badge_Grade_Dashboard)

![PyPI version](<https://img.shields.io/pypi/v/jerryc05.svg>) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/jerryc05.svg) ![PyPI - Downloads](https://img.shields.io/pypi/dm/jerryc05.svg) ![PyPI - Status](https://img.shields.io/pypi/status/jerryc05.svg) ![Codacy grade](https://img.shields.io/codacy/grade/fd65fde9192d43a2bc973cafff626596.svg)

![GitHub commit activity](https://img.shields.io/github/commit-activity/y/jerryc05/jerryc05-pypi.svg) ![GitHub issues](https://img.shields.io/github/issues/jerryc05/jerryc05-pypi.svg) ![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/jerryc05/jerryc05-pypi.svg) ![GitHub License](https://img.shields.io/github/license/jerryc05/jerryc05-pypi.svg)

**jerryc05** is a tool collection developed by *@jerryc05* and published to [PyPI Repo](<https://pypi.org/project/jerryc05/>).

**IMPORTANT!!!** This repo is only actively maintained on [GitHub](<https://github.com/jerryc05/jerryc05-PyPI>). 

**For faster access from Mainland China**, there are two mirror sites: [GitLab](<https://gitlab.com/jerryc05/jerryc05-PyPI>) and [Tencent Dev](<https://dev.tencent.com/u/jerryc05/p/jerryc05-PyPI/git>). Please see [Contributing](#contributing) tab for more info if you want to report anything.

## Contents

-   [**Features**](#user-content-features)
-   [**Installation**](#user-content-installation)
-   [How To Use](#user-content-how-to-use)
-   [Contributing](#user-content-contributing)
-   [Author](#user-content-author)
-   [License](#user-content-license)

## Features

The following are features that you may make use of right away/in the near future. 

Feel free to try it out, and [submit an issue](#user-content-contributing) if you found a bug.

### Mature
-   N/A

### In progress
-   BaiduYun Storage Download

### Planning
-   Video Download
-   Music Download

### Won’t work
-   12306 Ticket Grabbing

## Installation

### Prerequisites

The following dependency is necessary:

-   **Python** 3.6+  (Either [CPython](https://www.python.org/downloads/) or [PyPy](<https://pypy.org/download.html>) works correctly)

### Option 1: Install via pip (recommended)

The official releases of `jerryc05` are distributed on [PyPI](https://pypi.python.org/pypi/jerryc05), and can be installed easily via the pip package manager.

Open `cmd.exe` or `powershell.exe` (<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAB4AAAAeCAYAAAA7MK6iAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAE5SURBVEhLYxgFwwfs/8/CsPyDMsOG17xQESqCVf/ZGFZ+VGde+cWbacXnAuYVX6Ywrfy8DUjfYl75+RdQ/D/Lqk82UNUkgvn/OVhXfNZhWP5RjWHNN3mggTOYVn7Zw7zi8z0g/gMyHB/GbzHQ5ayrvhgwr/wUwrTqSwXQwDlAw/cDLXkEZP8DG7LiczvIEHSDCWG8FhNl4KjFROJRi1HAyLOYYdUXCaZVX9PwYZaVX82IUYeOQXqgtmABA2XxgAX1qMVY8ajFROLBaTHDqpc8zMu/uDGt/JQJVNwDbL6sBzYELgIt+wo3hCYW4wPAAgCkmXXZZz2Gld8Vge2ppUCHnQAa+hrdEmyYfIvxgcVv+FhXfDFCajLNAobUPiD9ANhs+ks7i/GBbf/YQS1QhlXv+KEio4CegIEBADLBoK8laAG8AAAAAElFTkSuQmCC">) or `terminal` (<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAB4AAAAeCAYAAAA7MK6iAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAJRSURBVEhL7ZTPTxNBFMcr8WCixiPRA0VrUehaCQJBLttfKFHjxat69eAfYIwmXGmk2E2hUIpB6W5NSIxXPRiIdz151ZNtd5daWjtLJYaOb+qrQZ3IDKFGEz7JN5ud2f28ndm369rjv2NsjLZFjC9ePP07hLLV60GdvA/qThmHWk/QcKIhw6EsUPgtDreWsE6uNIs2oju3caq1hHSy8mO1BnmtLtP9ONVaoOBnKLgJ2/14eH71MA7vHupiVYHmuQ8rTIYMcg8KDroo3ce2OvJkvSOSdY7B2C24Jg7zGjzMzZHF+kG8XR51iR6C1Sw0t3NroEgOji9h/g1b9W/zBvkI3T6CKnHY+4JmefWrUC6kFnxa86BSDFjRXb5MLAGdbAQMchF1YrC/EHyTJk8okkDGoedSpRTqxAnr1TM8oUiGHlWoZ6JQ75u15LaYEc6S0a0yNUPoeRAOptfowNxa4zg0X24UYRlIl+nZ6SL1Tpq0YzxHjz/If0WVHIEsucyK9c58op5YoSGTSWc0V0eVHP2p0tXOaJ4rFY0/aV1DnThK2mx3c2Qy6YpZJvvJoFIcb6xQ4Qllcjpuv4PuPoJKMXwJe4knkw10eA1W3oba7VHS1XbWJDyZTHo0axmV4vRo9jOeTDTss2ILQJ047gV64GTMJDypSJTp1TuokqdXK6nw5Js88Z/SrdkvULFz/FPWKDTJelN6YiK/0R23VpREMelLFDOnHlof3NHvc+7xPLzX4nO8dXdQpuxL8Gu8gKc/0TdrH/UlSzf8c5UuHNrjX8Dl+gb9rDsxHNeLQAAAAABJRU5ErkJggg==">/<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAB4AAAAeCAYAAAA7MK6iAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAANKSURBVEhL7ZVZSFRRHMbHh+bqGL5kYeFDD+M4DinOeu+4oOCSy2iGjWmuIGaFGW1EVlAWSqApFUIRST6ERZtoiWnNjBZKVmqouK+5ZriUg6Lef+eORxnzgtsIPviD7+XM9/8+zj3n3uFss+UROskFds6Ut73YZR9e2lyEcvkuOwlZJpBQgDUnEFO5IpGIiy2bg52YzDIqXZSdhErBls1BICF1C2UOMhdw9VXNl4updmzZHFDRj5IPGiC9/CA75wFUf68F/9AIQ7mTk5MltpmemMSkRrU6FC6dOwwZmWkQEBgIx8+cNxTbUpQFtpke/wB5eV/RfpgqI+BPCQ9q8iUQHCQ3FPNlSjG2mZ7MK9KWznwC2p5yoT6XCz0vLCDjZtgMU4wu3nVsMzlmrj6qrvHWe6CvcICpukgYHfwCFZXV8xdMQg7xFQor7DUdIsrtbHB4jH5kdBz+l1dw6JRh1xLyEbabBr6zQmQvVc7kPXuxrJRRzuMneNforMVUEB7bMGb2MmW56mjU9PDvUdbizt5+wyvmoHCbFojJbpO8WvYS5UGZh+/gp6pq1tIFpaSmQWziaRo9GRo98mQ8vn7QV+nt7ez7Y2xlxnpdVAy+IWGgCo+aPUC6t+Hx9cF3VNiiHTQXlpSylhmr6lstHImOh8iEk4azZv5QcMzacfGUHqI8yJGe/kHWMmPVNTRB/qsCkHn40IZL5uy2G8esDajncGc/civHinkzKSkJ0D/8i7WQ0ehAJQzUXIPL6RmgioybOBEtrIevnB04anUwA6DlqmkdtxR0BDCqzbOmw2LjobWjm7V4svkW0FoC4k5FQF4WNc3M0BrCD0euDtAQnguFxrqRzAfPwBBoautYVqxvvLjMj/QcgGOGY1cGNDutWUJAX2YFYccCoaWja0lpb/8Q9JWrabYZWsvV4diVobXm7mwhjCoe2sxduJo6V1hSBqXaCki/cxdcvANmfxbYtLP4x2gdkYhjVwaZfdF5TbIEGeSoUIBQqpxAX7MxocJ1AH2p9H/f83qMPWj+Da3j7cWRqwc0HHNm5yggFalhMVBHtGDLEuY0xEv8+xRSEl7eOOisHFBwHK2xsMVLS6DfcQi63IKkP1vuwUvbbAU4nH+OlObS5Gfm9gAAAABJRU5ErkJggg==">), and type:

```console
pip3 install jerryc05 -U
```

*Note*: Windows users might want to use command `python3` instead of`python`.

<!---Icons credit to icons8.com.-->

**For faster access from Mainland China**, you might want to use:

```console
pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple jerryc05 -U
```

### Option 2: Download from Online Repository

You can download the latest pre-release archive of `jerryc05` from [GitHub](https://github.com/jerryc05/jerryc05-PyPI/archive/master.zip), [GitLab](https://gitlab.com/jerryc05/jerryc05-PyPI/-/archive/master/jerryc05-PyPI-master.zip), or [Tencent Dev](<https://dev.tencent.com/u/jerryc05/p/jerryc05-PyPI/git/archive/master>). This option is for advanced users, and they know what to do. Therefore, no further instructions will be addressed here.

## How To Use

See GitHub pages from <https://jerryc05.github.io/jerryc05-PyPI/>.

## Contributing

### Option 1: Submit via GitHub Issue (recommended)

It is strongly encouraged to submit bug reports and feature requests through [GitHub Issue](https://github.com/jerryc05/jerryc05-PyPI/issues) page. It makes it easier for me to manage all requests in one place, and every issue is guaranteed to get a response. 

**IMPORTANT!!!** Do not use issue pages in GitLab or Tencent Dev. It is a pain to maintain multiple separate issue pages, and your request will not get any response if you do so.

### Option 2: Contact Me via Direct Message Apps

This feature only applies to those who added me as their friend on QQ or WeChat; however, I still prefer to maintain issue together on [GitHub Issue](<https://github.com/jerryc05/jerryc05-PyPI/issues>) page.

## Authors

-   **[@jerryc05](<https://github.com/jerryc05>)** - *Initial work*

## License

This project is licensed under the GNU v3 License - see [LICENSE.md](https://github.com/jerryc05/jerryc05-Pypi/blob/master/LICENSE) file for details.