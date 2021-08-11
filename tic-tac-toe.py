# #!/usr/bin/env python3

# Created by Malcolm Tompkins
# Created on August 11, 2021
# Runs the tic-tac-toe game


def grid_generation(x, y):
    # Fix this shit
    grid = []
    for row in range(3):
        grid.append([])
        for column in range(3):
            if row == x:
                grid[row].append('x')
            else:
                grid[row].append(' ')
    for row in grid:
        print("|".join(row))
        


def main():
    print("Enter coordinates from 1-3 like so: x, y")
    user_x_value = (input("Your x coordinate: "))
    user_y_value = (input("Your y coordinate: "))
    try:
        x_value = int(user_x_value)
        try:
            y_value = int(user_y_value)
            grid_generation(x_value, y_value)
        except Exception:
            print("{} is not a valid integer or input".format(user_y_value))
    except Exception:
        print("{} is not a valid integer or input".format(user_x_value))
    

if __name__ == "__main__":
    main()
    
