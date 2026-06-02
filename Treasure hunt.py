import random
import os

# ── Colors ────────────────────────────────────────────────
RESET  = "\033[0m"
BOLD   = "\033[1m"
YELLOW = "\033[93m"
CYAN   = "\033[96m"
GREEN  = "\033[92m"
RED    = "\033[91m"
DIM    = "\033[2m"

# ── Grid setup ────────────────────────────────────────────
GRID_SIZE = 5
grid = [["." for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

treasure_x = random.randint(0, GRID_SIZE - 1)
treasure_y = random.randint(0, GRID_SIZE - 1)

player_x, player_y = 0, 0
grid[player_x][player_y] = "P"
moves = 0

# ── Display ───────────────────────────────────────────────
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_grid():
    """Display the grid with colors and symbols."""
    print(f"\n  {DIM}┌{'───┬' * (GRID_SIZE - 1)}───┐{RESET}")
    for i, row in enumerate(grid):
        print("  │", end="")
        for cell in row:
            if cell == "P":
                print(f" {CYAN}{BOLD}🧭{RESET} │", end="")
            else:
                print(f" {DIM}·{RESET} │", end="")
        print()
        if i < GRID_SIZE - 1:
            print(f"  {DIM}├{'───┼' * (GRID_SIZE - 1)}───┤{RESET}")
    print(f"  {DIM}└{'───┴' * (GRID_SIZE - 1)}───┘{RESET}\n")

def move_player(direction):
    """Move the player on the grid."""
    global player_x, player_y, moves
    grid[player_x][player_y] = "."
    moved = True

    if direction == "up" and player_x > 0:
        player_x -= 1
    elif direction == "down" and player_x < GRID_SIZE - 1:
        player_x += 1
    elif direction == "left" and player_y > 0:
        player_y -= 1
    elif direction == "right" and player_y < GRID_SIZE - 1:
        player_y += 1
    else:
        print(f"  {RED}⚠  You hit the boundary!{RESET}")
        moved = False

    grid[player_x][player_y] = "P"
    if moved:
        moves += 1

def check_treasure():
    """Check if the player found the treasure."""
    return player_x == treasure_x and player_y == treasure_y

# ── Game start ────────────────────────────────────────────
clear()
print(f"\n  {YELLOW}{BOLD}{'═' * 30}{RESET}")
print(f"  {YELLOW}{BOLD}    🏴‍☠️  TREASURE HUNT  🏴‍☠️{RESET}")
print(f"  {YELLOW}{BOLD}{'═' * 30}{RESET}")
print(f"\n  {DIM}A treasure is hidden on the grid.{RESET}")
print(f"  {DIM}Navigate with: up / down / left / right{RESET}")
display_grid()

# ── Game loop ─────────────────────────────────────────────
while True:
    move = input(f"  {CYAN}➤ Move:{RESET} ").strip().lower()

    if move not in ["up", "down", "left", "right"]:
        print(f"  {RED}Invalid input. Try: up, down, left, right{RESET}\n")
        continue

    move_player(move)
    clear()

    print(f"\n  {YELLOW}{BOLD}{'═' * 30}{RESET}")
    print(f"  {YELLOW}{BOLD}    🏴‍☠️  TREASURE HUNT  🏴‍☠️{RESET}")
    print(f"  {YELLOW}{BOLD}{'═' * 30}{RESET}")
    print(f"  {DIM}Moves: {moves}   |   Position: ({player_x}, {player_y}){RESET}")
    display_grid()

    if check_treasure():
        print(f"  {GREEN}{BOLD}🎉 You found the treasure in {moves} moves!{RESET}")
        print(f"  {GREEN}   Well done, treasure hunter!{RESET}\n")
        break
    else:
        print(f"  {DIM}Keep searching...{RESET}\n")