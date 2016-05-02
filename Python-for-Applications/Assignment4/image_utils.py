from PIL import Image

def pixelate(img):
	pixels = img.load();
	for x in range(0, img.size[0], 10):
		for y in range(0, img.size[1], 10):
			color = pixels[x,y];
			for i in range(10):
				for j in range(10):
					if((x+i)<img.size[0] and (y+j)<img.size[1]):
						pixels[x+i,y+j]=color;

def kaleidescope(img):
	pixels = img.load();
	#quad 3
	downscaled = downscale4(pixels, img);
	#quad 1
	vflipped = flipv(downscaled.load(), downscaled);
	#quad 4
	hflipped = fliph(downscaled.load(), downscaled);
	#quad 2
	vhflipped = flipv(hflipped.load(), hflipped);
	
	paster(pixels, vflipped, 1);
	paster(pixels, vhflipped, 2);
	paster(pixels, downscaled, 3);
	paster(pixels, hflipped, 4);
	

#returns a downscaled image
def downscale4(pixels, img):
	tempdimg = Image.new("RGB", (img.size[0]//2, img.size[1]//2), "white");
	colors = tempdimg.load();
	for x in range(0, img.size[0]-1, 2):
		for y in range(0, img.size[1]-1, 2):
			c1 = pixels[x,y];
			c2 = pixels[x+1,y];
			c3 = pixels[x, y+1];
			c4 = pixels[x+1, y+1];
			color = ((c1[0]+c2[0]+c3[0]+c4[0])//4, (c1[1]+c2[1]+c3[1]+c4[1])//4, (c1[2]+c2[2]+c3[2]+c4[2])//4);
			colors[(x//2), (y//2)] = color;
	return tempdimg;

#returns a vertically flipped image
def flipv(pixels, img):
	tempimg = Image.new("RGB", (img.size[0], img.size[1]), "white");
	flipped = tempimg.load();
	for x in range(img.size[0]):
		for y in range(img.size[1]):
			flipped[x, y] = pixels[x,img.size[1]-1-y];
	return tempimg;

#returns a horizontally flipped image	
def fliph(pixels, img):
	temphimg = Image.new("RGB", (img.size[0], img.size[1]), "white");
	flipped = temphimg.load();
	for x in range(img.size[0]):
		for y in range(img.size[1]):
			flipped[x,y] = pixels[img.size[0]-1-x, y];
	return temphimg;

#really hope all these images are the same size
def paster(bigPixels, img, quad):
	smallPixels = img.load();
	if(quad == 1):
		for x in range(img.size[0]):
			for y in range(img.size[1]):
				bigPixels[x,y] = smallPixels[x,y];
	elif(quad ==2):
		for x in range(img.size[0]):
			for y in range(img.size[1]):
				bigPixels[x+img.size[0],y] = smallPixels[x,y];
	elif(quad ==3):
		for x in range(img.size[0]):
			for y in range(img.size[1]):
				bigPixels[x,y+img.size[1]] = smallPixels[x,y];
	elif(quad ==4):
		for x in range(img.size[0]):
			for y in range(img.size[1]):
				bigPixels[x+img.size[0],y+img.size[1]] = smallPixels[x,y];

#makes a grayscale image
def grayday(img):
	pixels = img.load();
	for x in range(img.size[0]):
		for y in range(img.size[1]):
			avg = sum(pixels[x,y]) // 3;
			pixels[x, y] = (avg,) *3;

	
#makes a new image rotated 90 degrees to the right (repeated calls are a bit weird....)
def righty(img):
	pixels = img.load();
	rightImg = Image.new("RGB", (img.size[1], img.size[0]), "white");
	rightPixels = rightImg.load();
	for x in range(img.size[0]):
		for y in range(img.size[1]-1, 0, -1):
			rightPixels[rightImg.size[0]-y, rightImg.size[1]-x-1] = pixels[x,y];
	return rightImg;
