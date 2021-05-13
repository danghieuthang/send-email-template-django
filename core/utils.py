import json

def getVariables(request):
    body_unicode = request.body.decode("utf-8")
    try:
        body = json.loads(body_unicode)
        return body
    except:
        return None