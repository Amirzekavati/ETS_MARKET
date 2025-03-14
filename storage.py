import pandas as pd
import os
import config

def save_to_csv(data, filename=config.OUTPUT_FILE):
    """Saves scaped data to CSV file."""
    column_titles = [
        "تاریخ", "نوع ارز", "کد ارز", "خرید(اسکناس)", "فروش(اسکناس)*", "خرید(حواله)", "فروش(حواله)**", "خرید حواله کالاهای اساسی و ضروری", "فروش حواله کالاهای اساسی و ضروری***", "میانگین موزون****"
    ]
    os.makedirs("data", exist_ok=True)
    df = pd.DataFrame(data, columns=column_titles)
    df.to_csv(filename, encoding="utf-8-sig", index=False, mode='w', header=True)
    print(f"✅ Data saved to {filename}")
    