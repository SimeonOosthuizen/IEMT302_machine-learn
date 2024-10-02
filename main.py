#!/usr/bin/env python3

data = [(1, 'A'), (2, 'A'), (3, 'A'), (6, 'B'), (7, 'B'), (8, 'B')]

threshold = sum(num for num, label in data if label == 'A') / len([label for _, label in data if label == 'A'])
threshold += sum(num for num, label in data if label == 'B') / len([label for _, label in data if label == 'B'])
threshold /= 2  

if __name__ == "__main__":
    inputnr = float(input("Enter a number: "))
    
    if inputnr < threshold:
        print("Class A")
    else:
        print("Class B")
