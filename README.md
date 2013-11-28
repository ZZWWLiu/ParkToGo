ParkToGo
========

Recommend national or state parks for outdoors


core algorithm:
===============
pre-process:
    1. get park detail informations using campground API and store them in ParkDetails.json
    2. cluster those parks based on their details

recommend:
    1. ask user to rate 5 parks (this may change)
    2. recommend 3 parks based on user's ratings
