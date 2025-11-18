import pygame
import random

#setup
width = 720
height = 480
pygame.init()
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
running = True
difficulty = 10

# Game variables
snake_pos = [100, 50]
snake_body = [[100, 50], [100-10, 50], [100-(2*10), 50]]

food_pos = [random.randrange(1, (width//10)) * 10, random.randrange(1, (height//10)) * 10]
food_spawn = True

direction = 'RIGHT'

score = 0

# Game Over
def game_over():
    screen.fill("black")
    font = pygame.font.SysFont("Arial", 30) 
    text = font.render("You lost. HA HA LOSER", True, (255, 255, 255))
    textBox = text.get_rect()
    textBox.midtop = (300, 200)
    screen.blit(text, textBox)
    scoreText = font.render('Score : ' + str(score), True, "red")
    scoreBox = scoreText.get_rect()
    scoreBox.midtop = (100, 100)
    screen.blit(scoreText, scoreBox)
    pygame.display.update()




while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                #print("up")
                direction = 'UP'
            if event.key == pygame.K_DOWN:
                #print("down")
                direction = 'DOWN'
            if event.key == pygame.K_LEFT:
                #print("left")
                direction = 'LEFT'
            if event.key == pygame.K_RIGHT:
                #print("right")
                direction = 'RIGHT'

    # Moving the snake
    if direction == 'UP':
        snake_pos[1] -= 10
    if direction == 'DOWN':
        snake_pos[1] += 10
    if direction == 'LEFT':
        snake_pos[0] -= 10
    if direction == 'RIGHT':
        snake_pos[0] += 10

    # Snake body growing mechanism
    snake_body.insert(0, list(snake_pos))
    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        score += 1
        food_spawn = False
        difficulty +=5
    else:
        snake_body.pop()

    # Spawning food on the screen
    if not food_spawn:
        food_pos = [random.randrange(1, width//10), random.randrange(1, height//10)]
    food_spawn = True

    # GFX
    screen.fill("black")
    for pos in snake_body:
        pygame.draw.rect(screen, "green", pygame.Rect(pos[0], pos[1], 10, 10))

    # Snake food
    pygame.draw.rect(screen, "white", pygame.Rect(food_pos[0], food_pos[1], 10, 10))

    # Game Over conditions
    # Getting out of bounds
    if snake_pos[0] < 0 or snake_pos[0] > width-10:
        game_over()
    if snake_pos[1] < 0 or snake_pos[1] > height-10:
        game_over()
    # Touching the snake body
    for block in snake_body[1:]:
        if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
            game_over()

    #show_score(1, white, 'consolas', 20)
    font = pygame.font.SysFont("Arial", 30) 
    scoreText = font.render('Score : ' + str(score), True, "red")
    scoreBox = scoreText.get_rect()
    screen.blit(scoreText, scoreBox)
    pygame.display.update()

    # Refresh rate
    clock.tick(difficulty)

    # flip() the display to put your work on screen
    pygame.display.flip()


pygame.quit()
