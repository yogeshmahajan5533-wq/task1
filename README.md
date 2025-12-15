# Caesar Cipher Program in Python

This project is a Python implementation of the **Caesar Cipher**, one of the simplest and oldest encryption techniques.  
The program allows users to **encrypt and decrypt text** by providing a message and an **integer shift value**.

---

## 📖 Description

The Caesar Cipher works by shifting each character in the message by a fixed number of positions.

- Letters are shifted within the English alphabet.
- Digits are shifted within the range `0–9`.
- Spaces and special characters remain unchanged.
- Decryption is done by reversing the shift value.

---

## ⚙️ Features

- Encrypt text using a Caesar Cipher
- Decrypt encrypted text
- Accepts integer input for shift value
- Supports:
  - Uppercase letters
  - Lowercase letters
  - Numbers
- Preserves spaces and symbols

---

## 🧩 How It Works

- Alphabet characters use **modulo 26** for wrapping around.
- Digits use **modulo 10**.
- Decryption uses the negative of the shift value.

---

## ▶️ How to Run

1. Ensure Python is installed on your system.
2. Save the program as `caesar_cipher.py`.
3. Open the terminal or command prompt.
4. Execute the program:

```bash
python caesar_cipher.py

