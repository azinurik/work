import pygame
import sys
import datetime
# функции из tools.py (вспомогательные инструменты)
from tools import canvas_pos, flood_fill, draw_preview, commit_shape

pygame.init()

SCREEN_W = 900
SCREEN_H = 780
TOOLBAR_W = 180

CANVAS_X = TOOLBAR_W
CANVAS_W = SCREEN_W - TOOLBAR_W
CANVAS_H = SCREEN_H

# 🎨 Modern colors
BG_CANVAS = (255, 255, 255)# белый холст
BG_PANEL = (24, 26, 32)# тёмная панель
HIGHLIGHT = (100, 160, 255)# голубой акцент
TEXT_COLOR = (230, 235, 245)
DIVIDER = (70, 80, 100)

TOOLS = [
    "Pencil", "Line", "Rectangle", "Circle", "Square",
    "Right Triangle", "Equilateral Triangle", "Rhombus",
    "Eraser", "Fill", "Text"
]

PALETTE = [
    (0, 0, 0), (80, 80, 80), (160, 160, 160), (255, 255, 255),
    (255, 0, 0), (180, 0, 0), (255, 100, 0), (200, 60, 0),
    (255, 200, 0), (180, 140, 0), (0, 200, 0), (0, 120, 0),
    (0, 200, 200), (0, 100, 160), (0, 0, 255), (0, 0, 140),
    (180, 0, 180), (100, 0, 120), (255, 150, 200), (150, 80, 40),
]

screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
pygame.display.set_caption("Paint Pro 🎨")
clock = pygame.time.Clock()

font_tool = pygame.font.SysFont("Arial", 18, bold=True)
font_label = pygame.font.SysFont("Arial", 14)
font_text = pygame.font.SysFont("Arial", 28)

canvas = pygame.Surface((CANVAS_W, CANVAS_H))
canvas.fill(BG_CANVAS)


def draw_toolbar(surface, active_tool, draw_color, brush_size):
    mouse_pos = pygame.mouse.get_pos()

    pygame.draw.rect(surface, BG_PANEL, (0, 0, TOOLBAR_W, SCREEN_H))

    y = 15
    title = font_tool.render("Paint Pro", True, HIGHLIGHT)
    surface.blit(title, (20, y))
    y += 40

    for tool in TOOLS:
        rect = pygame.Rect(10, y, TOOLBAR_W - 20, 34)

        if rect.collidepoint(mouse_pos):
            color_btn = (60, 70, 90)
        elif tool == active_tool:
            color_btn = HIGHLIGHT
        else:
            color_btn = (40, 45, 60)

        pygame.draw.rect(surface, color_btn, rect, border_radius=10)

        if tool == active_tool:
            pygame.draw.rect(surface, (255, 255, 255), rect, 2, border_radius=10)

        label = font_label.render(tool, True, TEXT_COLOR)
        surface.blit(label, label.get_rect(center=rect.center))

        y += 40

    y += 10

    size_text = font_label.render(f"Brush: {brush_size}px", True, TEXT_COLOR)
    surface.blit(size_text, (20, y))
    y += 20

    hint = font_label.render("1 / 2 / 3 size", True, (140, 150, 170))
    surface.blit(hint, (20, y))
    y += 30

    # 🎨 Color palette
    for i, color in enumerate(PALETTE):
        x = 20 + (i % 4) * 35
        y2 = y + (i // 4) * 35
        r = pygame.Rect(x, y2, 30, 30)

        pygame.draw.rect(surface, color, r, border_radius=6)

        if r.collidepoint(mouse_pos):
            pygame.draw.rect(surface, (255, 255, 255), r, 2, border_radius=6)

        if color == draw_color:
            pygame.draw.rect(surface, HIGHLIGHT, r, 3, border_radius=6)

    # bottom text
    txt = font_label.render("C = clear | Ctrl+S = save", True, (150, 120, 120))
    surface.blit(txt, (10, SCREEN_H - 30))

#нажал ли пользователь на инструмент
def get_tool_at(mx, my):
    y = 55
    for tool in TOOLS:
        rect = pygame.Rect(10, y, TOOLBAR_W - 20, 34)
        if rect.collidepoint(mx, my):
            return tool
        y += 40
    return None

#нажал ли на цвет
def get_palette_color(mx, my):
    y_start = 55 + len(TOOLS) * 40 + 60

    for i, color in enumerate(PALETTE):
        x = 20 + (i % 4) * 35
        y = y_start + (i // 4) * 35
        if pygame.Rect(x, y, 30, 30).collidepoint(mx, my):
            return color
    return None


def main():
    active_tool = "Pencil"
    draw_color = (0, 0, 0)
    brush_size = 5

    drawing = False
    start_pos = None
    prev_pos = None

    typing = False
    text = ""
    text_pos = None

    while True:
        clock.tick(60)
        mx, my = pygame.mouse.get_pos()

        for event in pygame.event.get():

            #выход
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:

                if typing:
                    if event.key == pygame.K_RETURN:
                        canvas.blit(font_text.render(text, True, draw_color), text_pos)
                        typing = False
                        text = ""

                    elif event.key == pygame.K_ESCAPE:
                        typing = False
                        text = ""

                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]

                    else:
                        text += event.unicode
                
                #размер кисти
                else:
                    if event.key == pygame.K_1:
                        brush_size = 2
                    elif event.key == pygame.K_2:
                        brush_size = 5
                    elif event.key == pygame.K_3:
                        brush_size = 10
                    #очистка
                    elif event.key == pygame.K_c:
                        canvas.fill(BG_CANVAS)

                    mods = pygame.key.get_mods()
                    
                    #сохранение
                    if event.key == pygame.K_s and (mods & pygame.KMOD_CTRL or mods & pygame.KMOD_META):
                        filename = f"canvas_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
                        pygame.image.save(canvas, filename)
                        print("Saved:", filename)
                    if event.key == pygame.K_F5:
                        pygame.image.save(canvas, "test.png")
                        print("Saved test.png")
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

                if mx < TOOLBAR_W:
                    tool = get_tool_at(mx, my)#выбор инструмента
                    if tool:
                        active_tool = tool
                        typing = False

                    color = get_palette_color(mx, my)#выбор цвета
                    if color:
                        draw_color = color

                else:
                    cx, cy = canvas_pos(mx, my, CANVAS_X)

                    if active_tool == "Fill":
                        flood_fill(canvas, cx, cy, draw_color, CANVAS_W, CANVAS_H)

                    elif active_tool == "Text":
                        typing = True
                        text_pos = (cx, cy)
                        text = ""

                    else:
                        drawing = True#начало рисования
                        start_pos = (cx, cy)
                        prev_pos = (cx, cy)

            if event.type == pygame.MOUSEBUTTONUP:
                if drawing:
                    cx, cy = canvas_pos(mx, my, CANVAS_X)
                    commit_shape(canvas, active_tool, start_pos, (cx, cy), draw_color, brush_size)#отпускание мыши
                drawing = False

            if event.type == pygame.MOUSEMOTION and drawing:
                cx, cy = canvas_pos(mx, my, CANVAS_X)
                #pencil
                if active_tool == "Pencil":
                    pygame.draw.line(canvas, draw_color, prev_pos, (cx, cy), brush_size)
                    prev_pos = (cx, cy)
                
                #eraser
                elif active_tool == "Eraser":
                    pygame.draw.circle(canvas, BG_CANVAS, (cx, cy), brush_size * 2)

        screen.blit(canvas, (CANVAS_X, 0))

        # preview (предпросмотр)
        if drawing and start_pos:
            cx, cy = canvas_pos(mx, my, CANVAS_X)
            preview = canvas.copy()
            draw_preview(preview, active_tool, start_pos, (cx, cy), draw_color, brush_size)
            screen.blit(preview, (CANVAS_X, 0))
            
        # text preview
        if typing:
            screen.blit(font_text.render(text, True, draw_color),
                        (CANVAS_X + text_pos[0], text_pos[1]))

        # cursor brush
        if mx >= CANVAS_X:
            pygame.draw.circle(screen, draw_color, (mx, my), brush_size, 1)

        draw_toolbar(screen, active_tool, draw_color, brush_size)

        pygame.display.flip()


if __name__ == "__main__":
    main()