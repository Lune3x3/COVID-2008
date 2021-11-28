import pygame, pickle, os
from pygame import *

pygame.init()

x = -2738.7646
y = 977.266

background_image = pygame.image.load('maps_shot.png')
IMAGE_SMALL = pygame.transform.scale(background_image, (1280, 1024))

menu_image = pygame.image.load('covid.jpg')
new_menu = pygame.transform.scale(menu_image, (1280, 1024))

sun_image = pygame.image.load('sun.png')
moon_image = pygame.image.load('moon.png')
sundown_image = pygame.image.load('sundown.png')
daytime = [sun_image, moon_image, sundown_image]
icon = daytime[0]

csign = pygame.image.load('csign.png')
c_sign = pygame.transform.scale(csign, (320, 170))

cell = pygame.image.load('cell.png')
c_cell = pygame.transform.scale(cell, (160, 160))

q_1 = ['Are you currently experiencing any of these issues?', 
'- Severe difficulty breathing', 
'- Severe chest pain',
'- Feeling confused or unsure of where you are',
'- Losing consciousness']

q_2 = ['Are you currently experiencing any of these symptoms?',
'- Fever and/or chills',
'- Cough or barking cough (croup)',
'- Shortness of breath',
'- Decrease or loss of taste or smell',
'- Muscle aches/joint pain',
'- Extreme tiredness']

q_3 = ['In the last 10 days, have you been identified as a "close contact"',
'of someone who currently has COVID-19?', 
'If public health has advised you that you do not need to self-isolate, select "No." ']

q_4 = ['In the last 10 days, have you received a COVID Alert',
'exposure notification on your cell phone?',
'If you already went for a PCR test and got a negative result, select "No."']

q_5 = ['Have you been in close physical contact',
'(while not wearing the appropriate personal protective equipment)',
"with someone you don't live with who either:",
'is sick with symptoms associated with COVID-19 in the last 10 days?',
'or',
'returned from outside of Canada in the last 14 days?']

q_6 = ['In the last 14 days, have you travelled outside of Canada?',
'If exempt from federal quarantine requirements',
'(for example, you are fully vaccinated and have met the specific conditions,',
'or an essential worker who crosses the Canada-US border regularly for work),',
'select "No."']

all_q = [q_1, q_2, q_3, q_4, q_5 ,q_6]

end_statements = ['Call 911 or go directly to your nearest emergency department.',
'Based on your answers, We recommend that you get a COVID-19 test and self-isolate',
'Based on your answers, We recommend that you get a COVID-19 test and self-isolate',
'Based on your answers, We recommend that you get a COVID-19 test and self-isolate',
'You do not need to self-isolate or get tested. However, we recommend that you pay extra attention to your health.',
'You must stay at home for 14 days immediately after your return to Canada.',
'Based on your answers, you do not need to self-isolate or get tested. If you feel sick or not well, please stay home.']

BGCOLOR = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (20, 100, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (92, 92, 92)
YELLOW = (255, 255, 0)

f = 0
aph = 0
q = 0
FPS = 45
# buttons 
replay_button = pygame.Rect(490, 400, 300, 100)
main_menu = pygame.Rect(15, 15, 100, 50)
yes = pygame.Rect(400, 800, 200, 100)
no = pygame.Rect(700, 800, 200, 100)
simulation_button = pygame.Rect(470, 400, 340, 100)
self_assessment = pygame.Rect(470, 550, 340, 100)
previous = pygame.Rect(125, 145, 170, 30)

day_night = pygame.Rect(0, 0, 1280, 1024)

font = pygame.font.SysFont('Ariel', 30, False, False)
font_two = pygame.font.SysFont('Times New Roman', 50, False, False)
font_three = pygame.font.SysFont('Times New Roman', 30, False, False)

screen = pygame.display.set_mode((1280, 1024))
pygame.display.update()
clock = pygame.time.Clock()

def grab(filename):
    return pickle.load(open(f'{os.getcwd()}\\spreadData\\{filename}', 'rb'))

files = os.listdir(os.getcwd() + '\\spreadData')


menu = 0
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == MOUSEBUTTONDOWN:
            if menu == 0:
                if simulation_button.collidepoint(event.pos):
                    menu = 1
                elif self_assessment.collidepoint(event.pos):
                    menu = 3
            elif menu == 1:
                if main_menu.collidepoint(event.pos):
                    menu = 0
                    f = 0
                    aph = 0
            elif menu == 2:
                if replay_button.collidepoint(event.pos):
                    menu = 1
            elif menu == 3:
                if yes.collidepoint(event.pos):
                    if yes.collidepoint(event.pos):
                        menu = 4

                elif no.collidepoint(event.pos):
                    if q == 5:
                        menu = 4
                    q += 1
                    
                elif previous.collidepoint(event.pos) and q != 0:
                    q -= 1
                        
            elif menu == 4:
                if main_menu.collidepoint(event.pos):
                    menu = 0
                    q = 0

    screen.fill(BGCOLOR)
    
    if menu == 0:
        #menu screen
        screen.blit(new_menu, [0, 0])
        pygame.draw.rect(screen, GREY, simulation_button)
        replay_m = font_two.render("Simulation", True, WHITE)
        screen.blit(replay_m, [530, 420])
        if simulation_button.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, WHITE, simulation_button, 5)
        
        pygame.draw.rect(screen, GREY, self_assessment)
        assessment_m = font_two.render("Self Assessment", True, WHITE)
        screen.blit(assessment_m, [477, 570])
        
        if self_assessment.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, WHITE, self_assessment, 5)
        
    elif menu == 1:
        screen.blit(IMAGE_SMALL, [0, 0])
        data = grab(files[f])
        infected, uninfected = 0, 0
        
        if f != 8786:
            for i in data.keys():
                color = RED if data[i][0] else BLUE
                infected += data[i][0]
                uninfected += not(data[i][0])
                pygame.draw.circle(screen, color, [(data[i][2] - 40.193113) * x, (data[i][1] - 115.796458) * y], 2)
            
            f += 1
        else:
            menu = 2
            f = 0

        t = files[f].split(' ')
        t = f'{t[0]} {t[1]}:{t[2][:2]} ----- {uninfected} uninfected ----- {infected} infected'
        time_of_day = int(t[11:13])
        
        s = pygame.Surface((1280, 1024))
        if 17 <= time_of_day <= 20 and aph != 180:
            aph += 1
        elif 5 <= time_of_day <= 8 and aph != 0:
            aph -= 1

        s.set_alpha(aph)
        s.fill((0, 0, 0))
        screen.blit(s, (0, 0))

        pygame.draw.rect(screen, WHITE, [400, 0, 560, 40])
        time = font.render(t, True, BLACK)
        screen.blit(time, [410, 10])
        
        pygame.draw.rect(screen, GREY, main_menu)
        if main_menu.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, WHITE, main_menu, 5)
            
        mb = font.render("Menu", True, WHITE)
        screen.blit(mb, [37, 32])
        
        if time_of_day == 5 or time_of_day == 17:
            icon = daytime[2]
        elif time_of_day == 20:
            icon = daytime[1]
        elif time_of_day == 8:
            icon = daytime[0]
        
        screen.blit(icon, [0, 60])
        
    elif menu == 2:
        pygame.draw.rect(screen, GREY, replay_button)
        replay_m = font_two.render("Replay", True, WHITE)
        screen.blit(replay_m, [570, 420])
        f = 0
        aph = 0
    
    elif menu == 3:
        pygame.draw.rect(screen, YELLOW, [0, 0, 1280, 100])
        assess_title = font_two.render("COVID-19 Self Assessment", True, BLACK)
        screen.blit(assess_title, [350, 20])
        
        screen.blit(c_sign, [100, 600])
        screen.blit(c_cell, [1000, 300])
        
        if previous.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.line(screen, BLUE, [125, 175], [295, 175], 2)
            
        prev = font_three.render('Previous page', True, BLUE)
        screen.blit(prev, [125, 140])
        
        y_offset = 0
        for i in range(len(all_q[q])):
            questions = font_three.render(all_q[q][i], True, BLACK)
            screen.blit(questions, [20, 200 + y_offset])
            y_offset += 50
        
        pygame.draw.rect(screen, BLUE, yes)
        pygame.draw.rect(screen, BLUE, no)
        yes_b = font_two.render("Yes", True, BLACK)
        no_b = font_two.render("No", True, BLACK)
        screen.blit(yes_b, [yes.x + 55, yes.y + 20])
        screen.blit(no_b, [no.x + 65, no.y + 20])
        
    elif menu == 4:
        end_m = font.render(end_statements[q], True, BLACK)
        end_rect = end_m.get_rect(center = (1280 / 2, 400))
        screen.blit(end_m, [end_rect.x, end_rect.y])
        
        pygame.draw.rect(screen, GREY, main_menu)
        if main_menu.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, BLACK, main_menu, 5)
            
        mb = font_three.render("Menu", True, WHITE)
        screen.blit(mb, [30, 25])
        
    pygame.display.flip()

pygame.quit()
