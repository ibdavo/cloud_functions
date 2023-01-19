from flask import Response

def main_f2(request):
    print(f"[{__name__}] Received request: {request.data}")

    return Response("OK", status=200)