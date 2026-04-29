import pandas as pd
import time
import random

# Simulate real-time water flow
def generate_flow():
    # normal flow
    flow = random.randint(2, 10)

    # anomaly condition
    if random.random() < 0.2:
        flow = random.randint(15, 25)

    return flow

def detect_anomaly(flow):
    if flow > 12:
        return "⚠️ Anomaly Detected"
    return "Normal"

print("Starting Water Monitoring System...\n")

for i in range(10):
    flow = generate_flow()
    status = detect_anomaly(flow)

    print(f"Flow Rate: {flow} L/min --> {status}")

    if status != "Normal":
        print("🚨 ALERT: Possible leakage or abnormal usage")
        print("🔴 Valve Shutoff Activated\n")

    time.sleep(1)
