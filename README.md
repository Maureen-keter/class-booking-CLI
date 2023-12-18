# class-booking-CLI
Class CLI is a command-line application designed to manage educational institutions, lecture halls, and lectures. It utilizes SQLAlchemy as an ORM (Object-Relational Mapping) tool for database interactions and Faker to generate realistic fake data for testing purposes.

## Table of Contents

1.Getting Started
2.Prerequisites
3.Installation
4.Usage
5.Run the Application
5.Database Migration
7.Contributing
8.License

## Getting Started

### Prerequisites

Ensure you have the following software installed:

- Python 3.x

### Installation

1. **Clone the repository:**

   git clone https://github.com/your-username/class-cli.git

2. **Navigate to the project directory:**

   cd class-cli

3. **Set up a virtual environment:**

   pipenv install
   pipenv shell

4. **Install dependencies:**
   pip install -r requirements.txt

5. **Run the seed script to populate the database with fake data:**

   python seed.py

## Usage

### Run the Application

1. **Ensure the virtual environment is activated :**

   pipenv shell

## Database Migration

If changes are made to the models, perform a database migration using Alembic.

1. **Install Alembic:**

   pip install alembic

2. **Create an Alembic migration:**

   alembic init alembic

## Contributing

Contributions are welcome! If you find a bug or have an improvement suggestion, please open an issue or create a pull request.

## License

This project is licensed under the MIT License .

## Author
Maureen Chelangat.
