import pygame
import os
from random import choice, randint

def modulj(a):
    return (a*-1 if a<0 else a)

pygame.init()
pygame.mixer.init()
pygame.font.init()

with open("config.txt", "r", encoding="utf-8") as config:
    vinyl_name=config.readline().replace("\n", "").replace("CurrentAlderVinyl: ", "")+'.ALDERVINYL'
    path_to_aldervinyls = config.readline().replace("PathToAlderVinyls: ", "").replace("\n", "")
    volume = float(config.readline().replace("Volume: ", "").replace("\n", ""))
screen = pygame.display.set_mode((500, 500))
layerTop = pygame.Surface((500,500), pygame.SRCALPHA)
pygame.display.set_caption("AlderPlayer 0.3")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 36)
icon_image = pygame.image.load('sprites/icon.png')
pygame.display.set_icon(icon_image)

play_button_image = pygame.image.load(f'sprites/play_button.png')
pause_button_image = pygame.image.load(f'sprites/pause_button.png')
flip_button_image = pygame.image.load(f'sprites/flip_button.png')
volume_up_button_image = pygame.image.load(f'sprites/volume_up_button.png')
volume_down_button_image = pygame.image.load(f'sprites/volume_down_button.png')
stop_button_image = pygame.image.load(f'sprites/stop_button.png')

loop_button_image = pygame.image.load(f'sprites/loop_button.png')
one_side_button_image = pygame.image.load(f'sprites/one_side_button.png')
both_sides_button_image = pygame.image.load(f'sprites/both_sides_button.png')
random_button_image = pygame.image.load(f'sprites/random_button.png')
down_direction_button_image = pygame.image.load(f'sprites/down_direction_button.png')
up_direction_button_image = pygame.image.load(f'sprites/up_direction_button.png')

left_button_image = pygame.image.load(f'sprites/left_button.png')
right_button_image = pygame.image.load(f'sprites/right_button.png')
add_button_image = pygame.image.load(f'sprites/add_button.png')

try:
    vinyl = [elem for elem in os.listdir(f'{path_to_aldervinyls}\\' + vinyl_name) if elem[-4:] == '.png' or elem[-4:] == '.mp3']
except:
    vinyl_name = 'demo.ALDERVINYL'
    vinyl = [elem for elem in os.listdir(f'{path_to_aldervinyls}\\' + vinyl_name) if elem[-4:] == '.png' or elem[-4:] == '.mp3']
vinyl.sort()

is_backside = False
for i in vinyl:
    if i[-4:]=='.png':
        bgimage = i
        vinyl.remove(i)
        break
try:
    bg_image = pygame.image.load(f'{path_to_aldervinyls}/{vinyl_name}/{bgimage}')
except:
    print([el for el in os.listdir('sprites/') if el[:13]=='default_cover'])
    bg_image = pygame.image.load('sprites/'+choice([el for el in os.listdir('sprites/') if el[:13]=='default_cover'])) #'sprites/default_cover.png'
is_showing_list_of_vinyls = False
press_them_to_play = []
vinyl_to_show=vinyl[:5]
for i in range(5):
    music_button_rects_x_position = 500 - 55 * 2 - 60 * i
    press_them_to_play.append(
        [screen.blit(play_button_image, (450, music_button_rects_x_position)),
         f'{path_to_aldervinyls}\\{vinyl_name}\\' + vinyl_to_show[i]])

current_playing = -1000
next_song_mode = "one_side" #one_side both_sides loop random
next_song_direction_is_down = True
show_UI=True
showing_five_vinyls = 5

def flip_aldervinyl():
    global is_backside, vinyl_to_show, press_them_to_play, current_playing, path_to_aldervinyls, vinyl_name
    is_backside = not is_backside
    pygame.mixer.music.stop()
    if is_backside:
        vinyl_to_show = vinyl[5:]
    else:
        vinyl_to_show = vinyl[:5]
    press_them_to_play = []
    for i in range(5):
        music_button_rects_x_position = 500 - 55 * 2 - 60 * i
        press_them_to_play.append(
            [screen.blit(play_button_image, (450, music_button_rects_x_position)),
             f'{path_to_aldervinyls}\\{vinyl_name}\\' + vinyl_to_show[i]])
    current_playing = -1000
AlderPlayer = True
while AlderPlayer:
    #Bg
    screen.blit(bg_image, (0, 0))

    #Спавн UI
    if show_UI:
        screen.blit(flip_button_image, (400, 10))
        screen.blit(add_button_image, (450, 10))
        name = font.render(vinyl_name.replace('.ALDERVINYL', ''), True, (0, 0, 0), (255,255,255))
        screen.blit(name, (0, 0))

        pygame.draw.rect(screen, (255, 255, 255), (390, 450, 80, 40))
        pygame.draw.rect(screen, (0, 0, 0), (390, 450, 80, 40), width=3)
        screen.blit(volume_up_button_image, (360, 450))
        screen.blit(volume_down_button_image, (450, 450))
        screen.blit(font.render(str(int(round(volume, 2)*100)), True, (0, 0, 0)), (410, 450))

        screen.blit(stop_button_image, (230, 450))
        screen.blit(left_button_image, (185, 450))
        screen.blit(right_button_image, (275, 450))

        if next_song_mode=="one_side":
            screen.blit(one_side_button_image, (10, 450))
        elif next_song_mode=="both_sides":
            screen.blit(both_sides_button_image, (10, 450))
        elif next_song_mode=="loop":
            screen.blit(loop_button_image, (10, 450))
        elif next_song_mode=="random":
            screen.blit(random_button_image, (10, 450))

        if next_song_direction_is_down:
            pass
        else:
            pass

        for i in range(5):
            txtsurf = font.render(vinyl_to_show[i][:-4][:28]+'...'*(len(vinyl_to_show[i][:-4])>28), True, (0, 0, 0))
            music_rects_x_position = 500 - 60 * 2 - 60 * i
            if i==modulj(current_playing+(-1 if current_playing>0 else 1)):
                pygame.draw.rect(screen, (128, 166, 255), (0, music_rects_x_position, 500, 60))
            else:
                pygame.draw.rect(screen, (255, 255, 255), (0, music_rects_x_position, 500, 60))
            pygame.draw.rect(screen, (0, 0, 0), (0, music_rects_x_position, 500, 60), 5)
            music_button_rects_x_position = 500 - 55 * 2 - 60 * i
            if i==current_playing-1:
                screen.blit(pause_button_image, (450, music_button_rects_x_position))
            else:
                screen.blit(play_button_image, (450, music_button_rects_x_position))
            screen.blit(txtsurf, (10, music_button_rects_x_position))
        screen.blit(layerTop, (0, 0))

    #Opredelenije sledujuschego treka
    if not pygame.mixer.music.get_busy():
        try:
            if next_song_mode=="loop" and current_playing>=0:
                pygame.mixer.music.queue(press_them_to_play[current_playing-1][1])
                pygame.mixer.music.play()
            elif current_playing>=0:
                pygame.mixer.music.stop()
                pygame.mixer.music.unload()
                if current_playing == 1:
                    if next_song_mode=="both_sides" or (next_song_mode=="random" and randint(0,1)==0):
                        flip_aldervinyl()
                    current_playing = 5
                else:
                    if next_song_mode=="random" and randint(0,1)==0:
                        flip_aldervinyl()
                    current_playing -= 1
                if next_song_mode!="random":
                    pygame.mixer.music.load(press_them_to_play[current_playing - 1][1])
                else:
                    current_playing=randint(1,5)
                    pygame.mixer.music.load(press_them_to_play[current_playing-1][1])
                pygame.mixer.music.play()
                pygame.mixer.music.set_volume(volume)
        except:
            pass

    #Meniu vybora vinilov
    if is_showing_list_of_vinyls:
        vinyls_choice = []
        aldervinyls = [e for e in os.listdir(path_to_aldervinyls) if e[-11:] == '.ALDERVINYL'][showing_five_vinyls-5:showing_five_vinyls]
        for q in range(5):
            record_name = aldervinyls[q].replace('.ALDERVINYL', '')
            one_of_vinyls = font.render(record_name[:10]+'...'*(len(record_name)>10), True, (0, 0, 0))
            vinyls_choice.append((aldervinyls[q], pygame.draw.rect(screen, (255, 255, 255), (300, 10 + 50 * (q + 1), 200, 50))))
            pygame.draw.rect(screen, (0, 0, 0), (300, 10 + 50 * (q + 1), 200, 50), 5)
            screen.blit(one_of_vinyls, (310, 10 + 50 * (q + 1)))

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            with open("config.txt", "w", encoding="utf-8") as config:
                config.writelines(["CurrentAlderVinyl: "+vinyl_name.replace('.ALDERVINYL', '')+'\n',
                                   "PathToAlderVinyls: "+path_to_aldervinyls+"\n",
                                   "Volume: "+str(round(volume, 2))])
            AlderPlayer=False
        if event.type == pygame.MOUSEWHEEL and is_showing_list_of_vinyls:
            if event.y==1:
                showing_five_vinyls-=1*(showing_five_vinyls>5)
            if event.y==-1:
                showing_five_vinyls +=1*(showing_five_vinyls<len(os.listdir(path_to_aldervinyls)))
        # kliki myshkoj
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 2:
                show_UI=not show_UI
            if event.button == 1:
                # flip aljdervinila
                if 400 <= pygame.mouse.get_pos()[0] <= 440 and 10 <= pygame.mouse.get_pos()[1] <= 50:
                    flip_aldervinyl()
                # Zamena vinila
                elif 450 <= pygame.mouse.get_pos()[0] <= 490 and 10 <= pygame.mouse.get_pos()[1] <= 50:
                    is_showing_list_of_vinyls = not is_showing_list_of_vinyls
                # Izmenenije gromkosti
                elif 360 <= pygame.mouse.get_pos()[0] <= 400 and 450 <= pygame.mouse.get_pos()[1] <= 490:
                    volume += 0.05*(volume<0.89)
                    pygame.mixer.music.set_volume(volume)
                elif 450 <= pygame.mouse.get_pos()[0] <= 490 and 450 <= pygame.mouse.get_pos()[1] <= 490:
                    volume -= 0.05 * (volume>0.01)
                    pygame.mixer.music.set_volume(volume)
                # stop muziaki
                elif 230 <= pygame.mouse.get_pos()[0] <= 270 and 450 <= pygame.mouse.get_pos()[1] <= 490:
                    pygame.mixer.music.stop()
                    current_playing=-1000
                # Loop
                elif 10 <= pygame.mouse.get_pos()[0] <= 50 and 450 <= pygame.mouse.get_pos()[1] <= 490:
                    if next_song_mode == "one_side":
                        next_song_mode = "both_sides"
                    elif next_song_mode == "both_sides":
                        next_song_mode = "loop"
                    elif next_song_mode == "loop":
                        next_song_mode = "random"
                    elif next_song_mode == "random":
                        next_song_mode = "one_side"
                # Vlevo i vpravo
                elif 185 <= pygame.mouse.get_pos()[0] <= 225 and 450 <= pygame.mouse.get_pos()[1] <= 490:
                    try:
                        pygame.mixer.music.stop()
                        pygame.mixer.music.unload()
                        if next_song_mode=="random":
                            if randint(0, 1) == 0:
                                flip_aldervinyl()
                            current_playing = randint(1, 5)
                            pygame.mixer.music.load(press_them_to_play[current_playing - 1][1])
                        else:
                            if current_playing == 5:
                                if next_song_mode=="both_sides":
                                    flip_aldervinyl()
                                current_playing = 1
                            else:
                                current_playing = modulj(current_playing) + 1
                            pygame.mixer.music.load(press_them_to_play[current_playing - 1][1])
                        pygame.mixer.music.play()
                        pygame.mixer.music.set_volume(volume)
                    except:
                        pass
                elif 275 <= pygame.mouse.get_pos()[0] <= 315 and 450 <= pygame.mouse.get_pos()[1] <= 490:
                    try:
                        pygame.mixer.music.stop()
                        pygame.mixer.music.unload()
                        if next_song_mode=="random":
                            if randint(0, 1) == 0:
                                flip_aldervinyl()
                            current_playing = randint(1,5)
                            pygame.mixer.music.load(press_them_to_play[current_playing-1][1])
                        else:
                            if current_playing == 1:
                                if next_song_mode=="both_sides":
                                    flip_aldervinyl()
                                current_playing = 5
                            else:
                                current_playing = modulj(current_playing) - 1
                        pygame.mixer.music.load(press_them_to_play[current_playing-1][1])
                        pygame.mixer.music.play()
                        pygame.mixer.music.set_volume(volume)
                    except:
                        pass
                else:
                    pass

                # Vosproizvedenije muzyki
                for i in press_them_to_play:
                    if i[0][0] <= pygame.mouse.get_pos()[0] <= i[0][0] + i[0][2] and i[0][1] <= pygame.mouse.get_pos()[
                        1] <= \
                            i[0][1] + i[0][2]:
                        if current_playing-1 <= -1:
                            if press_them_to_play.index(i)+1 == modulj(current_playing) and pygame.mixer.music.get_pos() > 0.01:
                                pygame.mixer.music.unpause()
                            else:
                                try:
                                    pygame.mixer.music.unload()
                                except:
                                    pass
                                pygame.mixer.music.load(i[1])
                                pygame.mixer.music.play()
                                pygame.mixer.music.set_volume(volume)
                                # or
                            current_playing = press_them_to_play.index(i)+1
                        else:
                            if press_them_to_play.index(i)+1 == modulj(current_playing) and pygame.mixer.music.get_pos() > 0.01:
                                current_playing *= -1
                                pygame.mixer.music.pause()
                            else:
                                try:
                                    pygame.mixer.music.unload()
                                except:
                                    pass
                                pygame.mixer.music.load(i[1])
                                pygame.mixer.music.play()
                                pygame.mixer.music.set_volume(volume)
                                current_playing = press_them_to_play.index(i) + 1

                # smena vinila
                if is_showing_list_of_vinyls:
                    try:
                        for i in vinyls_choice:
                            if i[1].collidepoint(pygame.mouse.get_pos()):
                                pygame.mixer.music.stop()
                                vinyl_name = i[0]
                                vinyl = [elem for elem in os.listdir(f'{path_to_aldervinyls}\\' + vinyl_name) if
                                         elem[-4:] == '.png' or elem[-4:] == '.mp3']
                                vinyl.sort()
                                is_backside = False
                                for i in vinyl:
                                    if i[-4:] == '.png':
                                        bgimage = i
                                        vinyl.remove(i)
                                try:
                                    bg_image = pygame.image.load(f'{path_to_aldervinyls}/{vinyl_name}/{bgimage}')
                                except:
                                    bg_image = pygame.image.load('sprites/' + choice(
                                        [el for el in os.listdir('sprites/') if
                                         el[:13] == 'default_cover']))  # 'sprites/default_cover.png'
                                press_them_to_play = []
                                vinyl_to_show = vinyl[:5]
                                for i in range(5):
                                    music_button_rects_x_position = 500 - 55 * 2 - 60 * i
                                    press_them_to_play.append(
                                        [screen.blit(play_button_image, (450, music_button_rects_x_position)),
                                         f'{path_to_aldervinyls}\\{vinyl_name}\\' + vinyl_to_show[i], 0])
                                is_showing_list_of_vinyls = False
                                current_playing = -1000
                    except:
                        pass
                else:
                    pass

    #Cylk nuzhnyj kapec kakoj-to
    pygame.display.flip()
    pygame.display.update()
    clock.tick(10)