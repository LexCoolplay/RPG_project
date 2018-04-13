import pygame
import os
import menu
import util
import Camera
import Creature
import LevelLoader


display = pygame.display
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
action_list = util.action_list

map_name = 0
map_index = 0
gamecycle = True
pygame.init()
background = pygame.image.load(os.path.join('data', 'menu_screen.png'))
screen.fill((255, 255, 255))
clock = pygame.time.Clock()
black = (0, 0, 0, 255)
image = 0
rotation_turn = 0
accelerating, rotating, steering = False, False, False
entities = pygame.sprite.Group()
paused = False
moving = 0
music = -1


game_GUI = menu.init_default_GUI(screen)


#pygame.mixer.init()

game = False
major_gamecycle = True

#music_acceleration = pygame.mixer.Sound(os.path.join('data', 'accelerating.ogg'))
#music_rotating = pygame.mixer.Sound(os.path.join('data', 'rotate.ogg'))
#music_steering = pygame.mixer.Sound(os.path.join('data', 'steering.ogg'))


while major_gamecycle:
    if gamecycle:
        menu_GUI = menu.menu_GUI(screen)
    while gamecycle:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                gamecycle = False
            if e.type == pygame.MOUSEBUTTONDOWN:
                pressed_button = menu_GUI.get_event(e.pos)
                if pressed_button:
                    action = pressed_button.on_click()
                    if action:
                        exec(action_list[action])
        screen.fill(black)
        screen.blit(background, (0, 0))
        menu_GUI.draw(screen)
        display.update()
    if game:
        mapdata, tiles, obstacles, items = LevelLoader.load_level(map_name)
        entities = pygame.sprite.Group()
        hero = Creature.Hero(100,100,'main hero', 'hero', pygame.image.load('data/hero.png'))
        camera = Camera.Camera(Camera.camera_configure, mapdata.width * 32, mapdata.height * 32, screen.get_width(), screen.get_height())
        camera.apply(hero)
        entities.add(hero)
        game_GUI = menu.init_default_GUI(screen)
        paused = False
        inventory_opened = False
        inventoryGUI = menu.inventory_gui(screen)
        inventoryGUI.set_state(inventory_opened)
        rotation_turn = 0
        accelerating, rotating, steering = False, False, False
    while game:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                gamecycle = False
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_a:
                    rotation_turn = 10
                if e.key == pygame.K_s:
                    moving = -1
                if e.key == pygame.K_d:
                    rotation_turn = -10
                if e.key == pygame.K_w:
                    moving = 1
                if e.key == pygame.K_TAB:
                    inventory_opened = not inventory_opened
                    inventoryGUI.set_state(inventory_opened)
                    print(inventoryGUI.get_GUIElement_by_name('0 0').visible)
                if e.key == pygame.K_ESCAPE:
                    game_GUI.get_GUIElement_by_name('menu_overlay').visible = not game_GUI.get_GUIElement_by_name('menu_overlay').visible
                    game_GUI.get_GUIElement_by_name('continue').visible = not game_GUI.get_GUIElement_by_name('continue').visible
                    game_GUI.get_GUIElement_by_name('exit_game').visible = not game_GUI.get_GUIElement_by_name('exit_game').visible
                    game_GUI.get_GUIElement_by_name('exit_to_menu').visible = not game_GUI.get_GUIElement_by_name('exit_to_menu').visible
                    paused = not paused and not inventory_opened
            if e.type == pygame.KEYUP:
                if e.key == pygame.K_a:
                    rotation_turn = 0
                if e.key == pygame.K_s:
                    moving = 0
                if e.key == pygame.K_d:
                    rotation_turn = 0
                if e.key == pygame.K_w:
                    moving = 0

            if e.type == pygame.MOUSEBUTTONDOWN:
                pressed_button = game_GUI.get_event(e.pos)
                if pressed_button:
                    action = pressed_button.on_click()
                    if action:
                        exec(action_list[action])
                pressed_button = inventoryGUI.get_event(e.pos)
                if pressed_button:
                    inventory_cords = pressed_button.name.split()
                    inventory = hero.get_inventory()
                    if(len(inventory)>10*int(inventory_cords[1])+int(inventory_cords[0])):
                        selected_item = inventory[10*int(inventory_cords[1])+int(inventory_cords[0])]
                        if(selected_item.type == 'consumable'):
                            action = selected_item.script
                            hero.items.remove(selected_item)
                            if action:
                                exec(action_list[action])
                        else:
                            hero.weapon = selected_item
                            selected_item_index = int(10*inventory.cords[1])+int(inventory_cords[0])


        screen.fill(black)
        if not paused:
            pass
        for e in tiles:
            screen.blit(e.image, camera.apply(e))
        for e in obstacles:
            screen.blit(e.image, camera.apply(e))
        for e in entities:
            screen.blit(e.image, camera.apply(e))
        for e in items:
            screen.blit(e.image, camera.apply(e))
        health_image = pygame.image.load(os.path.join('data', 'health'+str(hero.health)+'.png'))
        screen.blit(health_image, camera.apply(hero))
        # print(GUI.sprite_group)
        hero.update(screen, moving, rotation_turn, items)
        camera.update(hero)
        game_GUI.draw(screen)
        inventoryGUI.draw(screen)
        if(inventory_opened):
            for item_index in range(len(hero.get_inventory())):
                screen.blit(hero.get_inventory()[item_index].image, ((item_index%10)*64,(item_index//2)*64))

        # print(main_car.rect)
        # print(main_car.rect.x, main_car.rect.y)
        display.update()
    #pygame.mixer.stop()
pygame.quit()

