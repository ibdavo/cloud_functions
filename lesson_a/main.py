try:
    print(f"[{__name__}] Start")
    print(1/0)
except Exception as e:
    print(f"[{__name__}] Error: {e}")