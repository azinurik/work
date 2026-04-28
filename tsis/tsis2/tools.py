import pygame

#координаты холста
def canvas_pos(mx, my, canvas_x):
    x = max(0, mx - canvas_x)
    y = max(0, my)
    return x, y

#flood fill (заливка)
def flood_fill(surface, x, y, new_color, w, h):
    old_color = surface.get_at((x, y))
    new_color = pygame.Color(*new_color)

    if old_color == new_color:
        return

    stack = [(x, y)]

    while stack:
        if len(stack) > 100000:
            break

        x, y = stack.pop()

        if x < 0 or x >= w or y < 0 or y >= h:
            continue

        if surface.get_at((x, y)) == old_color:
            surface.set_at((x, y), new_color)

            stack.append((x + 1, y))
            stack.append((x - 1, y))
            stack.append((x, y + 1))
            stack.append((x, y - 1))

#preview фигур
def draw_preview(surface, tool, start, end, color, size):

    x1, y1 = start
    x2, y2 = end

    if tool == "Line":
        pygame.draw.line(surface, color, start, end, size)

    elif tool == "Rectangle":
        rect = pygame.Rect(min(x1, x2), min(y1, y2),
                           abs(x2 - x1), abs(y2 - y1))
        pygame.draw.rect(surface, color, rect, size)

    elif tool == "Circle":
        rect = pygame.Rect(min(x1, x2), min(y1, y2),
                           abs(x2 - x1), abs(y2 - y1))
        pygame.draw.ellipse(surface, color, rect, size)

    elif tool == "Square":
        side = min(abs(x2 - x1), abs(y2 - y1))
        x = x1 if x2 >= x1 else x1 - side
        y = y1 if y2 >= y1 else y1 - side
        pygame.draw.rect(surface, color, (x, y, side, side), size)

    elif tool == "Right Triangle":
        pygame.draw.polygon(surface, color,
                            [start, (x2, y1), end], size)

    elif tool == "Equilateral Triangle":
        side = abs(x2 - x1)
        h = int((3 ** 0.5 / 2) * side)
        pygame.draw.polygon(surface, color,
                            [(x1, y1), (x1 + side, y1), (x1 + side // 2, y1 - h)], size)

    elif tool == "Rhombus":
        cx = (x1 + x2) // 2
        cy = (y1 + y2) // 2
        pygame.draw.polygon(surface, color,
                            [(cx, y1), (x2, cy), (cx, y2), (x1, cy)], size)

#финальное рисование
def commit_shape(canvas, tool, start, end, color, size):
    draw_preview(canvas, tool, start, end, color, size)