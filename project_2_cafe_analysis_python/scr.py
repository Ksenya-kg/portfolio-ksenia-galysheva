import random
from datetime import datetime, timedelta

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --- стабильность и кириллица ---
random.seed(42)
plt.rcParams["font.family"] = "DejaVu Sans"
sns.set()

# --- генерация данных ---
dishes = [
    "Капучино", "Американо", "Латте", "Овсянка с фруктами",
    "Яичница с беконом", "Салат Цезарь", "Бизнес-ланч",
    "Круассан", "Паста с курицей", "Борщ", "Сэндвич с тунцом"
]

def generate_orders(n=300, days=90):
    base_time = datetime.now() - timedelta(days=days)
    rows = []
    for _ in range(n):
        t = base_time + timedelta(minutes=random.randint(0, days * 24 * 60))
        dish = random.choice(dishes)
        qty = random.randint(1, 3)
        price = random.randint(150, 550)
        rows.append({
            "datetime": t,
            "dish": dish,
            "quantity": qty,
            "price": price * qty
        })
    df_ = pd.DataFrame(rows).sort_values("datetime").reset_index(drop=True)
    return df_

def main():
    df = generate_orders()

    # CSV для Excel на Windows (BOM) + аккуратные даты
    df["datetime"] = pd.to_datetime(df["datetime"])
    df.to_csv("cafe_orders_sample.csv", index=False, encoding="utf-8-sig", date_format="%Y-%m-%d %H:%M:%S")

    # --- анализ ---
    df["hour"] = df["datetime"].dt.hour
    top_dishes = (
        df.groupby("dish")["quantity"]
          .sum()
          .sort_values(ascending=False)
          .head(5)
    )
    hourly_orders = df.groupby("hour")["quantity"].sum().reindex(range(24), fill_value=0)

    # --- визуализация ---
    plt.figure(figsize=(14, 6))

    plt.subplot(1, 2, 1)
    sns.barplot(x=top_dishes.values, y=top_dishes.index)
    plt.title("Топ-5 популярных блюд")
    plt.xlabel("Кол-во заказов")
    plt.ylabel("Блюдо")

    plt.subplot(1, 2, 2)
    sns.lineplot(x=hourly_orders.index, y=hourly_orders.values, marker="o")
    plt.title("Распределение заказов по времени суток")
    plt.xlabel("Час дня")
    plt.ylabel("Кол-во заказов")
    plt.xticks(range(0, 24))

    plt.tight_layout()
    plt.savefig("cafe_orders_analysis.png", dpi=150, bbox_inches="tight")
    # plt.show()  # включи локально, если хочешь окно с графиками

if __name__ == "__main__":
    main()
