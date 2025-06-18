# Your university is going to organize a sport event. Two events are being organized at the same time. 
# A. Long Jump and 
# B. Hockey 
# The organizing committee has to shortlist participants to avoid confusion. 
# Use the Python set to write a Python code to solve the following. 
# 1. List the participants who are enrolled for one event. 
# 2. Find the number of unique participants across both events. 
# 3. Determine if all participants of Long Jump are enrolled for Hockey. 
# 4. Identify the participants who are enrolled in both events.

# Sample participant lists
long_jump = {"Alice", "Bob", "Charlie", "David"}
hockey = {"Bob", "Eve", "Frank", "Charlie"}

# 1. Participants enrolled for only one event
only_one_event = (long_jump.symmetric_difference(hockey))
print("Participants enrolled for only one event:", only_one_event)

# 2. Number of unique participants across both events
unique_participants = long_jump.union(hockey)
print("Number of unique participants:", len(unique_participants))

# 3. Check if all Long Jump participants are also in Hockey
all_long_jump_in_hockey = long_jump.issubset(hockey)
print("Are all Long Jump participants enrolled for Hockey?", all_long_jump_in_hockey)

# 4. Participants enrolled in both events
both_events = long_jump.intersection(hockey)
print("Participants enrolled in both events:", both_events)
