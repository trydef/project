result = []

def divider(a, b):
    if a < b:
        raise ValueError("a менше за b")
    if b > 100:
        raise IndexError("b більше 100")
    return a / b

data = {10: 2, 2: 5, "123": 4, 18: 0, 5: 150, (): 3}

for key in data:
    try:
        res = divider(key, data[key])
        result.append(res)
    except Exception as e:
        print(f"Виняток для пари ({key}: {data[key]}): {type(e).__name__} – {e}")

print("Результат:", result)
