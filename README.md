# Cohere-Powered Chatbot

## Overview
This project is a Flask-based chatbot that uses the Cohere API to answer car-related queries. It includes a topic filtering utility to ensure responses stay relevant. The system is designed to handle user greetings separately and determine whether a given question is on-topic before sending it to the Cohere API.

## Folder Structure
```
📂 project_root/
│── 📂 static/             # Contains static files (CSS, JS, images)
│   └── style.css          # Main stylesheet for the project
│── 📂 templates/          # Contains HTML templates for rendering web pages
│   └── index.html         # Homepage of the project
│── 📂 utils/              # Contains utility scripts
│   ├── topic_filter.py    # Python script for filtering relevant topics
│   └── __pycache__/       # Cached Python files (automatically generated)
│── 📂 venv/               # Virtual environment for dependency management
│── .gitignore             # Git ignore file for unnecessary files
│── .env                   # Environment variables file
│── app.py                 # Main application script
│── requirements.txt       # Dependencies required for the project
│── README.md              # Documentation file
```

## Installation

1. Clone the repository:
   ```sh
   git clone <repository_url>
   cd project_root
   ```

2. Create and activate a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate     # On Windows
   ```

3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Requirements
The `requirements.txt` file includes the following dependencies:
```
flask==2.3.3
cohere==5.3.4
python-dotenv==1.0.0
```

## Usage

1. Run the Flask application:
   ```sh
   python app.py
   ```

2. Open the browser and visit:
   ```
   http://127.0.0.1:5000
   ```

## Environment Variables
Create a `.env` file in the root directory to store sensitive configuration values:
```
COHERE_API_KEY=your_cohere_api_key
```

## Features
- Uses the Cohere API to provide intelligent responses.
- Filters out off-topic questions using `utils/topic_filter.py`.
- Detects and tracks greetings separately.
- Provides a structured response system for user queries.

## Topic Filtering (`utils/topic_filter.py`)
The `topic_filter.py` script ensures that the chatbot only answers questions related to cars. It maintains a `last_topic` variable to detect follow-up questions.

### How It Works:
1. It checks whether a user’s question contains specific car-related keywords (e.g., "engine", "model", "mileage").
2. If a question lacks these keywords but follows a previous car-related query, it assumes it's a continuation.
3. If a question is deemed unrelated to cars, the chatbot informs the user that only car-related questions are supported.

## License
This project is licensed under the MIT License.

## Contributing
Feel free to open issues or submit pull requests.

## Requirement
- Create `venv/` file.
- Create `.env` file.

```COHERE_API_KEY = "YOUR_API_KEY" # Add your API key here ```

---
Maintained by **Sam**
