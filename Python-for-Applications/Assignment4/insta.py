from PIL import Image
import image_utils
import os

if __name__ == "__main__":
	print("Welcome to instapy" + "\n" + "=================");
	keepGoing = True;
	while(keepGoing == True):	
		option = input("(f)ilter an image or (q)uit"+"\n"+">");
		#chose (f)
		if(option == "f"):
			path = input("What is the full path to your image?"+"\n"+">");
			if(os.path.exists(path)):
				img = Image.open(path);
				filters = input("Write a series of filters to apply:"+ "\n" +"(p)ixelate" +"\n" +"(k)aleidescope" +"\n" 
				+ "(g)ray-day" +"\n" +"(r)ighty"+"\n"+">");
		
				#iterate over filters
				for i in range(len(filters)):
					if(filters[i] == "p"):
						image_utils.pixelate(img);
					elif(filters[i] == "k"):
						image_utils.kaleidescope(img);
					elif(filters[i] == "g"):
						image_utils.grayday(img);
					elif(filters[i] == "r"):
						img = image_utils.righty(img);
				
				#end iteration over filters		
				img.show();
		
		#chose (q)uit
		elif(option == "q"):
			keepGoing = False;
		#chose someting weird
		else:
			keepGoing = True;
