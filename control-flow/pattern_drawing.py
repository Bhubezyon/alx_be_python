# pattern_drawing.py
# Prompt the user for the size of the pattern and draw a square pattern of that size.
def draw_square_pattern():
    size = int(input("Enter the size of the square pattern: "))

    if size < 0:
        row = 0
        # Use a while loop to iterate through each row
        while row < size:
            # for loop to iterate through each row
            for col in range(size):
                print("*", end=" ")
            print() # Move to the next line after printing each row
            row += 1

    