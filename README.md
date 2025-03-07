# Onitama-AI-Agent

## 📌 Description
This repository contains the implementation of an artificial intelligence bot for the board game **Onitama** in **CodinGame**. The bot uses the **MiniMax** algorithm with **alpha-beta pruning** to make optimal decisions in turn-based matches.

This project was developed as a **final project** for the **Artificial Intelligence** course in the **second year** of the **Computer Engineering** degree at the **Universidad Pública de Navarra (UPNA)**.

## 🏆 Project Objectives
- Develop a **smart agent** capable of playing Onitama.
- Implement the **MiniMax** algorithm with **alpha-beta pruning** to improve the bot's performance.
- Evaluate and enhance the bot's decision-making using **game heuristics**.

## 🚀 Technologies Used
- **Python** 🐍
- **CodinGame SDK** 🎮
- **Search Algorithms**: MiniMax with alpha-beta pruning

## 📖 Basic Rules of Onitama
Onitama is a strategic two-player board game based on moving pieces according to **movement cards**. The objective is to capture the opponent’s master or move your own master to the opponent's starting square.

## 🏗️ Usage
### 1️⃣ Copy the Code
Go to [this link in CodinGame](https://www.codingame.com/ide/puzzle/onitama) and copy the provided code into the editor.

### 2️⃣ Run the Bot
Once the code is pasted in CodinGame, the bot will run directly without requiring any additional installations.

## 🤖 How the Bot Works
1. **Load the game state** from CodinGame's input.
2. **Generate possible moves** based on the available cards.
3. **Evaluate the best move** using **MiniMax with alpha-beta pruning**.
4. **Select and execute the optimal move**.
