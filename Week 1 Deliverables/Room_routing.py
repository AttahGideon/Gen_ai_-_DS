# Ask a user their name
# If their first name starts with A or B 
# tell them they go to room AB
# IF their first name starts with C
# tell them to go to room CD
# If their first name starts with another letter, ask for their last name
# IF their last name starts with Z, tell them to go to room Z
# if their last name starts with any other letter, tell them to go to room OTHER
# When you are done
# Anna should be in room AB
# Bob should be in room AB
# Charlie should be in room C
# Khalid Haque should be in room OTHER
# Xin Zhao should be in room Z

First_name = input('what is your first name?')
if First_name.lower().startswith('a') or First_name.lower().startswith('b'):
    print('go to room AB')
elif  First_name.lower().startswith('c'):
    print('go to room CD')
else:
    Last_name = input('whats your last name?')
    if Last_name.lower().startswith('z'):
        print('go to room z')
    else:
        print('go to another room')