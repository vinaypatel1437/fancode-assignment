from api import fetch_users, fetch_todos

def filter_fancode_users(users):
    """Filters users based on the latitude and longitude of the FanCode city."""
    fancode_users = []
    for user in users:
        lat = float(user['address']['geo']['lat'])
        lng = float(user['address']['geo']['lng'])
        if -40 <= lat <= 5 and 5 <= lng <= 100:
            fancode_users.append(user)
    return fancode_users

def calculate_task_completion_percentage(todos, user_id):
    """Calculates the task completion percentage for a specific user."""
    user_todos = [todo for todo in todos if todo['userId'] == user_id]
    total_tasks = len(user_todos)
    completed_tasks = sum(1 for todo in user_todos if todo['completed'])
    return (completed_tasks / total_tasks) * 100 if total_tasks > 0 else 0

def main():
    """Main function to filter users and calculate task completion percentage."""
    users = fetch_users()
    todos = fetch_todos()

    fancode_users = filter_fancode_users(users)

    for user in fancode_users:
        completion_percentage = calculate_task_completion_percentage(todos, user['id'])
        if completion_percentage > 50:
            print(f"User {user['name']} from city 'FanCode' has completed more than 50% of their tasks: {completion_percentage:.2f}%")

if __name__ == "__main__":
    main()
