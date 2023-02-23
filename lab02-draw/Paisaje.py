import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 400

SKY_COLOR = arcade.color.SKY_BLUE


def draw_sky():
    """Dibuja el cielo"""
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT, 0, SKY_COLOR)


def draw_sun():
    """Dibuja el sol"""
    arcade.draw_circle_filled(100, 350, 50, arcade.color.SUNGLOW)


def draw_moon():
    """Dibuja la luna"""
    arcade.draw_circle_filled(700, 350, 50, arcade.color.MANATEE)


def draw_mountains():
    """Dibuja las montañas"""
    arcade.draw_triangle_filled(0, 0, 150, 200, 300, 0, arcade.color.DARK_GRAY)
    arcade.draw_triangle_filled(200, 0, 150, 200, 300, 0, arcade.color.TAUPE_GRAY)
    arcade.draw_triangle_filled(200, 0, 350, 150, 500, 0, arcade.color.TROLLEY_GREY)
    arcade.draw_triangle_filled(400, 0, 350, 150, 500, 0, arcade.color.DIM_GRAY)


def on_draw(delta_time):
    """Función principal de dibujo"""
    arcade.start_render()
    draw_sky()
    draw_sun()
    draw_moon()
    draw_mountains()


arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Paisaje")
arcade.set_background_color(SKY_COLOR)

arcade.schedule(on_draw, 1/60)

arcade.run()
