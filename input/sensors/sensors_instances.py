__author__ = 'lorenzo@pramantha.net'


SENSORS = [
    {
        "@id": "http://api.pramantha.net/data/sensors/CHIVA-detector",
        "name": "CHIVA-detector",
        "chronos:relMission": {"@id": "http://api.pramantha.net/data/mission/Rosetta_(spacecraft)"},
        "@type": "http://ontology.projectchronos.eu/subsystems/Spacecraft_Detector",
        "spacecraft:embedSensor": [
            "http://api.pramantha.net/data/sensors/CHIVA-P",
            "http://api.pramantha.net/data/sensors/CHIVA-M1",
            "http://api.pramantha.net/data/sensors/CHIVA-M2"
        ],
        "rdfs:comment": "this is a generic detector for a mission, look for more specific components that are part of this payload (spacecraft:isComponentOf)"
    },
    {
        "@id": "http://api.pramantha.net/data/sensors/CHIVA-P",
        "subsystems:manufacturer": "http://api.pramantha.net/data/dbpediadocs/European_Space_Agency",
        "name": "CHIVA-P",
        "fullName": "ÇIVA-P",
        "chronos:relMission": {"@id": "http://api.pramantha.net/data/mission/Rosetta_(spacecraft)"},
        "@type": "http://ontology.projectchronos.eu/sensors/CCD",
        "spacecraft:isComponentOf": {"@id": "http://api.pramantha.net/data/sensors/CHIVA-detector"},
        "sensor:detects": "http://ontology.projectchronos.eu/sensors/Visible",
        "sensor:emits": "",
        "sensor:hasFieldOfResearch": "http://ontology.projectchronos.eu/astronomy/PlanetaryScience",
        "sensor:hasOutput": "http://ontology.projectchronos.eu/sensors/Voltage",
        "sensor:hasWorkingPrinciple": "http://ontology.projectchronos.eu/sensors/PhotoElectronEmission",
        "sensor:isTraversedBy": "http://ontology.projectchronos.eu/sensors/Photon",
        "sensor:measures": "http://ontology.projectchronos.eu/sensors/Intensity"
    },
    {
        "@id": "http://api.pramantha.net/data/sensors/CHIVA-M1",
        "manufactoring": "http://api.pramantha.net/data/dbpediadocs/European_Space_Agency",
        "name": "CHIVA-M1",
        "fullName": "çiva-M1",
        "chronos:relMission": {"@id": "http://api.pramantha.net/data/mission/Rosetta_(spacecraft)"},
        "@type": "http://ontology.projectchronos.eu/sensors/Microscope",
        "spacecraft:isComponentOf": {"@id": "http://api.pramantha.net/data/sensors/CHIVA-detector"},
        "sensor:detects": "http://ontology.projectchronos.eu/sensors/Visible",
        "sensor:emits": "",
        "sensor:hasFieldOfResearch": "http://ontology.projectchronos.eu/astronomy/PlanetaryScience",
        "sensor:hasOutput": "",
        "sensor:hasWorkingPrinciple": "http://ontology.projectchronos.eu/sensors/RayOptics",
        "sensor:isTraversedBy": "http://ontology.projectchronos.eu/sensors/Photon",
        "sensor:measures": ""
    },
    {
        "@id": "http://api.pramantha.net/data/sensors/CHIVA-M2",
        "subsystems:manufacturer": "http://api.pramantha.net/data/dbpediadocs/European_Space_Agency",
        "name": "CHIVA-M2",
        "fullName": "çiva-M2",
        "chronos:relMission": {"@id": "http://api.pramantha.net/data/mission/Rosetta_(spacecraft)"},
        "@type": "http://ontology.projectchronos.eu/sensors/Spectrometer",
        "spacecraft:isComponentOf": {"@id": "http://api.pramantha.net/data/sensors/CHIVA-detector"},
        "sensor:detects": "http://ontology.projectchronos.eu/sensors/Infrared",
        "sensor:emits": "",
        "sensor:hasFieldOfResearch": "http://ontology.projectchronos.eu/astronomy/PlanetaryScience",
        "sensor:hasOutput": "http://ontology.projectchronos.eu/sensors/Voltage",
        "sensor:hasWorkingPrinciple": [
            "http://ontology.projectchronos.eu/sensors/RayOptics",
            "http://ontology.projectchronos.eu/sensors/PhotonElectronEmission"
        ],
        "sensor:isTraversedBy": "http://ontology.projectchronos.eu/sensors/Photon",
        "sensor:measures": ""
    },
    {
        "@id": "http://api.pramantha.net/data/sensors/LORRI",
        "subsystems:manufacturer": "http://api.pramantha.net/data/dbpediadocs/NASA",
        "name": "LORRI",
        "fullName": "LORRI",
        "chronos:relMission": {"@id": "http://api.pramantha.net/data/mission/New_Horizons"},
        "@type": "http://ontology.projectchronos.eu/sensors/CCD",
        "sensor:detects": "http://ontology.projectchronos.eu/sensors/Visible",
        "sensor:emits": "",
        "sensor:hasFieldOfResearch": "http://ontology.projectchronos.eu/astronomy/PlanetaryScience",
        "sensor:hasOutput": "http://ontology.projectchronos.eu/sensors/Voltage",
        "sensor:hasWorkingPrinciple": "http://ontology.projectchronos.eu/sensors/PhotonElectronEmission",
        "sensor:isTraversedBy": "http://ontology.projectchronos.eu/sensors/Photon",
        "sensor:measures": "http://ontology.projectchronos.eu/sensors/Intensity"
    },
    {
        "@id": "http://api.pramantha.net/data/sensors/REX",
        "subsystems:manufacturer": "http://api.pramantha.net/data/dbpediadocs/NASA",
        "name": "REX",
        "fullName": "REX",
        "chronos:relMission": {"@id": "http://api.pramantha.net/data/mission/New_Horizons"},
        "@type": "http://ontology.projectchronos.eu/sensors/Radiometer",
        "subComponentOf": "",
        "sensor:detects": "http://ontology.projectchronos.eu/sensors/Radio",
        "sensor:emits": "",
        "sensor:hasFieldOfResearch": "http://ontology.projectchronos.eu/astronomy/AtmosphericScience",
        "sensor:hasOutput": "http://ontology.projectchronos.eu/sensors/Voltage",
        "sensor:hasWorkingPrinciple": "http://ontology.projectchronos.eu/sensors/AntennaTheory",
        "sensor:isTraversedBy": "http://ontology.projectchronos.eu/sensors/Photon",
        "sensor:measures": "http://ontology.projectchronos.eu/sensors/RadiantFlux"
    },
    {
        "@id": "http://api.pramantha.net/data/sensors/SMAP-radiometer",
        "chronos:relMission": {"@id": "http://api.pramantha.net/data/mission/Soil_Moisture_Active_Passive"},
        "manufactoring": "http://api.pramantha.net/data/dbpediadocs/NASA",
        "name": "SMAP-radiometer",
        "fullName": "SMAP-radiometer",
        "@type": "http://ontology.projectchronos.eu/sensors/Radiometer",
        "subComponentOf": "",
        "sensor:detects": "http://ontology.projectchronos.eu/sensors/Radio L-Band",
        "rdfs:comment": "Radiometer Frequency: 1.41 GHz",
        "sensor:emits": "",
        "sensor:hasFieldOfResearch": "http://ontology.projectchronos.eu/astronomy/EarthObservation",
        "sensor:hasOutput": "http://ontology.projectchronos.eu/sensors/Voltage",
        "sensor:hasWorkingPrinciple": "http://ontology.projectchronos.eu/sensors/AntennaTheory",
        "sensor:isTraversedBy": "http://ontology.projectchronos.eu/sensors/Photon",
        "sensor:measures": [
            "http://ontology.projectchronos.eu/sensors/RadiantFlux",
            "http://ontology.projectchronos.eu/sensors/Power",
            "http://ontology.projectchronos.eu/sensors/Temperature",
            "Brightness"
        ]
    },
    {
        "@id": "http://api.pramantha.net/data/sensors/SMAP-radar",
        "chronos:relMission": {"@id": "http://api.pramantha.net/data/mission/Soil_Moisture_Active_Passive"},
        "name": "SMAP-radar",
        "fullName": "SMAP-radar",
        "@type": "http://ontology.projectchronos.eu/sensors/Radar",
        "subComponentOf": "",
        "sensor:detects": [
            "http://ontology.projectchronos.eu/sensors/EMSpectrum",
            "Radio L-Band"
        ],
        "sensor:emits": "http://ontology.projectchronos.eu/sensors/RadioCentrimetric",
        "rdfs:comment": "emits: 1.26 GHz, Non imaging (unfocused) synthetic aperture\n measures:surface backscatter crosssection for HH and VV polarizations\n research: Soil moisture, freezed or thawed soils",
        "sensor:hasFieldOfResearch": "http://ontology.projectchronos.eu/astronomy/EarthObservation",
        "sensor:hasOutput": "http://ontology.projectchronos.eu/sensors/Voltage",
        "sensor:hasWorkingPrinciple": "http://ontology.projectchronos.eu/sensors/AntennaTheory",
        "sensor:isTraversedBy": "",
        "sensor:measures": "http://ontology.projectchronos.eu/sensors/RadiantFlux"
    },
    {
        "@id": "http://api.pramantha.net/data/sensors/MMS-detector",
        "chronos:relMission": {"@id": "http://api.pramantha.net/data/mission/Magnetospheric_Multiscale_Mission"},
        "subsystems:manufacturer": "http://api.pramantha.net/data/dbpediadocs/NASA",
        "name": "MMS-detector",
        "spacecraft:embedSensor": [
            "http://api.pramantha.net/data/sensors/FPI",
            "http://api.pramantha.net/data/sensors/MMS-DIS",
            "http://api.pramantha.net/data/sensors/MMS-DES",
            "http://api.pramantha.net/data/sensors/HPCA",
            "http://api.pramantha.net/data/sensors/FEEPS",
            "http://api.pramantha.net/data/sensors/AFG",
            "http://api.pramantha.net/data/sensors/DFG"
        ],
        "@type": "http://ontology.projectchronos.eu/subsystems/Spacecraft_Detector",
        "rdfs:comment": "this is a generic detector for a mission, look for more specific components that are part of this payload (spacecraft:isComponentOf)"
    },
    {
        "@id": "http://api.pramantha.net/data/sensors/FPI",
        "chronos:relMission": {"@id": "http://api.pramantha.net/data/mission/Magnetospheric_Multiscale_Mission"},
        "name": "FPI",
        "fullName": "Fast Plasma Instrument",
        "@type": "http://ontology.projectchronos.eu/sensors/MassSpectrometer",
        "spacecraft:isComponentOf": {"@id": "http://api.pramantha.net/data/sensors/MMS-detector"},
        "spacecraft:hasComponent": [
            "http://api.pramantha.net/data/sensors/DES",
            "http://api.pramantha.net/data/sensors/DIS"
        ],
        "sensor:detects": [
            "http://ontology.projectchronos.eu/sensors/Ion",
            "http://ontology.projectchronos.eu/sensors/Electron"
        ],
        "sensor:emits": "",
        "sensor:hasFieldOfResearch": [
            "http://ontology.projectchronos.eu/astronomy/SpacePhysics",
            "http://ontology.projectchronos.eu/astronomy/SpaceWeather"
        ],
        "sensor:hasOutput": "http://ontology.projectchronos.eu/sensors/Voltage",
        "sensor:hasWorkingPrinciple": [
            "http://ontology.projectchronos.eu/sensors/IonOptics",
            "http://ontology.projectchronos.eu/sensors/ElectronEmission"
        ],
        "sensor:isTraversedBy": [
            "http://ontology.projectchronos.eu/sensors/Ion",
            "http://ontology.projectchronos.eu/sensors/Electron"
        ],
        "sensor:measures": [
            "http://ontology.projectchronos.eu/sensors/ParticleFlux",
            "http://ontology.projectchronos.eu/sensors/Ion",
            "http://ontology.projectchronos.eu/sensors/Electron"
        ],
        "rdfs:comment": "3D ion and electron flux distributions over the energy range ~10 eV to 30 keVwith an energy resolution of 20%. Electrons will be measured with a time resolution of 30 ms, ions with a time resolution 150 ms."
    },
    {
        "@id": "http://api.pramantha.net/data/sensors/MMS-DES",
        "chronos:relMission": {"@id": "http://api.pramantha.net/data/mission/Magnetospheric_Multiscale_Mission"},
        "name": "MMS-DES",
        "fullName": "Dual Electron Spectrometer (DES)",
        "@type": "http://ontology.projectchronos.eu/sensors/MassSpectrometer",
        "spacecraft:isComponentOf": {"@id": "http://api.pramantha.net/data/sensors/FPI"},
        "spacecraft:hasComponent": "http://ontology.projectchronos.eu/sensors/MicroChannelPlate",
        "sensor:detects": "http://ontology.projectchronos.eu/sensors/Electron",
        "sensor:emits": "",
        "sensor:hasFieldOfResearch": "",
        "sensor:hasOutput": "http://ontology.projectchronos.eu/sensors/Voltage",
        "sensor:hasWorkingPrinciple": "http://ontology.projectchronos.eu/sensors/ElectronEmission",
        "sensor:isTraversedBy": "http://ontology.projectchronos.eu/sensors/Electron",
        "sensor:measures": [
            "http://ontology.projectchronos.eu/sensors/ParticleFlux",
            "http://ontology.projectchronos.eu/sensors/Electron"
        ]
    },
    {
        "@id": "http://api.pramantha.net/data/sensors/MMS-DIS",
        "chronos:relMission": {"@id": "http://api.pramantha.net/data/mission/Magnetospheric_Multiscale_Mission"},
        "name": "MMS-DIS",
        "fullName": "Dual Ion Spectrometer (DIS)",
        "@type": "http://ontology.projectchronos.eu/sensors/MassSpectrometer",
        "spacecraft:isComponentOf": {"@id": "http://api.pramantha.net/data/sensors/FPI"},
        "spacecraft:hasComponent": "http://ontology.projectchronos.eu/sensors/MicroChannelPlate",
        "sensor:detects": "http://ontology.projectchronos.eu/sensors/Ion",
        "sensor:emits": "",
        "sensor:hasFieldOfResearch": "",
        "sensor:hasOutput": "http://ontology.projectchronos.eu/sensors/Voltage",
        "sensor:hasWorkingPrinciple": "http://ontology.projectchronos.eu/sensors/ElectronEmission",
        "sensor:isTraversedBy": "http://ontology.projectchronos.eu/sensors/Ion",
        "sensor:measures": [
            "http://ontology.projectchronos.eu/sensors/ParticleFlux",
            "http://ontology.projectchronos.eu/sensors/Ion"
        ]
    },
    {
        "@id": "http://api.pramantha.net/data/sensors/HPCA",
        "chronos:relMission": {"@id": "http://api.pramantha.net/data/mission/Magnetospheric_Multiscale_Mission"},
        "name": "HPCA",
        "fullName": "Hot Plasma Composition Analyzer",
        "@type": "http://ontology.projectchronos.eu/sensors/TimeOfFlightMassSpectrometer",
        "spacecraft:isComponentOf": {"@id": "http://api.pramantha.net/data/sensors/MMS-detector"},
        "spacecraft:hasComponent": "http://ontology.projectchronos.eu/sensors/MicroChannelPlate",
        "sensor:detects": "http://ontology.projectchronos.eu/sensors/Ion",
        "sensor:emits": "http://ontology.projectchronos.eu/sensors/Radio",
        "rdfs:comment": "emits: RF (radio frequency) Only internal for protection from protons\n measures: Measure minor ions such as oxygen and helium in regions of high flux. Energy range = ~10 eV to 30 keV; energy resolution = 20%; time resoluton = 15 s",
        "sensor:hasFieldOfResearch": [
            "http://ontology.projectchronos.eu/astronomy/SpacePhysics",
            "http://ontology.projectchronos.eu/astronomy/SpaceWeather"
        ],
        "sensor:hasOutput": "http://ontology.projectchronos.eu/sensors/Voltage",
        "sensor:hasWorkingPrinciple": [
            "http://ontology.projectchronos.eu/sensors/IonOptics",
            "http://ontology.projectchronos.eu/sensors/ElectronsEmission"
        ],
        "sensor:isTraversedBy": "http://ontology.projectchronos.eu/sensors/Ion",
        "sensor:measures": "http://ontology.projectchronos.eu/sensors/TimeOfFlight"
    },
    {
        "@id": "http://api.pramantha.net/data/sensors/FEEPS",
        "chronos:relMission": {"@id": "http://api.pramantha.net/data/mission/Magnetospheric_Multiscale_Mission"},
        "name": "FEEPS",
        "fullName": "Fly's Eye Energetic Particle Sensor",
        "@type": "http://ontology.projectchronos.eu/sensors/SolidStateDetector",
        "spacecraft:isComponentOf": {"@id": "http://api.pramantha.net/data/sensors/MMS-detector"},
        "sensor:detects": [
            "http://ontology.projectchronos.eu/sensors/Ion",
            "http://ontology.projectchronos.eu/sensors/Electron"
        ],
        "sensor:emits": "",
        "sensor:hasFieldOfResearch": [
            "http://ontology.projectchronos.eu/astronomy/SpacePhysics",
            "http://ontology.projectchronos.eu/sensors/:SpaceWeather"
        ],
        "sensor:hasOutput": "http://ontology.projectchronos.eu/sensors/Voltage",
        "sensor:hasWorkingPrinciple": "http://ontology.projectchronos.eu/sensors/ElectronsEmission",
        "sensor:isTraversedBy": [
            "http://ontology.projectchronos.eu/sensors/Ion",
            "http://ontology.projectchronos.eu/sensors/Electron"
        ],
        "sensor:measures": "http://ontology.projectchronos.eu/sensors/Energy",
        "rdfs:comment": "measures: 3D energetic ion and electron flux distributions over the energy ranges ~25 keV to 500 keV (electrons) and ~45 keV to 500 keV (ions). Time resolution = 10 s."
    },
    {
        "@id": "http://api.pramantha.net/data/sensors/AFG",
        "chronos:relMission": {"@id": "http://api.pramantha.net/data/mission/Magnetospheric_Multiscale_Mission"},
        "name": "AFG",
        "fullName": "Analog Fluxgate Magnetometer",
        "@type": "http://ontology.projectchronos.eu/sensors/Magnetometer",
        "spacecraft:isComponentOf": {"@id": "http://api.pramantha.net/data/sensors/MMS-detector"},
        "sensor:detects": [
            "http://ontology.projectchronos.eu/sensors/MagneticField",
            "http://ontology.projectchronos.eu/sensors/ElectricCurrent"
        ],
        "sensor:emits": "",
        "sensor:hasFieldOfResearch": [
            "http://ontology.projectchronos.eu/astronomy/SpacePhysics",
            "http://ontology.projectchronos.eu/astronomy/SpaceWeather"
        ],
        "sensor:hasOutput": "http://ontology.projectchronos.eu/sensors/ElectricCurrent",
        "sensor:hasWorkingPrinciple": "http://ontology.projectchronos.eu/sensors/Ferromagnetism",
        "sensor:isTraversedBy": "http://ontology.projectchronos.eu/sensors/Photon",
        "sensor:measures": "http://ontology.projectchronos.eu/sensors/MagneticFieldStrength",
        "rdfs:comment": "measures: Measurements of the magnetic field and current in space. Analogic measurements."
    },
    {
        "@id": "http://api.pramantha.net/data/sensors/DFG",
        "chronos:relMission": {"@id": "http://api.pramantha.net/data/mission/Magnetospheric_Multiscale_Mission"},
        "name": "DFG",
        "fullName": "Digital Fluxgate Magnetometer",
        "@type": "http://ontology.projectchronos.eu/sensors/Magnetometer",
        "spacecraft:isComponentOf": {"@id": "http://api.pramantha.net/data/sensors/MMS-detector"},
        "sensor:detects": [
            "http://ontology.projectchronos.eu/sensors/MagneticField",
            "http://ontology.projectchronos.eu/sensors/ElectricCurrent"
        ],
        "sensor:emits": "",
        "sensor:hasFieldOfResearch": [
            "http://ontology.projectchronos.eu/sensors/SpacePhysics",
            "http://ontology.projectchronos.eu/sensors/SpaceWeather"
        ],
        "sensor:hasOutput": "http://ontology.projectchronos.eu/sensors/ElectricCurrent",
        "sensor:hasWorkingPrinciple": "http://ontology.projectchronos.eu/sensors/Ferromagnetism",
        "sensor:isTraversedBy": "http://ontology.projectchronos.eu/sensors/Photon",
        "sensor:measures": "http://ontology.projectchronos.eu/sensors/MagneticFieldStrength",
        "rdfs:comment": "measures:Measurements of the magnetic field and current in space. Digital measurements."
    },
    {
        "@id": "http://api.pramantha.net/data/sensors/Dawn-FC",
        "name": "FC",
        "fullName": "Framing Camera",
        "chronos:relMission": {"@id": "http://api.pramantha.net/data/mission/Dawn_(spacecraft)"},
        "@type": "http://ontology.projectchronos.eu/sensors/CCD",
        "sensor:detects": [
            "http://ontology.projectchronos.eu/sensors/NearInfrared",
            "http://ontology.projectchronos.eu/sensors/Visible"
        ],
        "sensor:emits": "",
        "sensor:hasFieldOfResearch": "http://ontology.projectchronos.eu/astronomy/PlanetaryScience",
        "sensor:hasOutput": "http://ontology.projectchronos.eu/sensors/Voltage",
        "sensor:hasWorkingPrinciple": "http://ontology.projectchronos.eu/sensors/PhotoElectronEmission",
        "sensor:isTraversedBy": "http://ontology.projectchronos.eu/sensors/Photon",
        "sensor:measures": "http://ontology.projectchronos.eu/sensors/Intensity"
    }
]
