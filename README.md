# Clinic Booking System

A simple patient appointment booking system built with Python, Streamlit, SQLite, and Pandas.

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/celinec41/Booking-System.git
cd Booking-System
```

2. Create a Python virtual environment:

```bash
python3 -m venv venv
```

3. Activate the virtual environment:

On Mac/Linux:

```bash
source venv/bin/activate
```

On Windows:

```bash
venv\Scripts\activate
```

4. Install dependencies:

```bash
pip install -r requirements.txt
```

5. Add sample data:

```bash
python sample_data.py
```

Note: `sample_data.py` only needs to be run once. Running it multiple times may insert duplicate sample bookings.

6. Run the app:

```bash
streamlit run app.py
```

7. Open the app in your browser.

The app may open automatically. If not, copy the Local URL shown in the terminal and paste it into your browser.

Note: The Streamlit app runs locally while the terminal command is active. If the browser shows a connection error, stop the app with `Ctrl + C` and run:

```bash
streamlit run app.py
```

again.

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
* Better UI styling
* Search and filter options for admin bookings

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
