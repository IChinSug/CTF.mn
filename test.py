import pyshark

cap = pyshark.FileCapture('flashbang.pcapng', display_filter='http.request')
datas = []
for pkt in cap:
    try:
        http = pkt.http
        datas.append(http.request_uri.split('&')[1].split('=')[1])
    except AttributeError:
        continue

full_data = ''.join(datas)

with open('flashbang.txt', 'w') as f:    
    f.write(full_data)