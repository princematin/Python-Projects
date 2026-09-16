import pygame


pygame.init()

screen = pygame.display.set_mode((300, 300))

white = (255, 255, 255)
screen.fill(white)

pen_size = 1

pen_color = (0, 0, 0)

while True:
    menu = input()

    if menu.startswith("change size"):
        result = menu.replace("change size", "")
        result = result.split()
        result = list(map(int, result))
        pen_size = result[0]

    elif menu.startswith("change color"):
        result = menu.replace("change color", "")
        result = result.split()
        result = list(map(int, result))
        pen_color = (result[0], result[1], result[2])

    elif menu.startswith("draw line"):
        result = menu.replace("draw line", "")
        result = result.split()
        result = list(map(int, result))
        pygame.draw.line(screen, pen_color, (result[0], result[1]), (result[2], result[3]), pen_size)

    elif menu.startswith("draw circle"):
        result = menu.replace("draw circle", "")
        result = result.split()
        result = list(map(int, result))
        pygame.draw.circle(screen, pen_color, (result[0], result[1]), result[2], pen_size)

    elif menu.startswith("draw polygon"):
        result = menu.replace("draw polygon", "")
        result = result.split()
        result = list(map(int, result))
        nums = list()
        for i in range(0, len(result), 2):
            nums_in = (result[i], result[i + 1])
            nums.append(nums_in)
        pygame.draw.polygon(screen, pen_color,nums, pen_size)

    elif menu.startswith("end drawing"):
        pygame.image.save(screen, "draw.png")
        pygame.quit()
        break