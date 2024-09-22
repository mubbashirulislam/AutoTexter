

---

# SMS Automation Tool

This project is a **Flask-based SMS Automation Tool** that allows users to send random SMS messages to a specific phone number at regular intervals. It uses the **Twilio API** to send SMS messages and is designed with a **dark-themed UI** for ease of use. The frontend is built using **HTML, CSS, and JavaScript**, while the backend handles the SMS sending logic.

## Features

- Send random SMS messages from a list at a customizable interval.
- Validate phone number format for better accuracy.
- Start and stop SMS automation via the UI.
- Real-time feedback with success and error notifications.
- Dark-themed UI following modern design standards.
- Full integration with the Twilio API for SMS sending.

## Prerequisites

Before using this tool, ensure you have the following:

1. **Twilio Account**:
   - You need a Twilio account and a verified Twilio phone number.
   - Get your **Account SID**, **Auth Token**, and **Twilio Phone Number** from the [Twilio Console](https://www.twilio.com/console).

2. **Python**: Make sure you have Python installed (version 3.6+ recommended).

3. **Node.js (optional)**: Required only for advanced JavaScript development.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/mubbashirulislam/AutoTexter.git
   cd AutoTexter
   ```

2. **Create and Activate a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install Required Packages**:
   Use the following command to install all required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**:
   Create a `.env` file in the root directory and add your Twilio credentials:
   ```bash
   TWILIO_ACCOUNT_SID=your_account_sid_here
   TWILIO_AUTH_TOKEN=your_auth_token_here
   TWILIO_PHONE_NUMBER=your_twilio_phone_number_here
   ```

## Running the Application

Once you've completed the installation, follow these steps to run the application:

1. **Start the Flask Server**:
   ```bash
   python main.py
   ```

   By default, the Flask server will start at `http://127.0.0.1:5000`.

2. **Open the Frontend**:
   - Open your browser and navigate to `http://127.0.0.1:5000` to access the web interface.

## How to Use

1. **Enter a Message**: Type the message you want to send in the "New Message" field.
   
2. **Enter the Phone Number**: Provide the recipient's phone number in **international format** (e.g., `+880123456789` for Bangladesh).
   
3. **Set the Interval**: Choose the time interval (in seconds) between each SMS message (must be between 1 and 3600 seconds).

4. **Start Sending SMS**: Click the **"Start Sending SMS"** button to begin the process.

5. **Stop SMS**: Click the **"Stop Sending SMS"** button to stop the automation.

6. **Check Status**: The status of SMS automation (active/inactive) will be shown on the page.

## API Endpoints

### 1. Start SMS Automation
   - **URL**: `/start`
   - **Method**: POST
   - **Request Body**:
     ```json
     {
       "phone": "+880123456789",
       "interval": 10,
       "messages": ["Hello!", "How are you?", "Have a nice day!"]
     }
     ```
   - **Response**:
     ```json
     {
       "message": "Started sending SMS to +880123456789 every 10 seconds."
     }
     ```

### 2. Stop SMS Automation
   - **URL**: `/stop`
   - **Method**: POST
   - **Response**:
     ```json
     {
       "message": "Stopped sending SMS."
     }
     ```

### 3. Get Automation Status
   - **URL**: `/status`
   - **Method**: GET
   - **Response**:
     ```json
     {
       "status": "active"
     }
     ```

## Tech Stack

- **Backend**: Python, Flask, Twilio API
- **Frontend**: HTML, CSS (Dark UI), JavaScript
- **Environment Management**: `python-dotenv` for environment variables
- **Threading**: Python's `threading` module to handle SMS automation

## Possible Issues & Debugging

1. **Twilio API Errors**: Ensure your Twilio credentials (Account SID, Auth Token, and Phone Number) are correct and your phone number is verified.
2. **Phone Number Validation**: The phone number must be in international format (e.g., `+880123456789`).
3. **Server Not Starting**: Ensure all dependencies are installed, and the `.env` file is correctly set up.

## Future Improvements

- Add user authentication to secure the app.
- Improve the UI to allow batch SMS sending with a CSV upload.
- Add more error logging and monitoring for better issue tracking.

## License

This project is licensed under the **MIT License**. Feel free to use and modify the tool as needed.

---
