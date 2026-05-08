# Clinic Booking System

A simple patient appointment booking system built with Python, Streamlit, SQLite, and Pandas.

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/celinec41/Booking-System.git
cd Booking-System
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Add sample data:

```bash
python sample_data.py
```

Note: `sample_data.py` only needs to be run once. Running it multiple times may insert duplicate sample bookings.

4. Run the app:

```bash
streamlit run app.py
```

5. Open the Local URL shown in the terminal.

For example:

```text
http://localhost:8501
```

## Optional: Using a Virtual Environment

If you want to keep the project dependencies separate, you can create a virtual environment first:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

On Windows, activate it with:

```bash
venv\Scripts\activate
```

## What I Built

I built a clinic booking system with two main parts:

**Patient Booking Interface**

* Patients can choose a physician.
* Patients can select an available appointment time.
* Patients can enter their name, email, phone number, and reason for visit.
* New bookings are saved with `pending` status.
* Booked time slots are protected from double booking.

**Admin Dashboard**

* Admins can view all bookings.
* Admins can see booking statistics.
* Admins can update booking statuses to `pending`, `confirmed`, or `cancelled`.

## Key Technical and Product Decisions

I used **Streamlit** because it allows fast development of an interactive Python web app without needing a separate frontend.

I used **SQLite** because it is lightweight, local, and easy to set up for a small project.

I used **Pandas** to display booking data clearly in the admin dashboard.

I used **mock data** for physicians and time slots to keep the project simple while still showing the full booking flow.

New bookings start as `pending` so clinic staff can review them before confirming or cancelling.

Cancelled bookings do not block appointment times, so those slots become available again.

I added basic validation so patients must enter required information before submitting a booking.

## What I Would Improve With More Time

* Admin login
* Email confirmations
* Separate schedules for each physician
* Admin controls for adding or removing time slots
* Calendar-style appointment selection

## Project Structure

```text
├── app.py
├── sample_data.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Technologies Used

* Python
* Streamlit
* SQLite
* Pandas
