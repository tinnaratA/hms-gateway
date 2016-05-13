
def Trakcare_encrypt(xpswd):
	xconst = 37;
	xout = "";

	for xpiece in range(0,len(xpswd)):
		xchar = xpswd[xpiece]
		if xchar == 'D':
			xchar = chr(2)
		if xchar == 'p':
			xchar = chr(3)
		if xchar == 'd':
			xchar = chr(4)
		if xchar == 't':
			xchar = chr(5)

		xnum = ord(xchar)
		xnum = (xnum - (xpiece + 1) + xconst) % 255

		if xnum > 127:
			xnum = (xnum + 128) % 255

		if xnum < 32 :
			xnum = (xnum + 40) % 255

		if chr(xnum) == '^':
			xnum += 1

		xout += chr(xnum % 255);


	xlen = len(xout);

	for xpiece in range(xlen+1,13):
		xchar = xout[xpiece - 1 - xlen]
		xnum  = ord(xchar)
		doublexnum = (xnum * 2.345 * xconst * (xconst - 7)) % 255;
		xnum = int(doublexnum);


		if xnum > 127 :
			xnum = (xnum + 128) % 255;

		if xnum < 32 :
			xnum = (xnum + 40) % 255;

		if xnum == ord('^') :
			xnum += 1

		xout += chr(xnum%255)

	return (xout)