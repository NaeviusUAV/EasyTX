
import network, espnow, ubinascii
import ujson as json


#\\\\ MANDATORY SETTING TO CHANGE
mac_str='xx:yy:xx:yy:xx:yy'
#---------------------------------


#\\ initiating wireless stuff --------------------
peer=ubinascii.unhexlify(mac_str.replace(':', ''))
w0 = network.WLAN(network.STA_IF); w0.active(True)
e = espnow.ESPNow()
e.active(True)  
e.add_peer(peer)
# ------------------------------------------------


#\\ util for encoding to base64  ----------------
def encode_data(data):
    json_bytes = json.dumps(data).encode('utf-8')
    b64_bytes = ubinascii.b2a_base64(json_bytes).rstrip(b'\n')
    return b64_bytes.decode('ascii')
# -----------------------------------------------

#\\ main api ------------------------------------
def transmit(data):
    print('transmitting data')
    
    encoded_data = encode_data(data)
    e.send(peer, encoded_data)
    return
# -----------------------------------------------
