__author__ = 'lorenzo@pramantha.net'


########################################################################
#
# LAYER ZERO: THE NASA-STI TAXONOMY
#


def dump_concepts(build, test):
    """
    Looks for concepts in bs4 SKOS-XML DOM, loops over all and stores them using XMLskos.store_sti_document
    :return: None
    """
    #try:
    # load XML-munching utilities
    from objectsapi.XMLstringHandler.XMLskos import XMLskos
    if not test:
        # load the full DOM from the input package
        from input.JPLSKOS.jpl_skos import jpl_skos_xml
    else:
        # load a partial DOM
        from tests.test_inputs.mockData import NASAxml_test
        jpl_skos_xml = NASAxml_test

    # instance of XMLskos utility class
    xml_processing = XMLskos(build=build, xml_string=jpl_skos_xml)
    # add root object
    xml_processing.add_root()

    # loop all the <skos:Concept> in the file
    for obj in xml_processing.return_soup().find_all('skos:concept'):
        # find the STI code
        obj_code = obj.find("nt2:code").string
        print(obj_code)
        # store a document that implements the <skos:Concept> in the DB
        xml_processing.store_sti_document(obj, obj_code)

    del xml_processing
    return True
    #except Exception as e:
        #raise ErrorInOperations(e)


def dump_hierarchy(build, test):
    """
    Stores in the database all the hierarchical information in the SKOS-XML DOM
    :return: None
    """

    # load XML-munching utilities
    from objectsapi.XMLstringHandler.XMLskos import XMLskos
    if not test:
        # load the full DOM from the input package
        from input.JPLSKOS.jpl_skos import jpl_skos_xml
    else:
        # load a partial DOM
        from tests.test_inputs.mockData import NASAxml_test
        jpl_skos_xml = NASAxml_test

    xml_processing = XMLskos(build=build, xml_string=jpl_skos_xml)

    # add links
    for obj in xml_processing.return_soup().find_all('skos:concept'):
        xml_processing.link_sti_document(build=build, obj=obj)

    xml_processing.check_concept_complete(build=build)

    del xml_processing
    return True


def semantic_hierarchy(build, keywords):
    """
    use the tagmeapi to store annotations about keywords and subjects
    :return: None
    """
    from tagmeapi.tagMeOperation import TagMeOperation

    # use TagMe to link concepts (keywords) to dbpedia documents
    new = TagMeOperation(build=build)
    # insert sections (wider arguments and categories)
    new.insert_sections()

    # add dbpedia documents semantically linked
    for k in keywords:
        print("KEYWORD >>> ", k["skos:prefLabel"])
        try:
            new.link_annotated_keywords_and_subjects(k)
        except Exception as e:
            print(Exception(">>>>>>>>> ERROR Tagging Keyword: " + str(e)))
            continue

    del new
    return True


###############################################################################
#
# LAYER ONE: THE CHRONOS LEGACY
#


def get_and_store_targets_from_chronos_dump(build):
    """
    Stores in the database all the information about missions' targets, taken from a JSON file
    and also stores annotations about the given target
    :return: None
    """

    from tagmeapi.tagMeOperation import TagMeOperation
    from objectsapi.ChronosObjects.chronosTarget import CHRONOStarget
    from input.Targets.targets import Chronos_Targets

    ops = TagMeOperation(build=build)
    for t in Chronos_Targets:
        # instance of the CHRONOSTarget class
        new = CHRONOStarget(build=build, obj=t)
        # store target
        new.store_target()
        del new

    del ops
    return True


def get_and_store_missions_from_chronos_dump(build, test):
    """
    Stores in the database all the information about missions, taken from a JSONs: a single file about missions
    and many others about launches
    :return: None
    """

    from objectsapi.ChronosObjects.chronosMission import CHRONOSmission
    from input.Missions.missions import Chronos_Missions
    from input.Launches.GetLaunches import get_launches_from_file

    # aggregate missions by codename
    missions_to_store = {}

    for m in Chronos_Missions:
        if m["codename"] not in missions_to_store.keys():
            missions_to_store[m["codename"]] = m
            target = missions_to_store[m["codename"]]["target"]
            missions_to_store[m["codename"]]["target"] = list()
            missions_to_store[m["codename"]]["target"].append(target)
        else:
            missions_to_store[m["codename"]]["target"].append(m["target"])
            if "slug" in m:
                missions_to_store[m["codename"]]["slug"] = m["slug"]
    missions_to_store = list(missions_to_store.values())

    # from pprint import pprint
    # pprint(missions_to_store)

    # first part added from mission.py file
    for i, m in enumerate(missions_to_store):
        # instance of CHRONOSMission class
        new = CHRONOSmission(build=build, obj=m)
        new.store_mission()
        if test and i > 25:
            break

    # second part added from Launches directory
    history = get_launches_from_file()
    for i, year in enumerate(history.keys()):
        for m in history[year]:
            new = CHRONOSmission(build=build, obj=m)
            new.store_launch(year)
        if test and i == 2:
            # if test is True store only two years of launches
            break
    return True


def get_and_store_events_from_chronos_dump(build, test):
    """
    Stores in the database all the events connected to a missions from an input file containing Chronos data
    :return: None
    """

    from toolbox import tools
    from datastoreapi.datastoreErrors import DocumentExistNot
    from input.Details.missions_ids import missions_ids
    from objectsapi.ChronosObjects.chronosEvent import CHRONOSEvent

    for i, m in enumerate(missions_ids):
        # retrieve events referred to a mission from old APIs
        js = tools.retrieve_json("http://www.spacexplore.it:80/api/missions/details/" + str(m))
        try:
            new = CHRONOSEvent(build=build, old_id=m, obj=js)
            new.store_event()
        except DocumentExistNot:
            if test:
                continue
            else:
                print(DocumentExistNot("EVENTS API: This mission is not in the DB"))
        # if test, dont raise the error adn stop after some events are stored
        if test and i > 20:
            break
    return True


def get_and_store_sensors(build):
    """
    takes the examples of sensors from the JSON file and store them in the db.sensors collection
    :return:
    """
    from input.sensors.sensors_instances import SENSORS

    for s in SENSORS:
        id_ = build.mongod.sensors.insert(s)
        print("sensor stored: " + str(s['name']))

    return None


def annotate_targets_and_events(build, test, docs):
    """
    Establishes "chronos:relTarget" or "chronos:relEvent" or "chronos:relMission" predicate to group "dbpediadocs"
    :return: None
    """

    from tagmeapi.tagMeOperation import TagMeOperation

    ops = TagMeOperation(build=build)
    for i, d in enumerate(docs):
        ops.store_annotations_for_targets_and_events(doc=d)
        if test and i > 15:
            break

    del ops
    return True


def annotate_missions(build, test, missions):
    """
    use the tagmeapi to store annotations about targets and events stored above
    :return: None
    """

    from toolbox import surfing
    from datastoreapi.datastoreErrors import DocumentExists, DocumentExistNot
    from tagmeapi.tagMeOperation import TagMeOperation

    for i, m in enumerate(missions):
        # get resource
        # get body of the resource
        to_crawl = m["owl:sameAs"][0]["@value"]
        try:
            new = surfing.JsonLD()
            text = new.get_body_text_from_dbpedia_jsonld(to_crawl)
            del new
        except DocumentExistNot:
            continue

        new = TagMeOperation(build=build)
        new.tag_and_link_resources_to_mission(m, text)
        del new
        if test and i > 15:
            break

    return True


def link_correlated_dbpediadocs(build, test, dbpedias):
    from toolbox import surfing
    from datastoreapi.datastoreErrors import DocumentExists
    from tagmeapi.tagMeService import TagMeService
    from toolbox import tools

    for i, d in enumerate(dbpedias):
        # relate with the rest of dbpedias
        # filter by rhos
        # link each other chronos:relatedMatch
        name = tools.from_dbpedia_url_return_slug(d["owl:sameAs"][0]["@value"])
        print(d["skos:altLabel"], name)
        for t, d2 in enumerate(dbpedias):
            ops = surfing.JsonLD()
            comparing = tools.from_dbpedia_url_return_slug(d2["owl:sameAs"][0]["@value"])
            del ops
            if name != "Space" and comparing != "Space" and name != comparing:
                print("Relating...")
                output = TagMeService.relate(name, comparing, min_rho=0.67)
                if output and len(output) != 0:
                    print(">>>>>>>>>>>>>>>> Linking " + name + " with " + comparing)
                    try:
                        build.append_link_to_mongodoc(d, "chronos:relatedMatch", d2, "base")
                    except DocumentExists:
                        pass
                    try:
                        build.append_link_to_mongodoc(d2, "chronos:relatedMatch", d, "base")
                    except DocumentExists:
                        pass
            if test and t > 5:
                break
        if test and i > 10:
            break


###############################################################################
#
# LAYER TWO: CRAWLING SPACE AGENCIES WEBSITES
#


class ErrorInOperations(Exception):
    """
    Exception raised in datastoreapi.Operations
    """
    pass