import network, espnow, ubinascii
import ujson as json

# // initiating wireless stuff -------------------
w0 = network.WLAN(network.STA_IF); w0.active(True)
e = espnow.ESPNow()
e.active(True)
#-------------------------------------------------

# // util for decoding base64 received -----------
def decode_data(encoded_data):

    if isinstance(encoded_data, str):
        b64 = encoded_data.encode('ascii')
    else:
        b64 = encoded_data

    json_bytes = ubinascii.a2b_base64(b64)
    return json.loads(json_bytes.decode('utf-8'))
#-------------------------------------------------




# // main api for receiving ----------------------
def receive():
    host, msg = e.recv()   # blocks until message arrives
    if msg:
        decoded_msg=decode_data(msg)
        return decoded_msg
#-------------------------------------------------


#// helper api for printing mac adress -----------
def check_mac_adress():
    import ubinascii

    wlan = w0
    raw_mac = wlan.config('mac')
    mac_str = ubinascii.hexlify(raw_mac, ':').decode().upper()

    print('ESP MAC:', mac_str)
    print('put that in the easy transmission code')
    return mac_str
#-------------------------------------------------




# \\ demo ---------------------------------------
if __name__ == '__main__':
    while True:
        res=receive()
        print('received: ',res)
        
        # it is still a list!
        # print(res[0]) works as well
        
        
#-------------------------------------------------

