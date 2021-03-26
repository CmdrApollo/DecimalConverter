import pygame

pygame.init()

#RGB COLORS

lg = (150, 255, 150)
BLACK = (127, 127, 127)
WHITE = (255, 255, 255)

SIZE = 600 #SCREEN SIZE IN PIXELS

#SETUP WINDOW
WIN = pygame.display.set_mode((SIZE, SIZE))
pygame.display.set_caption("Number Converter")

def get_place_vals(ran, base):
    placevals = []
    for i in range(ran):
        placevals.append(base**i)
    return placevals

def remove_char_from_start(char, string):
    retstr = ""
    should_append = False
    for el in string[::-1]:
        if el != char and el != " ":
            should_append = True
        if should_append:
            retstr += el
    
    return retstr[::-1]

def new_num(base, num):
    numindec = int("".join(str(num).split('-')))
    depth = 10
    basegten = base > 10
    placevals = get_place_vals(depth, base)
    retstr = ""
    for val in placevals:
        retstr += str((numindec//val)%base)[::-1]
        if basegten:
            retstr += " "

    retstr = remove_char_from_start("0", retstr)
    
    if "-" in str(num):
            retstr+= "-"

    return retstr[::-1]

def main(fps, size):
    clock = pygame.time.Clock()
    run = True
    num = 0
    font = pygame.font.SysFont("Comic Sans MS", 26)
    base = 8
    basenum = "0"
    onhelpscreen = False

    def draw(basenumtex, numtex, text):
        WIN.fill(lg)
        if not onhelpscreen:
            WIN.blit(basenumtex, (size//2-basenumtex.get_rect().width//2, size//3))
            WIN.blit(numtex, (size//2-numtex.get_rect().width//2, size//3+numtex.get_rect().height * 1.05))
            WIN.blit(text, (size//2-text.get_rect().width//2, text.get_rect().height//3))
        else:
            tex1 = font.render("'a' and 'd' to change base.", True, BLACK)
            tex2 = font.render("l/r arrow to -/+ the number", True, BLACK)
            WIN.blit(tex1, (size//2-tex1.get_rect().w//2, size//3))
            WIN.blit(tex2, (size//2-tex2.get_rect().w//2, size//3+tex2.get_rect().h*1.15))
        pygame.display.update()

    while run:
        clock.tick(fps)

        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                run = False
            if event.type == pygame.KEYUP:
                if keys[pygame.K_RIGHT] and not onhelpscreen:
                    num += 1
                elif keys[pygame.K_LEFT] and not onhelpscreen:
                    num -= 1
                if keys[pygame.K_d] and not onhelpscreen:
                    base += 1
                elif keys[pygame.K_a] and not onhelpscreen:
                    base -= 1
                if keys[pygame.K_h]:
                    onhelpscreen = not onhelpscreen
                for i in range(9):
                    if keys[i+48]:
                        print(i+48)
        
        basenum = new_num(base, num)

        basenumtex = font.render(basenum + " : Base " + str(base), True, BLACK)
        numtex = font.render(str(num) + " : Decimal", True, BLACK)
        text = font.render("Press 'h' for help", True, BLACK)

        draw(basenumtex, numtex, text)
    
    pygame.quit()

main(30, SIZE)