ParkToGo
========

Recommend national or state parks for outdoors


core algorithm:
===============
pre-process:

    1. get park detail informations using campground API and store them in ParkDetails.json
    
    2. classify those parks based on their details(amenities)
    
    3. before step 2, we use national parks data as training data

recommend:

    1. ask user to pick one favorite park from 5 given parks 
    
    2. recommend 1 national park and 3 state parks based on user's choice
    
How to run it:

    1. download everything in the core_algorithm
    
    2. command-line:
           $ python recommender.py
