Chronos-stable
==========================

# Deploy Pramantha Datastore

See the [wiki](https://github.com/SpaceAppsXploration/StartPramanthaUp/wiki) also<br/><br/>

Main scripts and libraries to create a multi-database instance of Pramantha's Datastore, with data from static modules (`input/` directory), websites
crawling and TagMe API's results.
<br/><br/>

Copyright 2014, 2015 Pramantha Ltd
Credits to Lorenzo, Claudio and Jacopo

This package contains the file to run a complete Cloud re-creation from local and online resources, using
the TagMe API
<br/><br/>

* Install MongoDB with default address and port

* Install requirements in `requirements.txt`.

        pip install -r requirements.txt

* `PhantomJS` and `bson` support are required as system requirements. Find the right way of installing them in your system.<br/>
* run the script in `main.py` for the [multi-layers deploying](https://github.com/SpaceAppsXploration/StartPramanthaUp/wiki/Multi-layers-deployments-for-Linked-Data-with-MongoDB)

<br/><br/>
<img src="http://www.faviki.com/img/dbpedia_powered.gif" height="50" width="75" >
<img src="http://acube.di.unipi.it/wp-content/uploads/2011/07/powered_by_tagme.png" height="50" width="100" >
<img src="https://raw.githubusercontent.com/BlackPearSw/fhirball/master/res/branding/mongodb-powered-by-badge-white.jpg" height="50" width="100" >
<br/><br/>

TagMe API by:<br/>
Paolo Ferragina, Ugo Scaiella<br/>
TagMe research paper:<br/>
Fast and Accurate Annotation of Short Texts with Wikipedia Pages. IEEE Software 29(1): 70-75 (2012)



## To-dos

* add Sensors from Chronos API and from spreadsheet
* implement Google Search API in crawling
* add OrientDB support for graph description of the datastore
* ...
