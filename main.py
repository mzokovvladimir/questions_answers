import pygame
from random import randint

pygame.init()
# создание окна игры
clock = pygame.time.Clock()
back: tuple = (215, 215, 215)  # цвет фона (background)
mw = pygame.display.set_mode((500, 500))  # окно программы (main window)
mw.fill(back)
# цвета
BLACK: tuple = (0, 0, 0)
LIGHT_BLUE: tuple = (100, 200, 155)


class TextArea:
    def __init__(self, x: int=0, y: int=0, width: int=10, height: int=10, color=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = color
        # возможные надписи
        self.titles = list()

    # добавить текст в список возможных надписей
    def add_text(self, text: str):
        self.titles.append(text)

    # установить текст
    def set_text(self, number:str=0, fsize: str=12, text_color: tuple=BLACK):
        self.text = self.titles[number]
        self.image = pygame.font.Font(None, fsize).render(self.text, True, text_color)

    # отрисовка прямоугольника с текстом
    def draw(self, shift_x: int=0, shift_y: int=0):
        pygame.draw.rect(mw, self.fill_color, self.rect)
        mw.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))
    

# создание карточек
quest_card = TextArea(120, 100, 290, 70, LIGHT_BLUE)
quest_card.add_text('Вопрос')
quest_card.add_text('Столица Еквадора:')
quest_card.add_text('Что растёт на дубе?')
quest_card.add_text('На каком языке программирования написана эта игра?')
quest_card.add_text('Самая маленькая страна в мире:')

quest_card.set_text(0, 75)

ans_card = TextArea(120, 240, 290, 70, LIGHT_BLUE)
ans_card.add_text('Ответ')
ans_card.add_text('Кито')
ans_card.add_text('Желуди')
ans_card.add_text('Python')
ans_card.add_text('Ватикан')

ans_card.set_text(0, 75)

quest_card.draw(10, 10)
ans_card.draw(10, 10)

while 1:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                num = randint(1, len(quest_card.titles) - 1)
                quest_card.set_text(num, 25)

                quest_card.draw(10, 25)
            if event.key == pygame.K_a:
                num = randint(1, len(ans_card.titles) - 1)
                ans_card.set_text(num, 25)

                ans_card.draw(10, 25)
    clock.tick(40)
