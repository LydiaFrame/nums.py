#!/usr/bin/env python3
"""Program to read positive numbers and print sorted data."""

__author__ = "Lydia Frame"
__date__ = "03/01/2025"

def main():
    """Main function to collect numbers and display sorted results."""
    numbers = []
    evens = []
    odds = []

    while True:
        try:
            num = int(input("Num? "))  
            print()
            
            if num < 0:
                break 
            
            numbers.append(num)
            
            if num % 2 == 0:
                evens.append(num)
            else:
                odds.append(num)
                
        except ValueError:
            print("Invalid input! Please enter an integer.")

    print("All (sorted):", sorted(numbers, reverse=True))
    print("Evens:", evens)
    print("Odds:", odds)

if __name__ == "__main__":
    main()