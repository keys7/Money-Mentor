# Money Mentor

**Money Mentor** is an intelligent financial assistant designed to empower users with better financial habits and insights. Through its advanced chatbot and data visualization capabilities, Money Mentor simplifies personal finance management, offering tailored recommendations for spending, budgeting, and savings goals.

## Features

- **Chatbot Assistance:** Resolve financial queries using an NLP-powered chatbot.
- **Budget Tracking:** Monitor spending habits and budget adherence.
- **Visualization:** Interactive data displays for insightful financial analytics.
- **User-Friendly UI:** Intuitive design for seamless user interaction.

## Technology Stack

- **Frontend:** HTML, CSS, and JavaScript for a dynamic and responsive interface.
- **Backend:** Flask (Python) for server-side logic.
- **Database:** MySQL for efficient storage and retrieval of user data.
Here is the edited version with your additions incorporated:

---

**Libraries and Frameworks:**
- **Flask**: For building the web application.
- **google.generativeai**: To integrate generative AI for dynamic text or content generation.
- **MySQL (via `mysql.connector`)**: For storing and managing user data.
- **Flask-Bcrypt**: To handle password hashing and security.
- **Werkzeug**: For secure password generation and validation.
- **Markdown**: For rendering Markdown into HTML.
- **NumPy**: For numerical computations and handling arrays.
- **Pandas**: For data manipulation and analysis.
- **Textwrap**: For formatting and wrapping text lines.
  
--- 

- **APIs:** Integration with financial data APIs for real-time insights.

## Installation and Setup

### Prerequisites
1. Install [Anaconda](https://www.anaconda.com/) / [VSCode](https://code.visualstudio.com/).
2. Clone the repository:
   ```bash
   git clone https://github.com/keys7/Money-Mentor.git
   cd Money-Mentor
   ```

### Backend Setup
1. Create a virtual environment and activate it:
   ```bash
   conda create -n money-mentor python=3.8
   conda activate money-mentor
   ```
2. Install the required packages:
   ```bash
   conda install flask pytorch nltk mysql-connector-python
   ```
3. Initialize the NLTK toolkit:
   ```python
   python -m nltk.downloader punkt
   ```

### Database Configuration
1. Ensure MySQL is installed and running on your machine.
2. Create a database for Money Mentor and update the connection details in the `config.py` file.

### Launch the Application
1. Train the chatbot:
   ```bash
   python train.py
   ```
2. Start the server:
   ```bash
   python app.py
   ```

Visit `http://localhost:5000` in your browser to access Money Mentor.

## Contribution Guidelines

1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature-branch-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add your message"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-branch-name
   ```
5. Open a pull request for review.

## Future Enhancements

- **Mobile App:** Develop a React Native-based app for broader accessibility.
- **AI Optimization:** Enhance the chatbot's intelligence with advanced AI techniques.
- **Multi-Language Support:** Extend chatbot support to multiple languages.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
