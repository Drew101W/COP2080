from nicegui import ui
from random import shuffle
import asyncio

# Create list of 8 unique emojis, duplicate, and shuffle
emojis = ['🐶', '🐱', '🐭', '🐰', '🐼', '🦊', '🐸', '🐨']
EMOJIS = emojis * 2
shuffle(EMOJIS)

buttons = []
opened = []
matched = []
moves = 0


move_label = None
status_label = None


async def reset_pair(i, j):
    """Flip non-matching cards back after short delay."""
    await asyncio.sleep(0.5)
    buttons[i].text = '❓'
    buttons[j].text = '❓'
    opened.clear()


async def handle_click(idx):
    """Handles what happens when a card is clicked."""
    global moves

    if idx in matched or idx in opened:
        return

    buttons[idx].text = EMOJIS[idx]
    opened.append(idx)


    if len(opened) == 2:
        moves += 1
        move_label.text = f"Moves: {moves}"
        i, j = opened
        if EMOJIS[i] == EMOJIS[j]:
            matched.extend([i, j])
            opened.clear()
            if len(matched) == len(EMOJIS):
                status_label.text = "🎉 You win!"
        else:
            await reset_pair(i, j)


def restart_game():
    """Resets all game state and reshuffles emojis."""
    global EMOJIS, opened, matched, moves
    emojis = ['🐶', '🐱', '🐭', '🐰', '🐼', '🦊', '🐸', '🐨']
    EMOJIS = emojis * 2
    shuffle(EMOJIS)
    opened.clear()
    matched.clear()
    moves = 0
    move_label.text = "Moves: 0"
    status_label.text = ""
    for b in buttons:
        b.text = '❓'




ui.label("🐾 Memory Match Game 🧠").classes("text-2xl font-bold text-center my-4")

with ui.row().classes("justify-center items-center gap-4"):
    move_label = ui.label("Moves: 0").classes("text-lg")
    ui.button("Restart 🔁", on_click=restart_game, color='blue')
    status_label = ui.label("").classes("text-lg text-green-600 font-semibold")

with ui.grid(columns=4).classes("gap-3 justify-center"):
    for i in range(16):
        b = ui.button(
            '❓',
            on_click=lambda i=i: handle_click(i),
            color='gray'
        ).classes("text-white text-2xl")
        b.props('unelevated')
        buttons.append(b)


ui.run(title='Memory Game')
