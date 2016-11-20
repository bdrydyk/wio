import network
import webrepl
import gc
import socket
import machine
import machine, neopixel, time

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


pin = machine.Pin(0, machine.Pin.IN, machine.Pin.PULL_UP)




##circle_it(np,(255,0,0),.5)
np = neopixel.NeoPixel(machine.Pin(4), 12)

def get_colors(np):
	out_list =[]
	for i in range(np.n):
		out_list.append(np[i])
	return out_list

def blank_it(np):
	np.fill((0,0,0))
	np.write()

def circle_it(np,clr,tmr,rev=False):
	my_clrs = get_colors(np)
	color_on = clr


	for i in range(np.n):
		if rev:
			if i<np.n-1:
				np[i+1] = my_clrs[i+1]
			np[np.n-i] = color_on
		else:
			if i>0:
				np[i-1] = my_clrs[i-1]
			np[i] = color_on
			
		np.write()
		time.sleep(tmr)
		print(i)
		if i ==np.n-1:
			np[i] = my_clrs[i]
			np.write()
	else:
		for i in range(np.n):
			if i>0:
				np[i-1] = my_clrs[i-1]
			np[i] = color_on
			np.write()
			time.sleep(tmr)
			print(i)
			if i ==np.n-1:
				np[i] = my_clrs[i]
				np.write()
