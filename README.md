# pystore-webapp

Pystore-webapp is a comprehensive, three-tier web application designed for efficient grocery store management. This powerful system, built with a Python Flask backend and a user-friendly HTML/CSS/JS frontend, empowers you to streamline your store's operations, from product management to order tracking.

## Key Features:

*   **Product Management:** Easily add, edit, and remove products from your inventory.
*   **Order Management:** Create new orders, view past orders, and track their details.
*   **User-Friendly Interface:** An intuitive and responsive UI for seamless navigation and use.
*   **Robust Backend:** A reliable Python Flask server handles all business logic and data processing.
*   **MySQL Database:** All data is stored in a robust and scalable MySQL database.

## Technical Stack:

*   **Frontend:** HTML, CSS, JavaScript, Bootstrap
*   **Backend:** Python, Flask
*   **Database:** MySQL

## Installation

### Prerequisites

*   Python 3
*   MySQL Server
*   `pip` (Python package installer)

### Backend Setup

1.  **Install Python dependencies:**
    ```bash
    pip install mysql-connector-python flask flask-cors
    ```

2.  **Set up the database:**
    *   Make sure your MySQL server is running.
    *   Execute the `pystoredb_setup.sql` script to create the database and tables:
        ```bash
        mysql -u your_username -p < backend/pystoredb_setup.sql
        ```

3.  **Run the backend server:**
    ```bash
    cd backend
    python server.py
    ```
    The server will be running on `http://127.0.0.1:5000`.

### Frontend Setup

1.  Open the `ui/index.html` file in your web browser.

## Usage

*   **Manage Products:** Click on the "Manage Products" button to add, edit, or delete products.
*   **Create Orders:** Click on the "New Order" button to create a new customer order.
*   **View Orders:** The main dashboard displays a list of all past orders.

## Project Structure

```
pystore-webapp/
├── backend/
│   ├── server.py           # Flask backend server
│   ├── *.py                # Data Access Objects (DAOs) for database interaction
│   └── pystoredb_setup.sql # SQL script for database schema setup
├── ui/
│   ├── *.html              # HTML files for the user interface
│   ├── css/                # CSS stylesheets
│   └── js/                 # JavaScript files for frontend logic
└── README.md               # This file
```

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue.
