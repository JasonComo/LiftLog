
<div align="center">
  <img src="Assets/logo.png" alt="Logo">
</div>

### A Python Tkinter project that creates a GUI with signup/login functionality that allows users to create, view, edit, and delete workouts.


## Description
This project utilizes Python's Tkinter library to create a GUI that supports user signup, login, logout, as well as the creation, view, and edits of up to four workouts with eight exercises each. 

Key features:
- Signup/Login/Logout: LiftLog keeps track of user account information, allowing for users to create a username and password, login, and logout.
- Workout Creation: Users can create up to four workouts, with each workout containing up to eight exercises.
- Workout Editing/Deletion: Users can edit existing workouts, as well as delete them if need be.

- Workout View: Users can view the workouts they have created.
  
Keep in mind that LiftLog is not a fully functioning application that can remember account/workout information after closing the window, rather, it is a personal project intended to display both front-end and back-end development skills.

## Installation
The Pillow module is the only module that needs to be installed, as the other modules, Tkinter and os, are included in Python.
```
pip install Pillow
```
## Usage
After downloading the .zip file, navigate to the file directory on your terminal, and enter:
```
python main.py
```
### Signup
Selecting the signup button in the bottom right will take users to a signup screen, where they can create an account.

### Login
After creating an account. Users can login by entering their username and password.

### Create Workout
Users can create a workout by clicking the "Create Workouts" button. From there, they can add up to eight exercises, with names, sets, and reps, to the workout.

### View Workouts
Users can view existing workouts by clicking the "View Workouts" button.

### Edit Workouts
Users can edit or delete existing workouts by clicking the "Edit Workouts" button. From there, they can modify or remove exercises and their names, sets, and/or reps, as well as delete a workout entirely.

### Logout
Users can logout by clicking the "Logout" button on the bottom left corner of the window.
