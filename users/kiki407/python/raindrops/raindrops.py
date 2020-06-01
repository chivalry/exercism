def convert(number):
    res = f"{'Pling' if not number % 3 else ''}{'Plang' if not number % 5 else ''}{'Plong' if not number % 7 else ''}"
    return res if res else f"{number}"
