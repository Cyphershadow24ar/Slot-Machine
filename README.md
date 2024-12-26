# Slot Machine Simulation 🎰

This is a Python-based terminal game that simulates a slot machine. Players can deposit money, place bets on multiple lines, and spin the reels to test their luck. The game is interactive, user-friendly, and allows you to manage your balance while enjoying the thrill of gambling (virtually)!

---

## Features
- **Flexible Betting:** Bet on 1 to 3 lines with customizable amounts.
- **Symbolic Rewards:** Different symbols have different probabilities and payout values:
  - `A`: Rare, high payout.
  - `B`, `C`, `D`: Increasingly common with decreasing payouts.
- **Realistic Gameplay:** Randomized spins and dynamic win/loss calculations.
- **Balance Management:** Track deposits, bets, and winnings seamlessly.

---

## How to Play
1. **Deposit Money:** Enter the amount you want to deposit to start playing.
2. **Choose Lines:** Decide how many lines (1–3) you want to bet on.
3. **Place Bets:** Set your bet amount per line, within the minimum and maximum limits.
4. **Spin:** Watch the reels spin and check for winnings!
5. **Repeat or Quit:** Keep playing until you choose to quit or your balance runs out.

---

## Rules
1. **Symbols and Values:**
   - `A`: 2 occurrences, payout multiplier 5x.
   - `B`: 4 occurrences, payout multiplier 4x.
   - `C`: 6 occurrences, payout multiplier 3x.
   - `D`: 8 occurrences, payout multiplier 2x.
2. **Winning Lines:** A line wins if all symbols on it match across all columns.
3. **Bet Limits:** Minimum ₹100 and maximum ₹1,000,000 per line.

---

## Setup
1. Ensure Python is installed on your system.
2. Download the `Solt_machine.py` file from this repository.
3. Run the file in a terminal using the command:
   ```bash
   python Solt_machine.py


# Code Highlights
get_slot_machine_spin(rows, cols, symbols): Generates random symbols for the slot machine.
check_winnings(columns, lines, bet, values): Calculates winnings based on matching symbols and bets.
main(): The main game loop for managing balance, user inputs, and game interactions.

# How to Contribute

1. Contributions are welcome! Here’s how you can get involved:
   - **Fork the Repository:** Click the "Fork" button on the top-right corner of this page to create your copy of the repository.
2. **Clone Your Fork:** Use the following command to clone the repository to your local machine:
   ```bash
   git clone https://github.com/Cyphershadow24ar/slot-machine.git
   
3. Make Changes: Improve the code, fix bugs, or add new features. Please ensure your code follows best practices and is well-documented.
4. Test Your Changes: Run the program to ensure everything works as expected.
5. Submit a Pull Request: Push your changes to your fork and open a pull request. Provide a detailed description of your changes and their benefits.

# Future Enhancements
Add a graphical interface for better user experience.
Incorporate more symbols, paylines, and bonus features.
Save player progress and statistics.

# Enjoy your game and may luck be on your side! 🍀






