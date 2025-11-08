import os
import datetime
import subprocess

LOG_FILE = "pipeline_log.txt"

def log_message(message):
    """Helper to write messages to the log file"""
    with open(LOG_FILE, "a", encoding="utf-8") as log:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log.write(f"[{timestamp}] {message}\n")
    print(message)

# --- Run the full pipeline ---
steps = [
    "etl/fetch.py",
    "etl/transform.py",
    "etl/load.py",
    "visualize.py"
]

if __name__ == "__main__":
    log_message("Starting full ETL pipeline...\n")

    for step in steps:
        log_message(f"Running {step}...")
        try:
            subprocess.run(["python", step], check=True)
            log_message(f"{step} completed successfully.\n")
        except subprocess.CalledProcessError:
            log_message(f"{step} failed.\n")

    log_message("Pipeline completed successfully.\n")
