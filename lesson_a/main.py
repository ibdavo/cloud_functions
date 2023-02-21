from flask import Response
import os

def main(request):
    try:
        print(f"[{__name__}] Started...")
        # get request data
        request_json = request.get_json()
        if request.args and 'message' in request.args:
            data= request.args.get('message')
        elif request_json and 'message' in request_json:
            data= request_json['message']
        else:
            data= f'Hello World!'
        # debug = os.environ.get("DEBUG")
        # print(f"Debug variable: {debug}")
        print(f"[{__name__}] Finished...")
        return Response(response=data, status=200, mimetype="application/json")        

    except Exception as e:
        print(f"[{__name__}] Error: {e}")