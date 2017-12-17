# Goal

This project has for goal to create a little project with data for my application to EP. I choose to draw a graph of the tags for each article on my micro-blog, shaarli.bwatt.eu This one is made with shaarli: https://github.com/shaarli/Shaarli

Each tag represent one tag, and when two tags are attached to the same article, one edge between them is created. The width and the color of the edge depends on how many articles the two tags are found. You can see the result here: ep-project.bwatt.eu

The project use Alchemy (https://graphalchemist.github.io/Alchemy/) as Javascript library to make the visualisation of the graph.

# Installation and running
##Dev

You just need to clone the repository, and install the libraries in the Pipfile.lock with either pip or pipenv. Then to create the graph, you need to export your shaarli tags, save them in the repository, and launch the command:
`python create_graph.py <your_data_file>`
This will create a tags.json file on the static dir.

Then you can launch the server with this command:
`python server.py`

You then can go to localhost:5000 to see the result.

##Prod

I personally use Docker to put this project on prod with the Dockerfile present here. If you want to do the same, you have to install the application on dev (see above) then create the graph. You can after create a git repository with this. You then just have to change my git repository in the Dockerfile by yours. The script start.sh is used to launch the server. If you are interested by how I do, see my repository which containes the code to launch all my services: https://bwatt-fr/server

Note on the server: on production, I don't use the dev server provided by Flask, but Nginx. In order to do that, I have to put two tools before Nginx, Circus and Chaussette.

# Upgrade possible

This project was developped very fast, and suffers of lacks of problem. Lots of things can be done to improve it:
- although Alchemy do the work for the datavisualisation here, it is an old library which is no more updated, and has some bugs. It would be better to replace it by another one
- the installation of the project is still manual. It would be good to create a script, and make a better README here
- for the moment, there are two steps to make the project, one to create the graph and one which is the server. It would be better to mix both, and to provide an interface to upload the export of shaarli, and make the transformation directly on the server
- in the future, why not trying to provide this as an extension for shaarli?
