import pygame

try:
    pygame.mixer.init()
    sound_enabled = True
except pygame.error:
    print("⚠️ Audio not available. Running without sound.")
    sound_enabled = False

cast_sound = None
bite_sound = None
break_sound = None

if sound_enabled:
    try:
        cast_sound = pygame.mixer.Sound("sounds/cast.wav")
        bite_sound = pygame.mixer.Sound("sounds/bite.wav")
        break_sound = pygame.mixer.Sound("sounds/break.wav")
    except:
        print("⚠️ Sound files not found. Continuing without sound.")
        sound_enabled = False

def play_cast():
    if sound_enabled and cast_sound:
        cast_sound.play()

def play_bite():
    if sound_enabled and bite_sound:
        bite_sound.play()

def play_break():
    if sound_enabled and break_sound:
        break_sound.play()
