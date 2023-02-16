import arcade

arcade.open_window(600, 600, "Drawing thingis")

arcade.set_background_color(arcade.color.BLACK)

arcade.start_render()

arcade.draw_point(50, 300, arcade.color.RED, 50)

arcade.draw_line(75, 300, 300, 300, arcade.color.WHITE, 10)

texture = arcade.load_texture(":resources:images/space_shooter/playerShip1_orange.png")
scale = .6
arcade.draw_scaled_texture_rectangle(300, 300, texture, scale, 90)

arcade.draw_rectangle_filled(350, 400, 100, 10, arcade.color.RED_VIOLET)
arcade.draw_rectangle_filled(350, 200, 100, 10, arcade.color.RED_VIOLET)

arcade.draw_arc_outline(150, 81, 15, 36, arcade.color.BRIGHT_MAROON, 90, 360)

arcade.draw_circle_outline(300, 300, 30, arcade.color.ORANGE, 72,  90, 360)

arcade.run()
