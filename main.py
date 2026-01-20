import pygame
import random
pygame.init()
tank = ['DVA','Doomfist','Hazard','Junker Queen','Mauga','Orisa','Ramattra','Reinhardt','Roadhog','Sigma','Winston','Wrecking Ball','Zarya']
dps = ["Ashe","Bastion","Cassidy","Freja","Echo","Genji","Hanzo","Junkrat","Mei","Pharah","Reaper","Sojourn","Soldier","Sombra","Symmetra","Torbjorn","Tracer","Venture","Widowmaker","Vendetta"]
support = ["Ana","Baptiste","Brigitte","Illari","Juno","Kiriko","Lifeweaver","Lucio","Mercy","Moira","Zenyatta","Wuyang"]
all = tank + dps + support
small_font = pygame.font.SysFont("Arial", 14)
background_color = (180,180,180)
button_color = (120,120,120)
button_light = (255,255,255)
button_dark = (50,50,50)
screen = pygame.display.set_mode((300,150))
pygame.display.set_caption("Overwatch Picker")
screen.fill(background_color)
text = small_font.render("QUIT", True, button_color)
text2 = small_font.render("DPS", True, button_color)
text3 = small_font.render("TANK", True, button_color)
text4 = small_font.render("SUPP", True, button_color)
text5 = small_font.render("ALL", True, button_color)
width_1 = 250
height_1 = 10
output_list = random.sample(all, 3)
number_1 = small_font.render(str(output_list[0]), True, button_color)
number_2 = small_font.render(str(output_list[1]), True, button_color)
number_3 = small_font.render(str(output_list[2]), True, button_color)
output1 = str(output_list[0])
output2 = str(output_list[1])
output3 = str(output_list[2])
img1 = pygame.image.load("OW_pictures/"+(output1)+".png")
img2 = pygame.image.load("OW_pictures/"+(output2)+".png")
img3 = pygame.image.load("OW_pictures/"+(output3)+".png")
width = img1.get_width()
height = img1.get_height()
running = True
while running:
    mouse_pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if width_1 <= mouse_pos[0] <= width_1+50 and height_1 <= mouse_pos[1] <= height_1+20:
                pygame.quit()
            if width_1-36 <= mouse_pos[0] <= width_1 and height_1 <= mouse_pos[1] <= height_1+20:
                output_list = random.sample(dps, 3)
                pygame.draw.rect(screen, background_color, [0, 0, 300, 150])
                number_1 = small_font.render(str(output_list[0]), True, button_color)
                number_2 = small_font.render(str(output_list[1]), True, button_color)
                number_3 = small_font.render(str(output_list[2]), True, button_color)
                output1 = str(output_list[0])
                output2 = str(output_list[1])
                output3 = str(output_list[2])
                img1 = pygame.image.load("OW_pictures/" + (output1) + ".png")
                img2 = pygame.image.load("OW_pictures/" + (output2) + ".png")
                img3 = pygame.image.load("OW_pictures/" + (output3) + ".png")
                screen.blit(number_1, (20, 125))
                screen.blit(number_2, (120, 125))
                screen.blit(number_3, (220, 125))
            if width_1-80 <= mouse_pos[0] <= width_1-40 and height_1 <= mouse_pos[1] <= height_1+20:
                output_list = random.sample(tank, 3)
                pygame.draw.rect(screen, background_color, [0, 0, 300, 150])
                number_1 = small_font.render(str(output_list[0]), True, button_color)
                number_2 = small_font.render(str(output_list[1]), True, button_color)
                number_3 = small_font.render(str(output_list[2]), True, button_color)
                output1 = str(output_list[0])
                output2 = str(output_list[1])
                output3 = str(output_list[2])
                img1 = pygame.image.load("OW_pictures/" + (output1) + ".png")
                img2 = pygame.image.load("OW_pictures/" + (output2) + ".png")
                img3 = pygame.image.load("OW_pictures/" + (output3) + ".png")
                screen.blit(number_1, (20, 125))
                screen.blit(number_2, (120, 125))
                screen.blit(number_3, (220, 125))
            if width_1-120 <= mouse_pos[0] <= width_1-84 and height_1 <= mouse_pos[1] <= height_1+20:
                output_list = random.sample(support, 3)
                pygame.draw.rect(screen, background_color, [0, 0, 300, 150])
                number_1 = small_font.render(str(output_list[0]), True, button_color)
                number_2 = small_font.render(str(output_list[1]), True, button_color)
                number_3 = small_font.render(str(output_list[2]), True, button_color)
                output1 = str(output_list[0])
                output2 = str(output_list[1])
                output3 = str(output_list[2])
                img1 = pygame.image.load("OW_pictures/" + (output1) + ".png")
                img2 = pygame.image.load("OW_pictures/" + (output2) + ".png")
                img3 = pygame.image.load("OW_pictures/" + (output3) + ".png")
                screen.blit(number_1, (20, 125))
                screen.blit(number_2, (120, 125))
                screen.blit(number_3, (220, 125))
            if width_1-160 <= mouse_pos[0] <= width_1-124 and height_1 <= mouse_pos[1] <= height_1+20:
                output_list = random.sample(all, 3)
                pygame.draw.rect(screen, background_color, [0, 0, 300, 150])
                number_1 = small_font.render(str(output_list[0]), True, button_color)
                number_2 = small_font.render(str(output_list[1]), True, button_color)
                number_3 = small_font.render(str(output_list[2]), True, button_color)
                output1 = str(output_list[0])
                output2 = str(output_list[1])
                output3 = str(output_list[2])
                img1 = pygame.image.load("OW_pictures/" + (output1) + ".png")
                img2 = pygame.image.load("OW_pictures/" + (output2) + ".png")
                img3 = pygame.image.load("OW_pictures/" + (output3) + ".png")
                screen.blit(number_1, (20, 125))
                screen.blit(number_2, (120, 125))
                screen.blit(number_3, (220, 125))
    if width_1 <= mouse_pos[0] <= width_1+36 and height_1 <= mouse_pos[1] <= height_1+20:
        pygame.draw.rect(screen, button_light, [width_1, height_1, 36,20])
    else:
        pygame.draw.rect(screen, button_dark, [width_1, height_1, 36,20])
    if width_1-36 <= mouse_pos[0] <= width_1 and height_1 <= mouse_pos[1] <= height_1+20:
        pygame.draw.rect(screen, button_light, [width_1-40, height_1, 36,20])
    else:
        pygame.draw.rect(screen, button_dark, [width_1-40, height_1, 36, 20])
    if width_1-80 <= mouse_pos[0] <= width_1-40 and height_1 <= mouse_pos[1] <= height_1+20:
        pygame.draw.rect(screen, button_light, [width_1-80, height_1, 36,20])
    else:
        pygame.draw.rect(screen, button_dark, [width_1-80, height_1, 36, 20])
    if width_1-120 <= mouse_pos[0] <= width_1-84 and height_1 <= mouse_pos[1] <= height_1+20:
        pygame.draw.rect(screen, button_light, [width_1-120, height_1, 36,20])
    else:
        pygame.draw.rect(screen, button_dark, [width_1-120, height_1, 36, 20])
    if width_1-160 <= mouse_pos[0] <= width_1-124 and height_1 <= mouse_pos[1] <= height_1+20:
        pygame.draw.rect(screen, button_light, [width_1-160, height_1, 36,20])
    else:
        pygame.draw.rect(screen, button_dark, [width_1-160, height_1, 36, 20])
    img1 = pygame.transform.scale(img1, (int(width / 4), int(height / 4)))
    img2 = pygame.transform.scale(img2, (int(width / 4), int(height / 4)))
    img3 = pygame.transform.scale(img3, (int(width / 4), int(height / 4)))
    screen.blit(img1, (20, 60))
    screen.blit(img2, (120, 60))
    screen.blit(img3, (220, 60))
    screen.blit(text, (width_1+4, height_1))
    screen.blit(text2, (width_1-34, height_1))
    screen.blit(text3, (width_1-78, height_1))
    screen.blit(text4, (width_1 - 118, height_1))
    screen.blit(text5, (width_1 - 153, height_1))
    pygame.display.flip()