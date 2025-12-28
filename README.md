# 🎰 Simple Bet (Slot Machine CLI App)

A **command-line slot machine betting game** built in Python.  
This project focuses on **core programming fundamentals**: control flow, data structures, randomness, and clean function-based design.

---

## 📌 Overview

**Simple Bet** simulates a slot machine where the user:
- Deposits money
- Chooses how many lines to bet on
- Places a bet per line
- Spins the slot machine
- Wins or loses based on matching symbols across rows

The game runs entirely in the terminal and maintains balance until the user quits.

---

## 🧠 Key Concepts Practiced

This project was intentionally built to strengthen fundamentals:

- Function design and data flow
- Returning values vs global state
- Nested loops and control flow
- Dictionary-based configuration
- Random sampling without replacement
- Row vs column data representation
- Input validation and error handling
- Debugging logical and indexing errors
- Clean separation of responsibilities

---

## 🎮 How the Game Works

### 1️⃣ Deposit
User deposits an initial balance.

### 2️⃣ Choose Lines
User selects how many horizontal lines to bet on (1–3).

### 3️⃣ Place Bet
User sets a bet amount **per line**, validated against min/max limits.

### 4️⃣ Spin
- The slot machine generates a **3×3 grid**
- Symbols are generated column-wise
- Rows are evaluated for winning combinations

### 5️⃣ Winnings
- A line wins **only if all symbols match**
- Winnings = `symbol value × bet`
- Multiple lines can win in a single spin

---

## 🔢 Symbol Configuration

### Symbol Frequency
``python


symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}


# Project Structure 
```
simplepy/
├── main.py
├── README.md
├── pyproject.toml
├── uv.lock
├── .gitignore
└── .python-version


---

## ▶️ How to Run

### 1️⃣ Clone the repository
```bash
git clone <repo-url>
cd simplepy
