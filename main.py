def on_button_a():
    Spieler.change(LedSpriteProperty.X, -1)
input.on_button_event(Button.A, input.button_event_click(), on_button_a)

def on_button_b():
    Spieler.change(LedSpriteProperty.X, 1)
input.on_button_event(Button.B, input.button_event_click(), on_button_b)

Spieler: game.LedSprite = None
Spieler = game.create_sprite(2, 4)
Gegner = game.create_sprite(randint(0, 4), 0)

def on_every_interval():
    if Gegner.get(LedSpriteProperty.Y) == 4:
        Gegner.set(LedSpriteProperty.Y, 0)
        Gegner.set(LedSpriteProperty.X, randint(0, 4))
loops.every_interval(500, on_every_interval)

def on_forever():
    basic.pause(150)
    Gegner.change(LedSpriteProperty.Y, 1)
basic.forever(on_forever)

def on_forever2():
    if Spieler.is_touching(Gegner):
        basic.show_string("Game Over!")
basic.forever(on_forever2)
