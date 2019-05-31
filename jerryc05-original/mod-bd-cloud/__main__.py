# https://d.pcs.baidu.com/file/7818ab848534ad131371daa0a09a87b4?fid=3205693110-250528-649395292803828&dstime=1559273794&rt=sh&sign=FDtAERVY-DCb740ccc5511e5e8fedcff06b081203-eICTTY6w64XVrEWSGIHPQW4jLIM%3D&expires=8h&chkv=1&chkbd=0&chkpc=et&dp-logid=3490142661738592362&dp-callid=0&shareid=545015430&r=827065577

sign = timestamp = bdstoken = clienttype = web = app_id = logid = '???'

url =\
    r'https://pan.baidu.com/api/sharedownload?'\
    f'sign={sign}'\
    f'&timestamp={timestamp}'\
    f'&bdstoken={bdstoken}'\
    r'&channel=chunlei'\
    f'&clienttype=0'\
    f'&web=1'\
    f'&app_id=498065'\
    f'&logid={logid}'

print(url)

# https://pan.baidu.com/api/sharedownload?
# sign=235d41f86ab691a92d7fe89ef5efca8717ec8070
# &timestamp=1559275059
# &bdstoken=a38b529554faca290a75fbd966b89e7b
# &channel=chunlei
# &clienttype=0
# &web=1
# &app_id=250528
# &logid=MTU1OTI3NTE3MDY4MTAuNzQyMTY0ODU2NjA3MDQ1MQ==