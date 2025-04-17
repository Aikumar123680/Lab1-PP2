import pygame

def draw_square(screen, color, start_pos, end_pos):
    size = min(abs(end_pos[0] - start_pos[0]), abs(end_pos[1] - start_pos[1]))  # To ensure square aspect ratio
    pygame.draw.rect(screen, color, (start_pos[0], start_pos[1], size, size))

def draw_right_triangle(screen, color, start_pos, end_pos):
    # Draw right triangle by calculating the points based on start and end position
    p1 = start_pos
    p2 = (start_pos[0], end_pos[1])  # Make a point on the same vertical line
    p3 = (end_pos[0], end_pos[1])  # Make a point on the same horizontal line
    pygame.draw.polygon(screen, color, [p1, p2, p3])

def draw_equilateral_triangle(screen, color, start_pos, end_pos):
    # Side length based on the distance between start_pos and end_pos
    side_length = int(((end_pos[0] - start_pos[0]) ** 2 + (end_pos[1] - start_pos[1]) ** 2) ** 0.5)
    height = (3 ** 0.5) / 2 * side_length  # Height of equilateral triangle
    
    # Calculate the 3 points
    p1 = (start_pos[0], start_pos[1] - height // 2)
    p2 = (start_pos[0] - side_length // 2, start_pos[1] + height // 2)
    p3 = (start_pos[0] + side_length // 2, start_pos[1] + height // 2)
    
    pygame.draw.polygon(screen, color, [p1, p2, p3])

def draw_rhombus(screen, color, start_pos, end_pos):
    # Diagonal lengths based on the distance between start and end positions
    diagonal1 = abs(end_pos[0] - start_pos[0])
    diagonal2 = abs(end_pos[1] - start_pos[1])
    
    # Calculate the 4 points of the rhombus
    p1 = (start_pos[0] + diagonal1 // 2, start_pos[1])
    p2 = (start_pos[0], start_pos[1] + diagonal2 // 2)
    p3 = (start_pos[0] - diagonal1 // 2, start_pos[1])
    p4 = (start_pos[0], start_pos[1] - diagonal2 // 2)
    
    pygame.draw.polygon(screen, color, [p1, p2, p3, p4])

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    
    mode = 'draw'  # Default mode to 'draw'
    color = (0, 0, 255)  # Default color is blue
    start_pos = None
    shapes = []
    drawing = False
    
    while True:
        screen.fill((255, 255, 255))  # Fill screen with white
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    color = (255, 0, 0)  # Red
                    print("Red color selected")
                elif event.key == pygame.K_g:
                    color = (0, 255, 0)  # Green
                    print("Green color selected")
                elif event.key == pygame.K_b:
                    color = (0, 0, 255)  # Blue
                    print("Blue color selected")
                elif event.key == pygame.K_e:
                    mode = 'eraser'
                    print("Eraser mode selected")
                elif event.key == pygame.K_c:
                    mode = 'circle'
                    print("Circle mode selected")
                elif event.key == pygame.K_t:
                    mode = 'rectangle'
                    print("Rectangle mode selected")
                elif event.key == pygame.K_s:
                    mode = 'square'
                    print("Square mode selected")
                elif event.key == pygame.K_i:
                    mode = 'right_triangle'
                    print("Right Triangle mode selected")
                elif event.key == pygame.K_l:
                    mode = 'equilateral_triangle'
                    print("Equilateral Triangle mode selected")
                elif event.key == pygame.K_h:
                    mode = 'rhombus'
                    print("Rhombus mode selected")
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                start_pos = event.pos
                drawing = True
                print(f"Mouse down at {start_pos}, mode: {mode}")
                if mode == 'draw':
                    shapes.append(('line', start_pos, start_pos, color))
                elif mode == 'eraser':
                    shapes.append(('line', start_pos, start_pos, (255, 255, 255)))  # White color for eraser
            
            if event.type == pygame.MOUSEMOTION and drawing:
                if mode == 'draw' or mode == 'eraser':
                    shapes.append(('line', shapes[-1][2], event.pos, color if mode == 'draw' else (255, 255, 255)))
                    print(f"Drawing line from {shapes[-1][1]} to {event.pos}")
            
            if event.type == pygame.MOUSEBUTTONUP and start_pos:
                end_pos = event.pos
                print(f"Mouse up at {end_pos}, mode: {mode}")
                if mode == 'rectangle':
                    shapes.append(('rectangle', start_pos, end_pos, color))
                elif mode == 'circle':
                    radius = int(((end_pos[0] - start_pos[0]) ** 2 + (end_pos[1] - start_pos[1]) ** 2) ** 0.5)
                    shapes.append(('circle', start_pos, radius, color))
                elif mode == 'square':
                    draw_square(screen, color, start_pos, end_pos)
                elif mode == 'right_triangle':
                    draw_right_triangle(screen, color, start_pos, end_pos)
                elif mode == 'equilateral_triangle':
                    draw_equilateral_triangle(screen, color, start_pos, end_pos)
                elif mode == 'rhombus':
                    draw_rhombus(screen, color, start_pos, end_pos)
                
                drawing = False
                start_pos = None
        
        for shape in shapes:
            if shape[0] == 'rectangle':
                pygame.draw.rect(screen, shape[3], pygame.Rect(shape[1], (shape[2][0] - shape[1][0], shape[2][1] - shape[1][1])))
            elif shape[0] == 'circle':
                pygame.draw.circle(screen, shape[3], shape[1], shape[2])
            elif shape[0] == 'line':
                pygame.draw.line(screen, shape[3], shape[1], shape[2], 3)
        
        pygame.display.flip()  # Update display
        clock.tick(60)  # Maintain 60 FPS

main()