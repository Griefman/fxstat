"""
Time;Type;Volume;Symbol;Price;S/L;T/P;Time;Price;Commission;Swap;Profit;Comment
"""
file = 'Y:\YandexDisk\GitHub\/fxstat\prado\history_do_12022023.txt'

with open(file, 'r', encoding='utf-8') as f:
    for line in f:
        if 'cancelled' not in line:
            print(line)