from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import imageio
import os


class OverLaidGif():

	images = []
	textPosition = None
	
	"""Our overlaid gif constructor"""
	def __init__(self, sourcesDir, size=None):

		#Load the images
		self.loadImages(sourcesDir,size)
		#Set the default text formats
		self.setFontOptions()


	"""Load our source images into a list"""
	def loadImages(self,sourcesDir,size=None):
		
		#This is a folder containing source images.   
		self.sourcesDir = sourcesDir

		#For each image in the imagedir we must overlay the text.
		for imgsource in os.listdir(self.sourcesDir):
			
			#Only JPGs, GIFs and PNGs are allowed.
			if imgsource.endswith(".jpg") or imgsource.endswith(".gif") or imgsource.endswith(".png"): 
			
				#Open the image and add the image to the images list
				img = Image.open(self.sourcesDir + "/" + imgsource)
				
				#If size has been set then resize.
				if size is not None:
					img.thumbnail(size)
				
				self.images.append(img)


	"""Call this method to customise the default text format	"""
	def setFontOptions(self, **kwargs):
		
		self.fontColor = kwargs.pop('fontColor','white') #This is the color of the overlaid text (Optional)
		self.fontSize = kwargs.pop('fontSize',40) #This is the font size (Optional)
		self.fontStyle = kwargs.pop('fontStyle','Helvetica') #This is the font style.  It should be a path to the TTF file.
		self.font = ImageFont.truetype(self.fontStyle, self.fontSize)


	"""This method overlays each image with the text and adds it to the images list for processing later"""
	def textOverlay(self, textSource, location="C"):
		
		#This is the text to be overlaid (Essential)
		self.textSource = textSource
		
		#Get the size of the image and text to be added
		W, H = self.images[0].size
		draw = ImageDraw.Draw(self.images[0])
		w, h = draw.textsize(self.textSource,font=self.font)
		textPosition = self.getPosition(W,H,w,h,location)
	
		#Open each of the images, create a draw object and add the text
		for img in self.images:
			draw = ImageDraw.Draw(img)
			draw.text(textPosition,self.textSource,self.fontColor,font=self.font)

	"""Calculate the position of the text based on the image and text dimensions"""
	def getPosition(self, W, H, w, h, location):
		#Get vertical position.
		if 'N' in location:
			y = 10
		elif 'S' in location:
			y = H-h-10
		else:
			y = int((H-h)/2)
			
		#Get horizontal position
		if 'W' in location:
			x = 10
		elif 'E' in location:
			x = W-w-10
		else:
			x = int((W-w)/2)
		
		#return position as a tuple.
		return (x,y)

	""" This method uses all the filenames to create a animated gif	"""
	def makeGif(self, exportName, loop = False, sourcesDelete = False):
		
		self.exportName = exportName #This is the file name you want to be given to the exported file.
		self.sourcesDelete = sourcesDelete #Set this to true if you want to delete the sources - Default False
			
		#We need to save each PIL image into a temp file so it can be loaded by imageio into the frames list.
		frames = []
		for img in self.images:
			img.save("temp.jpg")
			frames.append(imageio.imread("temp.jpg"))
			
		#If there is a request to loop it then copy and reverse the list
		if loop:
			frames = frames + frames[::-1]

		# Save them as frames into a gif
		imageio.mimsave(self.exportName, frames)

		#Delete the temp files and sources if requested
		os.remove("temp.jpg")
		if self.sourcesDelete:
			for img in os.listdir(self.sourcesDir):
				os.remove(self.sourcesDir + "/" + img)


"""ITS A MAIN CLASS"""
if __name__ == '__main__':
	
	anigif = OverLaidGif("circular",(640,480))
	
	anigif.setFontOptions(fontStyle="Coda-Heavy.ttf")
	
	anigif.textOverlay("N",'N')	
	anigif.textOverlay("NE",'NE')
	anigif.textOverlay("E",'E')
	anigif.textOverlay("SE",'SE')	
	anigif.textOverlay("S",'S')
	anigif.textOverlay("SW",'SW')
	anigif.textOverlay("W",'W')	
	anigif.textOverlay("NW",'NW')
	anigif.textOverlay("C")
	
	#Create the animated gif.
	anigif.makeGif("export.gif", loop=True, sourcesDelete=False)
	
###	 MAIN PROG ###
