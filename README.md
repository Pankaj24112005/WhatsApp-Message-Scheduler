# WhatsApp Message Scheduler using Twilio

## Overview

WhatsApp Message Scheduler is a Python-based automation tool that allows users to schedule and send WhatsApp messages at a specific date and time using the Twilio WhatsApp API.

The application accepts recipient details, message content, and a scheduled delivery time from the user. It then automatically waits until the specified time and sends the message through Twilio's WhatsApp service.

This project demonstrates API integration, scheduling logic, date and time manipulation, exception handling, and automation using Python.

---

## Features

* Send WhatsApp messages using Twilio API
* Schedule messages for future delivery
* User-friendly command-line interface
* Date and time validation
* Automatic message dispatch
* Error handling for failed message delivery
* Simple and lightweight implementation

---

## Technologies Used

* Python 3.x
* Twilio API
* Datetime Module
* Time Module

---

## Project Structure

```text
whatsapp-message-scheduler/
│
├── main.py
├── requirements.txt
└── README.md
```

---

## Prerequisites

Before running this project, ensure you have:

* Python 3.8 or higher installed
* A Twilio account
* Twilio WhatsApp Sandbox enabled
* Account SID and Auth Token from Twilio

---

## Clone the Repository

```bash
git clone https://github.com/Pankaj24112005/whatsapp-message-scheduler.git

cd whatsapp-message-scheduler
```

Replace the repository URL with your actual GitHub repository link.

---

## Create a Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

Or install Twilio manually:

```bash
pip install twilio
```

---

## Configure Twilio Credentials

Open the Python file and replace the following values:

```python
account_sid = "YOUR_ACCOUNT_SID"
auth_token = "YOUR_AUTH_TOKEN"
```

You can find these credentials in your Twilio Console Dashboard.

---

## Join Twilio WhatsApp Sandbox

1. Login to your Twilio account.
2. Navigate to the WhatsApp Sandbox section.
3. Follow the instructions provided by Twilio.
4. Join the sandbox from your WhatsApp account.
5. Verify that your WhatsApp number is connected.



---

## Running the Application

Execute the Python script:

```bash
python main.py
```

You will be prompted to enter:

```text
Recipient Name
Recipient WhatsApp Number
Message Content
Scheduled Date
Scheduled Time
```

Example:

```text
Enter recipient's name: John

Enter recipient's WhatsApp number with country code:
+919876543210

Enter the message you want to send:
Meeting reminder at 10 AM

Enter the date to send the message:
2026-07-10

Enter the time to send the message:
09:55
```

---

## How It Works

### Step 1

The application collects user input:

* Recipient Name
* Recipient Number
* Message Content
* Date
* Time

### Step 2

The entered date and time are converted into a Python datetime object.

### Step 3

The system calculates the difference between the current time and the scheduled time.

### Step 4

The application waits until the scheduled time using the `time.sleep()` function.

### Step 5

Once the scheduled time is reached, the message is sent using Twilio's WhatsApp API.

---

## Example Output

```text
Message scheduled to be sent to John at 2026-07-10 09:55:00

Message sent successfully!
Message SID: SMxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

---

## Error Handling

The application handles:

* Invalid date and time formats
* Scheduling messages in the past
* Twilio API failures
* Network-related issues

Example:

```text
Scheduled time is in the past.
Please enter a future date and time.
```

---

## Requirements File

Create a file named `requirements.txt` and add:

```text
twilio
```

Install dependencies using:

```bash
pip install -r requirements.txt
```

---

## Future Improvements

* Web-based dashboard using Flask or FastAPI
* User authentication system
* Message history tracking
* Message editing and cancellation
* Contact management
* Bulk messaging support
* Database integration
* AI-powered message generation
* Voice-to-message scheduling
* Real-time delivery status monitoring

---

## Learning Outcomes

This project helps developers understand:

* API Integration
* Python Automation
* Datetime Handling
* Scheduling Tasks
* Exception Handling
* WhatsApp Business API Concepts
* Command-Line Application Development

---

## Author

Pankaj Jadhav

Artificial Intelligence and Machine Learning Engineer

GitHub: https://github.com/Pankaj24112005

LinkedIn: https://www.linkedin.com/in/pankaj-jadhav-82453a2a7/

---

## License

This project is licensed under the MIT License.

Feel free to use, modify, and distribute this project for educational and personal purposes.
