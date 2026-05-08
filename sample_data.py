import sqlite3
from datetime import datetime

DB_NAME = "bookings.db"

def add_sample_data():
    """Add sample booking data for testing"""
    conn = sqlite3.connect(DB_NAME, timeout=30.0, check_same_thread=False)
    cursor = conn.cursor()

    # Sample bookings
    sample_bookings = [
        (
            "John Smith",
            "john.smith@email.com",
            "(555) 123-4567",
            "Dr. Alice Baker - Family Medicine",
            "2026-05-14 09:00",
            "Annual checkup and blood pressure check",
            "confirmed",
            "2026-05-07 10:30:00"
        ),
        (
            "Sarah Johnson",
            "sarah.j@email.com",
            "(555) 234-5678",
            "Dr. Chris Horton - Cardiology",
            "2026-05-14 10:00",
            "Heart palpitations and chest discomfort",
            "pending",
            "2026-05-07 11:15:00"
        ),
        (
            "Michael Davis",
            "m.davis@email.com",
            "(555) 345-6789",
            "Dr. Doris Lee - Orthopedics",
            "2026-05-14 11:00",
            "Knee pain from sports injury",
            "confirmed",
            "2026-05-07 09:45:00"
        ),
        (
            "Emma Wilson",
            "emma.w@email.com",
            "(555) 456-7890",
            "Dr. Alice Baker - Family Medicine",
            "2026-05-14 14:00",
            "Flu symptoms and fever",
            "pending",
            "2026-05-07 02:20:00"
        ),
        (
            "James Brown",
            "j.brown@email.com",
            "(555) 567-8901",
            "Dr. Chris Horton - Cardiology",
            "2026-05-15 09:00",
            "Hypertension follow-up",
            "cancelled",
            "2026-05-06 14:00:00"
        ),
        (
            "Lisa Anderson",
            "lisa.a@email.com",
            "(555) 678-9012",
            "Dr. Doris Lee - Orthopedics",
            "2026-05-15 10:00",
            "Back pain and spinal issues",
            "pending",
            "2026-05-07 03:10:00"
        ),
    ]

    try:
        for booking in sample_bookings:
            cursor.execute(
                """
                INSERT INTO bookings (
                    patient_name,
                    patient_email,
                    patient_phone,
                    physician,
                    appointment_time,
                    reason,
                    status,
                    created_at
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """,
                booking
            )
        
        conn.commit()
        print(f"✓ Added {len(sample_bookings)} sample bookings successfully!")
        
        # Show what was added
        cursor.execute("SELECT COUNT(*) FROM bookings")
        total = cursor.fetchone()[0]
        print(f"Total bookings in database: {total}")
        
    except Exception as e:
        print(f"Error adding sample data: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    add_sample_data()