import pandas as pd
import os
import config

def save_to_csv(data, filename=config.OUTPUT_FILE):
    """Saves scaped data to CSV file."""
    os.makedirs("data", exist_ok=True)
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False, mode='a', header=not os.path.exists(filename))
    print(f"✅ Data saved to {filename}")
