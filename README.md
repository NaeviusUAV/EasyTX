# EasyTX
super easy to use micropython functions to let 2 esp32's talk to eachother wirelessly!
- max 200 meters distance
- a little over 1 ms latency
- just a simple integration of espnow

You can very easily transmit a list of numbers:
```python
from easy_transmission import transmit

# // joystick for example 
x, y, button = wait_for_joystick() 

# // transmitting joystick data 
transmit(data=[x,y,button])
```

then on the receiving end:
```python
from easy_receiver import receive

data=receive()       # will block here until data is received, returns it in the exact same list.
```

2 lines of code is all it takes


# setup - Receiver esp32
go to easy_receiver.py in this repo, and copy and paste the file onto your esp32.
You can use Thonny for that if you arent already.

When its on there, go into your main script and paste this to get the mac adress of your esp (you need to have it for the transmitter to know where to transmit to)
```python
from easy_receiver import check_mac_adress
check_mac_adress()
```
it will print out the mac adress, copy that for setting up the transmitter esp.
But you are done for the receiving end now, you can use it as shown on top of this readme.

# setup - Transmitter esp32
go to easy_transmission.py in this repo, and copy and paste the file onto your esp32.
at the top, you see a section where you need to paste the mac adress of the receiving esp32
```python

#\\\\ MANDATORY SETTING TO CHANGE
mac_str='xx:yy:xx:yy:xx:yy' 
#---------------------------------

```
after that it is ready to transmit like shown on top!
