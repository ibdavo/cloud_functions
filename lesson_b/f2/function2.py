import base64
from flask import Response
import json

def main_f2(request):
    try:
        print(f"[{__name__}] Received request: {request.data}")
     
        # get request data
        if request.args:
            data = request.args # data is in query string params
        else:
            data = request.json # data is in body

        # check to see if request coming from pub/sub
        if 'message' in data.keys():
            # decode data and update data dict to schema
            decoded_data = json.loads(base64.b64decode(data['message']['data']).decode('utf-8'))
            print(f"[{__name__}] Decoded data: {decoded_data}")

    except Exception as e:
        print(f"[{__name__}] Exception: {e}")
        raise e

    finally:
        return Response("OK", status=200)
