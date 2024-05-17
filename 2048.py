import customtkinter as ctk
from tkinter import filedialog
from PIL import Image
import ctypes
from random import choice, randint
import pygame

pygame.init()


def nouvelle_grille():
    return [['0' for a in range(4)] for i in range(4)]


def nouvelle_partie():
    global grid
    grid = nouvelle_grille()
    grid[randint(0, 3)][randint(0, 3)] = alea_tuile[randint(0, 9)]
    play()


def home_page():
    global score
    global musique
    score = 0
    effacer_tout()
    app.title("Menu")
    title = ctk.CTkLabel(master=app,
                         text="2048",
                         fg_color="#EDC22E",
                         text_color='white',
                         width=225,
                         height=225,
                         corner_radius=10,
                         font=('Kozuka Mincho Pro B', 100))
    langue = ctk.CTkButton(master=app,
                           text=language,
                           fg_color='#EDC22E',
                           text_color='white',
                           command=change_langue,
                           width=225,
                           font=police,
                           hover_color='#F59563')
    fermer = ctk.CTkButton(master=app,
                           text=exit_text,
                           fg_color='#EDC22E',
                           text_color='white',
                           command=close,
                           width=225,
                           font=police,
                           hover_color='red')
    jouer = ctk.CTkButton(master=app,
                          text=game_text,
                          fg_color='#EDC22E',
                          text_color='white',
                          command=nouvelle_partie,
                          width=225,
                          font=police,
                          hover_color='#F59563')
    mode = ctk.CTkButton(master=app,
                         text='Mode',
                         fg_color='#EDC22E',
                         text_color='white',
                         width=225,
                         font=police,
                         hover_color='#F59563')
    dark = ctk.CTkButton(master=app,
                         image=dark_image_moon,
                         text='',
                         command=button_dark,
                         fg_color='transparent',
                         width=0,
                         height=0,
                         hover=False)
    light = ctk.CTkButton(master=app,
                          image=dark_image_sun,
                          text='',
                          command=button_light,
                          fg_color='transparent',
                          width=0,
                          height=0,
                          hover=False)
    musique = ctk.CTkButton(master=app,
                            image=theme_musique_off,
                            text='',
                            command=toggle_audio,
                            fg_color='transparent',
                            width=0,
                            height=0,
                            hover=False)

    stop_audio()
    musique.place(relx=0.9, rely=0.01, anchor=ctk.NE)
    light.place(relx=0.94, rely=0.01, anchor=ctk.NE)
    dark.place(relx=0.99, rely=0.01, anchor=ctk.NE)
    title.place(relx=0.5, rely=0.25, anchor=ctk.CENTER)
    jouer.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)
    mode.place(relx=0.5, rely=0.57, anchor=ctk.CENTER)
    langue.place(relx=0.5, rely=0.64, anchor=ctk.CENTER)
    fermer.place(relx=0.5, rely=0.71, anchor=ctk.CENTER)


def change_langue():
    global text_score
    global language
    global game_text
    global exit_text
    global back_text
    global save_text
    global load_text
    global loose_text
    if language == 'Français':
        language = 'English'
    else:
        language = 'Français'
    with open(f'langues/{language}.txt') as file:
        game_text = file.readline().replace("\n", "")
        exit_text = file.readline().replace("\n", "")
        back_text = file.readline().replace("\n", "")
        save_text = file.readline().replace("\n", "")
        load_text = file.readline().replace("\n", "")
        loose_text = file.readline().replace("\n", "")
        text_score = file.readline().replace("\n", "")
    home_page()


def couleur_tuile(nombre=str):
    nombre = int(nombre)
    if nombre == 2 or nombre == 4:
        return ('#EEE4DA', '#776E65')
    if nombre == 8:
        return ('#776E65', 'white')
    if nombre == 16:
        return ("#F59563", 'white')
    if nombre == 32:
        return ("#F67C5F", 'white')
    if nombre == 64:
        return ("#F65E3B", 'white')
    if nombre == 128:
        return ('#EDCF72', 'white')
    if nombre == 256:
        return ('#EDCC61', 'white')
    if nombre == 512:
        return ('#EDC850', 'white')
    if nombre == 1024:
        return ('#EDC53F', 'white')
    if nombre == 2048:
        return ('#EDC22E', 'white')
    if nombre > 2048:
        return ('#3C3A32', 'white')


def play():
    global touche_active
    global score
    global grid
    global alea_tuile
    global verif
    global add_chiffre
    global musique
    effacer_tout()
    app.title("Jeu")
    app.bind('<KeyPress>', key_pressed)
    touche_active = True

    # boutons et autre
    menu = ctk.CTkButton(master=app,
                         text=back_text,
                         fg_color='#EDC22E',
                         text_color='white',
                         command=home_page,
                         font=police,
                         hover_color='#F59563')
    enregistrer = ctk.CTkButton(master=app,
                                text=save_text,
                                fg_color='#EDC22E',
                                text_color='white',
                                command=save,
                                font=police,
                                hover_color='#F59563')
    charger = ctk.CTkButton(master=app,
                            text=load_text,
                            fg_color='#EDC22E',
                            text_color='white',
                            command=load,
                            font=police,
                            hover_color='#F59563')
    haut = ctk.CTkButton(master=app,
                         text='↑',
                         fg_color='#EDC22E',
                         text_color='white',
                         width=100,
                         height=50,
                         command=up,
                         font=police,
                         hover_color='#F59563')
    gauche = ctk.CTkButton(master=app,
                           text='←',
                           fg_color='#EDC22E',
                           text_color='white',
                           width=50,
                           height=100,
                           command=left,
                           font=police,
                           hover_color='#F59563')
    droite = ctk.CTkButton(master=app,
                           text='→',
                           fg_color='#EDC22E',
                           text_color='white',
                           width=50,
                           height=100,
                           command=right,
                           font=police,
                           hover_color='#F59563')
    bas = ctk.CTkButton(master=app,
                        text='↓',
                        fg_color='#EDC22E',
                        text_color='white',
                        width=100,
                        height=50,
                        command=down,
                        font=police,
                        hover_color='#F59563')
    dark = ctk.CTkButton(master=app,
                         image=dark_image_moon,
                         text='',
                         command=button_dark,
                         fg_color='transparent',
                         width=0,
                         height=0,
                         hover=False)
    light = ctk.CTkButton(master=app,
                          image=dark_image_sun,
                          text='',
                          command=button_light,
                          fg_color='transparent',
                          width=0,
                          height=0,
                          hover=False)
    point = ctk.CTkLabel(master=app,
                         text=f'{text_score}{score} points',
                         fg_color='#EDC22E',
                         text_color='white',
                         font=police,
                         width=350,
                         height=50,
                         corner_radius=10)
    musique = ctk.CTkButton(master=app,
                            image=theme_musique_off,
                            text='',
                            command=toggle_audio,
                            fg_color='transparent',
                            width=0,
                            height=0,
                            hover=False)

    musique.place(relx=0.9, rely=0.01, anchor=ctk.NE)
    light.place(relx=0.94, rely=0.01, anchor=ctk.NE)
    dark.place(relx=0.99, rely=0.01, anchor=ctk.NE)
    menu.place(relx=0.01, rely=0.015, anchor=ctk.NW)
    enregistrer.place(relx=0.13, rely=0.015, anchor=ctk.NW)
    charger.place(relx=0.265, rely=0.015, anchor=ctk.NW)
    haut.place(relx=0.07, rely=0.7, anchor=ctk.SW)
    droite.place(relx=0.15, rely=0.835, anchor=ctk.SW)
    bas.place(relx=0.07, rely=0.9, anchor=ctk.SW)
    gauche.place(relx=0.03, rely=0.835, anchor=ctk.SW)
    point.place(relx=0.5, rely=0.13, anchor=ctk.CENTER)

    if add_chiffre:
        # chiffre aléatoire en plus
        empty_list = []
        for i in range(len(grid)):
            for e in range(len(grid[i])):
                if grid[i][e] == '0':
                    empty_list.append((i, e))
        if empty_list != []:
            a = choice(empty_list)
            index = randint(0, 9)
            grid[a[0]][a[1]] = alea_tuile[index]
        else:
            grid = nouvelle_grille()
            perdu()

    cadre_grille = ctk.CTkFrame(master=app,
                                width=500,
                                height=500)
    cadre_grille.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

    # affichage grille
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            element = grid[i][j]
            ligne = i
            colonne = j
            if element == '0':
                tuile_null = ctk.CTkLabel(cadre_grille,
                                          text=None,
                                          width=100,
                                          height=100)
                tuile_null.grid(row=ligne, column=colonne, padx=5, pady=5)
            else:
                couleur = couleur_tuile(element)
                tuile = ctk.CTkLabel(master=cadre_grille,
                                     text=element,
                                     width=100,
                                     height=100,
                                     fg_color=couleur[0],
                                     text_color=couleur[1],
                                     corner_radius=5,
                                     font=police_tuile)
                tuile.grid(row=ligne, column=colonne, padx=5, pady=5)
        if not check_moves_possible():
            perdu()


def merge():
    global merging_change
    global verif
    global grid
    global add_chiffre
    global score

    verif = nouvelle_grille()
    for i in range(len(grid)):
        for e in range(len(grid[i])):
            verif[i][e] = grid[i][e]

    for i in range(len(grid)):
        todelete = []
        for e in range(len(grid[i])):
            if grid[i][e] == '0':
                todelete.append(e)
        # supprimer les 0
        todelete = todelete[::-1]
        for e in todelete:
            grid[i].pop(e)
        # chercher les nombres à fusionner
        if merging_change:
            for e in range(len(grid[i])):
                if e < len(grid[i])-1 and grid[i][e] == grid[i][e+1]:
                    grid[i][e] = str(int(grid[i][e])*2)
                    grid[i][e+1] = '0'
                    score += int(grid[i][e])
        else:
            for e in range(len(grid[i])-1, -1, -1):
                if e < len(grid[i])-1 and grid[i][e] == grid[i][e+1]:
                    grid[i][e] = str(int(grid[i][e])*2)
                    grid[i][e+1] = '0'
                    score += int(grid[i][e])
        # chercer les nouveaux 0 à supprimer
        todelete = []
        for e in range(len(grid[i])):
            if grid[i][e] == '0':
                todelete.append(e)
        # supprimer nouveaux les 0
        todelete = todelete[::-1]
        for e in todelete:
            grid[i].pop(e)


def check_moves_possible():
    # Vérifier les mouvements horizontaux
    for i in range(len(grid)):
        for j in range(len(grid[i]) - 1):
            if ((grid[i][j] == grid[i][j + 1]
                 ) or (grid[i][j] == '0'
                       ) or (grid[i][j + 1] == '0'
                             )):
                return True

    # Vérifier les mouvements verticaux
    for j in range(len(grid[0])):
        for i in range(len(grid) - 1):
            if ((grid[i][j] == grid[i + 1][j]
                 ) or (grid[i][j] == '0'
                       ) or (grid[i + 1][j] == '0'
                             )):
                return True
    return False


def key_pressed(event):
    if touche_active:
        if event.keysym == 'Right':
            right()
        elif event.keysym == 'Left':
            left()
        elif event.keysym == 'Up':
            up()
        elif event.keysym == 'Down':
            down()


def perdu():
    # remise a 0
    global score
    global touche_active
    touche_active = False
    effacer_tout()

    app.title("perdu")
    # boutons et autre
    loose = ctk.CTkLabel(master=app,
                         text=loose_text,
                         text_color='white',
                         fg_color='#F65E3B',
                         width=275,
                         height=275,
                         corner_radius=10,
                         font=('Kozuka Mincho Pro B', 100))
    jouer = ctk.CTkButton(master=app,
                          text=game_text,
                          fg_color='#EDC22E',
                          text_color='white',
                          width=275,
                          font=police,
                          hover_color='#F59563',
                          command=nouvelle_partie)
    menu = ctk.CTkButton(master=app,
                         text=back_text,
                         fg_color='#EDC22E',
                         text_color='white',
                         width=275,
                         font=police,
                         hover_color='#F59563',
                         command=home_page)
    point = ctk.CTkLabel(master=app,
                         text=f'{text_score}{score} points',
                         fg_color='#EDC22E',
                         text_color='white',
                         font=police,
                         width=350,
                         height=50,
                         corner_radius=10)
    # position des éléments
    score = 0

    loose.place(relx=0.5, rely=0.23, anchor=ctk.CENTER)
    point.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)
    jouer.place(relx=0.5, rely=0.6, anchor=ctk.CENTER)
    menu.place(relx=0.5, rely=0.7, anchor=ctk.CENTER)

    global cadre_grille
    if cadre_grille is not None:
        cadre_grille.destroy()
        cadre_grille = None


def right():
    global merging_change
    global verif
    global add_chiffre
    merging_change = False
    merge()
    # rajouter les 0
    for i in range(len(grid)):
        for e in range(len(grid)-len(grid[i])):
            grid[i].insert(0, '0')

    # vérif pour si il faut ajouter un chiffre
    if verif == grid:
        add_chiffre = False
    else:
        add_chiffre = True
    play()


def left():
    global merging_change
    global verif
    global add_chiffre
    merging_change = True
    merge()
    # rajouter les 0
    for i in range(len(grid)):
        for e in range(len(grid)-len(grid[i])):
            grid[i].append('0')

    # vérif pour si il faut ajouter un chiffre
    if verif == grid:
        add_chiffre = False
    else:
        add_chiffre = True
    play()


def up():
    global merging_change
    global verif
    global add_chiffre
    merging_change = False
    # tourner la grille
    for i in range(len(grid)):
        for e in range(i, len(grid)):
            grid[e][i], grid[i][e] = grid[i][e], grid[e][i]
    for i in range(len(grid)):
        grid[i].reverse()
    merge()
    # rajouter les 0
    for i in range(len(grid)):
        for e in range(len(grid)-len(grid[i])):
            grid[i].insert(0, '0')
    # vérif pour si il faut ajouter un chiffre
    if verif == grid:
        add_chiffre = False
    else:
        add_chiffre = True
    # retourner la grille
    for i in range(len(grid)):
        for e in range(i, len(grid)):
            grid[e][i], grid[i][e] = grid[i][e], grid[e][i]
    grid.reverse()

    play()


def down():
    global merging_change
    global verif
    global add_chiffre
    merging_change = True
    for i in range(len(grid)):
        for e in range(i, len(grid)):
            grid[e][i], grid[i][e] = grid[i][e], grid[e][i]
    for i in range(len(grid)):
        grid[i].reverse()
    merge()
    # rajouter les 0
    for i in range(len(grid)):
        for e in range(len(grid)-len(grid[i])):
            grid[i].append('0')
    # vérif pour si il faut ajouter un chiffre
    if verif == grid:
        add_chiffre = False
    else:
        add_chiffre = True
    # retourner la grille
    for i in range(len(grid)):
        for e in range(i, len(grid)):
            grid[e][i], grid[i][e] = grid[i][e], grid[e][i]
    grid.reverse()

    play()


def save():
    file_path = filedialog.asksaveasfilename()
    if not file_path:
        return None
    with open(file_path, 'w') as file:
        for i in grid:
            file.write(str(i)+'\n')


def load():
    global grid
    global score
    score = 0
    file_path = filedialog.askopenfilename()
    if not file_path:
        return None
    with open(file_path) as file:
        for i in range(len(grid)):
            grid[i] = file.readline().replace("\n", "").replace("[", "")\
                .replace("]", "").replace(" ", "").replace("'", "").split(',')
    play()


def button_dark():
    ctk.set_appearance_mode("dark")


def button_light():
    ctk.set_appearance_mode("light")


def effacer_widgets(container):
    for widget in container.winfo_children():
        widget.destroy()


def effacer_tout():
    effacer_widgets(app)


def close():
    app.destroy()


def toggle_audio():
    global musique_lecture
    global theme_musique
    if musique_lecture:
        pygame.mixer.music.stop()
        musique.configure(image=theme_musique_off)
        musique_lecture = False
    else:
        pygame.mixer.music.play(-1)  # jouer la musique en boucle
        musique.configure(image=theme_musique_on)
        musique_lecture = True


def stop_audio():
    global musique_lecture
    if musique_lecture:
        pygame.mixer.music.stop()
        musique_lecture = False
        musique.configure(image=theme_musique_off)


grid = nouvelle_grille()

verif = []
merging_change = True
add_chiffre = True

language = "Français"
game_text = "Nouvelle partie"
exit_text = "Quitter"
back_text = "Retour"
save_text = "Sauvegarder"
load_text = "Charger"
loose_text = "Perdu"
text_score = "Votre score est de : "

touche_active = False

user32 = ctypes.windll.user32
screen_width = user32.GetSystemMetrics(0)
screen_height = user32.GetSystemMetrics(1)

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()

app.geometry(f"{screen_width}x{screen_height}+0+0")


dark_image_moon = Image.open("images/moon.png")
dark_image_sun = Image.open("images/sun.png")
light_image_moon = Image.open("images/moon_theme_light.png")
light_image_sun = Image.open("images/sun_theme_light.png")
dark_image_sound = Image.open('images/sound_on_black.png')
light_image_sound = Image.open('images/sound_on_white.png')
dark_image_no_sound = Image.open('images/sound_off_black.png')
light_image_no_sound = Image.open('images/sound_off_white.png')

theme_musique_off = ctk.CTkImage(light_image=dark_image_no_sound,
                                 dark_image=light_image_no_sound,
                                 size=(40, 40))
theme_musique_on = ctk.CTkImage(light_image=dark_image_sound,
                                dark_image=light_image_sound,
                                size=(40, 40))
dark_image_moon = ctk.CTkImage(light_image=dark_image_moon,
                               dark_image=light_image_moon,
                               size=(40, 40))
dark_image_sun = ctk.CTkImage(light_image=dark_image_sun,
                              dark_image=light_image_sun,
                              size=(40, 40))

police = ('Kozuka Mincho Pro B', 25)
police_tuile = ('Kozuka Mincho Pro B', 40)

app.iconbitmap("images/logo.ico")

alea_tuile = ['2'for i in range(9)] + ['4']

score = 0

audio_file = "audio/musique_theme.mp3"
pygame.mixer.music.load(audio_file)
musique_lecture = False

home_page()

app.mainloop()
