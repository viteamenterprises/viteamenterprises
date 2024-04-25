import os
import time

def main():
    width = 20
    height = 10
    x = width // 2
    y = height // 2
    velocity_x = 1
    velocity_y = 0
    snake = [(x, y)]
    fruit = (width // 2 + 1, height // 2)
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        for i in range(height):
            for j in range(width):
                if (j, i) in snake:
                    print('O', end=' ')
                elif (j, i) == fruit:
                    print('*', end=' ')
                else:
                    print('.', end=' ')
            print()
        new_head = (snake[-1][0] + velocity_x, snake[-1][1] + velocity_y)
        if new_head[0] >= width or new_head[0] < 0 or new_head[1] >= height or new_head[1] < 0 or new_head in snake:
            print("Game over!")
            break
        snake.append(new_head)
        if new_head == fruit:
            fruit = (int(time.time()) % width, int(time.time()) % height)
        else:
            snake.pop(0)
        time.sleep(0.2)

if __name__ == '__main__':
    main()
