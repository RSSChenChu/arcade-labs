import arcade

arcade.open_window(600, 600, "Drawing thingis")

arcade.set_background_color(arcade.color.BLACK)

arcade.start_render()

arcade.draw_point(50, 300, arcade.color.RED, 50)

arcade.draw_line(75, 300, 300, 300, arcade.color.RED,10)

texture = arcade.load_texture(":resources:images/space_shooter/playerShip1_orange.png")
scale = .6
arcade.draw_scaled_texture_rectangle(540, 120, texture, scale, 0)
arcade.draw_scaled_texture_rectangle(540, 60, texture, scale, 45)

arcade.finish_render()

arcade.run()