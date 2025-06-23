import random


subjects=[
    "Shahrukh Khan",
    "Rohit Sharma",
    "Nirmala Sitharaman",
    "A Mumbai Cat",
    "A group of Monkeys",
    "Prime Minister Modi",
    "Auto Rickshaw Driver from Delhi"
]


actions=[
    "launches",
    "cancels",
    "dances with",
    "eats",
    "declares war on",
    "orders",
    "celebrates"
]


places_or_things=[
    "at Red Fort",
    "in Mumbai Local Train",
    "a plate of Biriyani",
    "inside Parliament",
    "at Ganga Ghat",
    "during IPL Match",
    "at India Gate"
]


while True:
    subject=random.choice(subjects)
    action=random.choice(actions)
    places_or_thing=random.choice(places_or_things)

    
    headline=f" BREAKING NEWS :  {subject} {action} {places_or_thing} "
    print("\n"+ headline)
    
    
    user_input=input("\n Do you want another Headline? (yes/no)").strip().lower()
    if user_input=="no":
        break
print("Thank you for using Fake News Generator.")