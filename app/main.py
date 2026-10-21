@app.get("/stress")
def stress_test():
    # This loop runs for 60 seconds, forcing CPU to 100%
    import time
    start_time = time.time()
    while time.time() - start_time < 60.0:
        pass
    return {"status": "CPU Stressed!"}
