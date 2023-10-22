# Employee Management System

This project implements a basic CRUD application for an Employee Management System using Python and Django with an SQL database. The application allows users to manage employee records.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/your-repository.git


2. Navigate to the project directory:
```
cd your-repository
```
3. Create Virtual Environment
```
python3 -m venv venv
```
4. Active Virtual Environment
```
source venv/bin/activate
```
5. Install Requirements File
```
pip install -r requirements.txt
```
6. Migrate Database
```
python manage.py migrate
```
7. Create Super User
```
python manage.py createsuperuser
```
8. Run Project
```
python manage.py runserver
```
Usage
When the application starts, it will provide a menu with the following options:

Add Employees: Allows you to add new employee records.
Display All Employees: Displays all existing employee records.
Edit Employee Details: Enables you to edit the details of an existing employee.
Delete Employees: Lets you delete employee records from the system.

License
This project is licensed under the MIT License - see the LICENSE file for details.
