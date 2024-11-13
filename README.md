# Capstone Project 

# Team :-

Register Number - Name
21BCE10058 - Yash Yadav
21BCE10069 - Chirag
21BCE10139 - Vaibhav Grover
21BCE10304 - Udit Tyagi
21BCE11242 - Shubham Verma
Here’s a revised README for Money Mentor that reflects MySQL as the database and a T1 architecture. This should provide a clear structure and outline for new users and contributors:

---

# Money Mentor

Money Mentor is a financial management web application that allows users to manage expenses, set budgets, and make informed financial decisions. It is built with a robust backend using MySQL for data management in a T1 architecture.

## Table of Contents
- [Features](#features)
- [Getting Started](#getting-started)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Database Setup](#database-setup)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features
- **User Authentication**: Secure sign-up and login functionality.
- **Budget Tracking**: Ability to set and track budgets.
- **Expense Logging**: Record and categorize expenses to track spending patterns.
- **MySQL Database**: Data is securely stored and managed using MySQL.
- **T1 Architecture**: Supports single-server deployment, ideal for small to medium-scale applications.
- **Responsive UI**: Designed to be accessible on desktop and mobile devices.
- **Analytics**: Visual representation of budget vs. spending.

## Getting Started

To get a local copy up and running, follow these instructions.

### Prerequisites
- [Node.js](https://nodejs.org/) and npm (Node Package Manager)
- MySQL server setup locally or on a cloud provider
- A web browser

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/keys7/Money-Mentor.git
   cd Money-Mentor
   ```

2. **Install dependencies**:
   ```bash
   npm install
   ```

3. **Database Setup**:
   - Ensure your MySQL server is running.
   - Create a database for Money Mentor:
     ```sql
     CREATE DATABASE money_mentor_db;
     ```
   - Import the provided SQL schema to set up tables:
     ```bash
     mysql -u yourUsername -p money_mentor_db < path/to/schema.sql
     ```
   - Update the database configuration in `app.py` to connect to your MySQL instance.

4. **Run the Application**:
   ```bash
   npm start
   ```

5. **Access the application**:
   Open a browser and navigate to `http://localhost:3000` to start using Money Mentor locally.

## Database Setup

- Money Mentor uses a T1 architecture with MySQL to manage and store data efficiently.
- The main tables include:
  - **Users**: Stores user details and authentication information.
  - **Budgets**: Stores budget limits set by users.
  - **Expenses**: Logs user expenses with category and date.

Make sure to adjust your MySQL credentials in the application’s configuration file before running.

## Usage

- **Sign In**: Access your account by signing in with your username and password.
- **Register**: New users can sign up to create an account.
- **Dashboard**: View your budget, expenses, and visual insights.
- **Manage Finances**: Set budgets, log expenses, and track financial health.

## Contributing

We welcome contributions to enhance Money Mentor. Feel free to fork the repository, create new branches, and submit pull requests.

### Steps to Contribute
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-name`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add new feature'`).
5. Push to the branch (`git push origin feature-name`).
6. Open a pull request.

## License

This project is licensed under the MIT License.
