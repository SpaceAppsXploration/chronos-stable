"""
NASA-STI DIVISIONS
"""

STI_divisions = {
    "2871": {
        "name": "Space sciences",
        "definition": "Includes space sciences (general); astronomy; astrophysics; lunar and planetary science and "
                      "exploration; solar physics; and space radiation.",
        "lod": ["https://www.googleapis.com/freebase/v1/topic/m/0718x",
                "http://dbpedia.org/data/Outline_of_space_science.jsond"
        ],
        "label": "space+sciences"
    },
    "2528": {
        "name": "Physics",
        "definition": "Includes physics (general); acoustics; atomic and molecular physics; nuclear physics; optics; "
                      "plasma physics; solid-state physics; and physics of elementary particles and fields.",
        "lod": ["https://www.googleapis.com/freebase/v1/topic/m/05qjt",
        "http://dbpedia.org/data/Physics.jsond"],
        "label": "physics"
    },
    "1332": {
        "name": "Engineering",
        "definition": "Includes engineering (general); communications and radar; electronics and electrical engineering;"
                      " fluid mechanics and thermodynamics; instrumentation and photography; lasers and masers; "
                      "mechanical engineering; quality assurance and reliability; and structural mechanics. "
                      "For related information see also PHYSICS (categories 70 through 77).",
        "lod": ["https://www.googleapis.com/freebase/v1/topic/m/02ky346",
        "http://dbpedia.org/data/Engineering.jsond"],
        "label": "engineering"
    }

}

"""
NASA-STI CATEGORIES (SUBJECTS)
"""
# 89 - Astronomy

STI_subjects = {
 "89" : {
    "name": "Astronomy",
    "alt": "astronomical",
    "includes": "Includes observations of celestial bodies; astronomical instruments and techniques; radio, gamma-ray, x-ray, ultraviolet, and infrared astronomy; and astrometry.",
    "interest": "Exhaustive Interest : Except for astrophysics, all facets of astronomy including radio and gamma-ray astronomy, observations of celestial bodies, their structure, motions, and locations.",
    "exactMatch": [
        ["http://dbpedia.org/data/Astronomy.jsond", "https://www.googleapis.com/freebase/v1/topic/m/0dc_v"]
    ],
    "related": [
        ["https://www.googleapis.com/freebase/v1/topic/m/03n1_", "http://dbpedia.org/data/History_of_astronomy.jsond"]
    ],
    "set": [
        {
            "keyword": "asteroids",
            "scope": "observation",
            "division": 0
        },
        {
            "keyword": "binaries",
            "scope": "observation",
            "division": 0
        },
        {
            "keyword": "black holes",
            "scope": "observation",
            "division": 0
        },
        {
            "keyword": "celestial bodies",
            "scope": "observation",
            "division": 0
        },
        {
            "keyword": "celestial motion",
            "scope": "observation",
            "division": 0
        },
        {
            "keyword": "comets",
            "scope": "observation",
            "division": 0
        },
        {
            "keyword": "discovery of celestial bodies",
            "scope": "",
            "division": 0
        },
        {
            "keyword": "extrasolar planets",
            "scope": "observation",
            "division": 0
        },
        {
            "keyword": "galaxies",
            "scope": "observation",
            "division": 0
        },
        {
            "keyword": "gamma-ray astronomy",
            "scope": "",
            "division": 0
        },
        {
            "keyword": "Hubble telescope",
            "scope": "observation",
            "division": 0
        },
        {
            "keyword": "identification of celestial bodies",
            "scope": "observation",
            "division": 0
        },
        {
            "keyword": "infrared astronomy",
            "scope": "",
            "division": 0
        },
        {
            "keyword": "infrared telescopes",
            "scope": "",
            "division": 0
        },
        {
            "keyword": "JWST (James Webb Space Telescope)",
            "scope": "",
            "division": 0
        },
        {
            "keyword": "Large Space Telescope",
            "scope": "",
            "division": 0
        },
        {
            "keyword": "meteoroids",
            "scope": "observation",
            "division": 0
        },
        {
            "keyword": "meteors",
            "scope": "observation",
            "division": 0
        },
        {
            "keyword": "moons",
            "scope": "observation",
            "division": 0
        },
        {
            "keyword": "natural satellites",
            "scope": "observation",
            "division": 0
        },
        {
            "keyword": "nebulae",
            "scope": "observation",
            "division": 0
        },
        {
            "keyword": "novae",
            "scope": "observation",
            "division": 0
        },
        {
            "keyword": "observation of celestial bodies",
            "scope": "",
            "division": 0
        },
        {
            "keyword": "observatory",
            "scope": "",
            "division": 0
        },
        {
            "keyword": "optical telescope facilities",
            "scope": "",
            "division": 0
        },
        {
            "keyword": "optical telescope",
            "scope": "",
            "division": 0
        },
        {
            "keyword": "planet location",
            "scope": "",
            "division": 0
        },
        {
            "keyword": "pulsars",
            "scope": "observation",
            "division": 0
        },
        {
            "keyword": "quasars",
            "scope": "observation",
            "division": 0
        },
        {
            "keyword": "radar telescope and range finder facilities",
            "scope": "",
            "division": 0
        },
        {
            "keyword": "radar telescopes",
            "scope": "",
            "division": 0
        },
        {
            "keyword": "radio astronomy",
            "scope": "",
            "division": 0
        },
        {
            "keyword": "radio telescopes",
            "scope": "",
            "division": 0
        },
        {
            "keyword": "spaceborne astronomy",
            "scope": "",
            "division": 0
        },
        {
            "keyword": "spectroscopy",
            "scope": "astronomy",
            "division": 0
        },
        {
            "keyword": "star trackers",
            "scope": "observation",
            "division": 0
        },
        {
            "keyword": "stars",
            "scope": "observation",
            "division": 0
        },
        {
            "keyword": "stellar spectroscopy",
            "scope": "",
            "division": 0
        },
        {
            "keyword": "supernovae",
            "scope": "observation",
            "division": 0
        },
        {
            "keyword": "telescopes",
            "scope": "operation",
            "division": 0
        },
        {
            "keyword": "x-ray astronomy",
            "scope": "observation",
            "division": 0
        },
        {
            "keyword": "x-ray telescopes",
            "scope": "observation",
            "division": 0
        }
    ]

},



#Astrophysics - 90
  "90" : {
    "name": "Astrophysics",
    "includes": "Includes cosmology; celestial mechanics; space plasmas; and interstellar and interplanetary gases and dust. Excluded Planetary Sciences(91)",
    "interest": "Exhaustive Interest : All facets of the physical properties of celestial bodies, interplanetary, interstellar, and intergalactic properties; data analysis and calculations of celestial mechanics.",
    "exactMatch": [
        ["http://dbpedia.org/data/Astrophysics.jsond", "https://www.googleapis.com/freebase/v1/topic/m/01_j8n"]
    ],
    "related": [],
    "set": [
        {
            "keyword": "astrochemistry",
            "scope": "",
            "division": 0
        },
        {
            "keyword": "binaries",
            "scope": "astrophysics",
            "division": 0
        },
        {
            "keyword": "black holes",
            "scope": "astrophysics",
            "division": 0
        },
        {
            "keyword": "celestial body physical properties",
            "scope": "",
            "division": 0
        },
        {
            "keyword": "cosmic dust",
            "scope": "",
            "division": 0
        },
{
            "keyword": "cosmic noise",
            "scope": "",
            "division": 0
        },
        {
            "keyword": "cosmology",
            "scope": "",
            "division": 0
        },
        {
            "keyword": "dark energy",
            "scope": "",
            "division": 0
        },
        {
            "keyword": "dark matter",
            "scope": "",
            "division": 0
        },
        {
            "keyword": "expansion of the universe",
            "scope": "",
            "division": 0
        },
{
            "keyword": "galactic evolution",
            "scope": "",
            "division": 0
        },
        {
            "keyword": "galactic structure",
            "scope": "",
            "division": 0
        },
        {
            "keyword": "galaxies",
            "scope": "astrophysics",
            "division": 0
        },
        {
            "keyword": "galaxy clusters",
            "scope": "",
            "division": 0
        },
        {
            "keyword": "gravitational collapse",
            "scope": "astrophysics",
            "division": 0
        },
{
            "keyword": "gravitational theory",
            "scope": "astrophysics",
            "division": 0
        },
        {
            "keyword": "gravitational waves",
            "scope": "astrophysics",
            "division": 0
        },
        {
            "keyword": "hydromagnetics",
            "scope": "astrophysics",
            "division": 0
        },
        {
            "keyword": "intergalactic dust",
            "scope": "",
            "division": 0
        },
        {
            "keyword": "intergalactic gases",
            "scope": "",
            "division": 0
        },
{
            "keyword": "intergalactic matter",
            "scope": "",
            "division": 0
        },
        {
            "keyword": "interplanetary dust",
            "scope": "",
            "division": 0
        },
        {
            "keyword": "interplanetary gases",
            "scope": "",
            "division": 0
        },
        {
            "keyword": "interplanetary matter",
            "scope": "",
            "division": 0
        },
        {
            "keyword": "interplanetary shock waves",
            "scope": "",
            "division": 0
        },
{
            "keyword": "interstellar dust",
            "scope": "",
            "division": 0
        },
        {
            "keyword": "interstellar gases",
            "scope": "",
            "division": 0
        },
        {
            "keyword": "interstellar matter",
            "scope": "",
            "division": 0
        },
        {
            "keyword": "Magellanic clouds",
            "scope": "",
            "division": 0
        },
        {
            "keyword": "magnetism",
            "scope": "extraterrestrial",
            "division": 0
        },
{
            "keyword": "nebulae",
            "scope": "astrophysics",
            "division": 0
        },
        {
            "keyword": "novae",
            "scope": "astrophysics",
            "division": 0
        },
        {
            "keyword": "nuclear astrophysics",
            "scope": "",
            "division": 0
        },
        {
            "keyword": "physical properties of celestial bodies",
            "scope": "",
            "division": 0
        },
        {
            "keyword": "pulsars",
            "scope": "astrophysics",
            "division": 0
        },
{
            "keyword": "quasars",
            "scope": "astrophysics",
            "division": 0
        },
        {
            "keyword": "solar system evolution",
            "scope": "",
            "division": 0
        },
        {
            "keyword": "space plasmas",
            "scope": "",
            "division": 0
        },
        {
            "keyword": "stars",
            "scope": "astrophysics",
            "division": 0
        },
        {
            "keyword": "stellar evolution",
            "scope": "astrophysics",
            "division": 0
        },
{
            "keyword": "stellar luminosity",
            "scope": "",
            "division": 0
        },
        {
            "keyword": "stellar magnetic fields",
            "scope": "",
            "division": 0
        },
        {
            "keyword": "stellar mass accretion",
            "scope": "",
            "division": 0
        },
        {
            "keyword": "stellar physics",
            "scope": "",
            "division": 0
        },
        {
            "keyword": "stellar systems",
            "scope": "",
            "division": 0
        },
        {
            "keyword": "supernovae",
            "scope": "astrophysics",
            "division": 0
        },
    ]
},

#Optics - 74
  "74" : {
    "name": "Optics",
    "includes": "Includes light phenomena and the theory of optical devices. Lasers and Masers excluded",
    "interest": { "Exhaustive": "Theories of light transmission and lenses, light absorption, reflection, and scattering as they relate to aeronautics, astronautics, and space sciences.",
                  "Selective": "Optics and light phenomena with potential aerospace use.",
                  "Negative": "Industrial, commercial, and household applications of optics and light phenomena, lenses, and eyeglasses."
            },
    "exactMatch": [
        ["http://dbpedia.org/data/Optics.jsond", "https://www.googleapis.com/freebase/v1/topic/m/05mn2" ]
    ],
    "related": [],
    "set": [
        {
            "keyword": "Bragg cells",
            "scope": "optical applications",
            "division": 1
        },
        {
            "keyword": "Cassegrain optics",
            "scope": "",
            "division": 1
        },
{
            "keyword": "coherent light",
            "scope": "",
            "division": 1
        },
        {
            "keyword": "electron optics theory",
            "scope": "",
            "division": 1
        },
        {
            "keyword": "geometrical optics",
            "scope": "",
            "division": 1
        },
        {
            "keyword": "infrared optics",
            "scope": "",
            "division": 1
        },
{
            "keyword": "infrared radiation effects",
            "scope": "optical applications",
            "division": 1
        },
        {
            "keyword": "infrared signatures",
            "scope": "optical applications",
            "division": 1
        },
        {
            "keyword": "infrared spectra",
            "scope": "",
            "division": 1
        },
        {
            "keyword": "lens theory",
            "scope": "",
            "division": 1
        },
{
            "keyword": "lens",
            "scope": "optical properties",
            "division": 1
        },
        {
            "keyword": "light absorption",
            "scope": "absorption",
            "division": 1
        },
        {
            "keyword": "light reflection",
            "scope": "reflection",
            "division": 1
        },
        {
            "keyword": "light scattering",
            "scope": "",
            "division": 1
        },
{
            "keyword": "light transmission",
            "scope": "",
            "division": 1
        },
        {
            "keyword": "mirror interference",
            "scope": "optics",
            "division": 1
        },
        {
            "keyword": "modulation",
            "scope": "optics",
            "division": 1
        },
        {
            "keyword": "nonlinear optics",
            "scope": "",
            "division": 1
        },
{
            "keyword": "optical imaging devices",
            "scope": "theory",
            "division": 1
        },
        {
            "keyword": "optical materials",
            "scope": "",
            "division": 1
        },
        {
            "keyword": "optical properties",
            "scope": "",
            "division": 1
        },
        {
            "keyword": "optical",
            "scope": "optics",
            "division": 1
        },
{
            "keyword": "optoelectronics",
            "scope": "optics",
            "division": 1
        },
        {
            "keyword": "photon beams",
            "scope": "",
            "division": 1
        },
        {
            "keyword": "photonics",
            "scope": "",
            "division": 1
        },
        {
            "keyword": "polarization",
            "scope": "optics",
            "division": 1
        },
{
            "keyword": "refraction",
            "scope": "optics",
            "division": 1
        },
        {
            "keyword": "telescopes",
            "scope": "optical properties",
            "division": 1
        },
        {
            "keyword": "ultraviolet radiation",
            "scope": "optics",
            "division": 1
        },
        {
            "keyword": "wave propagation",
            "scope": "optics",
            "division": 1
        },
        {
            "keyword": "x-ray optics",
            "scope": "",
            "division": 1
        },
    ]
},



#Physics (General) - 70
  "70" : {
    "name": "Physics (General)",
    "includes": "Includes general research topics related to mechanics, kinetics, magnetism, and electrodynamics. For specific areas of physics see categories 71 through 77. For related instrumentation see 35 Instrumentation and Photography; for astrophysics, or solar physics see 90 Astrophysics; or 92 Solar Physics.",
    "interest": { "Exhaustive": "The elements of physics as they relate to aeronautics, astronautics, and the aerospace sciences.",
                  "Selective": "The elements of physics from all fields that might have potential aerospace applications.",
                  "Negative": "Nuclear physics for weaponry, large-scale commercial electricity generation, and other applications not having aerospace potential."
        },
    "exactMatch": [
        ["http://dbpedia.org/data/Physics.jsond", "https://www.googleapis.com/freebase/v1/topic/m/05qjt"]
    ],
    "related": [],
    "set": [
        {
            "keyword": "chaos",
            "scope": "",
            "division": 1
        },
        {
            "keyword": "dynamics",
            "scope": "physics",
            "division": 1
        },
        {
            "keyword": "electromagnetic radiation",
            "scope": "theory",
            "division": 1
        },
        {
            "keyword": "electromagnetism",
            "scope": "",
            "division": 1
        },
        {
            "keyword": "electrostatics",
            "scope": "",
            "division": 1
        },
{
            "keyword": "ferromagnetism",
            "scope": "",
            "division": 1
        },
        {
            "keyword": "field theory",
            "scope": "physics",
            "division": 1
        }
    ]
},


#Nuclear Physics - 73
  "73" : {
    "name": "Nuclear Physics",
    "includes": "Includes nuclear particles; and reactor theory. For space radiation see 93 Space Radiation. For atomic and molecular physics see 72 Atomic and Molecular Physics. For elementary particle physics see 77 Physics of Elementary Particles and Fields. For nuclear astrophysics see 90 Astrophysics.",
    "interest": { "Exhaustive": "The basic theories and formulas of nuclear physics and testing and research equipment to support these developments as they relate to aeronautics, astronautics, and aerospace sciences.",
                  "Selective": "Those applications of nuclear physics that may be of use to the aerospace program, e.g., propulsion systems and power sources, suitable for aerospace use.",
                  "Negative": "Large, commercial nuclear reactor applications; ship propulsion reactors."
        },
    "exactMatch": [
        ["http://dbpedia.org/data/Nuclear_physics.jsond", "https://www.googleapis.com/freebase/v1/topic/m/05bjy"]
    ],
    "related": [],
    "set": [
        {
            "keyword": "alpha rays",
            "scope": "theory",
            "division": 1
        },
        {
            "keyword": "beta rays",
            "scope": "theory",
            "division": 1
        },
{
            "keyword": "electron beams",
            "scope": "",
            "division": 1
        },
        {
            "keyword": "gamma rays",
            "scope": "theory",
            "division": 1
        },
        {
            "keyword": "ion beams",
            "scope": "nuclear interactions",
            "division": 1
        },
        {
            "keyword": "nuclear decay",
            "scope": "",
            "division": 1
        },
        {
            "keyword": "nuclear fission",
            "scope": "theory",
            "division": 1
        },
        {
            "keyword": "nuclear particles",
            "scope": "theory",
            "division": 1
        },
{
            "keyword": "nuclear physics",
            "scope": "",
            "division": 1
        },
        {
            "keyword": "nuclear scattering",
            "scope": "",
            "division": 1
        },
        {
            "keyword": "nuclear structure",
            "scope": "",
            "division": 1
        },
        {
            "keyword": "proton beams",
            "scope": "nuclear interactions",
            "division": 1
        },
        {
            "keyword": "radioisotopes",
            "scope": "",
            "division": 1
        },
        {
            "keyword": "x-ray radiation",
            "scope": "theory",
            "division": 1
        },
  ]
},

# Atomic and Molecular Physics -72
  "72" : {
    "name": "Atomic and Molecular Physics",
    "includes": "Includes nuclear particles; and reactor theory. For space radiation see 93 Space Radiation. For atomic and molecular physics see 72 Atomic and Molecular Physics. For elementary particle physics see 77 Physics of Elementary Particles and Fields. For nuclear astrophysics see 90 Astrophysics.",
    "interest": { "Exhaustive": "The basic theories and formulas of atomic and molecular physics as they relate to aeronautics, astronautics, and aerospace sciences. Those elements of atomic and molecular physics that have actual or potential application to the aerospace program.",
                  "Selective": "Those applications of atomic and molecular science that have potential use to the aerospace sciences.",
                  "Negative": "Basic theories and formulas of atomic and molecular physics that have no application to the aerospace sciences."
        },
    "exactMatch": [
        ["http://dbpedia.org/data/Atomic_physics.jsond", "https://www.googleapis.com/freebase/v1/topic/m/0mxq"],
        ["http://dbpedia.org/data/Molecular_physics.jsond", "https://www.googleapis.com/freebase/v1/topic/m/031z81"]
    ],
    "related": [],
    "set": [
        {
            "keyword": "absorption of radiation by atoms",
            "scope": "",
            "division": 1
        },
        {
            "keyword": "atomic beam measurements",
            "scope": "",
            "division": 1
        },
        {
            "keyword": "atomic collisions",
            "scope": "",
            "division": 1
        },
        {
            "keyword": "atomic electron properties",
            "scope": "",
            "division": 1
        },
        {
            "keyword": "atomic energy levels",
            "scope": "",
            "division": 1
        },
        {
            "keyword": "atomic nuclei",
            "scope": "theory",
            "division": 1
        },
{
            "keyword": "atomic physics",
            "scope": "",
            "division": 1
        },
        {
            "keyword": "atomic spectra",
            "scope": "",
            "division": 1
        },
        {
            "keyword": "atomic structure",
            "scope": "",
            "division": 1
        },
        {
            "keyword": "electron collisions",
            "scope": "",
            "division": 1
        },
        {
            "keyword": "electron scattering",
            "scope": "",
            "division": 1
        },
        {
            "keyword": "emission of radiation by atoms",
            "scope": "",
            "division": 1
        },
{
            "keyword": "intermolecular forces",
            "scope": "",
            "division": 1
        },
        {
            "keyword": "ion beams",
            "scope": "theory",
            "division": 1
        },
        {
            "keyword": "ion dynamics",
            "scope": "",
            "division": 1
        },
        {
            "keyword": "ion exchange",
            "scope": "",
            "division": 1
        },
        {
            "keyword": "molecular beams",
            "scope": "",
            "division": 1
        },
        {
            "keyword": "molecular energy",
            "scope": "",
            "division": 1
        },
{
            "keyword": "molecular interactions",
            "scope": "",
            "division": 1
        },
        {
            "keyword": "molecular physics",
            "scope": "",
            "division": 1
        },
        {
            "keyword": "molecular properties",
            "scope": "",
            "division": 1
        },
        {
            "keyword": "molecular spectra",
            "scope": "",
            "division": 1
        },
        {
            "keyword": "molecular spectroscopy",
            "scope": "",
            "division": 1
        },
        {
            "keyword": "molecular structure",
            "scope": "",
            "division": 1
        },
{
            "keyword": "photon interactions with atoms and molecules",
            "scope": "",
            "division": 1
        },
        {
            "keyword": "radiation absorption by atoms",
            "scope": "",
            "division": 1
        },
        {
            "keyword": "theories of atomic physics",
            "scope": "",
            "division": 1
        },
        {
            "keyword": "theories of molecular physics",
            "scope": "",
            "division": 1
        },
  ]

},



#Plasma Physics - 75
  "75" : {
    "name": "Plasma Physics",
    "includes": "Includes magnetohydrodynamics and plasma fusion. For ionospheric plasmas see 46 Geophysics. For space plasmas see 90 Astrophysics.",
    "interest": { "Exhaustive": "Theoretical magnetohydrodynamics and plasma fusion; research and test equipment for studies in plasma physics as related to aerospace sciences.",
                  "Selective": "Applications of magnetohydrodynamics and plasma fusion that may be of interest for propulsion, power sources, and other uses in the aerospace program.",
                  "Negative": "Heavy industrial and commercial applications; large power reactors."
        },
    "exactMatch": [
        ["http://dbpedia.org/data/Plasma_(physics).jsond", "https://www.googleapis.com/freebase/v1/topic/m/09jww5"]
    ],
    "related": [
        ["https://www.googleapis.com/freebase/v1/topic/m/06zj7c","http://dbpedia.org/data/Astrophysical_plasma.jsond"],
        ["https://www.googleapis.com/freebase/v1/topic/m/01mssk","http://dbpedia.org/data/Plasma_cosmology.jsond"]
    ],
    "set": [
        {
            "keyword": "electrogasdynamics",
            "scope": "",
            "division": 1
        },
        {
            "keyword": "electrohydrodynamics",
            "scope": "",
            "division": 1
        },
        {
            "keyword": "electron density",
            "scope": "plasma physics",
            "division": 1
        },
        {
            "keyword": "hydromagnetics",
            "scope": "plasma physics",
            "division": 1
        },
        {
            "keyword": "ion beams",
            "scope": "plasma physics",
            "division": 1
        },
        {
            "keyword": "laser interaction with plasmas",
            "scope": "",
            "division": 1
        },
{
            "keyword": "magnetogasdynamics",
            "scope": "",
            "division": 1
        },
        {
            "keyword": "magnetohydrodynamics",
            "scope": "",
            "division": 1
        },
        {
            "keyword": "magnetoplasmas",
            "scope": "",
            "division": 1
        },
        {
            "keyword": "microwave interaction with plasmas",
            "scope": "",
            "division": 1
        },
        {
            "keyword": "plasma conductivity",
            "scope": "",
            "division": 1
        },
        {
            "keyword": "plasma dynamics",
            "scope": "",
            "division": 1
        },
{
            "keyword": "plasma flow",
            "scope": "",
            "division": 1
        },
        {
            "keyword": "plasma oscillations",
            "scope": "",
            "division": 1
        },
        {
            "keyword": "plasma physics",
            "scope": "",
            "division": 1
        },
{
            "keyword": "plasma physics research equipment",
            "scope": "",
            "division": 1
        },
        {
            "keyword": "plasma theory",
            "scope": "",
            "division": 1
        },
        {
            "keyword": "plasma waves",
            "scope": "",
            "division": 1
        },


    ]

},

#Solid State Physics - 76
  "76" : {
    "name": "Solid State Physics",
    "includes": "Includes condensed matter physics, crystallography, and superconductivity.",
    "interest": { "Exhaustive": "All facets of solid-state physics and the solid-state effects in electrical and electronic devices as they relate to aeronautics, astronautics, and aerospace sciences.",
                  "Selective": "Commercial applications of solid-state physics that might have a potential for use in aerospace applications.",
                  "Negative": "Solid-state physics with no application to aerospace science."
        },
    "exactMatch": [
        ["https://www.googleapis.com/freebase/v1/topic/m/0pzvq", "http://dbpedia.org/data/Solid-state_physics.jsond"]
    ],
    "related": [],
    "set": [
        {
            "keyword": "acceptors",
            "scope": "solid state",
            "division": 1
        },
        {
            "keyword": "band structure of solids",
            "scope": "",
            "division": 1
        },
        {
            "keyword": "condensed matter physics",
            "scope": "",
            "division": 1
        },
{
            "keyword": "conductivity",
            "scope": "solid state",
            "division": 1
        },
        {
            "keyword": "donors",
            "scope": "solid state",
            "division": 1
        },
        {
            "keyword": "electrical transport properties in solids",
            "scope": "",
            "division": 1
        },
{
            "keyword": "energy gaps in semiconductors",
            "scope": "",
            "division": 1
        },
        {
            "keyword": "holes",
            "scope": "electron deficiencies",
            "division": 1
        },
        {
            "keyword": "radiation effects in semiconductors",
            "scope": "",
            "division": 1
        },
{
            "keyword": "semiconductor materials",
            "scope": "",
            "division": 1
        },
        {
            "keyword": "solid state physics",
            "scope": "",
            "division": 1
        },
        {
            "keyword": "superconducting materials",
            "scope": "",
            "division": 1
        },
{
            "keyword": "superconductivity",
            "scope": "theory",
            "division": 1
        },
        {
            "keyword": "thermoelectric materials",
            "scope": "",
            "division": 1
        },

    ]
},


#Physics of Elementary Particles and Fields - 77
  "77" : {
    "name": "Physics of Elementary Particles and Fields",
    "includes": "Includes quantum mechanics; theoretical physics; and statistical mechanics. For related information see also 72 Atomic and Molecular Physics; 73 Nuclear Physics.",
    "interest": { "Exhaustive": "SELINT: Aspects of elementary particles, field theory, and statistical physics for those applications that may be of use to the aerospace program."
        },
    "exactMatch": [
        ["https://www.googleapis.com/freebase/v1/topic/m/05skl", "http://dbpedia.org/data/Particle_physics.jsond"],
        ["http://dbpedia.org/data/Elementary_particle.jsond", "https://www.googleapis.com/freebase/v1/topic/m/02__0"]
    ],
    "related": [],
    "set": [
        {
            "keyword": "annihilation reactions",
            "scope": "",
            "division": 1
        },
        {
            "keyword": "antimatter",
            "scope": "",
            "division": 1
        },
        {
            "keyword": "antiparticles",
            "scope": "",
            "division": 1
        },
{
            "keyword": "elementary particle interactions",
            "scope": "",
            "division": 1
        },
        {
            "keyword": "elementary particles",
            "scope": "",
            "division": 1
        },
        {
            "keyword": "high energy physics",
            "scope": "",
            "division": 1
        },
        {
            "keyword": "particle physics",
            "scope": "",
            "division": 1
        },
        {
            "keyword": "strong interactions",
            "scope": "field theory",
            "division": 1
        },
{
            "keyword": "supergravity",
            "scope": "",
            "division": 1
        },
        {
            "keyword": "theoretical physics",
            "scope": "",
            "division": 1
        },
        {
            "keyword": "theory of relativity",
            "scope": "",
            "division": 1
        },
        {
            "keyword": "unified field theory",
            "scope": "",
            "division": 1
        },
        {
            "keyword": "weak interactions",
            "scope": "field theory",
            "division": 1
        },

    ]
},



#Solar Physics -92 - 0
  "92" : {
    "name": "Solar Physics",
    "includes": "Includes solar activity, solar flares, solar radiation and sunspots. For related information see 93 Space Radiation.",
    "interest": { "Exhaustive": "All facets of solar physics."
    },
    "exactMatch": [
        ["https://www.googleapis.com/freebase/v1/topic/m/082zm2", "http://dbpedia.org/data/Solar_physics.jsond"]
    ],
    "related": [
        ["https://www.googleapis.com/freebase/v1/topic/m/06m_p", "http://dbpedia.org/data/Sun.jsond"]
    ],
    "set": [
        {
            "keyword": "alpha rays",
            "scope": "solar",
            "division": 0
        },
        {
            "keyword": "beta rays",
            "scope": "solar",
            "division": 0
        },
        {
            "keyword": "chromosphere",
            "scope": "solar",
            "division": 0
        },
        {
            "keyword": "coronal mass ejections",
            "scope": "solar",
            "division": 0
        },
        {
            "keyword": "heliophysics",
            "scope": "",
            "division": 0
        },
{
            "keyword": "heliosphere",
            "scope": "",
            "division": 0
        },
        {
            "keyword": "lunar eclipses",
            "scope": "",
            "division": 0
        },
        {
            "keyword": "photosphere",
            "scope": "solar",
            "division": 0
        },
        {
            "keyword": "solar activity",
            "scope": "",
            "division": 0
        },
        {
            "keyword": "solar atmosphere",
            "scope": "",
            "division": 0
        },
        {
            "keyword": "solar constants",
            "scope": "",
            "division": 0
        },
        {
            "keyword": "solar corona",
            "scope": "",
            "division": 0
        },
        {
            "keyword": "solar cycles",
            "scope": "",
            "division": 0
        },
        {
            "keyword": "solar eclipses",
            "scope": "",
            "division": 0
        },
        {
            "keyword": "solar flares",
            "scope": "",
            "division": 0
        },
        {
            "keyword": "solar magnetic field",
            "scope": "",
            "division": 0
        },
        {
            "keyword": "solar mass",
            "scope": "",
            "division": 0
        },
        {
            "keyword": "solar physics",
            "scope": "",
            "division": 0
        },
        {
            "keyword": "solar radiation",
            "scope": "",
            "division": 0
        },
        {
            "keyword": "solar radio emissions",
            "scope": "",
            "division": 0
        },
        {
            "keyword": "solar spectra",
            "scope": "",
            "division": 0
        },
        {
            "keyword": "solar structure",
            "scope": "",
            "division": 0
        },
        {
            "keyword": "sun",
            "scope": "",
            "division": 0
        },
        {
            "keyword": "sunspots",
            "scope": "",
            "division": 0
        },

    ]
},



#Space Radiation - 93 - 0
  "93" : {
    "name": "Space Radiation",
    "includes": "Includes cosmic radiation; and inner and outer Earth radiation belts.",
    "interest": { "Exhaustive": "All facets of space radiation."
    },
    "exactMatch": [
        ["https://www.googleapis.com/freebase/v1/topic/m/0ctpn", "http://dbpedia.org/data/Cosmic_ray.jsond"]
    ],
    "related": [
        ["http://dbpedia.org/data/Health_threat_from_cosmic_rays.jsond", "https://www.googleapis.com/freebase/v1/topic/m/03d2v06"]
    ],
    "set": [
        {
            "keyword": "alpha rays",
            "scope": "space",
            "division": 0
        },
        {
            "keyword": "beta rays",
            "scope": "space",
            "division": 0
        },
        {
            "keyword": "cosmic radiation",
            "scope": "",
            "division": 0
        },
        {
            "keyword": "galactic radiation",
            "scope": "",
            "division": 0
        },
        {
            "keyword": "gamma rays",
            "scope": "space",
            "division": 0
        },
{
            "keyword": "inner Earth radiation belts",
            "scope": "",
            "division": 0
        },
        {
            "keyword": "intergalactic radiation",
            "scope": "",
            "division": 0
        },
        {
            "keyword": "interstellar radiation",
            "scope": "",
            "division": 0
        },
        {
            "keyword": "outer Earth radiation belts",
            "scope": "",
            "division": 0
        },
        {
            "keyword": "radiation belts",
            "scope": "",
            "division": 0
        },
{
            "keyword": "space radiation",
            "scope": "",
            "division": 0
        },
        {
            "keyword": "stellar radiation",
            "scope": "",
            "division": 0
        },
        {
            "keyword": "ultraviolet radiation",
            "scope": "space",
            "division": 0
        },
        {
            "keyword": "Van Allen belts",
            "scope": "",
            "division": 0
        },
        {
            "keyword": "x-ray radiation",
            "scope": "space",
            "division": 0
        },


    ]
},

#Lunar and Planetary Science and Exploration - 91 - 0
  "91" : {
    "name": "Lunar and Planetary Science and Exploration",
    "includes": "Includes planetology; selenology; meteorites; comets; craters; and manned and unmanned planetary and lunar flights.",
    "interest": { "Exhaustive": "All facets of lunar and planetary sciences, and manned, unmanned, or remote exploration of planets and their structure, including planets within the solar system or elsewhere within the universe."
    },
    "exactMatch": [
        ["https://www.googleapis.com/freebase/v1/topic/m/06wc5d", "http://dbpedia.org/data/Selenography.jsond"],
        ["https://www.googleapis.com/freebase/v1/topic/m/05xg2", "http://dbpedia.org/data/Planetary_science.jsond"]
    ],
    "related": [
        ["https://www.googleapis.com/freebase/v1/topic/m/04wv_", "http://dbpedia.org/data/Moon.jsond"],
        ["https://www.googleapis.com/freebase/v1/topic/m/06lwjk", "http://dbpedia.org/data/Geology_of_the_Moon.jsond"]
    ],
    "set": [
        {
            "keyword": "asteroids",
            "scope": "characteristics and composition",
            "division": 0
        },
        {
            "keyword": "cis-lunar",
            "scope": "",
            "division": 0
        },
        {
            "keyword": "comet exploration",
            "scope": "",
            "division": 0
        },
        {
            "keyword": "comet",
            "scope": "space exploration",
            "division": 0
        },
        {
            "keyword": "craters",
            "scope": "extraterrestrial",
            "division": 0
        },
{
            "keyword": "dwarf planets",
            "scope": "",
            "division": 0
        },
        {
            "keyword": "Earth analogs",
            "scope": "",
            "division": 0
        },
        {
            "keyword": "roving vehicles",
            "scope": "extraterrestrial",
            "division": 0
        },
        {
            "keyword": "flyby missions",
            "scope": "",
            "division": 0
        },
        {
            "keyword": "gas giant",
            "scope": "planets",
            "division": 0
        },
{
            "keyword": "lunar and planetary",
            "scope": "resource utilization",
            "division": 0
        },
        {
            "keyword": "lunar",
            "scope": "",
            "division": 0
        },
        {
            "keyword": "lunar evolution",
            "scope": "",
            "division": 0
        },
        {
            "keyword": "lunar exploration",
            "scope": "",
            "division": 0
        },
        {
            "keyword": "lunar landing sites",
            "scope": "planets",
            "division": 0
        },
{
            "keyword": "lunar mapping",
            "scope": "",
            "division": 0
        },
        {
            "keyword": "lunar photography",
            "scope": "",
            "division": 0
        },
        {
            "keyword": "lunar regolith simulants",
            "scope": "",
            "division": 0
        },
        {
            "keyword": "lunar samples",
            "scope": "",
            "division": 0
        },
        {
            "keyword": "lunar structure",
            "scope": "",
            "division": 0
        },
{
            "keyword": "manned flights",
            "scope": "space exploration",
            "division": 0
        },
        {
            "keyword": "manned lunar exploration",
            "scope": "",
            "division": 0
        },
        {
            "keyword": "manned Mars missions",
            "scope": "",
            "division": 0
        },
        {
            "keyword": "manned planetary exploration",
            "scope": "",
            "division": 0
        },
        {
            "keyword": "Mars exploration",
            "scope": "planets",
            "division": 0
        },
        {
            "keyword": "meteorites",
            "scope": "space exploration",
            "division": 0
        },
        {
            "keyword": "meteoroids",
            "scope": "space exploration",
            "division": 0
        },
        {
            "keyword": "meteors",
            "scope": "space exploration",
            "division": 0
        },
        {
            "keyword": "moons",
            "scope": "characteristics and composition",
            "division": 0
        },
        {
            "keyword": "natural satellites",
            "scope": "characteristics and composition",
            "division": 0
        },
{
            "keyword": "planetary atmospheres",
            "scope": "",
            "division": 0
        },
        {
            "keyword": "planetary evolution",
            "scope": "",
            "division": 0
        },
        {
            "keyword": "planetary exploration",
            "scope": "",
            "division": 0
        },
        {
            "keyword": "manned planetary exploration",
            "scope": "",
            "division": 0
        },
        {
            "keyword": "planetary mapping",
            "scope": "",
            "division": 0
        },
        {
            "keyword": "planetary motion",
            "scope": "",
            "division": 0
        },
        {
            "keyword": "planetary photography",
            "scope": "space exploration",
            "division": 0
        },
        {
            "keyword": "planetary samples",
            "scope": "",
            "division": 0
        },
        {
            "keyword": "planetary satellites",
            "scope": "characteristics and composition",
            "division": 0
        },
        {
            "keyword": "planetary structure",
            "scope": "",
            "division": 0
        },
{
            "keyword": "planetology",
            "scope": "",
            "division": 0
        },
        {
            "keyword": "remote exploration of planets",
            "scope": "",
            "division": 0
        },
        {
            "keyword": "selenography",
            "scope": "",
            "division": 0
        },
        {
            "keyword": "selenology",
            "scope": "",
            "division": 0
        },
        {
            "keyword": "soil sampling and analysis",
            "scope": "planetology",
            "division": 0
        },
        {
            "keyword": "solar system bodies",
            "scope": "space exploration",
            "division": 0
        },
        {
            "keyword": "planetary photography",
            "scope": "space exploration",
            "division": 0
        },
        {
            "keyword": "tektites",
            "scope": "",
            "division": 0
        },
        {
            "keyword": "terrestrial planets",
            "scope": "",
            "division": 0
        },
        {
            "keyword": "trans-lunar space environment",
            "scope": "",
            "division": 0
        },
        {
            "keyword": "unmanned flights",
            "scope": "space exploration",
            "division": 0
        },
        {
            "keyword": "unmanned lunar exploration",
            "scope": "",
            "division": 0
        },
        {
            "keyword": "unmanned planetary exploration",
            "scope": "",
            "division": 0
        },

    ]

},



#35 Instrumentation and Photography - 2
  "35" : {
    "name": "Instrumentation and Photography",
    "includes": "Includes remote sensors; measuring instruments and gages; detectors; cameras and photographic supplies; and holography. For aerial photography see 43 Earth Resources and Remote Sensing. For related information see also 06 Avionics and Aircraft Instrumentation; and 19 Spacecraft Instrumentation.",
    "interest": { "Exhaustive": "Design, development, installation, and use of devices for detecting, measuring, recording, telemetering, processing, or analyzing values or quantities related to aeronautical or space flight; the environment within or outside the flight vehicle; the physical operation and well being of the flight vehicle and its structure during all phases of flight; the facilities for testing and/or developing the flight vehicle; the observations and experiments performed as a result of the flight of these vehicles.",
                  "Selective": "Instrument design, development, and theory for other purposes that have potential aerospace applications because of advanced or unusual features, or are developed for extreme environments or unusual test conditions.",
                  "Negative": "Commercial off-the-shelf photographic equipment and instrument design and development for general use for artistic or commercial applications."
        },
    "exactMatch": [
        ["http://dbpedia.org/data/Instrumentation.jsond", "https://www.googleapis.com/freebase/v1/topic/m/0crcy"]
    ],
    "related": [
        ["http://dbpedia.org/data/Optical_telescope.jsond", "https://www.googleapis.com/freebase/v1/topic/m/01ngsz"],
        ["http://dbpedia.org/data/Sensor.jsond", "https://www.googleapis.com/freebase/v1/topic/m/01j7cq"]
    ],
    "set": [
        {
            "keyword": "ablation sensors",
            "scope": "design and techniques",
            "division": 2
        },
        {
            "keyword": "analyzing devices",
            "scope": "design and techniques",
            "division": 2
        },
        {
            "keyword": "anemometers",
            "scope": "design and techniques",
            "division": 2
        },
        {
            "keyword": "atomic clocks",
            "scope": "design and techniques",
            "division": 2
        },
        {
            "keyword": "attitude indicators",
            "scope": "design and techniques",
            "division": 2
        },
        {
            "keyword": "bioelectronic instruments",
            "scope": "theory and techniques",
            "division": 2
        },
        {
            "keyword": "bioinstrumentation",
            "scope": "theory and techniques",
            "division": 2
        },
        {
            "keyword": "Bragg cells",
            "scope": "design and techniques",
            "division": 2
        },
        {
            "keyword": "camera",
            "scope": "",
            "division": 2
        },
        {
            "keyword": "coronagraphs",
            "scope": "",
            "division": 2
        },
        {
            "keyword": "darkroom equipment",
            "scope": "",
            "division": 2
        },
        {
            "keyword": "detectors",
            "scope": "",
            "division": 2
        },
        {
            "keyword": "Earth sensors",
            "scope": "",
            "division": 2
        },
{
            "keyword": "electron microscopes",
            "scope": "",
            "division": 2
        },
        {
            "keyword": "electro-optical systems",
            "scope": "instrumentation",
            "division": 2
        },
        {
            "keyword": "emissivity measurements",
            "scope": "",
            "division": 2
        },
        {
            "keyword": "filters",
            "scope": "photographic",
            "division": 2
        },
        {
            "keyword": "flow visualization",
            "scope": "instrumentation",
            "division": 2
        },
        {
            "keyword": "fluid flow sensors",
            "scope": "",
            "division": 2
        },
        {
            "keyword": "gages",
            "scope": "",
            "division": 2
        },
        {
            "keyword": "geophysical sensors",
            "scope": "design and techniques",
            "division": 2
        },
        {
            "keyword": "gyroscopes",
            "scope": "design and operation",
            "division": 2
        },
        {
            "keyword": "image enhancement",
            "scope": "",
            "division": 2
        },
        {
            "keyword": "infrared sensors",
            "scope": "instrumentation",
            "division": 2
        },
        {
            "keyword": "instrumentation",
            "scope": "general",
            "division": 2
        },
        {
            "keyword": "interferometers",
            "scope": "",
            "division": 2
        },
{
            "keyword": "ion mass spectrometers",
            "scope": "instrumentation",
            "division": 2
        },
        {
            "keyword": "laser Doppler velocimeters",
            "scope": "instrumentation",
            "division": 2
        },
        {
            "keyword": "laser instruments",
            "scope": "design and operation",
            "division": 2
        },
        {
            "keyword": "lenses",
            "scope": "photographic",
            "division": 2
        },
        {
            "keyword": "mass spectrometers",
            "scope": "instrumentation",
            "division": 2
        },
        {
            "keyword": "measuring instruments",
            "scope": "",
            "division": 2
        },
        {
            "keyword": "micrometeoroid sensors",
            "scope": "instrumentation",
            "division": 2
        },
        {
            "keyword": "microscopes",
            "scope": "instrumentation",
            "division": 2
        },
        {
            "keyword": "multimode sensors",
            "scope": "",
            "division": 2
        },
        {
            "keyword": "multispectral sensors",
            "scope": "",
            "division": 2
        },
        {
            "keyword": "optical imaging devices",
            "scope": "design and techniques",
            "division": 2
        },
        {
            "keyword": "optical measuring instruments",
            "scope": "design and techniques",
            "division": 2
        },
        {
            "keyword": "oscilloscopes",
            "scope": "",
            "division": 2
        },
{
            "keyword": "ozonesondes",
            "scope": "",
            "division": 2
        },
        {
            "keyword": "photographic processing equipment",
            "scope": "instrumentation",
            "division": 2
        },
        {
            "keyword": "photographic supplies",
            "scope": "design and operation",
            "division": 2
        },
        {
            "keyword": "photography",
            "scope": "general",
            "division": 2
        },
        {
            "keyword": "photometry",
            "scope": "",
            "division": 2
        },
        {
            "keyword": "pressure transducers",
            "scope": "",
            "division": 2
        },
        {
            "keyword": "radiation instruments",
            "scope": "",
            "division": 2
        },
        {
            "keyword": "radiography",
            "scope": "instrumentation",
            "division": 2
        },
        {
            "keyword": "recording devices",
            "scope": "",
            "division": 2
        },
        {
            "keyword": "remote sensors",
            "scope": "",
            "division": 2
        },
        {
            "keyword": "scatterometers",
            "scope": "design and techniques",
            "division": 2
        },
        {
            "keyword": "sensors",
            "scope": "general",
            "division": 2
        },
        {
            "keyword": "shock tube instruments",
            "scope": "",
            "division": 2
        },
{
            "keyword": "spectral analysis instruments",
            "scope": "",
            "division": 2
        },
        {
            "keyword": "spectrometers",
            "scope": "general",
            "division": 2
        },
        {
            "keyword": "spectroscopes",
            "scope": "",
            "division": 2
        },
        {
            "keyword": "temperature measuring instruments",
            "scope": "",
            "division": 2
        },
        {
            "keyword": "thermocouples",
            "scope": "design and techniques",
            "division": 2
        },
        {
            "keyword": "transducers",
            "scope": "applications",
            "division": 2
        },
        {
            "keyword": "two-gas sensors",
            "scope": "general",
            "division": 2
        },
        {
            "keyword": "vidicon cameras",
            "scope": "",
            "division": 2
        },
        

    ]
}




}