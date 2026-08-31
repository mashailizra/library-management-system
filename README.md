# Library Member Management System
A FastAPI + Streamlit app to manage library members and their borrowed books, built to showcase OOP design: inheritance,polymorphism, magic methods, and operator overloading.Storage is a plain JSON file — no database.
## Status
In progress — Day 3.1/5 incomplete created main.py 
## Tech stack
Python 3, FastAPI, Streamlit
## Features 
- [x] Person base class, Member/Librarian subclasses with polymorphic describe().
- [x] __str__/__repr__/__eq__/__lt__ on Member; sortable member lists.
- [x] Library.__add__ merges two libraries (operator overloading).
- [x] Custom DuplicateMemberError / MemberNotFoundError.
- [x] Members persist to members.json .