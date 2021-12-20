# Digital Signature for Concert Ticket
*Program Studi Teknik Informatika* <br />
*Sekolah Teknik Elektro dan Informatika* <br />
*Institut Teknologi Bandung* <br />

*Semester I Tahun 2021/2022*

## Description
An API that can sell and verify ticket with a digital signature with RSA and Keccak (SHA3) Algorithm

## API Functionality
1. Read detail of all tickets
2. Read detail of specified ticket
3. Create new ticket
4. Update ticket detail
5. Delete ticket
6. Buy ticket
7. Verify Ticket

## Requirements
- [Python](https://www.python.org/downloads/)
- [PIP](https://pypi.org/project/pip/)
- [XAMPP](https://www.apachefriends.org/download.html)

## How To Run
1. Download and install all requirements
2. Clone this repository
3. Create a virtual environment folder
```
virtualenv venv
```
4. Activate virtual environment
5. Run this script to install all dependecies that needed on the virtual environment
```
pip install fastapi sqlalchemy pymysql uvicorn
```
6. Create a database on MySQL and create tickets table with attribute mentioned on model/ticket
7. Change the user name, user password, MySQL port and database name according to your configuration on config/db
8. Run this script to activate the API
```
uvicorn index:app --reload
```
9. Open http://127.0.0.1:8000/docs# to see the API on your browser  

## Author
Gde Anantha Priharsena (13519026)