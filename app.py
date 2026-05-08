import sqlite3
from datetime import datetime

import pandas as pd
import streamlit as st


DB_NAME = "bookings.db"


PHYSICIANS = [
    "Dr. Alice Baker - Family Medicine",
    "Dr. Chris Horton - Cardiology",
    "Dr. Doris Lee - Orthopedics",
]


TIME_SLOTS = [
    "2026-05-14 09:00",
    "2026-05-14 10:00",
    "2026-05-14 11:00",
    "2026-05-14 14:00",
    "2026-05-15 09:00",
    "2026-05-15 10:00",
    "2026-05-15 11:00",
    "2026-05-15 14:00",
]


def apply_custom_style():
    """
    Apply custom CSS styling to the Streamlit app.
    """
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&family=Playfair+Display:wght@600;700&display=swap');
        
        * {
            font-family: 'Poppins', sans-serif;
        }

        .stApp {
            background: linear-gradient(135deg, #f8fafc 0%, #f0f4f8 100%);
            color: #1e293b;
        }

        .main-header {
            background: linear-gradient(135deg, #06b6d4 0%, #0891b2 100%);
            padding: 3.5rem 2.5rem;
            border-radius: 24px;
            color: white;
            margin-bottom: 2.5rem;
            text-align: center;
            box-shadow: 0 20px 60px rgba(6, 182, 212, 0.25);
            border: 1px solid rgba(255, 255, 255, 0.2);
            position: relative;
            overflow: hidden;
        }

        .main-header::before {
            content: '';
            position: absolute;
            top: -50%;
            right: -10%;
            width: 400px;
            height: 400px;
            background: radial-gradient(circle, rgba(255,255,255,0.15) 0%, transparent 70%);
            border-radius: 50%;
        }

        .main-header h1 {
            margin-bottom: 0.5rem;
            font-size: 2.8rem;
            font-family: 'Playfair Display', serif;
            font-weight: 700;
            letter-spacing: -1px;
            position: relative;
            z-index: 1;
        }

        .main-header p {
            font-size: 1.1rem;
            opacity: 0.95;
            font-weight: 300;
            position: relative;
            z-index: 1;
        }

        .section-card {
            background: linear-gradient(135deg, #ffffff 0%, #f5f9fc 100%);
            padding: 2rem;
            border-radius: 20px;
            border: 1px solid rgba(6, 182, 212, 0.15);
            box-shadow: 0 8px 32px rgba(6, 182, 212, 0.08);
            margin-bottom: 1.5rem;
            backdrop-filter: blur(10px);
            transition: all 0.3s ease;
        }

        .section-card:hover {
            border-color: rgba(6, 182, 212, 0.3);
            box-shadow: 0 12px 40px rgba(6, 182, 212, 0.15);
        }

        .step-label {
            color: #0891b2;
            font-weight: 600;
            font-size: 0.95rem;
            margin-bottom: 0.75rem;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }

        .step-number {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            width: 24px;
            height: 24px;
            background: linear-gradient(135deg, #06b6d4, #0891b2);
            border-radius: 50%;
            color: white;
            font-size: 0.8rem;
            font-weight: 700;
        }

        .small-muted {
            color: #64748b;
            font-size: 0.95rem;
            font-weight: 300;
        }

        div.stButton > button:first-child {
            background: linear-gradient(135deg, #06b6d4 0%, #0891b2 100%);
            color: white;
            border-radius: 12px;
            border: none;
            padding: 0.75rem 1.8rem;
            font-weight: 600;
            font-size: 1rem;
            cursor: pointer;
            transition: all 0.3s ease;
            box-shadow: 0 8px 20px rgba(6, 182, 212, 0.25);
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }

        div.stButton > button:first-child:hover {
            transform: translateY(-2px);
            box-shadow: 0 12px 30px rgba(6, 182, 212, 0.35);
        }

        div.stButton > button:first-child:active {
            transform: translateY(0);
        }

        .stTabs [data-baseweb="tab-list"] {
            gap: 1rem;
            border-bottom: 2px solid rgba(6, 182, 212, 0.2);
        }

        .stTabs [data-baseweb="tab"] {
            color: #64748b;
            padding: 1rem 1.5rem;
            border-radius: 12px 12px 0 0;
            font-weight: 500;
            transition: all 0.3s ease;
        }

        .stTabs [aria-selected="true"] {
            color: #0891b2;
            background: rgba(6, 182, 212, 0.1);
            border-bottom: 3px solid #0891b2;
        }

        div[data-testid="stMetricValue"] {
            color: #0891b2;
            font-size: 2.2rem;
            font-weight: 700;
            font-family: 'Playfair Display', serif;
        }

        div[data-testid="stMetricLabel"] {
            color: #64748b;
            font-size: 0.9rem;
        }

        .stMetric {
            background: linear-gradient(135deg, rgba(6, 182, 212, 0.08) 0%, rgba(8, 145, 178, 0.04) 100%);
            padding: 1.5rem;
            border-radius: 16px;
            border: 1px solid rgba(6, 182, 212, 0.15);
            backdrop-filter: blur(10px);
        }

        .stSelectbox, .stTextInput, .stTextArea {
            color: #1e293b;
        }

        .stSelectbox [data-baseweb="select"], 
        .stTextInput input,
        .stTextArea textarea {
            background: #ffffff !important;
            color: #1e293b !important;
            border: 1px solid rgba(6, 182, 212, 0.25) !important;
            border-radius: 12px !important;
            font-family: 'Poppins', sans-serif !important;
        }

        .stSelectbox [data-baseweb="select"]:focus,
        .stTextInput input:focus,
        .stTextArea textarea:focus {
            border-color: #06b6d4 !important;
            box-shadow: 0 0 0 3px rgba(6, 182, 212, 0.15) !important;
        }

        .stInfo, .stSuccess, .stWarning, .stError {
            border-radius: 12px !important;
            border-left: 4px solid !important;
        }

        .stInfo {
            background: rgba(6, 182, 212, 0.1) !important;
            border-left-color: #06b6d4 !important;
        }

        .stSuccess {
            background: rgba(34, 197, 94, 0.1) !important;
            border-left-color: #22c55e !important;
        }

        .stWarning {
            background: rgba(245, 158, 11, 0.1) !important;
            border-left-color: #f59e0b !important;
        }

        .stDataFrame {
            border-radius: 12px !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def get_connection():
    """
    Establish and return a connection to the SQLite database.
    """
    return sqlite3.connect(DB_NAME)


def initialize_database():
    """
    Initialize the SQLite database and create the bookings table if it does not exist.
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS bookings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            patient_name TEXT NOT NULL,
            patient_email TEXT NOT NULL,
            patient_phone TEXT NOT NULL,
            physician TEXT NOT NULL,
            appointment_time TEXT NOT NULL,
            reason TEXT NOT NULL,
            status TEXT NOT NULL,
            created_at TEXT NOT NULL
        )
        """
    )

    conn.commit()
    conn.close()


def get_booked_slots(physician):
    """
    Retrieve all booked appointment slots for a specific physician.
    Cancelled appointments do not block a time slot.
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT appointment_time
        FROM bookings
        WHERE physician = ?
        AND status != 'cancelled'
        """,
        (physician,),
    )

    booked_slots = [row[0] for row in cursor.fetchall()]
    conn.close()

    return booked_slots


def create_booking(patient_name, patient_email, patient_phone, physician, appointment_time, reason):
    """
    Create a new appointment booking in the database.

    Returns:
        bool: True if the booking was created, False if the slot was already booked.
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT id
        FROM bookings
        WHERE physician = ?
        AND appointment_time = ?
        AND status != 'cancelled'
        """,
        (physician, appointment_time),
    )

    existing_booking = cursor.fetchone()

    if existing_booking:
        conn.close()
        return False

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
        (
            patient_name,
            patient_email,
            patient_phone,
            physician,
            appointment_time,
            reason,
            "pending",
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        ),
    )

    conn.commit()
    conn.close()
    return True


def get_all_bookings():
    """
    Retrieve all bookings from the database.
    """
    conn = get_connection()

    bookings = pd.read_sql_query(
        """
        SELECT
            id,
            patient_name,
            patient_email,
            patient_phone,
            physician,
            appointment_time,
            reason,
            status,
            created_at
        FROM bookings
        ORDER BY appointment_time ASC
        """,
        conn,
    )

    conn.close()
    return bookings


def update_booking_status(booking_id, new_status):
    """
    Update the status of an existing booking.
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE bookings
        SET status = ?
        WHERE id = ?
        """,
        (new_status, booking_id),
    )

    conn.commit()
    conn.close()


def patient_booking_page():
    """
    Render the patient-facing booking interface.
    """
    st.markdown(
        """
        <div class="section-card">
            <h2 style="font-family: 'Playfair Display', serif; font-size: 2rem; margin-bottom: 0.5rem;">Schedule Your Appointment</h2>
            <p class="small-muted">
                Fill in the details below to book your appointment. We'll review your request and confirm your booking.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    left_col, right_col = st.columns([1.2, 0.8])

    with left_col:
        st.markdown(
            '<div class="step-label"><span class="step-number">1</span> Select Your Doctor</div>',
            unsafe_allow_html=True,
        )

        physician = st.selectbox("Doctor", PHYSICIANS, label_visibility="collapsed")

        booked_slots = get_booked_slots(physician)
        available_slots = [slot for slot in TIME_SLOTS if slot not in booked_slots]

        st.markdown(
            '<div class="step-label"><span class="step-number">2</span> Choose Your Time</div>',
            unsafe_allow_html=True,
        )

        if not available_slots:
            st.warning("No appointment times are currently available for this doctor.")
            return

        appointment_time = st.selectbox(
            "Available time slots",
            available_slots,
            label_visibility="collapsed",
        )

        st.markdown(
            f"""
            <div class="section-card" style="margin-top: 1.5rem;">
                <div style="display: flex; align-items: center; gap: 1rem;">
                    <div style="width: 40px; height: 40px; background: linear-gradient(135deg, #06b6d4, #0891b2); border-radius: 10px;"></div>
                    <div>
                        <div style="color: #475569; font-size: 0.9rem; text-transform: uppercase; letter-spacing: 0.5px;">Selected Appointment</div>
                        <div style="color: #0f172a; font-size: 1.1rem; font-weight: 600; margin-top: 0.25rem;">{appointment_time}</div>
                        <div style="color: #0f172a; font-size: 0.9rem; margin-top: 0.5rem; font-weight: 500;">{physician}</div>
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with right_col:
        st.markdown(
            """
            <div class="section-card">
                <h3 style="font-size: 1.1rem; margin-bottom: 1rem; color: #0891b2;">How It Works</h3>
                <div style="display: flex; flex-direction: column; gap: 1rem;">
                    <div>
                        <div style="color: #0891b2; font-weight: 600; font-size: 0.9rem;">Hours</div>
                        <div style="color: #64748b; font-size: 0.85rem; margin-top: 0.25rem;">Mon–Fri, 9:00 AM – 5:00 PM</div>
                    </div>
                    <div>
                        <div style="color: #0891b2; font-weight: 600; font-size: 0.9rem;">Status</div>
                        <div style="color: #64748b; font-size: 0.85rem; margin-top: 0.25rem;">Requests start as pending</div>
                    </div>
                    <div>
                        <div style="color: #0891b2; font-weight: 600; font-size: 0.9rem;">Next Step</div>
                        <div style="color: #64748b; font-size: 0.85rem; margin-top: 0.25rem;">You'll get confirmation via email</div>
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown(
        '<div class="step-label" style="margin-top: 2rem;"><span class="step-number">3</span> Your Information</div>',
        unsafe_allow_html=True,
    )

    with st.form("booking_form"):
        col1, col2 = st.columns(2)

        with col1:
            patient_name = st.text_input("Full name", placeholder="John Doe")
            patient_email = st.text_input("Email address", placeholder="john@example.com")

        with col2:
            patient_phone = st.text_input("Phone number", placeholder="(555) 123-4567")

        reason = st.text_area(
            "Reason for visit",
            placeholder="Describe your symptoms or reason for visiting...",
            height=100,
        )

        col_submit, col_empty = st.columns([1, 4])

        with col_submit:
            submitted = st.form_submit_button(
                "Request Appointment",
                width="stretch",
            )

        if submitted:
            if not patient_name or not patient_email or not patient_phone or not reason:
                st.error("Please fill in all fields before submitting.")
            elif "@" not in patient_email or "." not in patient_email:
                st.error("Please enter a valid email address.")
            elif len(patient_phone) < 7:
                st.error("Please enter a valid phone number.")
            else:
                booking_created = create_booking(
                    patient_name,
                    patient_email,
                    patient_phone,
                    physician,
                    appointment_time,
                    reason,
                )

                if booking_created:
                    st.success("Your appointment request has been submitted successfully!")
                    st.info("Check your email for confirmation and updates on your booking status.")
                else:
                    st.error(
                        "Sorry, this appointment time was just booked. Please choose another available time."
                    )


def admin_dashboard_page():
    """
    Render the clinic admin dashboard interface.
    """
    st.markdown(
        """
        <div class="section-card">
            <h2 style="font-family: 'Playfair Display', serif; font-size: 2rem; margin-bottom: 0.5rem;">Admin Dashboard</h2>
            <p class="small-muted">
                Manage patient appointments, review requests, and update booking statuses.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    bookings = get_all_bookings()

    if bookings.empty:
        st.info("No bookings yet. Appointments will appear here once patients submit requests.")
        return

    total_bookings = len(bookings)
    pending_count = len(bookings[bookings["status"] == "pending"])
    confirmed_count = len(bookings[bookings["status"] == "confirmed"])
    cancelled_count = len(bookings[bookings["status"] == "cancelled"])

    st.markdown("### Quick Stats")

    metric_col1, metric_col2, metric_col3, metric_col4 = st.columns(4)

    with metric_col1:
        st.metric("Total Bookings", total_bookings)

    with metric_col2:
        st.metric("Pending", pending_count)

    with metric_col3:
        st.metric("Confirmed", confirmed_count)

    with metric_col4:
        st.metric("Cancelled", cancelled_count)

    st.markdown("### Filter Bookings")

    filter_col1, filter_col2, filter_col3 = st.columns(3)

    with filter_col1:
        status_filter = st.selectbox(
            "Filter by status",
            ["All", "pending", "confirmed", "cancelled"],
        )

    with filter_col2:
        physician_filter = st.selectbox(
            "Filter by physician",
            ["All"] + PHYSICIANS,
        )

    with filter_col3:
        search_text = st.text_input(
            "Search patient name",
            placeholder="Enter patient name",
        )

    filtered_bookings = bookings.copy()

    if status_filter != "All":
        filtered_bookings = filtered_bookings[
            filtered_bookings["status"] == status_filter
        ]

    if physician_filter != "All":
        filtered_bookings = filtered_bookings[
            filtered_bookings["physician"] == physician_filter
        ]

    if search_text:
        filtered_bookings = filtered_bookings[
            filtered_bookings["patient_name"].str.contains(
                search_text,
                case=False,
                na=False,
            )
        ]

    st.markdown("### All Bookings")

    if filtered_bookings.empty:
        st.info("No bookings match the selected filters.")
    else:
        display_bookings = filtered_bookings.rename(
            columns={
                "id": "ID",
                "patient_name": "Patient",
                "patient_email": "Email",
                "patient_phone": "Phone",
                "physician": "Doctor",
                "appointment_time": "Appointment",
                "reason": "Reason",
                "status": "Status",
                "created_at": "Submitted",
            }
        )

        st.dataframe(display_bookings, width="stretch", hide_index=True)

    st.markdown("### Update Booking Status")

    col1, col2, col3 = st.columns([1.2, 1.2, 1])

    with col1:
        selected_booking_id = st.selectbox(
            "Select Booking ID",
            bookings["id"].tolist(),
        )

    with col2:
        new_status = st.selectbox(
            "New Status",
            ["pending", "confirmed", "cancelled"],
        )

    with col3:
        st.write("")
        if st.button("Update Status", width="stretch"):
            update_booking_status(selected_booking_id, new_status)
            st.success(f"Booking #{selected_booking_id} updated to '{new_status}'.")
            st.rerun()


def main():
    """
    Main entry point for the Streamlit application.
    """
    st.set_page_config(
        page_title="Clinic Booking System",
        layout="wide",
    )

    initialize_database()
    apply_custom_style()

    st.markdown(
        """
        <div class="main-header">
            <h1>Clinic Booking</h1>
            <p>A modern appointment management system for seamless healthcare scheduling</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    tab1, tab2 = st.tabs(["Patient Booking", "Admin Dashboard"])

    with tab1:
        patient_booking_page()

    with tab2:
        admin_dashboard_page()


if __name__ == "__main__":
    main()