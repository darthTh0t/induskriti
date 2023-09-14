from flask import Blueprint, flash ,redirect, render_template, request, url_for
from app.blueprints.admin.models import ImageHash
from app.blueprints.admin.firebase import File

#calling the image url_list

gallery_page = Blueprint('gallery', __name__, template_folder='templates/', static_folder='static/')

@gallery_page.route('/')
def index():
	image_urls = File().image_download()
	return render_template('gallery.html', image_urls=image_urls)


#@gallery_page.route('/get_image')
#def get_image():
#	index = request.args.get("index")
#	try:
#		index = int(index)
#		if 0 <= index < len(image_urls):
#			image_url = image_urls[index]
#			response = requests.get(image_url)
#			if response.status_code == 200:
#				headers = {'Content-Type': response.headers['Content-Type']}
#				return Response(response.content, headers=headers)
#			else:
#				return 'Image Not Found', 404
#		else:
#			return 'Invalid Index', 400
#	except ValueError:
#		return 'Invalid Index', 400