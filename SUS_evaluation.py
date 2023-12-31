from collections import defaultdict

sus_scale = {
 1 : "I think that I would like to use this system frequently",
 2 : "I found the system unnecessarily complex",
 3 : "I thought the system was easy to use",
 4 : "I think that I would need the support of a technical person to be able to use this system",
 5 : "I found the various functions in this system were well integrated",
 6 : "I thought there was too much inconsistency in this system",
 7 : "I would imagine that most people would learn to use this system very quickly",
 8 : "I found the system very cumbersome to use",
 9 : "I felt very confident using the system",
 10 : "I needed to learn a lot of things before I could get going with this system"}

print("System usability scale.")
user_data = {}
while True:
   name = input('What is your name? ')
   user_data[name] = {}
   for k, q in sus_scale.items():
       answer = int(input(q))
       user_data[name][k] = [q, answer]
   if input('More subjects (yes/no)?').strip().lower() == 'no':
       break
print("Thanks for participating!")
print(user_data)
