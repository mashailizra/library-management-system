# Library Member Management System
A FastAPI + Streamlit app for managing library members and borrowed books,built to showcase object-oriented design. Storage is a JSON file— no database.
## Status
Complete
## OOP design highlights
- **Inheritance:** Person → Member / Librarian
- **Polymorphism:** describe() behaves differently per subclass
- **Magic methods:** __str__, __repr__, __eq__, __lt__ (enables 
sorted())
- **Operator overloading:** Library + Library merges two member 
lists
- **Custom exceptions:** DuplicateMemberError,MemberNotFoundError, mapped to HTTP 409/404 via a FastAPI exception handler
## Features
- Full CRUD API for members (FastAPI)
- Streamlit dashboard: add, search, sort, update, delete
- JSON-file persistence, no database required
## Tech stack
Python 3, FastAPI, Streamlit, Pandas, Requests
## Screenshots
![Dashboard](screenshot_dashboard.png)
## How to run
**Terminal 1:**
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```
**Terminal 2:**
```bash
source venv/bin/activate  # Windows: venv\Scripts\activate
streamlit run streamlit_app.py
```
## What I learned
- Designing a class hierarchy with real inheritance and 
polymorphism
- Implementing magic methods and operator overloading correctly
- Building a full CRUD API and mapping domain exceptions to HTTP 
responses
- Connecting a Streamlit dashboard to a stateful backend.