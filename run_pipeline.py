import os
import subprocess
from datetime import datetime

# --- Create logs folder if it doesn't exist ---
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

# --- Unique log file per run ---
LOG_FILE = os.path.join(LOG_DIR, f"pipeline_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt")


def log_message(message):
    """Helper to write messages to the log file"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a", encoding="utf-8") as log:
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
