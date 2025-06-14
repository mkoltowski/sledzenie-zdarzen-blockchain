import time
import os
import uuid
import hashlib
from datetime import datetime, timezone

def main():
    while True:
        device_id = os.getenv("DEVICE_ID", "device-1")
        event_id = str(uuid.uuid4())
        timestamp = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
        salt = os.urandom(8).hex()
        payload = f"{event_id}{timestamp}{salt}"
        hash_value = hashlib.sha256(payload.encode()).hexdigest()
        line = f"{device_id} | {event_id} | {timestamp} | {salt} | {hash_value}\n"
        print(line, end="")
        with open("/data/events.log", "a") as f:
            f.write(line)
        time.sleep(5)

if __name__ == "__main__":
    main()
