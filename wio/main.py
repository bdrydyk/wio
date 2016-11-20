import network, socket, time
import machine, neopixel, webrepl, gc
import urllib

#button_pin.irq(trigger=button_pin.IRQ_RISING, handler=button_callback)

# def neopixel_setup():
# 	#neopixel
# 	neopixel_pin = machine.Pin(13, machine.Pin.OUT, machine.Pin.PULL_UP)

# 	np = neopixel.NeoPixel(neopixel_pin, 24)
# 	np.fill((255,255,0))
# 	np.write()


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
