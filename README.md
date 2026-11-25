# To Do List (PyQt6)

Μια desktop εφαρμογή διαχείρισης εργασιών (To-Do List) φτιαγμένη με **Python** και **PyQt6**, με προσαρμοσμένο στυλ μέσω **CSS (QSS)**, SVG εικονίδια και αποθήκευση των εργασιών σε αρχείο **JSON**.

## Λειτουργίες

- **Προσθήκη Εργασιών:** Εισαγωγή νέων εργασιών μέσω πεδίου κειμένου (`QLineEdit`) και κουμπιού **Add**.
- **Σήμανση Ολοκλήρωσης:** Κάθε εργασία εμφανίζεται ως ξεχωριστό custom widget με checkbox, εφαρμόζοντας αυτόματα διαγράμμιση κειμένου (`line-through`) όταν ολοκληρώνεται.
- **Διαγραφή Εργασιών:** Αφαίρεση μεμονωμένων εργασιών από τη λίστα μέσω κουμπιού διαγραφής και custom PyQt signals (`pyqtSignal`).
- **Αποθήκευση σε JSON:** Φόρτωση και αποθήκευση των εργασιών και της κατάστασής τους (ολοκληρωμένη ή μη) στο αρχείο `static/tasks.json`.
- **Προσαρμοσμένο UI:** Μοντέρνα εμφάνιση με εξωτερικά αρχεία στυλ (`.css`) και vector εικονίδια (`.svg`).

---

##  Τεχνολογίες & Βιβλιοθήκες

- [Python 3](https://www.python.org/)
- [PyQt6](https://pypi.org/project/PyQt6/) — Δημιουργία γραφικού περιβάλλοντος (`QtWidgets`, `QtGui`, `QtCore`)
- **JSON (`json`)** — Τοπική αποθήκευση δεδομένων (ενσωματωμένη στην Python)
- **CSS / Qt Style Sheets (QSS)** — Προσαρμογή εμφάνισης παραθύρων και widgets

---

## 🚀 Εγκατάσταση & Εκτέλεση

### Προαπαιτούμενα
- **Python 3.8+**

### Βήματα

1. **Κλωνοποίηση του repository:**
   ```bash
   git clone [https://github.com/mariach26/](https://github.com/mariach26/)<repository-name>.git
   cd <repository-name>
   ```

2. **Εγκατάσταση εξαρτήσεων:**
   ```bash
   pip install PyQt6
   ```

3. **Εκτέλεση της εφαρμογής:**
   ```bash
   python main.py
   ```

---
##  Δομή Project

```text
<repository-name>/
├── main.py                  # Κύρια λογική εφαρμογής, signals & διαχείριση tasks.json
├── ui/
│   ├── main_ui.py           # Διάταξη κεντρικού παραθύρου (Ui_MainWindow)
│   └── task_ui.py           # Custom widget για κάθε εργασία (Ui_TaskForm)
├── static/
│   ├── tasks.json           # Αποθήκευση λίστας εργασιών
│   ├── style.css            # Στυλ κεντρικού παραθύρου
│   ├── style_task.css       # Στυλ κάρτας εργασίας
│   └── icons/               # Εικονίδια SVG (list.svg, add_min.svg, add_black.svg, close.svg)
└── README.md                # Τεκμηρίωση του project
```
