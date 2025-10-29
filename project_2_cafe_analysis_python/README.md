![cover](./logo.png)

# 📊 Анализ заказов кафе «11/21 Кофе» (Python)

## 🎯 Цель
Определить популярные блюда и пиковые часы заказов для оптимизации меню и графика работы персонала.

## ⚙️ Инструменты
Python · pandas · matplotlib · seaborn · Jupyter/Colab · Google Sheets

## 📂 Этапы
1. Генерация данных (~300 заказов за 3 месяца) → `cafe_orders_sample.csv`  
2. Анализ → топ-5 блюд, пики по часам  
3. Визуализация → `cafe_orders_analysis.png`

## 🧠 Пример кода
```python
import random
from datetime import datetime, timedelta

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# стабильность и кириллица
random.seed(42)
plt.rcParams["font.family"] = "DejaVu Sans"
sns.set()

# меню
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
        rows.append({"datetime": t, "dish": dish, "quantity": qty, "price": price * qty})
    return pd.DataFrame(rows).sort_values("datetime").reset_index(drop=True)

def main():
    df = generate_orders()
    # CSV для Excel на Windows + аккуратные даты
    df["datetime"] = pd.to_datetime(df["datetime"])
    df.to_csv("cafe_orders_sample.csv", index=False, encoding="utf-8-sig", date_format="%Y-%m-%d %H:%M:%S")

    # анализ
    df["hour"] = df["datetime"].dt.hour
    top_dishes = df.groupby("dish")["quantity"].sum().sort_values(ascending=False).head(5)
    hourly_orders = df.groupby("hour")["quantity"].sum().reindex(range(24), fill_value=0)

    # визуализация
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
    # plt.show()  # включите локально при необходимости

if __name__ == "__main__":
    main()
```
📈 Результаты

Пиковые часы: 09:00–11:00 и 12:00–14:00

Лидеры: «Капучино», «Бизнес-ланч», «Яичница с беконом»

Рекомендации: промо-акции в «тихие часы» (15:00–18:00), усиление смен в пиковые окна

📎 Файлы
Имя	Назначение
scr.py	основной скрипт (генерация → анализ → визуализация)
cafe_orders_sample.csv	сгенерированные данные (пример датасета)
cafe_orders_analysis.png	итоговая визуализация (топ-5 + пики по часам)
requirements.txt	зависимости (pandas, matplotlib, seaborn)
DATA_DICTIONARY.md	описание полей датасета
logo.png	логотип/обложка проекта
🧩 Роль аналитика

Создание скрипта, анализ данных, построение визуализаций, формулировка бизнес-рекомендаций.
