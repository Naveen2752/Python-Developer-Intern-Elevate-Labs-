# 🧮 Simple CLI Calculator

A lightweight and beginner-friendly **Command Line Interface (CLI) Calculator** built using Python.  
It supports four core arithmetic operations: **Addition**, **Subtraction**, **Multiplication**, and **Division**.

---

## 🚀 Features

- Clean and simple CLI interface  
- Supports `+`, `-`, `*`, `/`  
- Handles invalid inputs gracefully  
- Prevents division by zero  
- Keeps running until the user chooses to exit  

---

## 📁 Project Structure

The application is organized using separate functions for clarity and modularity:

### **Functions**

| Function | Description |
|---------|-------------|
| `add(a, b)` | Returns the sum of `a` and `b` |
| `subtract(a, b)` | Returns the difference between `a` and `b` |
| `multiply(a, b)` | Returns the product of `a` and `b` |
| `divide(a, b)` | Returns the quotient of `a` divided by `b`. Includes validation to prevent division by zero. |
| `main()` | Runs the main calculator loop and manages user interaction |

---

## 🔁 How the Calculator Works

Inside the `main()` function:

1. **Welcome Message**  
   Prints a friendly greeting.

2. **Infinite Loop**  
   Runs continuously until the user types `exit`.

3. **Operation Selection**  
   Prompts the user to choose an arithmetic operator or exit.

4. **Number Input**  
   Asks the user for two numbers and validates the input.

5. **Operation Processing**  
   Uses conditional statements to call the correct arithmetic function.

6. **Result Display**  
   Prints the computed result.

7. **Error Handling**  
   Uses `try-except` blocks to catch invalid inputs or unexpected errors.

---

## 🛠️ Installation & Usage

### **Prerequisites**
- Python 3 installed on your system

### **Run the Calculator**

Save your script as: calculator.py
Then open your terminal and run:

```bash
python calculator.py

### **📌 Example Interaction**
Welcome to the Simple CLI Calculator!
Choose an operation (+, -, *, /) or type 'exit': +
Enter the first number: 10
Enter the second number: 5
Result: 15
```
---

### **🤝 Contributing**

If you'd like to improve or extend this calculator, feel free to fork the repo and submit a pull request.




