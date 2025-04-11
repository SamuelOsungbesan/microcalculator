import sqlite3
from datetime import datetime


class MicroscopeCalculator:
    def __init__(self, db_path="specimens.db"):
        self.db_path = db_path
        self.setup_database()

    def setup_database(self):
        """Create the database and table if they don't exist"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS specimens (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            magnified_size REAL NOT NULL,
            magnification_factor REAL NOT NULL,
            actual_size REAL NOT NULL,
            date_added TIMESTAMP
        )
        ''')

        conn.commit()
        conn.close()

    def calculate_actual_size(self, magnified_size, magnification_factor):
        """Calculate the actual size by dividing magnified size by magnification factor"""
        if magnification_factor <= 0:
            raise ValueError("Magnification factor must be greater than zero")

        return magnified_size / magnification_factor

    def save_specimen(self, name, magnified_size, magnification_factor):
        """Save specimen data to the database"""
        actual_size = self.calculate_actual_size(magnified_size, magnification_factor)

        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute('''
        INSERT INTO specimens (name, magnified_size, magnification_factor, actual_size, date_added)
        VALUES (?, ?, ?, ?, ?)
        ''', (name, magnified_size, magnification_factor, actual_size, datetime.now()))

        conn.commit()
        conn.close()

        return actual_size

    def get_all_specimens(self):
        """Retrieve all specimens from the database"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM specimens ORDER BY date_added DESC')
        specimens = cursor.fetchall()

        conn.close()

        return specimens


# Test the core functionality
if __name__ == "__main__":
    calculator = MicroscopeCalculator()

    # Test calculation
    actual_size = calculator.calculate_actual_size(magnified_size=500, magnification_factor=100)
    print(f"Test calculation: Actual size = {actual_size} units")

    # Test saving to database
    calculator.save_specimen("Test Specimen", 500, 100)

    # Test retrieving from database
    specimens = calculator.get_all_specimens()
    print("\nStored specimens:")
    for specimen in specimens:
        print(f"ID: {specimen[0]}, Name: {specimen[1]}, Magnified Size: {specimen[2]}, "
              f"Magnification: {specimen[3]}, Actual Size: {specimen[4]}, Date: {specimen[5]}")