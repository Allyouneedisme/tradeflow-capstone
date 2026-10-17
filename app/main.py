import time

@app.get("/stress")
def stress_test():
    start_time = time.time()
    while time.time() - start_time < 1.0:
        pass
    return {"status": "CPU Stressed!"}
