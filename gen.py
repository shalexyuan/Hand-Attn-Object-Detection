from PIL import Image,ImageDraw
import numpy as np
import sys
	
def remove_white_space(hand_p,R,G,B):
	hand=Image.open(hand_p).convert("RGBA")
	pixels=hand.getdata()
	new_pixels = []
	for item in pixels:
	    if item[0] >= R and item[1] >= G and item[2] >= B:
	        new_pixels.append((255, 255, 255, 0))
	    else:
	        new_pixels.append(item)
	hand.putdata(new_pixels)
	save_p=hand_p[:-5]+"_cleared.png"
	# hand.show()
	hand.save(save_p)
	return hand

def merge(bg,fg,x,y):
	bg.paste(fg, (x,y), fg)
	return bg

def draw_finger_point(im,x,y):
	draw = ImageDraw.Draw(im)
	# draw.ellipse((387, 283, 397, 293), fill = 'red', outline ='red')
	draw.ellipse((x+5,y+3,x+10,y+8), fill = 'red', outline ='red')
	im.show()
	sys.exit(0)
	return im

if __name__ == '__main__':
	hand_p="./hand/r.jpeg"
	bg_p="./combine/1.jpg"
	save_p="./merge/"+bg_p[10:-4]+"1.png"
	hand=remove_white_space(hand_p,70,70,70)
	bg_new = Image.open(bg_p).convert("RGBA")
	x=bg_new.size[0]
	y=bg_new.size[1]
	im=merge(bg_new,hand,int(x/2)+5,int(y/2)-50)
	# im=merge(bg_new,hand,int(x/2),int(y/2))
	im=draw_finger_point(im,int(x/2)+5,int(y/2)-50)
	# im=draw_finger_point(im,int(x/2),int(y/2))
	im.save(save_p)
	im.show()