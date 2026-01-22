import pygame
import os
from random import choice, randint

#Темы для кнопок
def modulj(a):
    return (a*-1 if a<0 else a)

pygame.init()
pygame.mixer.init()
pygame.font.init()

class AlderVinylMusic:
    def __init__(self, button, path):
        self.button = button
        self.path = path
    def set_rect(self, new_rect):
        self.button = new_rect
    def set_path(self, new_path):
        self.path = new_path
    def AlderVinylName(self):
        splitted_path = self.path.split('\\')
        return splitted_path[len(splitted_path)-1]
    def PrintAlderVinylMusic(self):
        print(self.button, self.path, "\n")

with open("config.txt", "r", encoding="utf-8") as config:
    vinyl_name=config.readline().replace("\n", "").replace("CurrentAlderVinyl: ", "")+'.ALDERVINYL'
    path_to_aldervinyls = config.readline().replace("PathToAlderVinyls: ", "").replace("\n", "")
    volume = float(config.readline().replace("Volume: ", "").replace("\n", ""))
    small_window = bool(config.readline().replace("IsSmallWindow: ", "").replace("\n", ""))
screen = pygame.display.set_mode(((500, 500) if small_window else (500, 800)))
#layerTop = pygame.Surface((500,500), pygame.SRCALPHA)
pygame.display.set_caption("AlderPlayer 0.4")
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
window_button_image = pygame.image.load(f'sprites/window_button.png')

try:
    vinyl = [elem for elem in os.listdir(f'{path_to_aldervinyls}\\' + vinyl_name) if elem[-4:] == '.png' or elem[-4:] == '.mp3']
except:
    vinyl_name = 'demo.ALDERVINYL'
    vinyl = [elem for elem in os.listdir(f'{path_to_aldervinyls}\\' + vinyl_name) if elem[-4:] == '.png' or elem[-4:] == '.mp3']
vinyl.sort()

is_backside = True
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
bg_image_on_vinyl = pygame.transform.scale(bg_image, [150,150])
is_showing_list_of_vinyls = False
current_playing = -1000
next_song_mode = "one_side" #one_side both_sides loop random
show_UI=True
showing_five_vinyls = 5
showing_playable_vinyls = 5
angle = 0

def flip_aldervinyl():
    global is_backside, vinyl_to_show, press_them_to_play, current_playing, path_to_aldervinyls, vinyl_name, angle, press_them_to_play_show, showing_playable_vinyls
    is_backside = not is_backside
    pygame.mixer.music.stop()
    if is_backside:
        vinyl_to_show = vinyl[round(len(vinyl)/2):]
    else:
        vinyl_to_show = vinyl[:round(len(vinyl)/2)]
    press_them_to_play = []
    for i in range(len(vinyl_to_show)):
        try:
            #music_button_rects_x_position = 510 + 60 * i - 360 * (small_window == True)
            press_them_to_play.append(
            AlderVinylMusic(screen.blit(play_button_image, (1000, 0)),
            f'{path_to_aldervinyls}\\{vinyl_name}\\' + vinyl_to_show[i])) #idk lol
        except:
            pass
    press_them_to_play_show = press_them_to_play[:5]
    current_playing = -1000
    angle = 0
    showing_playable_vinyls = 5

flip_aldervinyl()

AlderPlayer = True
while AlderPlayer:
    #Bg
    screen.blit(bg_image, (0, 0))
    press_them_to_play_show = press_them_to_play[showing_playable_vinyls-5:showing_playable_vinyls]
    #Спавн UI
    if show_UI:
        if not small_window:
            pygame.draw.rect(screen, (0, 0, 0), (0, 500, 500, 300))
            #Vinilovyj disk
            angle = ((angle + 5 * (-1 if is_backside else 1)) % 360) * (current_playing != 0)
            rotating_bg_vinyl_image = pygame.transform.rotate(bg_image_on_vinyl, angle)
            new_rect = rotating_bg_vinyl_image.get_rect(center=bg_image_on_vinyl.get_rect(center=(250, 250)).center)
            screen.blit(rotating_bg_vinyl_image, new_rect)
            pygame.draw.circle(screen, (20, 20, 20), [250, 250], 222, 152)
            """for i in range(len(press_them_to_play)):
                press_them_to_play[i].circle = pygame.draw.circle(screen, (
                    (20, 20, 20) if i % 2 == 0 else (24, 24, 24)), [250 - 2000 * (small_window == True),
                                                                    250 - 2000 * (small_window == True)],
                                                                                                224 - 30.5 * i,
                                                                                                32)"""
            pygame.draw.circle(screen, (100, 100, 100),
                               [250, 250], 75, 5)
            pygame.draw.circle(screen, (100, 100, 100),
                               [250, 250], 225, 5)
            #Dyrochka
            pygame.draw.circle(screen, (20, 20, 20),
                               [250, 250], 15)
            pygame.draw.circle(screen, (100, 100, 100),
                               [250, 250], 15, 5)
            #Vosprinimajuschaja shtuka
            pygame.draw.line(screen, (128, 128, 128),
                             [550, 250],
                             [280, 332+(120/(len(press_them_to_play)-1))*(modulj(current_playing)-1)], 20)
            surface_for_rect = pygame.Surface((50,20), pygame.SRCALPHA)
            pygame.draw.rect(surface_for_rect, (100, 100, 100), (0,0,50,20),0,0,5,5,5,5)
            pygame.transform.rotate(surface_for_rect, 45)
            screen.blit(surface_for_rect, (250,323+(120/(len(press_them_to_play)-1))*(modulj(current_playing)-1)))
        #Vsio chto sverhu
        name = font.render(vinyl_name.replace('.ALDERVINYL', ''), True, (0, 0, 0), (255, 255, 255))
        window_button = screen.blit(window_button_image, (400, 10))
        flip_button = screen.blit(flip_button_image, (450, 60)) #(60, 455)
        add_button = screen.blit(add_button_image, (450, 10))
        screen.blit(name, (0, 0))

        #Po gromkosti
        pygame.draw.rect(screen, (255, 255, 255), (390, 455, 80, 40))
        pygame.draw.rect(screen, (0, 0, 0), (390, 455, 80, 40), width=3)
        volume_up_button = screen.blit(volume_up_button_image, (360, 455))
        volume_down_button = screen.blit(volume_down_button_image, (450, 455))
        screen.blit(font.render(str(int(round(volume, 2)*100)), True, (0, 0, 0)), (410, 455))

        #Knopki snizu v centre
        stop_button = screen.blit(stop_button_image, (230, 455))
        left_button = screen.blit(left_button_image, (185, 455))
        right_button = screen.blit(right_button_image, (275, 455))

        #Knopka rezhyma sledujuschej pesni
        if next_song_mode=="one_side":
            song_mode_button = screen.blit(one_side_button_image, (10, 455))
        elif next_song_mode=="both_sides":
            song_mode_button = screen.blit(both_sides_button_image, (10, 455))
        elif next_song_mode=="loop":
            song_mode_button = screen.blit(loop_button_image, (10, 455))
        elif next_song_mode=="random":
            song_mode_button = screen.blit(random_button_image, (10, 455))

        #Sami treki
        for i in range((len(press_them_to_play) if len(press_them_to_play)<=5 else 5)):
            music_rects_x_position = 500 + 60 * (i) - 360 * (small_window == True)
            try:
                txtsurf = font.render(press_them_to_play_show[i].AlderVinylName()[:-4][:28]+'...'*(len(press_them_to_play_show[i].AlderVinylName()[:-4])>28), True, (0, 0, 0))
                if i+(showing_playable_vinyls-5)==modulj(current_playing+(-1 if current_playing>0 else 1)):
                    pygame.draw.rect(screen, (175, 222, 252), (0, music_rects_x_position, 500, 60))
                else:
                    pygame.draw.rect(screen, (255, 255, 255), (0, music_rects_x_position, 500, 60))
                pygame.draw.rect(screen, (0, 0, 0), (0, music_rects_x_position, 500, 60), 5)
                music_button_rects_x_position = music_rects_x_position+10
                if i+(showing_playable_vinyls-5)==current_playing-1:
                    press_them_to_play_show[i].set_rect(screen.blit(pause_button_image, (450, music_button_rects_x_position)))
                else:
                    press_them_to_play_show[i].set_rect(screen.blit(play_button_image, (450, music_button_rects_x_position)))
                screen.blit(txtsurf, (10, music_button_rects_x_position))
            except IndexError:
                pygame.draw.rect(screen, (0, 0, 0), (0, music_rects_x_position, 500, 60))
        #screen.blit(layerTop, (0, 0))

    #Opredelenije sledujuschego treka
    if not pygame.mixer.music.get_busy():
        try:
            if next_song_mode=="loop" and current_playing>=0:
                pygame.mixer.music.queue(press_them_to_play[current_playing-1].path)
                pygame.mixer.music.play()
            elif current_playing>=0:
                pygame.mixer.music.stop()
                pygame.mixer.music.unload()
                if current_playing == len(press_them_to_play):
                    if next_song_mode=="both_sides" or (next_song_mode=="random" and randint(0,1)==0):
                        flip_aldervinyl()
                    current_playing = 1
                else:
                    if next_song_mode=="random" and randint(0,1)==0:
                        flip_aldervinyl()
                    current_playing += 1
                if next_song_mode!="random":
                    pygame.mixer.music.load(press_them_to_play[current_playing - 1].path)
                else:
                    current_playing=randint(1,len(press_them_to_play))
                    pygame.mixer.music.load(press_them_to_play[current_playing-1].path)
                showing_playable_vinyls = (5 if current_playing <= 5 else current_playing)
                pygame.mixer.music.play()
                pygame.mixer.music.set_volume(volume)
        except:
            pass

    #Meniu vybora vinilov
    if is_showing_list_of_vinyls and show_UI:
        vinyls_choice = []
        all_aldervinyls = [e for e in os.listdir(path_to_aldervinyls) if e[-11:] == '.ALDERVINYL']
        all_aldervinyls.append("<   +   >")
        aldervinyls = all_aldervinyls[showing_five_vinyls-5:showing_five_vinyls]
        for q in range(5 if len(all_aldervinyls)>5 else len(all_aldervinyls)): #os.listdir(path_to_aldervinyls)
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
                                   "Volume: "+str(round(volume, 2))+"\n",
                                   "IsSmallWindow: "+str(int(small_window))])
            AlderPlayer=False
        if event.type == pygame.MOUSEWHEEL:
            if is_showing_list_of_vinyls:
                if event.y==1:
                    showing_five_vinyls-=1*(showing_five_vinyls>5)
                if event.y==-1:
                    showing_five_vinyls +=1*(showing_five_vinyls<len(os.listdir(path_to_aldervinyls))+1)
            else:
                if event.y==1:
                    showing_playable_vinyls-=1*(showing_playable_vinyls>5)
                if event.y==-1:
                    showing_playable_vinyls += 1 * (showing_playable_vinyls < len(press_them_to_play))
        # kliki myshkoj
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 2:
                show_UI=not show_UI
            if event.button == 1:
                #Umenjshenije i uvelichenije okna
                if window_button.collidepoint(pygame.mouse.get_pos()):
                    small_window = not small_window
                    if small_window:
                        screen = pygame.display.set_mode((500, 500))
                    else:
                        screen = pygame.display.set_mode((500, 800))
                # flip aljdervinila
                if flip_button.collidepoint(pygame.mouse.get_pos()):
                    flip_aldervinyl()
                # Zamena vinila
                elif add_button.collidepoint(pygame.mouse.get_pos()):
                    is_showing_list_of_vinyls = not is_showing_list_of_vinyls
                # Izmenenije gromkosti
                elif volume_up_button.collidepoint(pygame.mouse.get_pos()):
                    volume += 0.05*(volume<0.89)
                    pygame.mixer.music.set_volume(volume)
                elif volume_down_button.collidepoint(pygame.mouse.get_pos()):
                    volume -= 0.05 * (volume>0.01)
                    pygame.mixer.music.set_volume(volume)
                # stop muziaki
                elif stop_button.collidepoint(pygame.mouse.get_pos()):
                    pygame.mixer.music.stop()
                    current_playing=-1000
                # Loop
                elif song_mode_button.collidepoint(pygame.mouse.get_pos()):
                    if next_song_mode == "one_side":
                        next_song_mode = "both_sides"
                    elif next_song_mode == "both_sides":
                        next_song_mode = "loop"
                    elif next_song_mode == "loop":
                        next_song_mode = "random"
                    elif next_song_mode == "random":
                        next_song_mode = "one_side"
                # Vlevo i vpravo
                elif left_button.collidepoint(pygame.mouse.get_pos()):
                    try:
                        pygame.mixer.music.stop()
                        pygame.mixer.music.unload()
                        if next_song_mode=="random":
                            if randint(0, 1) == 0:
                                flip_aldervinyl()
                            current_playing = randint(1,len(press_them_to_play))
                            pygame.mixer.music.load(press_them_to_play[current_playing-1].path)
                        else:
                            if current_playing == 1:
                                if next_song_mode=="both_sides":
                                    flip_aldervinyl()
                                current_playing = len(press_them_to_play)
                            else:
                                current_playing = modulj(current_playing) - 1
                        pygame.mixer.music.load(press_them_to_play[current_playing-1].path)
                        pygame.mixer.music.play()
                        pygame.mixer.music.set_volume(volume)
                        showing_playable_vinyls = (5 if current_playing <= 5 else current_playing)
                    except:
                        pass
                elif right_button.collidepoint(pygame.mouse.get_pos()):
                    try:
                        pygame.mixer.music.stop()
                        pygame.mixer.music.unload()
                        if next_song_mode=="random":
                            if randint(0, 1) == 0:
                                flip_aldervinyl()
                            current_playing = randint(1, len(press_them_to_play))
                            pygame.mixer.music.load(press_them_to_play[current_playing - 1].path)
                        else:
                            if current_playing == len(press_them_to_play):
                                if next_song_mode=="both_sides":
                                    flip_aldervinyl()
                                current_playing = 1
                            else:
                                current_playing = modulj(current_playing) + 1
                            pygame.mixer.music.load(press_them_to_play[current_playing - 1].path)
                        pygame.mixer.music.play()
                        pygame.mixer.music.set_volume(volume)
                        showing_playable_vinyls = (5 if current_playing <= 5 else current_playing)
                    except:
                        pass
                else:
                    pass

                # Vosproizvedenije muzyki
                for i in press_them_to_play: #if i[0][0] <= pygame.mouse.get_pos()[0] <= i[0][0] + i[0][2] and i[0][1] <= pygame.mouse.get_pos()[1] <= \i[0][1] + i[0][2]:
                    if i.button.collidepoint(pygame.mouse.get_pos()):
                        if current_playing-1 <= -1:
                            if press_them_to_play.index(i)+1 == modulj(current_playing) and pygame.mixer.music.get_pos() > 0.01:
                                pygame.mixer.music.unpause()
                            else:
                                try:
                                    pygame.mixer.music.unload()
                                except:
                                    pass
                                pygame.mixer.music.load(i.path)
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
                                pygame.mixer.music.load(i.path)
                                pygame.mixer.music.play()
                                pygame.mixer.music.set_volume(volume)
                                current_playing = press_them_to_play.index(i) + 1

                # smena vinila
                if is_showing_list_of_vinyls:
                    try:
                        for i in vinyls_choice:
                            if i[1].collidepoint(pygame.mouse.get_pos()):
                                if i[0]=="<   +   >":
                                    os.system(f"start {path_to_aldervinyls}")
                                else:
                                    vinyl_name = i[0]
                                    pygame.mixer.music.stop()
                                    vinyl = [elem for elem in os.listdir(f'{path_to_aldervinyls}\\' + vinyl_name) if
                                             elem[-4:] == '.png' or elem[-4:] == '.mp3']
                                    vinyl.sort()
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
                                    bg_image_on_vinyl = pygame.transform.scale(bg_image, [150, 150])
                                    flip_aldervinyl()
                                    is_showing_list_of_vinyls = False
                    except:
                        pass
                else:
                    pass

    #Cylk nuzhnyj kapec kakoj-to
    pygame.display.flip()
    pygame.display.update()
    clock.tick(10)