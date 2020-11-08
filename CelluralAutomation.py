import pygame

ScreenResolution = (400, 400)
TimeStep = 100

pygame.init()
Screen = pygame.display.set_mode(ScreenResolution)

def drawGrid():
    blockSize = 20
    for x in range(ScreenResolution[0]):
        for y in range(ScreenResolution[1]):
            Rect = pygame.Rect(x*blockSize, y*blockSize, blockSize, blockSize)
            pygame.draw.rect(Screen, (0, 0, 0), Rect, 1)

NextMove = pygame.time.get_ticks() + TimeStep
GameRunning = True

while GameRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GameRunning = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                SpacePressed = True
                while SpacePressed:
                    for event2 in pygame.event.get():
                        if event2.type == pygame.KEYDOWN:
                            if event2.key == pygame.K_SPACE:
                                SpacePressed = False
    
    CurrentTime = pygame.time.get_ticks()

    if CurrentTime >= NextMove:
        Screen.fill((200, 200, 200))
        drawGrid()
        pygame.display.update()
        NextMove = pygame.time.get_ticks() + TimeStep
