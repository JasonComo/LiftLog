from tkinter import *
from tkinter import font
from tkinter import messagebox
from PIL import Image, ImageTk
import os

from account import Account
from account import Workout
from account import Exercise

# Creating Root object.
root = Tk()
root.geometry("1000x1000+800+200")

# Setting background image.
image = Image.open("C:/Users/jayco/OneDrive/Desktop/GUI/run.jpg")
image = image.resize((root.winfo_screenwidth(), root.winfo_screenheight()), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(image)
background_label = Label(root, image=photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Creating fonts.
userpass_font = font.Font(family="Arial", size=20, weight="bold")
arial_1 = font.Font(family="Arial", size=12)
arial_2 = font.Font(family="Arial", size=18, weight="bold")
arial_3 = font.Font(family="Arial", size=10, weight="bold")
arial_4 = font.Font(family="Arial", size=24, weight="bold")

# Importing buttons and labels that use an outside image
weight = Image.open(os.path.join("Assets", "weight_btn.png"))
weight_btn = ImageTk.PhotoImage(weight)

create_workout = Image.open(os.path.join("Assets", "create_workout.png"))
create_workout_label = ImageTk.PhotoImage(create_workout)

view_workouts = Image.open(os.path.join("Assets", "view_workouts.png"))
view_workouts_label = ImageTk.PhotoImage(view_workouts)

edit_workouts = Image.open(os.path.join("Assets", "edit_workouts.png"))
edit_workouts_label = ImageTk.PhotoImage(edit_workouts)

clipboard = Image.open(os.path.join("Assets", "clipboard_btn.png"))
clipboard_btn = ImageTk.PhotoImage(clipboard)

blank = Image.open(os.path.join("Assets", "blank_btn.png"))
blank_btn = ImageTk.PhotoImage(blank)

blank_small = Image.open(os.path.join("Assets", "blank_small.png"))
small_btn = ImageTk.PhotoImage(blank_small)

pencil = Image.open(os.path.join("Assets", "pencil_btn.png"))
pencil_btn = ImageTk.PhotoImage(pencil)

logo = Image.open(os.path.join("Assets", "logo.png"))
logo_label = ImageTk.PhotoImage(logo)

signin = Image.open(os.path.join("Assets", "sign_in.png"))
signin_btn = ImageTk.PhotoImage(signin)

confirm = Image.open(os.path.join("Assets", "confirm_btn.png"))
confirm_btn = ImageTk.PhotoImage(confirm)

signup = Image.open(os.path.join("Assets", "sign_up.png"))
signup_btn = ImageTk.PhotoImage(signup)

class GUI:
    """Graphical User Interface (GUI) for a workout application.

    This class manages the various frames and windows of the application and provides methods for creating and displaying
    different GUI elements.

    Attributes:
        root (Tk): The main window of the application.
        welcome_frame (Frame): The frame for the welcome screen.
        cac_frame (Frame): The frame for creating an account.
        hub_frame (Frame): The main hub frame after login.
        cw_frame (Frame): The frame for creating a new workout.
        vw_frame (Frame): The frame for viewing existing workouts.
        edit_frame (Frame): The frame for editing existing workouts.
        accounts_list (list): A list of Account objects representing user accounts.
        account (Account): The current user's account.
        username_entry (Entry): The entry widget for username input.
        password_entry (Entry): The entry widget for password input.
    """
    def __init__(self, root):
        """Initialize the GUI object.

        Args:
            root (Tk): The main window of the application.
        """
        self.welcome_frame = None
        self.cac_frame = None
        self.hub_frame = None
        self.cw_frame = None
        self.vw_frame = None
        self.edit_frame = None
        self.accounts_list = []
        self.account = None
        self.username_entry = None
        self.password_entry = None
        
    def createWelcomeFrame(self):
        """Create and display the welcome screen."""
        if self.cac_frame:
            self.cac_frame.destroy()
        if self.hub_frame:
            self.hub_frame.destroy()
        if self.welcome_frame:
            self.welcome_frame.destroy()
            
        self.welcome_frame = Frame(root, width=600, height=800, bg="white", highlightbackground="black", highlightthickness=2, highlightcolor="black")
        self.welcome_frame.place(relx=0.5, rely=0.5, anchor=CENTER)
        log_label = Label(self.welcome_frame, bg="white", image=logo_label, font=arial_1, fg="white")
        log_label.place(relx=0.5, rely=0.2, anchor=CENTER)

        username_label = Label(self.welcome_frame, bg="white", text="Username", font=userpass_font, fg="#3c78d8")
        username_label.place(relx=0.223, rely=0.38, anchor=CENTER)
        self.username_entry = Entry(self.welcome_frame, highlightbackground="black", highlightthickness=1, highlightcolor="black", width=50, font=arial_1)
        self.username_entry.place(relx=0.5, rely=0.43, anchor=CENTER)
        self.username_entry.insert(0, "Enter your username")

        password_label = Label(self.welcome_frame, bg="white", text="Password", font=userpass_font, fg="#3c78d8")
        password_label.place(relx=0.223, rely=0.53, anchor=CENTER)
        self.password_entry = Entry(self.welcome_frame, highlightbackground="black", highlightthickness=1, highlightcolor="black", width=50, font=arial_1)
        self.password_entry.place(relx=0.5, rely=0.58, anchor=CENTER)
        self.password_entry.insert(0, "Enter your password")
        
        def check():
            """Verify login and set logged-in account to the current Account object."""
            username = self.username_entry.get()
            password = self.password_entry.get()

            for account in self.accounts_list:
                if account.username == username:
                    if account.password == password:
                        self.account = account  
                        self.createHubFrame()
                        return
                    else:
                        messagebox.showerror("Error", "Incorrect password.")
                        return

            messagebox.showerror("Error", "No account with that username exists.")
            
        signin_button = Button(self.welcome_frame, image=blank_btn, text="Sign in", compound="center", activebackground="white", activeforeground="white", bg="white", fg="white", font=arial_2, bd=0, command=check)
        signin_button.place(relx=0.33, rely=0.75, anchor=CENTER)

        signup_button = Button(self.welcome_frame, image=blank_btn, text="Sign up", compound="center", activebackground="white", activeforeground="white",bg="white", fg="white", font=arial_2, borderwidth=0, command=self.createAccountFrame)
        signup_button.place(relx=0.66, rely=0.75, anchor=CENTER)

    def createAccountFrame(self):
        """Create and display the frame for creating a new user account."""
        self.welcome_frame.destroy()
        self.cac_frame = Frame(root, width=600, height=800, bg="white", highlightbackground="black", highlightthickness=2, highlightcolor="black")
        self.cac_frame.place(relx=0.5, rely=0.5, anchor=CENTER)
        cac_label = Label(self.cac_frame, bg="white", text="Create an Account", font=arial_1, fg="white")
        cac_label.place(relx=0.5, rely=0.2, anchor=CENTER)
        log_label = Label(self.cac_frame, bg="white", image=logo_label, font=arial_1, fg="white")
        log_label.place(relx=0.5, rely=0.2, anchor=CENTER)
        
        username_label = Label(self.cac_frame, bg="white", text="Username", font=userpass_font, fg="#3c78d8")
        username_label.place(relx=0.223, rely=0.38, anchor=CENTER)
        self.username_entry = Entry(self.cac_frame, highlightbackground="black", highlightthickness=1, highlightcolor="black", width=50, font=arial_1)
        self.username_entry.place(relx=0.5, rely=0.43, anchor=CENTER)
        self.username_entry.insert(0, "Enter your username")

        password_label = Label(self.cac_frame, bg="white", text="Password", font=userpass_font, fg="#3c78d8")
        password_label.place(relx=0.223, rely=0.53, anchor=CENTER)
        self.password_entry = Entry(self.cac_frame, highlightbackground="black", highlightthickness=1, highlightcolor="black", width=50, font=arial_1)
        self.password_entry.place(relx=0.5, rely=0.58, anchor=CENTER)
        self.password_entry.insert(0, "Enter your password")
        
        back_button = Button(self.cac_frame, image=small_btn, text="Back", activebackground="white", activeforeground="white", compound="center", bg="white", fg="white", font=arial_3, borderwidth=0, command=self.createWelcomeFrame)
        back_button.place(relx=0.11, rely=0.95, anchor=CENTER)
        
        def createAccount():
            """Create a new Account object and verify that it's username and password meet requirements."""
            username = self.username_entry.get()
            password = self.password_entry.get()

            if len(username) < 6:
                messagebox.showerror("Error", "Username must be at least 6 characters long.")
                return

            if " " in username:
                messagebox.showerror("Error", "Username cannot contain spaces.")
                return

            if len(password) < 8:
                messagebox.showerror("Error", "Password must be at least 8 characters long.")
                return

            if " " in password:
                messagebox.showerror("Error", "Password cannot contain spaces.")
                return

            for account in self.accounts_list:
                if account.username == username:
                    messagebox.showerror("Error", "Username already taken.")
                    return 
                
            else:
                self.account = Account(username, password) # Need to change
                self.accounts_list.append(self.account)
                self.createWelcomeFrame()

        signup_button = Button(self.cac_frame, image=blank_btn, text="Sign up", activebackground="white", activeforeground="white", compound="center", bg="white", fg="white", font=arial_2, borderwidth=0, command=createAccount)
        signup_button.place(relx=0.5, rely=0.75, anchor=CENTER)
           
    def createHubFrame(self):
        """Create and display the main hub frame after successful login.""" 
        
        self.cac_frame.destroy()
        self.welcome_frame.destroy()
        
        self.hub_frame = Frame(root, width=600, height=800, bg="white", highlightbackground="black", highlightthickness=2, highlightcolor="black")
        self.hub_frame.place(relx=0.5, rely=0.5, anchor=CENTER)
        
        create_workout_button = Button(self.hub_frame, image=weight_btn, borderwidth=0, bg="white", activebackground="white", command=self.createCreateWorkoutFrame)
        create_workout_button.place(relx=0.5, rely=0.25, anchor=CENTER)

        view_workouts_button = Button(self.hub_frame, image=clipboard_btn, borderwidth=0, bg="white", activebackground="white", command=self.createViewFrame)
        view_workouts_button.place(relx=0.5, rely=0.5, anchor=CENTER)

        edit_workouts_button = Button(self.hub_frame, image=pencil_btn, borderwidth=0, bg="white", activebackground="white", command=self.createEditFrame)
        edit_workouts_button.place(relx=0.5, rely=0.75, anchor=CENTER)
        
        logout_button = Button(self.hub_frame, image=small_btn, text="Logout", activebackground="white", activeforeground="white", compound="center", bg="white", fg="white", font=arial_3, borderwidth=0, command=self.createWelcomeFrame)
        logout_button.place(relx=0.11, rely=0.95, anchor=CENTER)
        
    def createCreateWorkoutFrame(self):
        """Create and display the frame for creating a new workout."""
        if len(self.account.workouts) == 4:
            messagebox.showerror("Error", "Accounts can create up to four workouts.")
            return 
        
        self.hub_frame.destroy()
        self.cw_frame = Frame(root, width=600, height=800, bg="white", highlightbackground="black", highlightthickness=2, highlightcolor="black")
        self.cw_frame.place(relx=0.5, rely=0.5, anchor=CENTER)
        cw_label = Label(self.cw_frame, bg="white", image=create_workout_label, fg="#3c78d8")
        cw_label.place(relx=0.5, rely=0.17, anchor=CENTER)
        back_button = Button(self.cw_frame, image=small_btn, text="Back", activebackground="white", activeforeground="white", compound="center", bg="white", fg="white", font=arial_3, borderwidth=0, command=self.createHubFrame)
        back_button.place(relx=0.11, rely=0.95, anchor=CENTER)

        workout_name_label = Label(self.cw_frame, bg="white", text="Workout Name", font=arial_2, fg="#3c78d8")
        workout_name_label.place(relx=0.5, rely=0.28, anchor=CENTER)
        workout_name_entry = Entry(self.cw_frame, highlightbackground="black", highlightthickness=1, highlightcolor="black", width=32, font=arial_1)
        workout_name_entry.place(relx=0.5, rely =0.33, anchor=CENTER)
        exercise_label = Label(self.cw_frame, bg="white", text="Exercise Name", font=arial_2, fg="#3c78d8")
        exercise_label.place(relx=0.193, rely=0.385, anchor=CENTER)
        sets_label = Label(self.cw_frame, bg="white", text="Sets", font=arial_2, fg="#3c78d8")
        sets_label.place(relx=0.595, rely=0.385, anchor=CENTER)
        reps_label = Label(self.cw_frame, bg="white", text="Reps", font=arial_2, fg="#3c78d8")
        reps_label.place(relx=0.8, rely=0.385, anchor=CENTER)
        
        exercise_names_list = []
        exercise_sets_list = [] 
        exercise_reps_list = []
            
        for i in range(8):
            exercise_names = Entry(self.cw_frame, highlightbackground="black", highlightthickness=1, highlightcolor="black", width=32, font=arial_1)
            rely = 0.43 + (i * 0.05)
            exercise_names.place(relx=0.30, rely=rely, anchor=CENTER)
            exercise_names_list.append(exercise_names)
            
        for i in range(8):
            exercise_sets = Entry(self.cw_frame, highlightbackground="black", highlightthickness=1, highlightcolor="black", width=12, font=arial_1)
            rely = 0.43 + (i * 0.05)
            exercise_sets.place(relx=0.65, rely=rely, anchor=CENTER)
            exercise_sets_list.append(exercise_sets)
            
        for i in range(8):
            exercise_reps = Entry(self.cw_frame, highlightbackground="black", highlightthickness=1, highlightcolor="black", width=12, font=arial_1)
            rely = 0.43 + (i * 0.05)
            exercise_reps.place(relx=0.848, rely=rely, anchor=CENTER)
            exercise_reps_list.append(exercise_reps)
        
        def storeWorkout():
            """Store exercise information into Workout object and append it to Account workouts."""
            exercise_names_values = [exercise_name.get().strip() for exercise_name in exercise_names_list]
            exercise_sets_values = [exercise_set.get().strip() for exercise_set in exercise_sets_list]
            exercise_reps_values = [exercise_rep.get().strip() for exercise_rep in exercise_reps_list]
            
            if len(workout_name_entry.get()) == 0:
                messagebox.showerror("Error", "Enter a workout name.")
                return 
            
            if all(len(value) == 0 for value in exercise_names_values) and all(len(value) == 0 for value in exercise_sets_values) and all(len(value) == 0 for value in exercise_reps_values):
                messagebox.showerror("Error", "Enter at least one exercise.")
                return 
            
            for name, sets, reps in zip( exercise_names_values, exercise_sets_values, exercise_reps_values):
                if len(name) == 0 and len(sets) == 0 and len(reps) == 0:
                    continue  
                        
                if len(name) == 0 or len(sets) == 0 or len(reps) == 0:
                    messagebox.showerror("Error", "All entries must be filled for each exercise.")
                    return

                if len(name) > 12:
                    messagebox.showerror("Error", "Exercise name cannot be more than 14 characters.")
                    return

                if not sets.isdigit():
                    messagebox.showerror("Error", "Sets must be a number.")
                    return
                    
                if not reps.isdigit():
                    messagebox.showerror("Error", "Reps must be a number.")
                    return
                
                if len(sets) > 3:
                    messagebox.showerror("Error", "Sets cannot exceed triple digits.")
                    return
            
                if len(reps) > 3:
                    messagebox.showerror("Error", "Reps cannot exceed triple digits.")
                    return
                               
            for i in exercise_names_values.copy():
                if len(i) == 0:
                    exercise_names_values.remove(i)
            for i in exercise_sets_values.copy():
                if len(i) == 0:
                    exercise_sets_values.remove(i)
            for i in exercise_reps_values.copy():
                if len(i) == 0:
                    exercise_reps_values.remove(i)    

            workout = Workout(workout_name_entry.get())
            
            for i in range(0, len(exercise_names_values)):
                exercise = Exercise(exercise_names_values[i], exercise_sets_values[i], exercise_reps_values[i])
                workout.exercises.append(exercise)  
                     
            self.account.workouts.append(workout)
                        
            self.createHubFrame()

        create_button = Button(self.cw_frame, image=blank_btn, text="Confirm", activebackground="white", activeforeground="white", compound="center", bg="white", fg="white", font=arial_2, borderwidth=0, command=storeWorkout)
        create_button.place(relx=0.5, rely=0.85, anchor=CENTER)
        
    def createViewFrame(self):
        """Create and display the frame for viewing existing workouts."""
        if len(self.account.workouts) == 0:
            messagebox.showerror("Error", "No workouts have been created yet.")
            return 
        if self.vw_frame:
            self.vw_frame.destroy()
        self.vw_frame = Frame(root, width=600, height=800, bg="white", highlightbackground="black", highlightthickness=2, highlightcolor="black")
        self.vw_frame.place(relx=0.5, rely=0.5, anchor=CENTER)
        vw_label = Label(self.vw_frame, bg="white", image=view_workouts_label, fg="#3c78d8")
        vw_label.place(relx=0.5, rely=0.17, anchor=CENTER)
        back_button = Button(self.vw_frame, image=small_btn, text="Back", activebackground="white", activeforeground="white", compound="center", bg="white", fg="white", font=arial_3, borderwidth=0, command=self.createHubFrame)
        back_button.place(relx=0.11, rely=0.95, anchor=CENTER)
        num_workouts = len(self.account.workouts)

        def viewWorkout(number):
            """Create and display the freame for viewing a specific workout's exercises."""
            self.vw_frame.destroy()
            num_exercises = len(self.account.workouts[number].exercises)
            self.vw_frame = Frame(root, width=600, height=800, bg="white", highlightbackground="black", highlightthickness=2, highlightcolor="black")
            self.vw_frame.place(relx=0.5, rely=0.5, anchor=CENTER)
            vw_label = Label(self.vw_frame, bg="white", image=view_workouts_label, fg="#3c78d8")
            vw_label.place(relx=0.5, rely=0.17, anchor=CENTER)
            back_button = Button(self.vw_frame, image=small_btn, text="Back", activebackground="white", activeforeground="white", compound="center", bg="white", fg="white", font=arial_3, borderwidth=0, command=self.createViewFrame)
            back_button.place(relx=0.11, rely=0.95, anchor=CENTER)   
                     
            for i in range(0, num_exercises):
                exercise_name_label = Label(self.vw_frame, bg="white", text=self.account.workouts[number].exercises[i].name, font=arial_2, fg="#3c78d8")
                exercise_sr_label = Label(self.vw_frame, bg="white", text=f'{self.account.workouts[number].exercises[i].sets} x {self.account.workouts[number].exercises[i].reps}', font=arial_2, fg="#3c78d8")               
                rely = 0.35 + (i * 0.5 ) / num_exercises
                exercise_name_label.place(relx=0.35, rely=rely, anchor=CENTER)
                exercise_sr_label.place(relx=0.65, rely=rely, anchor=CENTER)
                
        for i in range(num_workouts):
            rely = 0.35 + (i * 0.5) / num_workouts  
            view_button = Button(self.vw_frame, background="white", image=blank_btn, text=self.account.workouts[i].name, activebackground="white", activeforeground="white", compound="center", bg="white", fg="white", font=arial_2, borderwidth=0, command=lambda workout_num=i: viewWorkout(workout_num))
            view_button.place(relx=0.5, rely=rely, anchor=CENTER) 
    
        
    def createEditFrame(self):
        """Create and display the frame for editing existing workouts."""
        if len(self.account.workouts) == 0:
            messagebox.showerror("Error", "No workouts have been created yet.")
            return
        self.edit_frame = Frame(root, width=600, height=800, bg="white", highlightbackground="black", highlightthickness=2, highlightcolor="black")
        self.edit_frame.place(relx=0.5, rely=0.5, anchor=CENTER)
        ew_label = Label(self.edit_frame, bg="white", image=edit_workouts_label, fg="#3c78d8")
        ew_label.place(relx=0.5, rely=0.17, anchor=CENTER)
        back_button = Button(self.edit_frame, image=small_btn, text="Back", activebackground="white", activeforeground="white", compound="center", bg="white", fg="white", font=arial_3, borderwidth=0, command=self.createHubFrame)
        back_button.place(relx=0.11, rely=0.95, anchor=CENTER)
        
        num_workouts = len(self.account.workouts)
        
        for i in range(num_workouts):
            rely = 0.35 + (i * 0.5) / num_workouts  
            edit_button = Button(self.edit_frame, background="white", image=blank_btn, text=self.account.workouts[i].name, activebackground="white", activeforeground="white", compound="center", bg="white", fg="white", font=arial_2, borderwidth=0, command=lambda: editWorkout(i))
            edit_button.place(relx=0.5, rely=rely, anchor=CENTER)        
        
        def editWorkout(number):
            """Create and display the frame for editing a specific workout."""
            self.edit_frame.destroy()
            self.edit_frame = Frame(root, width=600, height=800, bg="white", highlightbackground="black", highlightthickness=2, highlightcolor="black")
            self.edit_frame.place(relx=0.5, rely=0.5, anchor=CENTER)
            ew_label = Label(self.edit_frame, bg="white", image=edit_workouts_label, fg="#3c78d8")
            ew_label.place(relx=0.5, rely=0.17, anchor=CENTER)
            back_button = Button(self.edit_frame, image=small_btn, text="Back", activebackground="white", activeforeground="white", compound="center", bg="white", fg="white", font=arial_3, borderwidth=0, command=self.createHubFrame)
            back_button.place(relx=0.11, rely=0.95, anchor=CENTER)
            
            workout_name_label = Label(self.edit_frame, bg="white", text="Workout Name", font=arial_2, fg="#3c78d8")
            workout_name_label.place(relx=0.5, rely=0.28, anchor=CENTER)
            workout_name_entry = Entry(self.edit_frame, highlightbackground="black", highlightthickness=1, highlightcolor="black", width=32, font=arial_1)
            workout_name_entry.place(relx=0.5, rely=0.33, anchor=CENTER)
            workout_name_entry.insert(0, self.account.workouts[number].name)
            exercise_label = Label(self.edit_frame, bg="white", text="Exercise Name", font=arial_2, fg="#3c78d8")
            exercise_label.place(relx=0.193, rely=0.385, anchor=CENTER)
            sets_label = Label(self.edit_frame, bg="white", text="Sets", font=arial_2, fg="#3c78d8")
            sets_label.place(relx=0.595, rely=0.385, anchor=CENTER)
            reps_label = Label(self.edit_frame, bg="white", text="Reps", font=arial_2, fg="#3c78d8")
            reps_label.place(relx=0.8, rely=0.385, anchor=CENTER)
        
            exercise_names_list = []
            exercise_sets_list = [] 
            exercise_reps_list = []
            
            for i in range(8):
                exercise_names = Entry(self.edit_frame, highlightbackground="black", highlightthickness=1, highlightcolor="black", width=32, font=arial_1)
                rely = 0.43 + (i * 0.05)
                exercise_names.place(relx=0.30, rely=rely, anchor=CENTER)
                exercise_names_list.append(exercise_names)
                
                if i < len(self.account.workouts[number].exercises):
                    exercise_names.insert(0, self.account.workouts[number].exercises[i].name)

            for i in range(8):
                exercise_sets = Entry(self.edit_frame, highlightbackground="black", highlightthickness=1, highlightcolor="black", width=12, font=arial_1)
                rely = 0.43 + (i * 0.05)
                exercise_sets.place(relx=0.65, rely=rely, anchor=CENTER)
                exercise_sets_list.append(exercise_sets)
                
                if i < len(self.account.workouts[number].exercises):
                    exercise_sets.insert(0, self.account.workouts[number].exercises[i].sets)
                
            for i in range(8):
                exercise_reps = Entry(self.edit_frame, highlightbackground="black", highlightthickness=1, highlightcolor="black", width=12, font=arial_1)
                rely = 0.43 + (i * 0.05)
                exercise_reps.place(relx=0.848, rely=rely, anchor=CENTER)
                exercise_reps_list.append(exercise_reps)
            
                if i < len(self.account.workouts[number].exercises):
                    exercise_reps.insert(0, self.account.workouts[number].exercises[i].reps)
                
            def storeWorkout():
                """Store newly-edited exercise information into Workout object, remove the previous Workout object, and append the new one to Account workouts."""
                exercise_names_values = [exercise_name.get().strip() for exercise_name in exercise_names_list]
                exercise_sets_values = [exercise_set.get().strip() for exercise_set in exercise_sets_list]
                exercise_reps_values = [exercise_rep.get().strip() for exercise_rep in exercise_reps_list]
                
                if len(workout_name_entry.get()) == 0:
                    messagebox.showerror("Error", "Enter a workout name.")
                    return 
                
                if all(len(value) == 0 for value in exercise_names_values) and all(len(value) == 0 for value in exercise_sets_values) and all(len(value) == 0 for value in exercise_reps_values):
                    messagebox.showerror("Error", "Enter at least one exercise.")
                    return 
                
                for name, sets, reps in zip( exercise_names_values, exercise_sets_values, exercise_reps_values):
                    if len(name) == 0 and len(sets) == 0 and len(reps) == 0:
                        continue  
                            
                    if len(name) == 0 or len(sets) == 0 or len(reps) == 0:
                        messagebox.showerror("Error", "All entries must be filled for each exercise.")
                        return

                    if len(name) > 12:
                        messagebox.showerror("Error", "Exercise name cannot be more than 14 characters.")
                        return

                    if not sets.isdigit():
                        messagebox.showerror("Error", "Sets must be a number.")
                        return
                        
                    if not reps.isdigit():
                        messagebox.showerror("Error", "Reps must be a number.")
                        return
                    
                    if len(sets) > 3:
                        messagebox.showerror("Error", "Sets cannot exceed triple digits.")
                        return
                
                    if len(reps) > 3:
                        messagebox.showerror("Error", "Reps cannot exceed triple digits.")
                        return
                
                for i in exercise_names_values.copy():
                    if len(i) == 0:
                        exercise_names_values.remove(i)
                for i in exercise_sets_values.copy():
                    if len(i) == 0:
                        exercise_sets_values.remove(i)
                for i in exercise_reps_values.copy():
                    if len(i) == 0:
                        exercise_reps_values.remove(i)    

                workout = Workout(workout_name_entry.get())
                
                for i in range(0, len(exercise_names_values)):
                    exercise = Exercise(exercise_names_values[i], exercise_sets_values[i], exercise_reps_values[i])
                    workout.exercises.append(exercise)  
                
                self.account.workouts.pop(number)  
                self.account.workouts.append(workout)
                self.edit_frame.destroy()
                self.createEditFrame()
                
            def deleteWorkout():
                """Delete an existing workout by removing the Workout object from the Account workouts """
                self.account.workouts.pop(number)
                messagebox.showwarning("Warning", "This exercise will be deleted.")
                self.edit_frame.destroy()
                self.createHubFrame() 
                return
        
            create_button = Button(self.edit_frame, image=blank_btn, text="Confirm", activebackground="white", activeforeground="white", compound="center", bg="white", fg="white", font=arial_2, borderwidth=0, command=storeWorkout)
            create_button.place(relx=0.35, rely=0.85, anchor=CENTER)
            delete_button = Button(self.edit_frame, image=blank_btn, text="Delete", activebackground="white", activeforeground="white", compound="center", bg="white", fg="white", font=arial_2, borderwidth=0, command=deleteWorkout)
            delete_button.place(relx=0.65, rely=0.85, anchor=CENTER) 



