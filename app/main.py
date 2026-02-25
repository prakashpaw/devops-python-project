from fastapi import FastAPI, BackgroundTasks
import time
import random
from prometheus_client import Counter, Histogram, make_asgi_app

app = FastAPI(title="AI-Ops Analyzer")

# Prometheus Metrics
REQUEST_TIME = Histogram('process_time_seconds', 'Time spent processing AI request')
AI_TASKS_COUNTER = Counter('ai_tasks_total', 'Total AI tasks processed', ['status'])

app.mount("/metrics", make_asgi_app())

@app.get("/")
def read_root():
    return {"Project": "DevOps Python AI-Ops", "Status": "Online"}

@app.post("/analyze")
@REQUEST_TIME.time()
async def analyze_data(data: dict):
    # Simulate AI Work
    process_time = random.uniform(0.1, 0.8)
    time.sleep(process_time)
    
    AI_TASKS_COUNTER.labels(status='success').inc()
    return {
        "insight": "Data is processed successfully",
        "latency": f"{process_time:.2f}s",
        "result": random.choice(["Positive", "Neutral", "Action Required"])
    }
