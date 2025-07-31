import sys
from robust_division_calculator import safe_devide
def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")
        sys.exit(1)

        numerator = sys.argv[1]
        denominator = sys.argv[2]   

        result = safe_devide(numerator, denominator)
        print(f"Result: {result}")

        if __name__ == "__main__":
            main()
            