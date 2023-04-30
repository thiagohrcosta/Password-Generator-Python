# Password Generator (Python)
![enter image description here](https://res.cloudinary.com/dloadb2bx/image/upload/v1682892740/pass2_eeao63.png)

## Technologies used
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)  ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) 

This project was created using Docker to studying the basic concepts of Python learned at day 05  in the **[100 Days of Code: The Complete Python Pro Bootcamp](https://www.udemy.com/course/100-days-of-code/)**.  The object is to generate a list of letters, characters and numbers and create a password with all these items.

## Summary
**Day 05**: This day the focus was python Loops, create and use Lists and the range() and random functions.

## What user can do?

**User:** Can type the amount of letters, numbers and characters that will be used to generate a password.

## How to run this project
This project was created with Docker, the Dockerfile is:

    FROM  python:3
    
    WORKDIR  /app
    
    COPY  .  .
    
    CMD  ["python",  "app/main.py"]

To run just download this project and run the follow commands:  `docker build -t password-generator .`  then run `docker run -it password-generator`. 