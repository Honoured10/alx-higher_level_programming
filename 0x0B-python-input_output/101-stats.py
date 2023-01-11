#!/usr/bin/python3
import sys
from collections import defaultdict

status_codes = defaultdict(int)
total_size = 0
line_count = 0

try:
    for line in sys.stdin:
        line_count += 1
        try:
            _, _, _, status_code, file_size = line.split(" ")
            status_codes[status_code] += 1
            total_size += int(file_size)
        except ValueError:
            print("Invalid input format")
            continue
        if line_count % 10 == 0:
            print("Total file size: ", total_size)
            for code in sorted(status_codes.keys()):
                print(f"{code}: {status_codes[code]}")
except KeyboardInterrupt:
    print("\nFinal statistics:")
    print("Total file size: ", total_size)
    for code in sorted(status_codes.keys()):
        print(f"{code}: {status_codes[code]}")
