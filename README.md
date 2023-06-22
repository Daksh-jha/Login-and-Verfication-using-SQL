# Login and Verification System Using SQL and Flask

Welcome to the Login and Verification System Using SQL and Flask repository. This project provides a secure and reliable user authentication and verification system built using SQL database and Flask framework.

## Description
The Login and Verification System allows users to create accounts, log in securely, and verify their email addresses. It ensures the privacy and security of user data by utilizing SQL database for storage and Flask framework for handling user authentication and verification.

## Features
- **User Registration**: Users can create accounts by providing necessary information such as username, email, and password.
- **Secure Password Storage**: User passwords are securely hashed and stored in the SQL database to ensure confidentiality.
- **Login Functionality**: Registered users can log in using their credentials to access their accounts.
- **Email Verification**: Users receive an email with a verification link upon registration to verify their email addresses.
- **Database Management**: SQL database is used to store user information and manage account-related data.

## Tech Stack
- **Python**: Python is used for the backend development and implementing the Flask framework.
- **Flask**: Flask is a micro web framework used for handling user authentication and request handling.
- **SQL**: SQL (Structured Query Language) is used for database management and storage.
- **HTML/CSS**: HTML and CSS are used for the frontend design and layout.

## Getting Started
To get started with the Login and Verification System, follow these steps:

1. Clone the repository: `git clone <repository_url>`
2. Install the necessary dependencies: `pip install -r requirements.txt`
3. Set up the SQL database and configure the connection in `config.py`.
4. Run the Flask application: `python app.py`
5. Access the application at `http://localhost:5000`

Make sure to update the email configuration in `config.py` to enable email sending for verification and password reset functionalities.

## Contributing
Contributions are welcome! If you have any ideas, improvements, or bug fixes, please submit a pull request.

## License
This project is licensed under the [MIT License](LICENSE). Feel free to use and modify the code for your own purposes.
