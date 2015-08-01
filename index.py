import StringIO
import tempfile
import base64
from flask import Flask, request, make_response, send_file
from PIL import Image #not actually Pil, pillow

app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def img():
	if request.method == 'GET':
		return "yo, you forgot to post"
	else:
		vimg = request.files["image"]
		img = Image.open(vimg).convert('RGBA')
		
		pixels = img.load()
		for y in xrange(img.size[1]):
		    for x in xrange(img.size[0]):
				#print ("checking[x:y] " + str(y) + ":" + str(x) + str(pixels[x,y]))
				if pixels[x, y] == (255, 255, 255, 255):
					pixels[x, y] = (255, 255, 255, 0)
					#print "edited[x/y]: " + str(y) + ":" + str(x)

					
		
		vfile = tempfile.SpooledTemporaryFile()
		img.save(vfile, format="PNG")
		vfile.seek(0)
		contents = vfile.read()
		vfile.close()
		
		responseData = base64.b64encode(contents)
		
		resp = make_response(responseData)
		resp.statusCode = 200
		return resp
	
	
if __name__ == "__main__":
	app.debug = True
	app.run(host='0.0.0.0')