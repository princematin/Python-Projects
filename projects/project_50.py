import pygame


class Game:
    def __init__(self) -> None:
        pygame.init()
        self.width= 640
        self.height = 480

        self.size= (self.width, self.height)

        self.screen = pygame.display.set_mode(self.size)

        self.speed = [1, 1]

        self.black = (0, 0, 0)

        self.ball, self.ballrect = self.load_image("sq.png")

    @staticmethod
    def load_image(image_name: str):
        louded_img = pygame.image.load(image_name)
        rect_img = louded_img.get_rect()
        return louded_img, rect_img

    def move_ball(self) -> None:
        result = self.ballrect.move(self.speed)

        if result.left < 0 or result.right > self.width:
            self.speed[0] = -self.speed[0]
        if result.top < 0 or result.bottom > self.height:
            self.speed[1] = -self.speed[1]

        self.ballrect = result

    def draw(self) -> None:
        self.screen.fill(self.black)

        self.screen.blit(self.ball, self.ballrect)

        pygame.display.update()


    @staticmethod
    def handle_events() -> None:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()


import sys
g = Game()
while True:
    g.move_ball()
    g.draw()
    pygame.time.delay(10)
    if g.handle_events():
        sys.exit()
    pygame.event.pump()
