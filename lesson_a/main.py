from flask import Response

def main(request):
    try:
        print(f"[{__name__}] Started...")
        # get request data
        if request.args:
            data = request.args  # data is in query string params
        else:
            data = request.json  # data is in body
        
        print(f"[{__name__}] Data: {data}")

        return Response(response=data, status=200, mimetype="application/json")        

    except Exception as e:
        print(f"[{__name__}] Error: {e}")