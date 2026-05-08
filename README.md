# Clinic Booking System

A simple patient appointment booking system built with Python, Streamlit, SQLite, and Pandas.

## How to Run

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Add sample data:

```bash
python sample_data.py
```

3. Run the app:

```bash
streamlit run app.py
```

4. Open the local Streamlit link shown in the terminal

## What I Built

I built a clinic booking system with two main parts:

**Patient Booking Interface**

* Patients can choose a physician.
* Patients can select an available appointment time.
* Patients can enter their name, email, phone number, and reason for visit.
* New bookings are saved with `pending` status.

**Admin Dashboard**

* Admins can view all bookings.
* Admins can see booking statistics.
* Admins can update booking statuses to `pending`, `confirmed`, or `cancelled`.

## Key Technical and Product Decisions

I used **Streamlit** because it allows fast development of an interactive Python web app without a separate frontend.

I used **SQLite** because it is lightweight, local, and easy to set up.

I used **mock data** for physicians and time slots to keep the project simple while still showing the full booking flow.

New bookings start as `pending` so clinic staff can review them before confirming or cancelling.

Cancelled bookings do not block appointment times, so those slots become available again.

## What I Would Improve With More Time

With more time, I would add:

* Admin login
* Email confirmations
* Better email and phone validation
* Separate schedules for each physician
* Admin controls for adding or removing time slots
* Search and filtering in the admin dashboard
* Stronger double-booking protection
* Unit tests
* Deployment to a public URL
* Calendar-style appointment selection

## Project Structure

```
├── app.py
├── sample_data.py
├── requirements.txt
├── bookings.db
└── README.md
```

## Technologies Used

Python, Streamlit, SQLite, Pandas
```