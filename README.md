# Favourite-Starwars-app
App to view/Favourite Starwars data

Follow below steps to run the server:
   
    1. Clone the git directory to your local pc
    2. open terminal at location
    3. you should see setup.sh file in that directory 
    4. just run command "./setup.sh" in terminal it will start the server
    5. then open browser go to 127.0.0.1:8000

You will see a home page:

    6. On the home page, select what you want to search for (movies/planet) from the dropdown menu 
    7. search for any keyword in search box, you will see the results accordingly
    8. click on add to favourite to store that data into your favourite movie/planet list
    9. You can check you favourite movies and planets using the given tabs on home page

* For better results prefer to use google chrome!

To reset your saved database!
    1. cd to starwar directory
    2. run "python3 manage.py shell"
    3. You will see python shell
    4. import data library: from starwar.models  import SavedFilm, SavedPlanet
    5. run "SavedFilm.objects.all().delete()" / similar for Saved Planet
