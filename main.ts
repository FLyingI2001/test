input.onButtonEvent(Button.A, input.buttonEventClick(), function () {
    Spieler.change(LedSpriteProperty.X, -1)
})
input.onButtonEvent(Button.B, input.buttonEventClick(), function () {
    Spieler.change(LedSpriteProperty.X, 1)
})
let Spieler: game.LedSprite = null
Spieler = game.createSprite(2, 4)
let Gegner = game.createSprite(randint(0, 4), 0)
loops.everyInterval(500, function () {
    if (Gegner.get(LedSpriteProperty.Y) == 4) {
        Gegner.set(LedSpriteProperty.Y, 0)
        Gegner.set(LedSpriteProperty.X, randint(0, 4))
    }
})
basic.forever(function () {
    basic.pause(150)
    Gegner.change(LedSpriteProperty.Y, 1)
})
basic.forever(function () {
    if (Spieler.isTouching(Gegner)) {
        basic.showString("Game Over!")
    }
})
