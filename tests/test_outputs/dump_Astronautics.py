__author__ = 'lorenzo'

dump_astronautics = {
    '@id': 'http://pramantha.eu/areas/astronautics',
     '@language': 'en',
     '@type': 'http://www.w3.org/2004/02/skos/core#Concept',
     'chronos:code': '578',
     'chronos:group': 'areas',
     'owl:sameAs': {},
     'schema:provider': {'@id': 'http://pramantha.eu/organization/NASA+Sientific+and+Technical+Information+Program',
                         '@type': 'http://www.w3.org/2004/02/skos/core#Concept'},


     'skos:broader': {'@id': 'http://pramantha.eu/organization/NASA+Sientific+and+Technical+Information+Program',
                      '@type': 'http://www.w3.org/2004/02/skos/core#Concept'
     },

    'skos:narrower': [{'@id': 'http://pramantha.eu/subjects/astrodynamics',
                        '@type': 'http://www.w3.org/2004/02/skos/core#Concept',
                        'skos:topConceptOf': {'@id': '_:subj13',
                                          '@type': 'http://www.w3.org/2004/02/skos/core#ConceptScheme'}
                        },

                   {'@id': 'http://pramantha.eu/subjects/astronautics+(general)',
                    '@type': 'http://www.w3.org/2004/02/skos/core#Concept',

                    'skos:topConceptOf': {'@id': '_:subj12',
                                          '@type': 'http://www.w3.org/2004/02/skos/core#ConceptScheme'}
                    },

                   {'@id': 'http://pramantha.eu/subjects/ground+support+systems+and+facilities+(space)',
                    '@type': 'http://www.w3.org/2004/02/skos/core#Concept',

                    'skos:topConceptOf': {'@id': '_:subj14',
                                          '@type': 'http://www.w3.org/2004/02/skos/core#ConceptScheme'
                                          }
                    },
                   {'@id': 'http://pramantha.eu/subjects/launch+vehicles+and+launch+operations',
                    '@type': 'http://www.w3.org/2004/02/skos/core#Concept',

                    'skos:topConceptOf': {'@id': '_:subj15',
                                          '@type': 'http://www.w3.org/2004/02/skos/core#ConceptScheme'}
                    },
                   {'@id': 'http://pramantha.eu/subjects/space+transportation+and+safety',
                    '@type': 'http://www.w3.org/2004/02/skos/core#Concept',
                    'skos:topConceptOf': {'@id': '_:subj16',
                                          '@type': 'http://www.w3.org/2004/02/skos/core#ConceptScheme',
                                          }
                    },
                   {'@id': 'http://pramantha.eu/subjects/spacecraft+design+testing+and+performance',
                    '@type': 'http://www.w3.org/2004/02/skos/core#Concept',

                    'skos:topConceptOf': {'@id': '_:subj18',
                                          '@type': 'http://www.w3.org/2004/02/skos/core#ConceptScheme',
                                          }
                    },
                   {'@id': 'http://pramantha.eu/subjects/spacecraft+instrumentation+and+astrionics',
                    '@type': 'http://www.w3.org/2004/02/skos/core#Concept',

                    'skos:topConceptOf': {'@id': '_:subj19',
                                          '@type': 'http://www.w3.org/2004/02/skos/core#ConceptScheme',
                                          }
                    },
                   {'@id': 'http://pramantha.eu/subjects/spacecraft+propulsion+and+power',
                    '@type': 'http://www.w3.org/2004/02/skos/core#Concept',

                    'skos:topConceptOf': {'@id': '_:subj20',
                                          '@type': 'http://www.w3.org/2004/02/skos/core#ConceptScheme',

                   }}
                    ],
 'skos:prefLabel': 'Astronautics',
 'skos:scopeNote': 'Includes astronautics (general); astrodynamics; ground\n    support systems and facilities (space); launch vehicles and\n    launch operations; space transportation and safety; space\n    communications, spacecraft communications, command, and\n    tracking; spacecraft design, testing and performance;\n    spacecraft instrumentation and astrionics; and spacecraft\n    propulsion and power. For related information see also\n    Aeronautics (categories 01 through 09).\n  '
 }
