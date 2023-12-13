import os
import uuid
from django.views.decorators.csrf import csrf_exempt  # disable csrftoken
from django.http import JsonResponse  # return JSON file
from django.conf import settings


@csrf_exempt
def upload_file(request):

    # get upload pics
    upload = request.FILES.get('upload')
    # return uid
    uid = ''.join(str(uuid.uuid4()).split('-'))
    # modify pic name
    # asdasd.jpg  fddg.png  ['sasda', 'jpg']
    names = str(upload.name).split('.')
    names[0] = uid
    upload.name = '.'.join(names)
    
    new_path = os.path.join(settings.MEDIA_ROOT, 'upload/', upload.name) 
    # upload pics
    with open(new_path, 'wb+') as file:
        for chunk in upload.chunks():
            file.write(chunk)
    
    # return desired data type
    filename = upload.name
    url = '/media/upload/' + filename
    retdata = { 'url': url, 
                'uploaded': '1',
                'fileName': filename }
    return JsonResponse(retdata)