import logging
from datetime import timedelta
from django.core.management.base import BaseCommand
from octofit.models import User, Team, Activity, Leaderboard, Workout
from octofit_tracker.test_data import test_users, test_teams, test_activities, test_leaderboard, test_workouts

# Configure logging
logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

class Command(BaseCommand):
    help = 'Populate the database with test data'

    def handle(self, *args, **kwargs):
        try:
            # Populate users
            user_objects = {}
            for user_data in test_users:
                user, _ = User.objects.get_or_create(**user_data)
                user_objects[user.username] = user

            # Populate teams
            for team_data in test_teams:
                team, _ = Team.objects.get_or_create(name=team_data['name'])
                if team_data.get('members'):
                    try:
                        team.members.set([user_objects[username] for username in team_data['members']])
                    except Exception as e:
                        self.stdout.write(self.style.ERROR(f'Error setting team members: {e}'))

            # Populate activities
            for activity_data in test_activities:
                Activity.objects.get_or_create(
                    user=user_objects[activity_data['user']],
                    activity_type=activity_data['activity_type'],
                    duration=parse_duration(activity_data['duration'])
                )

            # Populate leaderboard
            for leaderboard_data in test_leaderboard:
                Leaderboard.objects.get_or_create(
                    user=user_objects[leaderboard_data['user']],
                    score=leaderboard_data['score']
                )

            # Populate workouts
            for workout_data in test_workouts:
                Workout.objects.get_or_create(
                    name=workout_data['name'],
                    description=workout_data['description']
                )

            self.stdout.write(self.style.SUCCESS('Database populated with test data.'))
        except Exception as e:
            logging.error(f"Error populating database: {e}")
            self.stdout.write(self.style.ERROR('Failed to populate the database. Check logs for details.'))

def parse_duration(duration_str):
    # Expects format 'HH:MM:SS'
    h, m, s = map(int, duration_str.split(':'))
    return timedelta(hours=h, minutes=m, seconds=s)
