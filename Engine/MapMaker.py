from turtle import *
import random

# Function that draws the blocks on the canvas
def block_draw():
    pendown()
    begin_fill()
    for cube in range(4):
        forward(20)
        right(90)
    end_fill()

    forward(20)
    penup()

# Lists of all of the blocks
grass_list = []
dirt_list = []
stone_list = []
diorite_list = []
sand_list = []
snow_list = []
trunk_list = []
leaf_list = []

pos_list = []

# Tree spawning function
def tree(leaf, trunk_color, leaf_color):
    trunk_size = random.randint(1, 4)
    penup()
    setheading(90)
    forward(trunk_size * 20)
    
    # Makes the leaves of the tree
    if leaf:
        forward(40)
        right(90)
        fillcolor(leaf_color)
        block_pos = f'({float(round((xcor() + 10), 0))}0,{float(round((ycor() - 10), 0))}0)'
        leaf_list.append(block_pos)
        pos_list.append(block_pos)
        block_draw()
        back(40)
        right(90)
        forward(20)
        left(90)
        for leafs in range(3):
            block_pos = f'({float(round((xcor() + 10), 0))}0,{float(round((ycor() - 10), 0))}0)'
            leaf_list.append(block_pos)
            pos_list.append(block_pos)
            block_draw()
        back(40)
        right(90)
        forward(20)
        left(90)
    # Used for cactuses
    if not leaf:
        right(90)
        forward(20)

    # Makes the truk of the tree
    fillcolor(trunk_color)
    block_pos = f'({float(round((xcor() + 10), 0))}0,{float(round((ycor() - 10), 0))}0)'
    trunk_list.append(block_pos)
    pos_list.append(block_pos)
    for trunk in range(trunk_size):
        block_draw()
        right(90)
        forward(20)
        left(90)
        back(20)
        block_pos = f'({float(round((xcor() + 10), 0))}0,{float(round((ycor() - 10), 0))}0)'
        trunk_list.append(block_pos)
        pos_list.append(block_pos)


# Makes the bioms and chooses the properties for them
# Options: leaf spawning, leaf color, trunk color, tree spawning, main block, 
biom_list = [[True, 'forestgreen', 'peru', True, 'G'],  # GRASS
                  [True, 'seagreen', 'chocolate', True, 'Sn'],  # SNOW
                  [False, 'forestgreen', 'darkgreen', True, 'Sa'],  # DESERT
                  [True, 'forestgreen', 'peru', False, 'S']]    # ROCKY
biom_choice = random.choice(biom_list)
main_block = biom_choice[4]


# Random Blocks in Stone Layers and normal layers
RL = [' ']  + ['Di'] * 5 + ['Sa'] * 5 + ['D'] * 10 * 5 + [main_block] * 25 * 5 + ['S'] * 25 * 5

# Terrain
map_list = [['PG'] * 70 for _ in range(5)] + [['RL'] * 70] + [['SLR'] * 70 for _ in range(21)]

# Sets up the scene                    
def sceneMaker():
    bgcolor('#3776AB')
    setup(width=1.0, height=1.0)
    hideturtle()
    speed(0)
    setheading(0)

    penup()
    goto(-700, 340)
    pendown()
    color('#C6C6C6')
    begin_fill()
    for slot in range(4):
        fd(48)
        rt(90)
    end_fill()
    penup()
    goto(-699, 339)
    pencolor('black')
    fillcolor('#8B8B8B')
    pendown()
    begin_fill()
    for slot1 in range(4):
        fd(44)
        rt(90)
    end_fill()

    setheading(0)
    pencolor('black')
    pensize(0)

def maker():
    # Set up te scene
    sceneMaker()

    # Draws the block
    # Column
    for x in range(26):
        penup()
        goto(-700, (120 - (x * 20)))
        pendown()

        # Row
        for y in range(70):
            # Goes with the assumption that the block is not air
            air = False

            # Block coordinates
            block_pos = f'({float(round((xcor() + 10), 0))}0,{float(round((ycor() - 10), 0))}0)'

            # Check if the block is from SLR(Stone Layer Random) list and if it is asign the correct block to it
            if map_list[x][y] == 'SLR':
                air_amount = 2
                material_amount = 5
                if x < 25 and y < 69:
                    # Procedural generation for caves
                    if (map_list[x][y - 1] == ' ') or (map_list[x - 1][y] == ' '):
                        air_amount = int(270 * 3.5)

                    if (map_list[x][y - 1] == ' ') and (map_list[x - 1][y] == ' '):
                        material_amount = 1
                    
                    if (map_list[x - 1][y] != ' ') and (' ' in map_list[x - 1][y:]) and (' ' in map_list[x - 1][:y]):
                        air_amount = 0

                SLR = [' '] * air_amount  + ['Di'] * material_amount + ['Sa'] * material_amount + ['D'] * material_amount + ['S'] * (material_amount * 90)
                map_list[x][y] =  random.choice(SLR)
                
                      

            # Check if the block is from RL(Random Layer) list and if it is asign the correct block to it
            if map_list[x][y] == 'RL':
                map_list[x][y] =  random.choice(RL)

            # Procedural generation blocks
            if map_list[x][y] == 'PG':

                # Chance of a block spawning
                block_chance = 7
                tree_chance = 5
                air_chance = 49
                spawn_chance_list = [' '] * air_chance + ['T'] * tree_chance + [main_block] * block_chance
                
                # Spawns a block if there is one above it
                if map_list[x - 1][y] == main_block or map_list[x - 1][y] == 'T':
                    map_list[x][y] = main_block
                
                # Spawns a block right of the block that is spawned by the last function
                elif y > 0 and map_list[x - 1][y - 1] == main_block:
                    map_list[x][y] = main_block
                
                # Spawns a block left of the block that is spawned by the last function
                elif y < 69 and map_list[x - 1][y + 1] == main_block:
                    map_list[x][y] = main_block

                # If the block is should be spawned normally this gives it a chance of spawning
                else:
                    if main_block in map_list[x - 1]:
                        block_chance += 7
                        air_chance -= 7
                        if main_block in map_list[x - 2]:
                            block_chance += 7
                            air_chance -= 7
                            if main_block in map_list[x - 3]:
                                block_chance += 7
                                air_chance -= 7
                                if main_block in map_list[x - 4]:
                                    block_chance += 6
                                    air_chance -= 6

                    # More chance of a block spawning if it is surrounded by other blocks
                    if 0 < y < 69 and map_list[x][y - 1] == main_block and map_list[x][y + 1] == main_block:
                        block_chance = block_chance * 2
                    # More chance of air spawning if it is surrounded by air
                    if 0 < y < 69 and map_list[x][y - 1] != main_block and map_list[x][y + 1] != main_block:
                        block_chance = int(block_chance / 2)
                
                    # Choosing what block(air, tree, main block) should spawn
                    spawn_choice = random.choice(spawn_chance_list)

                    # Spawns trees by chance, biom, position. If the choice is not a tree it continiues as normal
                    if spawn_choice == 'T':
                        if biom_choice[3] == True:
                            if (map_list[x - 1][y] != 'SLR') or (map_list[x][y - 1] != ' '):
                                map_list[x][y] = ' '
                            else:
                                map_list[x][y] = 'T'
                        else:
                            map_list[x][y] = ' '
                    else:
                        map_list[x][y] = spawn_choice


            # Grass
            if map_list[x][y] == 'G':
                fillcolor('green')
                grass_list.append(block_pos)
            # Dirt
            elif map_list[x][y] == 'D':
                fillcolor('SaddleBrown')
                dirt_list.append(block_pos)
            # Stone
            elif map_list[x][y] == 'S':
                fillcolor('cornsilk4')
                stone_list.append(block_pos)
            # Diorite
            elif map_list[x][y] == 'Di':
                fillcolor('gray80')
                diorite_list.append(block_pos)
            # Sand
            elif map_list[x][y] == 'Sa':
                fillcolor('khaki3')
                sand_list.append(block_pos)
            # Snow
            elif map_list[x][y] == 'Sn':
                fillcolor('white')
                snow_list.append(block_pos)

            # Trees spawning and its properties
            if map_list[x][y] == 'T':
                tree(leaf=biom_choice[0], leaf_color=biom_choice[1], trunk_color=biom_choice[2])

            # Air
            elif map_list[x][y] == ' ':
                air = True
                penup()
                forward(20)
                pendown()

            # Append the collider(position) to normal blocks    
            else:
                pos_list.append(block_pos)


            # Skips this step if the block is air
            if not air:
                block_draw()

