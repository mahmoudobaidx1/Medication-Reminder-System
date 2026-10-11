# 💊 Medication Reminder System

A lightweight Python application designed to log and manage medication schedules using an **SQLite3** database. The system tracks drug intake times and alerts the user when it's time to take a specific medication by matching the scheduled time against the current system time.

---

## ✨ Features

- **Database Persistence**: Uses SQLite (`data.db`) to permanently store medication records.
- **Add New Medication**: Easily register new drug names along with their designated times via console input.
- **Fetch & Browse**: Retrieve and list all registered medications stored in the database.
- **Time Check & Alert**: Continuously checks the current system hour and minute (`HH.MM`) against stored medication schedules to trigger notifications.

---

## 📁 Project Structure

```text
.
├── additional.py    # Database handler (connection, inserting, fetching)
├── main.py          # Main application entry point & time-checking logic
└── data.db          # SQLite database storing the 'druglist' table
```

---

## 🛠️ Code Breakdown

### 1. `additional.py`
- Connects to the local SQLite database `data.db`.
- **`setup()`**: Prompts user for input (`time` and `name`) and inserts a new record into the `druglist` table.
- **`brows()`**: Queries all records from the `druglist` table and returns them as a list of tuples.

### 2. `main.py`
- Imports `datetime` and the `brows()` function from `additional.py`.
- Formats system time into `HH.MM`.
- Iterates over the retrieved drug list and checks if the scheduled time matches the current system time.

---

## 🚀 How to Run

### Prerequisites
- **Python 3.x** installed on your system.
- Standard libraries used: `sqlite3`, `datetime` (no external `pip` installations required).

### Execution Steps

1. **Add a new medication:**
   Call the `setup()` function inside `additional.py` or run a script that invokes it:
   ```bash
   python -c "import additional; additional.setup()"
   ```

2. **Run the time checker:**
   Execute the main script:
   ```bash
   python main.py
   ```

---

## 📌 Future Improvements
- [ ] Add parameterized SQL queries to prevent potential syntax errors/injections.
- [ ] Implement an infinite background loop with `time.sleep()` for continuous time monitoring.
- [ ] Add a graphical user interface (GUI) using Tkinter or PyQt.
