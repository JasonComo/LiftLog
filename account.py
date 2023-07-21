class Account:
    """Represents a user account.

    Attributes:
        username (str): The username of the account.
        password (str): The password of the account.
        workouts (list): A list of Workout objects associated with this account.
    """
    def __init__(self, username, password):
        """Initialize the Account object."""
        self.username = username
        self.password = password
        self.workouts = []
        
class Workout:
    """Represents a workout.

    Attributes:
        name (str): The name of the workout.
        exercises (list): A list of Exercise objects associated with this workout.
    """
    def __init__(self, name):
        """Initialize the Workout object."""
        self.name = name
        self.exercises = []

class Exercise:
    """Represents an exercise.

    Attributes:
        name (str): The name of the exercise.
        sets (str): The number of sets for the exercise.
        reps (str): The number of reps for the exercise.
    """
    def __init__(self, name, sets, reps):
        """Initialize the Exercise object."""
        self.name = name
        self.sets = sets
        self.reps = reps