import time
from django.http import JsonResponse

def api(request):
    time.sleep(1)
    payload = {'message': 'Hello from Crowbotics!'}
    if "task_id" in request.GET:
        payload['task_id'] = request.GET['task_id']
    return JsonResponse(payload)