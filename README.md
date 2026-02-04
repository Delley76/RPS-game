# Rock Paper Scissors Game

Hey! So I made this little RPS game in Python because I was bored one afternoon and wanted to practice my tkinter skills. Nothing fancy, just a simple GUI where you can play against the computer.

## What it does

It's literally just rock paper scissors lol. You click one of the emoji buttons (rock, paper, or scissors) and the computer picks randomly. Then it shows who won and keeps score. That's pretty much it.

## Running it

You just need Python installed (I used 3.8 but any recent version should work fine). Tkinter comes with Python so you don't need to install anything extra which is nice.

```
python rps_game.py
```

Just run that and the window pops up. Click the emojis to play.

## Why I made this

Honestly just wanted something quick to build. I've been meaning to get better at GUI stuff and this seemed like a good starter project. Plus RPS is simple enough that I could finish it in one sitting without getting too frustrated.

## The code

It's not the cleanest code ever but it works! I used a class to organize everything which maybe is overkill for something this small, but whatever. The logic is pretty straightforward:
- You pick your move
- Computer picks randomly  
- Check who won using a simple comparison
- Update the scores
- Show the result with colors (green for win, red for loss, orange for tie)

There's also a reset button if you want to start the scores over.

## Some notes

- The emojis might look different depending on your OS, that's just how emojis work
- I went with a purple/blue color scheme because I thought it looked decent
- Score doesn't save when you close the app, it just resets. Could add that later if I feel like it

## Issues/bugs

Haven't really found any yet but if you do let me know I guess? It's pretty basic so there's not much that can go wrong.

## Future stuff (maybe)

If I get motivated I might add:
- Best of 5 mode or something
- Different difficulty levels (though idk how you'd make RPS harder)
- Sound effects maybe?
- A dark mode toggle

But honestly I'll probably just leave it as is. It does what it needs to do.

---

Feel free to use this code for whatever. Learn from it, modify it, I don't really care. Just have fun with it!# RPS-game
