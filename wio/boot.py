import network, socket, time
import machine, neopixel, webrepl, gc
import urllib
#esp.osdebug(None)

ap_if = network.WLAN(network.AP_IF)
sta_if = network.WLAN(network.STA_IF)

ap_if.active(False)
sta_if.active(True)

sta_if.connect("FARTFACTORY","seebeck10")
sta_if.ifconfig()

webrepl.start()
#('10.0.1.29', '255.255.255.0', '10.0.1.1', '10.0.1.1')
#('10.0.1.12', '255.255.255.0', '10.0.1.1', '10.0.1.1')
#('10.0.1.30', '255.255.255.0', '10.0.1.1', '10.0.1.1')
gc.collect()

#set this pin on to enable grove modules
grove_pwr_pin = machine.Pin(15, machine.Pin.OUT, machine.Pin.PULL_UP)
grove_pwr_pin.value(1)

on_url = "http://10.0.1.67/outlet?a=ON"
off_url = "http://10.0.1.67/outlet?a=OFF"

OUTLET_STATE = True

button_pin = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_UP)

#button

def http_get(url):
	_, _, host, path = url.split('/', 3)
	addr = socket.getaddrinfo(host, 80)[0][-1]
	s = socket.socket()
	s.connect(addr)
	s.send(bytes('GET /%s HTTP/1.0\r\nHost: %s\r\n\r\n' % (path, host), 'utf8'))
	while True:
		data = s.recv(100)
		if data:
			print(str(data, 'utf8'), end='')
		else:
			break

def button_callback(p):
	global OUTLET_STATE
	print("changing button state shit")
	if OUTLET_STATE == True:
		print("turning off")
		OUTLET_STATE = False
		http_get(off_url)
		
	elif OUTLET_STATE == False:
		print("turning on")
		OUTLET_STATE = True
		http_get(on_url)
		

button_pin.irq(trigger=button_pin.IRQ_FALLING, handler=button_callback)