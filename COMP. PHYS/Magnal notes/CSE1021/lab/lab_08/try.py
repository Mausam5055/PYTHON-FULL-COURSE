# Participants in each event
participants_python_basics = ['John', 'Edwin', 'Sophia', 'Olivia', 'Lee']
participants_advanced_java = ['Sophia', 'Olivia', 'William', 'James', 'Edwin']

# Convert lists to sets
python_set = set(participants_python_basics)
java_set = set(participants_advanced_java)

# 1. Participants registered for both events (intersection)
both_events = python_set & java_set
print("Participants registered for both events:", both_events)

# 2. Participants registered for only one event (symmetric difference)
only_one_event = python_set ^ java_set
print("Participants registered for only one event:", only_one_event)

# 3. Check if all Advanced Java participants registered for Python Basics (subset check)
all_java_in_python = java_set <= python_set
print("All Advanced Java participants registered for Python Basics:", all_java_in_python)

# 4. Total number of unique participants across both events (union)
unique_participants = python_set | java_set
print("Total unique participants across both events:", unique_participants)
print("Number of unique participants:", len(unique_participants))
