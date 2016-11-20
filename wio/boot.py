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


grove_pwr_pin = machine.Pin(15, machine.Pin.OUT, machine.Pin.PULL_UP)
grove_pwr_pin.value(1)


#neopixel
neopixel_pin = machine.Pin(13, machine.Pin.OUT, machine.Pin.PULL_UP)

np = neopixel.NeoPixel(neopixel_pin, 24)
np.fill((255,255,0))
np.write()


#webpower

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

on_url = "http://fart:seebeck10@10.0.1.67/outlet?a=ON"
off_url = "http://fart:seebeck10@10.0.1.67/outlet?a=OFF"


#button
button_pin = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_UP)
def button_callback(p):
	http_get(on_url)

button_pin.irq(trigger=button_pin.IRQ_RISING | button_pin.IRQ_FALLING, handler=button_callback)


#self.base_url = "http://admin:seebeck10@10.0.1.67/"
#requests.get(self.base_url + 'login.tgi', params={'Username':'admin', 'Password':'seebeck10'})

# while 1:
# 	print(button_pin.value())
# 	time.sleep(1)
##circle_it(np,(255,0,0),.5)
# np = neopixel.NeoPixel(machine.Pin(4), 12)

# def get_colors(np):
# 	out_list =[]
# 	for i in range(np.n):
# 		out_list.append(np[i])
# 	return out_list

# def blank_it(np):
# 	np.fill((0,0,0))
# 	np.write()

# def circle_it(np,clr,tmr,rev=False):
# 	my_clrs = get_colors(np)
# 	color_on = clr


# 	for i in range(np.n):
# 		if rev:
# 			if i<np.n-1:
# 				np[i+1] = my_clrs[i+1]
# 			np[np.n-i] = color_on
# 		else:
# 			if i>0:
# 				np[i-1] = my_clrs[i-1]
# 			np[i] = color_on
			
# 		np.write()
# 		time.sleep(tmr)
# 		print(i)
# 		if i ==np.n-1:
# 			np[i] = my_clrs[i]
# 			np.write()
# 	else:
# 		for i in range(np.n):
# 			if i>0:
# 				np[i-1] = my_clrs[i-1]
# 			np[i] = color_on
# 			np.write()
# 			time.sleep(tmr)
# 			print(i)
# 			if i ==np.n-1:
# 				np[i] = my_clrs[i]
# 				np.write()
