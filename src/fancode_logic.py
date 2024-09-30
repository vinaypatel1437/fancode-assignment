def is_user_in_fancode_city(user):
    lat = float(user['address']['geo']['lat'])
    lng = float(user['address']['geo']['lng'])
    return -40 <= lat <= 5 and 5 <= lng <= 100

def calculate_completion_percentage(todos, user_id):
    user_todos = [todo for todo in todos if todo['userId'] == user_id]
    if not user_todos:
        return 0
    completed_tasks = [todo for todo in user_todos if todo['completed']]
    return (len(completed_tasks) / len(user_todos)) * 100

def check_fancode_users_completion(users, todos):
    fancode_users = [user for user in users if is_user_in_fancode_city(user)]
    users_with_low_completion = []

    for user in fancode_users:
        completion_percentage = calculate_completion_percentage(todos, user['id'])
        if completion_percentage <= 50:
            users_with_low_completion.append({
                'user_id': user['id'],
                'name': user['name'],
                'completion_percentage': completion_percentage
            })
    
    return users_with_low_completion
