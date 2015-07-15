Chronos-stable
==========================

# Deploy Pramantha Datastore

This software takes as input a lot of data coming from scattered sources, to dump it into a MongoDB instance that stores documents as Linked Data. LD dictionaries are also provided. 
The dumping (`main/`) takes place with different layers of data, each layer adds more data and improve links between existing data. A uncomplete description of the process can be found (here)[https://docs.google.com/document/d/1w5ndqSWiWaIzo4wlsJcfqQ2hOSaEyhf_w-u2nuxtNs0/edit?usp=sharing].<br/>
Different entities are tagged with TagME API, there is also a basic and raw scraping utility for Webpages implemented.<br/>
Types of entities stored can be found [here](https://github.com/SpaceAppsXploration/chronos-stable/blob/master/objectsapi/basicDocs.py).<br/>
Schema about the resulting graph of object classes can be found (here)[https://docs.google.com/drawings/d/19YG8fZo_7n1roV97VRtT1lxmQMvtOAi9yAQKVuW5Ifc/edit?usp=sharing].<br/>


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
