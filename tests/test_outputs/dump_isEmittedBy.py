__author__ = 'lorenzo'

dump_isemitteby = {
        "owl:inverseOf" : "http://pramantha.eu/ontology/sensors/emits",
        "@type" : [
                "owl:AsymmetricProperty",
                "owl:IrreflexiveProperty",
                "owl:ObjectProperty"
        ],
        "rdfs:domain" : "http://pramantha.eu/ontology/sensors/PhysicalEntity",
        "rdfs:range" : "http://pramantha.eu/ontology/sensors/Detector",
        "@id" : "http://pramantha.eu/ontology/sensors/isEmittedBy",
        "rdfs:comment" : "A relation between a PhysicalEntity and a Detector. It is the inverse of the emits property. In case the detector is an active sensor, it \"fires\" something out, usually light, which is backscattered and absorbed. This \"something\", say, light, isEmittedBy the firing Detector"
}

