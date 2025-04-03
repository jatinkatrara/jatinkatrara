import time
import pyttsx3
import os
from termcolor import colored
from pyfiglet import figlet_format
import simpleaudio as sa
import pygame
import random
import sys

def play_song():
    wave_obj = sa.WaveObject.from_wave_file("birthday_song.wav")
    play_obj = wave_obj.play()
    play_obj.wait_done()

def attack_on_titan_wish():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(colored(figlet_format("⚡⚡ BOOM ⚡⚡"), "red"))
    time.sleep(0.5)
    print(colored("⚡ A powerful thunder strikes! ⚡", "yellow"))
    time.sleep(1)
    print(colored(figlet_format("Happy Birthday"), "red"))
    print(colored(figlet_format("Falguni!"), "yellow"))
    time.sleep(1)
    print(colored("🔥 Your Legendary Birthday Begins! 🔥", "cyan"))
    time.sleep(1)
    print(colored("🎆 The Attack on Titan Theme Starts Playing! 🎆", "magenta"))
    time.sleep(1)

def speak_wish():
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.say("Happy Birthday Falguni! May your day be as legendary as Attack on Titan!")
    engine.runAndWait()

def start_japan_slideshow():
    pygame.init()
    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Japan Slideshow")
    
    image_paths = ["mount_fuji.jpg", "tokyo_tower.jpg", "fushimi_inari.jpg", "osaka_castle.jpg", "shibuya_crossing.jpg"]
    images = [pygame.image.load(img) for img in image_paths]
    images = [pygame.transform.scale(img, (WIDTH, HEIGHT)) for img in images]
    
    clock = pygame.time.Clock()
    index = 0
    running = True
    while running:
        screen.blit(images[index], (0, 0))
        pygame.display.flip()
        time.sleep(2)
        index = (index + 1) % len(images)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()

def start_jumping_itachi_game():
    pygame.init()
    WIDTH, HEIGHT = 800, 400
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Jumping Itachi")

    clock = pygame.time.Clock()
    running = True
    start_time = time.time()
    player = pygame.Rect(100, 300, 50, 50)
    gravity = 0
    jump_power = -15
    is_jumping = False

    obstacle = pygame.Rect(600, 300, 50, 50)
    obstacle_speed = 5
    
    font = pygame.font.Font(None, 36)
    instruction_text = font.render("Press SPACE to Jump. Survive for 1 minute!", True, (255, 255, 255))

    while running:
        screen.fill((30, 30, 30))
        screen.blit(instruction_text, (200, 20))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and not is_jumping:
                gravity = jump_power
                is_jumping = True

        player.y += gravity
        gravity += 1
        if player.y >= 300:
            player.y = 300
            is_jumping = False

        obstacle.x -= obstacle_speed
        if obstacle.x < -50:
            obstacle.x = WIDTH

        pygame.draw.rect(screen, (255, 0, 0), player)
        pygame.draw.rect(screen, (0, 255, 0), obstacle)

        if player.colliderect(obstacle):
            running = False

        if time.time() - start_time >= 60:
            running = False
            print("🎉 Falguni Wins the Game! 🎉")

        pygame.display.flip()
        clock.tick(30)
    pygame.quit()

def ask_for_gift():
    choice = input("Do you want a gift? Type 'gift' to receive one: ")
    if choice.lower() == "gift":
        wish = input("Make a wish: ")
        print(colored(f"✨ Your wish '{wish}' is now sent to the universe! ✨", "green"))
        start_jumping_itachi_game()
    else:
        print(colored("Okay, enjoy your special day! 🎉", "blue"))

def choose_gift():
    gifts = ["A Special Anime Poster", "A Personalized Message", "A Secret Surprise", "A Digital Artwork"]
    print("\nChoose a gift box (1-4):")
    for i in range(1, 5):
        print(f"[{i}] Mystery Box {i}")
    choice = int(input("Enter the number of your chosen box: "))
    if 1 <= choice <= 4:
        print(f"\n🎁 Congratulations! You got: {gifts[choice - 1]} 🎉")
        print("\n🎇 As you open the box, an epic explosion of light appears! 🎇")
        print("\nAkatsuki members appear in 3D and say: 'We are always with you. Any problem must go through us before it touches you.'")
        print("\nAfter that, Mahadev with family, Mata Rani, Krishna ji, and Radha ji appear in 3D and bless you to always be happy and succeed in life.")
        print("\n✨ A divine background music plays as they bless you. ✨")
        print("\nLastly, a special message appears with glowing effect: 'Ek chota sa gift apke dost ke pass rakha hai.' 🎁")
        secret_code = input("Type a secret word to unlock an extra surprise: ")
        if secret_code.lower() == "uchiha" or secret_code.lower() == "divine":
            print("🌟 You unlocked a hidden legendary surprise! Stay tuned! 🌟")
    else:
        print("Invalid choice! No gift for you 😜")

# Running the script
import threading
slideshow_thread = threading.Thread(target=start_japan_slideshow)
slideshow_thread.start()
attack_on_titan_wish()
play_song()
speak_wish()
ask_for_gift()
