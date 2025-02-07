import json
import random
import string

# Генерация случайного ID
random_id = ''.join(random.choices(string.ascii_letters + string.digits, k=12))

data = {
    "id": random_id,
    "level": 1,
    "type": 0
}

with open("data.json", "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

