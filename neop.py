import machine, neopixel, time

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





def demo(np):
    n = np.n

    # cycle
    for i in range(4 * n):
        for j in range(n):
            np[j] = (0, 0, 0)
        np[i % n] = (255, 255, 255)
        np.write()
        time.sleep_ms(25)

    # bounce
    for i in range(4 * n):
        for j in range(n):
            np[j] = (0, 0, 128)
        if (i // n) % 2 == 0:
            np[i % n] = (0, 0, 0)
        else:
            np[n - 1 - (i % n)] = (0, 0, 0)
        np.write()
        time.sleep_ms(60)

    # fade in/out
    for i in range(0, 4 * 256, 8):
        for j in range(n):
            if (i // 256) % 2 == 0:
                val = i & 0xff
            else:
                val = 255 - (i & 0xff)
            np[j] = (val, 0, 0)
        np.write()

    # clear
    for i in range(n):
        np[i] = (0, 0, 0)
    np.write()
