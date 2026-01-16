import constants, pygame

class Display(pygame.sprite.Sprite):
    def __init__(self, score):
        super().__init__(self.containers)
        self.score = 0
        self.position = pygame.Vector2(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2)
        self.height = constants.SCREEN_HEIGHT/12
        self.width = constants.SCREEN_WIDTH/12    
        self.font = pygame.font.Font(None, 70)
    
    def draw(self, screen):
        pygame.draw.rect(screen, "white", (0,0,self.width, self.height), constants.LINE_WIDTH)

        text_surf = self.font.render(str(self.score), True, "white")
        text_rect = text_surf.get_rect(center=pygame.Rect(20,30,20,20).center)

        screen.blit(text_surf, text_rect)