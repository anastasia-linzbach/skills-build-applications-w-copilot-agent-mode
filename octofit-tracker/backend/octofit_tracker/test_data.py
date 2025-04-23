# Adjusted test data for populating the octofit_db database

test_users = [
    {"username": "john_doe", "email": "john@example.com", "password": "password123"},
    {"username": "jane_smith", "email": "jane@example.com", "password": "password123"}
]

test_teams = [
    {"name": "Team Alpha", "members": []},
    {"name": "Team Beta", "members": []}
]

test_activities = [
    {"user": "john_doe", "activity_type": "Running", "duration": "00:30:00"},
    {"user": "jane_smith", "activity_type": "Cycling", "duration": "00:45:00"}
]

test_leaderboard = [
    {"user": "john_doe", "points": 100},
    {"user": "jane_smith", "points": 150}
]

test_workouts = [
    {"name": "Morning Run", "description": "A quick morning run to start the day", "duration": 30},
    {"name": "Evening Yoga", "description": "Relaxing yoga session", "duration": 60}
]
