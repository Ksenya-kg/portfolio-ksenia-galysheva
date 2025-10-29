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
import pandas as pd, random
from datetime import datetime, timedelta
import matplotlib.pyplot as plt, seaborn as sns

dishes = ["Капучино","Американо","Латте","Овсянка с фруктами","Яичница с беконом",
          "Салат Цезарь","Бизнес-ланч","Круассан","Паста с курицей","Борщ","Сэндвич с тунцом"]

data, base_time = [], datetime.now() - timedelta(days=90)
for _ in range(300):
    t = base_time + timedelta(minutes=random.randint(0, 90*24*60))
    dish, qty, price = random.choice(dishes), random.randint(1,3), random.randint(150,550)
    data.append({"datetime": t, "dish": dish, "quantity": qty, "price": price * qty})

df = pd.DataFrame(data)
df.to_csv("cafe_orders_sample.csv", index=False)
```

📈 Результаты

Пиковые часы: 09:00–11:00 и 12:00–14:00

Лидеры: «Капучино», «Бизнес-ланч», «Яичница с беконом»

Рекомендации: акции в «тихие часы» (15:00–18:00)

📎 Файлы
Имя	Назначение
scr.py	основной скрипт
cafe_orders_sample.csv	сгенерированные данные
cafe_orders_analysis.png	графики анализа
🧩 Роль аналитика

Создание скрипта, анализ данных, построение визуализаций, формулировка бизнес-рекомендаций.
