"""
This module contains the raw XML string of NASA-JPL's SKOS taxonomy
-------------------------------------------------------------------
Relevant nodes are <skos:Concept>
"""

jpl_skos_xml = """

<?xml version="1.0" encoding="ISO-8859-1"?>
<rdf:RDF
    xmlns:rdf='http://www.w3.org/1999/02/22-rdf-syntax-ns#'
    xmlns:rdfs='http://www.w3.org/2000/01/rdf-schema#'
    xmlns:skos='http://www.w3.org/2004/02/skos/core#'
    xmlns:nt2='http://nasataxonomy.jpl.nasa.gov/cvFields#'
    xmlns:dcterms='http://purl.org/dc/terms/'
    xmlns:dc='http://purl.org/dc/elements/1.1/'>
 <skos:Concept rdf:about='subj:45'>
  <skos:prefLabel>Environment Pollution</skos:prefLabel>
  <skos:scopeNote>Includes atmospheric, water, soil, noise, and thermal
    pollution.
  </skos:scopeNote>
  <skos:altLabel>aerosols (pollution aspects)</skos:altLabel>
  <skos:altLabel>air pollution</skos:altLabel>
  <skos:altLabel>atmospheric analysis (pollution)</skos:altLabel>
  <skos:altLabel>atmospheric pollution</skos:altLabel>
  <skos:altLabel>atmospheric sampling (pollution)</skos:altLabel>
  <skos:altLabel>biosphere (pollution aspects)</skos:altLabel>
  <skos:altLabel>commercial pollution</skos:altLabel>
  <skos:altLabel>contamination control</skos:altLabel>
  <skos:altLabel>environmental clean up</skos:altLabel>
  <skos:altLabel>environmental engineering</skos:altLabel>
  <skos:altLabel>environmental modifications</skos:altLabel>
  <skos:altLabel>environmental monitoring</skos:altLabel>
  <skos:altLabel>environmental pollution</skos:altLabel>
  <skos:altLabel>environmental surveys</skos:altLabel>
  <skos:altLabel>exhaust emissions (pollution)</skos:altLabel>
  <skos:altLabel>greenhouse effect (pollution aspects)</skos:altLabel>
  <skos:altLabel>indoor air pollution</skos:altLabel>
  <skos:altLabel>industrial pollution</skos:altLabel>
  <skos:altLabel>noise abatement</skos:altLabel>
  <skos:altLabel>noise pollution</skos:altLabel>
  <skos:altLabel>ozone depletion (pollution aspects)</skos:altLabel>
  <skos:altLabel>pollution control</skos:altLabel>
  <skos:altLabel>pollution monitoring</skos:altLabel>
  <skos:altLabel>radioactive contamination</skos:altLabel>
  <skos:altLabel>residential pollution</skos:altLabel>
  <skos:altLabel>soil pollution</skos:altLabel>
  <skos:altLabel>sonic boom (noise pollution)</skos:altLabel>
  <skos:altLabel>stratospheric pollution</skos:altLabel>
  <skos:altLabel>thermal pollution</skos:altLabel>
  <skos:altLabel>transportation pollution</skos:altLabel>
  <skos:altLabel>waste treatment (pollution control)</skos:altLabel>
  <skos:altLabel>water pollution</skos:altLabel>
  <skos:altLabel>water treatment (pollution control)</skos:altLabel>
  <skos:broader rdf:resource='subj:1874'/>
  <nt2:status>Approved</nt2:status>
  <nt2:type>Descriptor</nt2:type>
  <nt2:inputdate>2007-01-11</nt2:inputdate>
  <dcterms:dateAccepted>2006-12-01</dcterms:dateAccepted>
  <dcterms:modified>2007-01-11</dcterms:modified>
  <nt2:notValidDate></nt2:notValidDate>
  <nt2:code>45</nt2:code>
 </skos:Concept>
 <skos:Concept rdf:about='subj:18'>
  <skos:prefLabel>Spacecraft Design, Testing and Performance</skos:prefLabel>
  <skos:scopeNote>Includes satellites; space platforms; space stations;
    spacecraft systems and components such as thermal and
    environmental controls; and spacecraft control and
    stability characteristics. For life support systems see 54
    Man/System Technology and Life Support. For related
    information see also 05 Aircraft Design, Testing and
    Performance; 39 Structural Mechanics; and 16 Space
    Transportation and Safety.
  </skos:scopeNote>
  <skos:altLabel>active communication satellite</skos:altLabel>
  <skos:altLabel>active satellite stabilization</skos:altLabel>
  <skos:altLabel>artificial satellites</skos:altLabel>
  <skos:altLabel>astronomical observatory satellites</skos:altLabel>
  <skos:altLabel>attitude control (spacecraft)</skos:altLabel>
  <skos:altLabel>automatic pilots (spacecraft)</skos:altLabel>
  <skos:altLabel>cabin pressurization (spacecraft)</skos:altLabel>
  <skos:altLabel>capture devices (spacecraft)</skos:altLabel>
  <skos:altLabel>communication satellites</skos:altLabel>
  <skos:altLabel>control effectiveness (spacecraft)</skos:altLabel>
  <skos:altLabel>control systems design (spacecraft)</skos:altLabel>
  <skos:altLabel>depressurization systems (spacecraft)</skos:altLabel>
  <skos:altLabel>docking (spacecraft)</skos:altLabel>
  <skos:altLabel>dynamic stability (spacecraft)</skos:altLabel>
  <skos:altLabel>expandable structures (spacecraft)</skos:altLabel>
  <skos:altLabel>fins (spacecraft)</skos:altLabel>
  <skos:altLabel>flight control (spacecraft)</skos:altLabel>
  <skos:altLabel>flight dynamics (spacecraft)</skos:altLabel>
  <skos:altLabel>flight path control (spacecraft)</skos:altLabel>
  <skos:altLabel>flutter (spacecraft)</skos:altLabel>
  <skos:altLabel>flying qualities (spacecraft)</skos:altLabel>
  <skos:altLabel>formation flying (satellites)</skos:altLabel>
  <skos:altLabel>free flyers (spacecraft)</skos:altLabel>
  <skos:altLabel>geophysical satellites</skos:altLabel>
  <skos:altLabel>handling qualities (spacecraft)</skos:altLabel>
  <skos:altLabel>hydraulic systems (spacecraft)</skos:altLabel>
  <skos:altLabel>inflatable structures (spacecraft)</skos:altLabel>
  <skos:altLabel>inlets (spacecraft)</skos:altLabel>
  <skos:altLabel>International Space Station (design)</skos:altLabel>
  <skos:altLabel>landing gear (spacecraft)</skos:altLabel>
  <skos:altLabel>LANDSAT (configurations)</skos:altLabel>
  <skos:altLabel>lateral control (spacecraft)</skos:altLabel>
  <skos:altLabel>lateral stability (spacecraft)</skos:altLabel>
  <skos:altLabel>longitudinal control (spacecraft)</skos:altLabel>
  <skos:altLabel>longitudinal stability (spacecraft)</skos:altLabel>
  <skos:altLabel>lunar landers</skos:altLabel>
  <skos:altLabel>lunar orbiters</skos:altLabel>
  <skos:altLabel>maneuvering (spacecraft)</skos:altLabel>
  <skos:altLabel>manned orbital laboratories</skos:altLabel>
  <skos:altLabel>manned spacecraft</skos:altLabel>
  <skos:altLabel>meteorite protection</skos:altLabel>
  <skos:altLabel>meteorological satellites</skos:altLabel>
  <skos:altLabel>models (spacecraft)</skos:altLabel>
  <skos:altLabel>navigation satellites</skos:altLabel>
  <skos:altLabel>observation satellites</skos:altLabel>
  <skos:altLabel>passive communication satellites</skos:altLabel>
  <skos:altLabel>passive satellite stabilization</skos:altLabel>
  <skos:altLabel>piloting (spacecraft)</skos:altLabel>
  <skos:altLabel>pitch control (spacecraft)</skos:altLabel>
  <skos:altLabel>pitch stability (spacecraft)</skos:altLabel>
  <skos:altLabel>planetary landers</skos:altLabel>
  <skos:altLabel>planetary orbiters</skos:altLabel>
  <skos:altLabel>planetary probes</skos:altLabel>
  <skos:altLabel>plasma wakes (spacecraft)</skos:altLabel>
  <skos:altLabel>pneumatic systems (spacecraft)</skos:altLabel>
  <skos:altLabel>pressurization systems (spacecraft)</skos:altLabel>
  <skos:altLabel>pressurized cabins (spacecraft)</skos:altLabel>
  <skos:altLabel>radiation effects on spacecraft and components</skos:altLabel>
  <skos:altLabel>reaction control systems (spacecraft)</skos:altLabel>
  <skos:altLabel>roll control (spacecraft)</skos:altLabel>
  <skos:altLabel>roll stability (spacecraft)</skos:altLabel>
  <skos:altLabel>satellite constellations</skos:altLabel>
  <skos:altLabel>satellite stabilization</skos:altLabel>
  <skos:altLabel>satellites for air, land, or sea navigation</skos:altLabel>
  <skos:altLabel>satellites for air, land, or sea traffic control</skos:altLabel>
  <skos:altLabel>scientific satellites</skos:altLabel>
  <skos:altLabel>search and rescue satellites</skos:altLabel>
  <skos:altLabel>SEASAT (configurations)</skos:altLabel>
  <skos:altLabel>separation and staging techniques (spacecraft)</skos:altLabel>
  <skos:altLabel>space flight dynamics (performance and testing)</skos:altLabel>
  <skos:altLabel>space laboratories</skos:altLabel>
  <skos:altLabel>space platforms</skos:altLabel>
  <skos:altLabel>space probes</skos:altLabel>
  <skos:altLabel>space station control</skos:altLabel>
  <skos:altLabel>space station design</skos:altLabel>
  <skos:altLabel>space stations</skos:altLabel>
  <skos:altLabel>spacecraft antennas</skos:altLabel>
  <skos:altLabel>spacecraft cabins</skos:altLabel>
  <skos:altLabel>spacecraft charging</skos:altLabel>
  <skos:altLabel>spacecraft components</skos:altLabel>
  <skos:altLabel>spacecraft control (design and performance)</skos:altLabel>
  <skos:altLabel>spacecraft design</skos:altLabel>
  <skos:altLabel>spacecraft environmental control</skos:altLabel>
  <skos:altLabel>spacecraft external contamination</skos:altLabel>
  <skos:altLabel>spacecraft flight simulation</skos:altLabel>
  <skos:altLabel>spacecraft flight tests</skos:altLabel>
  <skos:altLabel>spacecraft performance</skos:altLabel>
  <skos:altLabel>spacecraft simulation</skos:altLabel>
  <skos:altLabel>spacecraft structures</skos:altLabel>
  <skos:altLabel>spacecraft systems</skos:altLabel>
  <skos:altLabel>spacecraft testing</skos:altLabel>
  <skos:altLabel>spacecraft thermal control</skos:altLabel>
  <skos:altLabel>spacelab (design and testing)</skos:altLabel>
  <skos:altLabel>stability (spacecraft)</skos:altLabel>
  <skos:altLabel>stability augmentation (spacecraft)</skos:altLabel>
  <skos:altLabel>stability derivatives (spacecraft)</skos:altLabel>
  <skos:altLabel>stabilization surfaces (spacecraft)</skos:altLabel>
  <skos:altLabel>static stability (spacecraft)</skos:altLabel>
  <skos:altLabel>synchronous satellites</skos:altLabel>
  <skos:altLabel>tethered satellite systems</skos:altLabel>
  <skos:altLabel>thermal protection systems (spacecraft)</skos:altLabel>
  <skos:altLabel>tracking and data relay satellites</skos:altLabel>
  <skos:altLabel>unfoldable structures (spacecraft)</skos:altLabel>
  <skos:altLabel>vibration (spacecraft)</skos:altLabel>
  <skos:altLabel>Viking space probe</skos:altLabel>
  <skos:altLabel>weather satellites</skos:altLabel>
  <skos:altLabel>wind tunnel tests (spacecraft)</skos:altLabel>
  <skos:altLabel>yaw control (spacecraft)</skos:altLabel>
  <skos:altLabel>yaw stability (spacecraft)</skos:altLabel>
  <skos:broader rdf:resource='subj:578'/>
  <nt2:status>Approved</nt2:status>
  <nt2:type>Descriptor</nt2:type>
  <nt2:inputdate>2007-01-11</nt2:inputdate>
  <dcterms:dateAccepted>2006-12-01</dcterms:dateAccepted>
  <dcterms:modified>2007-01-11</dcterms:modified>
  <nt2:notValidDate></nt2:notValidDate>
  <nt2:code>18</nt2:code>
 </skos:Concept>
 <skos:Concept rdf:about='subj:70'>
  <skos:prefLabel>Physics (General)</skos:prefLabel>
  <skos:scopeNote>Includes general research topics related to mechanics,
    kinetics, magnetism, and electrodynamics. For specific
    areas of physics see categories 71 through 77. For related
    instrumentation see 35 Instrumentation and Photography; for
    geophysics, astrophysics, or solar physics see 46
    Geophysics; 90 Astrophysics;or 92 Solar Physics.
  </skos:scopeNote>
  <skos:altLabel>antigravity</skos:altLabel>
  <skos:altLabel>Brownian movement</skos:altLabel>
  <skos:altLabel>chaos</skos:altLabel>
  <skos:altLabel>dynamics (physics)</skos:altLabel>
  <skos:altLabel>electromagnetic radiation (theory)</skos:altLabel>
  <skos:altLabel>electromagnetism</skos:altLabel>
  <skos:altLabel>electrostatics</skos:altLabel>
  <skos:altLabel>ferromagnetism</skos:altLabel>
  <skos:altLabel>field theory (physics)</skos:altLabel>
  <skos:altLabel>kinetics</skos:altLabel>
  <skos:altLabel>magnetism</skos:altLabel>
  <skos:altLabel>many-body problems</skos:altLabel>
  <skos:altLabel>mechanics (theory and analysis)</skos:altLabel>
  <skos:altLabel>solitary waves</skos:altLabel>
  <skos:broader rdf:resource='subj:2528'/>
  <nt2:status>Approved</nt2:status>
  <nt2:type>Descriptor</nt2:type>
  <nt2:inputdate>2007-01-11</nt2:inputdate>
  <dcterms:dateAccepted>2006-12-01</dcterms:dateAccepted>
  <dcterms:modified>2007-01-11</dcterms:modified>
  <nt2:notValidDate></nt2:notValidDate>
  <nt2:code>70</nt2:code>
 </skos:Concept>
 <skos:Concept rdf:about='subj:44'>
  <skos:prefLabel>Energy Production and Conversion</skos:prefLabel>
  <skos:scopeNote>Includes specific energy conversion systems, e.g., fuel
    cells; and solar, geothermal, windpower, and waterwave
    conversion systems; energy storage; and traditional power
    generators. For technologies related to nuclear energy
    production see 73 Nuclear Physics. For related information
    see also 07 Aircraft Propulsion and Power; 20 Spacecraft
    Propulsion and Power; and 28 Propellants and Fuels.
  </skos:scopeNote>
  <skos:altLabel>alternative energy sources</skos:altLabel>
  <skos:altLabel>Brayton cycle turbines (applications)</skos:altLabel>
  <skos:altLabel>chemical energy conversion devices</skos:altLabel>
  <skos:altLabel>electric batteries (applications)</skos:altLabel>
  <skos:altLabel>electric energy conversion devices</skos:altLabel>
  <skos:altLabel>energy management technology</skos:altLabel>
  <skos:altLabel>energy production</skos:altLabel>
  <skos:altLabel>energy storage</skos:altLabel>
  <skos:altLabel>fuel cells</skos:altLabel>
  <skos:altLabel>generators (applications)</skos:altLabel>
  <skos:altLabel>geophysical energy conversion devices</skos:altLabel>
  <skos:altLabel>hybrid energy conversion devices</skos:altLabel>
  <skos:altLabel>magnetohydrodynamic (MHD) energy conversion device</skos:altLabel>
  <skos:altLabel>microwave energy conversion devices</skos:altLabel>
  <skos:altLabel>microwave energy transmission</skos:altLabel>
  <skos:altLabel>photovoltaic energy conversion devices</skos:altLabel>
  <skos:altLabel>silicon cells (applications)</skos:altLabel>
  <skos:altLabel>solar cells (energy conversion)</skos:altLabel>
  <skos:altLabel>solar generators</skos:altLabel>
  <skos:altLabel>solar heating (space applications)</skos:altLabel>
  <skos:altLabel>solar power (space applications)</skos:altLabel>
  <skos:altLabel>thermionic energy conversion devices</skos:altLabel>
  <skos:altLabel>thermoelectricity</skos:altLabel>
  <skos:altLabel>windpower</skos:altLabel>
  <skos:broader rdf:resource='subj:1874'/>
  <nt2:status>Approved</nt2:status>
  <nt2:type>Descriptor</nt2:type>
  <nt2:inputdate>2007-01-11</nt2:inputdate>
  <dcterms:dateAccepted>2006-12-01</dcterms:dateAccepted>
  <dcterms:modified>2007-01-11</dcterms:modified>
  <nt2:notValidDate></nt2:notValidDate>
  <nt2:code>44</nt2:code>
 </skos:Concept>
 <skos:Concept rdf:about='subj:89'>
  <skos:prefLabel>Astronomy</skos:prefLabel>
  <skos:scopeNote>Includes observations of celestial bodies; astronomical
    instruments and techniques; radio, gamma-ray, x-ray,
    ultraviolet, and infrared astronomy; and astrometry.
  </skos:scopeNote>
  <skos:altLabel>asteroid belt</skos:altLabel>
  <skos:altLabel>asteroids (observation)</skos:altLabel>
  <skos:altLabel>astrometry</skos:altLabel>
  <skos:altLabel>astronomical instruments</skos:altLabel>
  <skos:altLabel>binaries (observation)</skos:altLabel>
  <skos:altLabel>black holes (observation)</skos:altLabel>
  <skos:altLabel>celestial bodies (observation)</skos:altLabel>
  <skos:altLabel>celestial motion (observation)</skos:altLabel>
  <skos:altLabel>comets (observation)</skos:altLabel>
  <skos:altLabel>discovery of celestial bodies</skos:altLabel>
  <skos:altLabel>ephemerides of celestial bodies</skos:altLabel>
  <skos:altLabel>extrasolar planets (observation)</skos:altLabel>
  <skos:altLabel>galaxies (observation)</skos:altLabel>
  <skos:altLabel>gamma-ray astronomy</skos:altLabel>
  <skos:altLabel>Hubble telescope</skos:altLabel>
  <skos:altLabel>identification of celestial bodies</skos:altLabel>
  <skos:altLabel>infrared astronomy</skos:altLabel>
  <skos:altLabel>infrared telescopes</skos:altLabel>
  <skos:altLabel>JWST (James Webb Space Telescope)</skos:altLabel>
  <skos:altLabel>Large Space Telescope</skos:altLabel>
  <skos:altLabel>meteoroids (observation)</skos:altLabel>
  <skos:altLabel>meteors (observation)</skos:altLabel>
  <skos:altLabel>moons (observation)</skos:altLabel>
  <skos:altLabel>natural satellites (observation)</skos:altLabel>
  <skos:altLabel>nebulae (observation)</skos:altLabel>
  <skos:altLabel>novae (observation)</skos:altLabel>
  <skos:altLabel>observation of celestial bodies</skos:altLabel>
  <skos:altLabel>observatories</skos:altLabel>
  <skos:altLabel>occultation (astronomy)</skos:altLabel>
  <skos:altLabel>optical telescope facilities</skos:altLabel>
  <skos:altLabel>optical telescopes</skos:altLabel>
  <skos:altLabel>planet location</skos:altLabel>
  <skos:altLabel>pulsars (observation)</skos:altLabel>
  <skos:altLabel>quasars (observation)</skos:altLabel>
  <skos:altLabel>radar telescope and range finder facilities</skos:altLabel>
  <skos:altLabel>radar telescopes</skos:altLabel>
  <skos:altLabel>radio astronomy</skos:altLabel>
  <skos:altLabel>radio telescope facilities</skos:altLabel>
  <skos:altLabel>radio telescopes</skos:altLabel>
  <skos:altLabel>spaceborne astronomy</skos:altLabel>
  <skos:altLabel>spectroscopy (astronomy)</skos:altLabel>
  <skos:altLabel>star trackers (observation)</skos:altLabel>
  <skos:altLabel>stars (observation)</skos:altLabel>
  <skos:altLabel>stellar spectroscopy</skos:altLabel>
  <skos:altLabel>supernovae (observation)</skos:altLabel>
  <skos:altLabel>telescopes (operation)</skos:altLabel>
  <skos:altLabel>ultraviolet astronomy</skos:altLabel>
  <skos:altLabel>x-ray astronomy</skos:altLabel>
  <skos:altLabel>x-ray telescopes</skos:altLabel>
  <skos:altLabel>zodiacal light</skos:altLabel>
  <skos:broader rdf:resource='subj:2871'/>
  <nt2:status>Approved</nt2:status>
  <nt2:type>Descriptor</nt2:type>
  <nt2:inputdate>2007-01-11</nt2:inputdate>
  <dcterms:dateAccepted>2006-12-01</dcterms:dateAccepted>
  <dcterms:modified>2007-01-11</dcterms:modified>
  <nt2:notValidDate></nt2:notValidDate>
  <nt2:code>89</nt2:code>
 </skos:Concept>
 <skos:Concept rdf:about='subj:25'>
  <skos:prefLabel>Inorganic, Organic and Physical Chemistry</skos:prefLabel>
  <skos:scopeNote>Includes the analysis, synthesis, and use inorganic and
    organic compounds; combustion theory; electrochemistry; and
    photochemistry. For related information see category 34
    Fluid Dynamics and Thermodynamics. For astrochemistry see
    category 90 Astrophysics.
  </skos:scopeNote>
  <skos:altLabel>alkali metal vapors</skos:altLabel>
  <skos:altLabel>analytical chemistry</skos:altLabel>
  <skos:altLabel>catalysts (chemical)</skos:altLabel>
  <skos:altLabel>chemical analysis</skos:altLabel>
  <skos:altLabel>chemical engineering</skos:altLabel>
  <skos:altLabel>chemiluminescence</skos:altLabel>
  <skos:altLabel>chemistry of compounds</skos:altLabel>
  <skos:altLabel>chemistry of elements</skos:altLabel>
  <skos:altLabel>chromatography (application)</skos:altLabel>
  <skos:altLabel>combustion chemistry</skos:altLabel>
  <skos:altLabel>combustion kinetics</skos:altLabel>
  <skos:altLabel>combustion physics</skos:altLabel>
  <skos:altLabel>combustion processes</skos:altLabel>
  <skos:altLabel>combustion theory</skos:altLabel>
  <skos:altLabel>detonation processes</skos:altLabel>
  <skos:altLabel>electrochemical processes</skos:altLabel>
  <skos:altLabel>electrochemistry</skos:altLabel>
  <skos:altLabel>electrophoresis</skos:altLabel>
  <skos:altLabel>ferromagnetic resonance</skos:altLabel>
  <skos:altLabel>flame studies</skos:altLabel>
  <skos:altLabel>flammability</skos:altLabel>
  <skos:altLabel>gas absorption</skos:altLabel>
  <skos:altLabel>gaseous reactions</skos:altLabel>
  <skos:altLabel>gas-solid reactions</skos:altLabel>
  <skos:altLabel>gas-surface interactions</skos:altLabel>
  <skos:altLabel>gas-surface reactions</skos:altLabel>
  <skos:altLabel>ignition studies</skos:altLabel>
  <skos:altLabel>infrared gas analysis</skos:altLabel>
  <skos:altLabel>inorganic chemistry</skos:altLabel>
  <skos:altLabel>low pressure chemistry</skos:altLabel>
  <skos:altLabel>luminescence (chemistry)</skos:altLabel>
  <skos:altLabel>mass spectroscopy (application)</skos:altLabel>
  <skos:altLabel>organic chemistry</skos:altLabel>
  <skos:altLabel>organometallic materials</skos:altLabel>
  <skos:altLabel>osmosis (chemistry)</skos:altLabel>
  <skos:altLabel>photochemistry</skos:altLabel>
  <skos:altLabel>physical chemistry</skos:altLabel>
  <skos:altLabel>polarography (application)</skos:altLabel>
  <skos:altLabel>pyrolysis</skos:altLabel>
  <skos:altLabel>radiation chemistry</skos:altLabel>
  <skos:altLabel>spectrophotometry (application)</skos:altLabel>
  <skos:altLabel>spectroscopic chemical analysis (application)</skos:altLabel>
  <skos:altLabel>thermochemistry</skos:altLabel>
  <skos:altLabel>vacuum chemistry</skos:altLabel>
  <skos:broader rdf:resource='subj:1058'/>
  <nt2:status>Approved</nt2:status>
  <nt2:type>Descriptor</nt2:type>
  <nt2:inputdate>2007-01-11</nt2:inputdate>
  <dcterms:dateAccepted>2006-12-01</dcterms:dateAccepted>
  <dcterms:modified>2007-01-11</dcterms:modified>
  <nt2:notValidDate></nt2:notValidDate>
  <nt2:code>25</nt2:code>
 </skos:Concept>
 <skos:Concept rdf:about='subj:09'>
  <skos:prefLabel>Research and Support Facilities (Air)</skos:prefLabel>
  <skos:scopeNote>Includes airports, runways, hangars, and aircraft repair
    and overhaul facilities; wind tunnels, water tunnels, and
    shock tubes; flight simulators; and aircraft engine test
    stands. Also includes airport ground equipment and systems.
    For airport ground operations see 03 Air Transportation and
    Safety. For astronautical facilities see 14 Ground Support
    Systems and Facilities (Space).
  </skos:scopeNote>
  <skos:altLabel>aircraft ground handling equipment</skos:altLabel>
  <skos:altLabel>aircraft servicing equipment</skos:altLabel>
  <skos:altLabel>airport access</skos:altLabel>
  <skos:altLabel>airport lighting</skos:altLabel>
  <skos:altLabel>airport planning</skos:altLabel>
  <skos:altLabel>airports and airways</skos:altLabel>
  <skos:altLabel>altitude test facilities</skos:altLabel>
  <skos:altLabel>checkout facilities (aircraft)</skos:altLabel>
  <skos:altLabel>checkout systems (aircraft)</skos:altLabel>
  <skos:altLabel>clean rooms (aircraft manufacturing and test facilities)</skos:altLabel>
  <skos:altLabel>control towers</skos:altLabel>
  <skos:altLabel>crash test facilities</skos:altLabel>
  <skos:altLabel>development facilities (aircraft)</skos:altLabel>
  <skos:altLabel>engine test stands (aircraft)</skos:altLabel>
  <skos:altLabel>flight simulators (aircrew training and aircraft</skos:altLabel>
  <skos:altLabel>development)</skos:altLabel>
  <skos:altLabel>ground support equipment (aircraft)</skos:altLabel>
  <skos:altLabel>ground support facilities (aircraft)</skos:altLabel>
  <skos:altLabel>ground support systems (aircraft)</skos:altLabel>
  <skos:altLabel>ground support vehicles (aircraft)</skos:altLabel>
  <skos:altLabel>hangar facilities</skos:altLabel>
  <skos:altLabel>high temperature test facilities (aircraft)</skos:altLabel>
  <skos:altLabel>low temperature test facilities (aircraft)</skos:altLabel>
  <skos:altLabel>maintenance facilities (aircraft)</skos:altLabel>
  <skos:altLabel>overhaul facilities (aircraft)</skos:altLabel>
  <skos:altLabel>pressure test facilities (aircraft)</skos:altLabel>
  <skos:altLabel>repair facilities (aircraft)</skos:altLabel>
  <skos:altLabel>research facilities (aircraft)</skos:altLabel>
  <skos:altLabel>runway approach lighting and markers</skos:altLabel>
  <skos:altLabel>runway construction</skos:altLabel>
  <skos:altLabel>runway lighting</skos:altLabel>
  <skos:altLabel>runway surfaces and grooving</skos:altLabel>
  <skos:altLabel>runways</skos:altLabel>
  <skos:altLabel>shock tubes and tunnels</skos:altLabel>
  <skos:altLabel>simulators (aircraft)</skos:altLabel>
  <skos:altLabel>structures test facilities (aircraft)</skos:altLabel>
  <skos:altLabel>support facilities (aircraft)</skos:altLabel>
  <skos:altLabel>temperature test facilities (aircraft)</skos:altLabel>
  <skos:altLabel>test facilities (aircraft)</skos:altLabel>
  <skos:altLabel>tracking and communications installations (aircraft)</skos:altLabel>
  <skos:altLabel>wind tunnel test facilities (aircraft)</skos:altLabel>
  <skos:broader rdf:resource='subj:101'/>
  <nt2:status>Approved</nt2:status>
  <nt2:type>Descriptor</nt2:type>
  <nt2:inputdate>2007-01-11</nt2:inputdate>
  <dcterms:dateAccepted>2006-12-01</dcterms:dateAccepted>
  <dcterms:modified>2007-01-11</dcterms:modified>
  <nt2:notValidDate></nt2:notValidDate>
  <nt2:code>09</nt2:code>
 </skos:Concept>
 <skos:Concept rdf:about='subj:75'>
  <skos:prefLabel>Plasma Physics</skos:prefLabel>
  <skos:scopeNote>Includes magnetohydrodynamics and plasma fusion. For
    ionospheric plasmas see 46 Geophysics. For space plasmas
    see 90 Astrophysics.
  </skos:scopeNote>
  <skos:altLabel>electrogasdynamics</skos:altLabel>
  <skos:altLabel>electrohydrodynamics</skos:altLabel>
  <skos:altLabel>electron density (plasma physics)</skos:altLabel>
  <skos:altLabel>fusion devices</skos:altLabel>
  <skos:altLabel>hydromagnetics (plasma physics)</skos:altLabel>
  <skos:altLabel>ion beams (plasma physics)</skos:altLabel>
  <skos:altLabel>laser interaction with plasmas</skos:altLabel>
  <skos:altLabel>magnetogasdynamics</skos:altLabel>
  <skos:altLabel>magnetohydrodynamics</skos:altLabel>
  <skos:altLabel>magnetoplasmas</skos:altLabel>
  <skos:altLabel>MHD generators</skos:altLabel>
  <skos:altLabel>microwave interaction with plasmas</skos:altLabel>
  <skos:altLabel>mirror machine (plasma physics)</skos:altLabel>
  <skos:altLabel>nuclear fusion (plasma physics)</skos:altLabel>
  <skos:altLabel>plasma conductivity</skos:altLabel>
  <skos:altLabel>plasma diagnostics</skos:altLabel>
  <skos:altLabel>plasma dynamics</skos:altLabel>
  <skos:altLabel>plasma flow</skos:altLabel>
  <skos:altLabel>plasma fusion</skos:altLabel>
  <skos:altLabel>plasma oscillations</skos:altLabel>
  <skos:altLabel>plasma physics research equipment</skos:altLabel>
  <skos:altLabel>plasma pinch</skos:altLabel>
  <skos:altLabel>plasma propulsion (theory)</skos:altLabel>
  <skos:altLabel>plasma seeding</skos:altLabel>
  <skos:altLabel>plasma sheath</skos:altLabel>
  <skos:altLabel>plasma theory</skos:altLabel>
  <skos:altLabel>plasma waves</skos:altLabel>
  <skos:altLabel>stellarators</skos:altLabel>
  <skos:altLabel>tokamak devices</skos:altLabel>
  <skos:altLabel>whistlers (plasma physics)</skos:altLabel>
  <skos:broader rdf:resource='subj:2528'/>
  <nt2:status>Approved</nt2:status>
  <nt2:type>Descriptor</nt2:type>
  <nt2:inputdate>2007-01-11</nt2:inputdate>
  <dcterms:dateAccepted>2006-12-01</dcterms:dateAccepted>
  <dcterms:modified>2007-01-11</dcterms:modified>
  <nt2:notValidDate></nt2:notValidDate>
  <nt2:code>75</nt2:code>
 </skos:Concept>
 <skos:Concept rdf:about='subj:578'>
  <skos:prefLabel>Astronautics</skos:prefLabel>
  <skos:scopeNote>Includes astronautics (general); astrodynamics; ground
    support systems and facilities (space); launch vehicles and
    launch operations; space transportation and safety; space
    communications, spacecraft communications, command, and
    tracking; spacecraft design, testing and performance;
    spacecraft instrumentation and astrionics; and spacecraft
    propulsion and power. For related information see also
    Aeronautics (categories 01 through 09).
  </skos:scopeNote>
  <skos:broader rdf:resource='subj:100'/>
  <skos:narrower rdf:resource='subj:13'/>
  <skos:narrower rdf:resource='subj:12'/>
  <skos:narrower rdf:resource='subj:14'/>
  <skos:narrower rdf:resource='subj:15'/>
  <skos:narrower rdf:resource='subj:WQQ-225'/>
  <skos:narrower rdf:resource='subj:WQQ-226'/>
  <skos:narrower rdf:resource='subj:16'/>
  <skos:narrower rdf:resource='subj:18'/>
  <skos:narrower rdf:resource='subj:19'/>
  <skos:narrower rdf:resource='subj:20'/>
  <nt2:status>Approved</nt2:status>
  <nt2:type>Descriptor</nt2:type>
  <nt2:inputdate>2007-01-11</nt2:inputdate>
  <dcterms:dateAccepted>2006-12-01</dcterms:dateAccepted>
  <dcterms:modified>2007-01-11</dcterms:modified>
  <nt2:notValidDate></nt2:notValidDate>
  <nt2:code>578</nt2:code>
 </skos:Concept>
 <skos:Concept rdf:about='subj:83'>
  <skos:prefLabel>Economics and Cost Analysis</skos:prefLabel>
  <skos:scopeNote>Includes cost effectiveness studies.
  </skos:scopeNote>
  <skos:altLabel>aircraft production economic</skos:altLabel>
  <skos:altLabel>airline economics</skos:altLabel>
  <skos:altLabel>cost analysis</skos:altLabel>
  <skos:altLabel>cost effectiveness studies</skos:altLabel>
  <skos:altLabel>economic impacts</skos:altLabel>
  <skos:altLabel>economics</skos:altLabel>
  <skos:altLabel>insurance (aerospace)</skos:altLabel>
  <skos:altLabel>marketing predictions</skos:altLabel>
  <skos:altLabel>marketing research</skos:altLabel>
  <skos:altLabel>production costs</skos:altLabel>
  <skos:altLabel>production forecasts</skos:altLabel>
  <skos:altLabel>space transportation economics</skos:altLabel>
  <skos:altLabel>transportation funding forecasts (aerospace)</skos:altLabel>
  <skos:broader rdf:resource='subj:2767'/>
  <nt2:status>Approved</nt2:status>
  <nt2:type>Descriptor</nt2:type>
  <nt2:inputdate>2007-01-11</nt2:inputdate>
  <dcterms:dateAccepted>2006-12-01</dcterms:dateAccepted>
  <dcterms:modified>2007-01-11</dcterms:modified>
  <nt2:notValidDate></nt2:notValidDate>
  <nt2:code>83</nt2:code>
 </skos:Concept>
 <skos:Concept rdf:about='subj:92'>
  <skos:prefLabel>Solar Physics</skos:prefLabel>
  <skos:scopeNote>Includes solar activity, solar flares, solar radiation and
    sunspots. For related information see 93 Space Radiation.
  </skos:scopeNote>
  <skos:altLabel>alpha rays (solar)</skos:altLabel>
  <skos:altLabel>beta rays (solar)</skos:altLabel>
  <skos:altLabel>chromosphere (solar)</skos:altLabel>
  <skos:altLabel>lunar eclipses</skos:altLabel>
  <skos:altLabel>photosphere (solar)</skos:altLabel>
  <skos:altLabel>solar activity</skos:altLabel>
  <skos:altLabel>solar atmosphere</skos:altLabel>
  <skos:altLabel>solar constants</skos:altLabel>
  <skos:altLabel>solar corona</skos:altLabel>
  <skos:altLabel>solar cycles</skos:altLabel>
  <skos:altLabel>solar density</skos:altLabel>
  <skos:altLabel>solar eclipses</skos:altLabel>
  <skos:altLabel>solar flares</skos:altLabel>
  <skos:altLabel>solar magnetic field</skos:altLabel>
  <skos:altLabel>solar mass</skos:altLabel>
  <skos:altLabel>solar radiation</skos:altLabel>
  <skos:altLabel>solar radio emissions</skos:altLabel>
  <skos:altLabel>solar spectra</skos:altLabel>
  <skos:altLabel>solar structure</skos:altLabel>
  <skos:altLabel>solar wind</skos:altLabel>
  <skos:altLabel>sun</skos:altLabel>
  <skos:altLabel>sunspots</skos:altLabel>
  <skos:broader rdf:resource='subj:2871'/>
  <nt2:status>Approved</nt2:status>
  <nt2:type>Descriptor</nt2:type>
  <nt2:inputdate>2007-01-11</nt2:inputdate>
  <dcterms:dateAccepted>2006-12-01</dcterms:dateAccepted>
  <dcterms:modified>2007-01-11</dcterms:modified>
  <nt2:notValidDate></nt2:notValidDate>
  <nt2:code>92</nt2:code>
 </skos:Concept>
 <skos:Concept rdf:about='subj:20'>
  <skos:prefLabel>Spacecraft Propulsion and Power</skos:prefLabel>
  <skos:scopeNote>Includes main propulsion systems and components, e.g.,
    rocket engines; and spacecraft auxiliary power sources. For
    related information see also 07 Aircraft Propulsion and
    Power; 28 Propellants and Fuels; 15 Launch Vehicles and
    Launch Operations; and 44 Energy Production and Conversion.
  </skos:scopeNote>
  <skos:altLabel>aerospike engines</skos:altLabel>
  <skos:altLabel>attitude thrusters</skos:altLabel>
  <skos:altLabel>auxiliary power systems (spacecraft)</skos:altLabel>
  <skos:altLabel>auxiliary power units (APU) (spacecraft)</skos:altLabel>
  <skos:altLabel>boosters (spacecraft)</skos:altLabel>
  <skos:altLabel>chemical power sources (spacecraft)</skos:altLabel>
  <skos:altLabel>chemical propulsion engines (spacecraft)</skos:altLabel>
  <skos:altLabel>clustered rockets</skos:altLabel>
  <skos:altLabel>combustion chambers (spacecraft)</skos:altLabel>
  <skos:altLabel>combustors (spacecraft)</skos:altLabel>
  <skos:altLabel>ejectors (spacecraft)</skos:altLabel>
  <skos:altLabel>electric power systems (spacecraft)</skos:altLabel>
  <skos:altLabel>electric power units (spacecraft)</skos:altLabel>
  <skos:altLabel>electric propulsion systems (spacecraft)</skos:altLabel>
  <skos:altLabel>electric rocket engines</skos:altLabel>
  <skos:altLabel>electrostatic rocket engines</skos:altLabel>
  <skos:altLabel>electrothermal rocket engines</skos:altLabel>
  <skos:altLabel>fuel distribution pumps (spacecraft)</skos:altLabel>
  <skos:altLabel>fuel distribution systems (spacecraft)</skos:altLabel>
  <skos:altLabel>fuel injection systems (spacecraft)</skos:altLabel>
  <skos:altLabel>fuel system components (spacecraft)</skos:altLabel>
  <skos:altLabel>fuel systems (spacecraft)</skos:altLabel>
  <skos:altLabel>fuel tanks (spacecraft)</skos:altLabel>
  <skos:altLabel>hybrid propellant rocket engines</skos:altLabel>
  <skos:altLabel>igniters (rocket engines)</skos:altLabel>
  <skos:altLabel>ion engines</skos:altLabel>
  <skos:altLabel>ion propulsion</skos:altLabel>
  <skos:altLabel>ion rocket engines</skos:altLabel>
  <skos:altLabel>liquid propellant rocket engines</skos:altLabel>
  <skos:altLabel>low thrust engines</skos:altLabel>
  <skos:altLabel>magnetic sails</skos:altLabel>
  <skos:altLabel>magnetohydrodynamic (MHO) power sources</skos:altLabel>
  <skos:altLabel>magnetohydrodynamic (MHO) thrusters</skos:altLabel>
  <skos:altLabel>main propulsion system components (spacecraft)</skos:altLabel>
  <skos:altLabel>main propulsion systems (spacecraft)</skos:altLabel>
  <skos:altLabel>multistage rockets</skos:altLabel>
  <skos:altLabel>nozzles (spacecraft)</skos:altLabel>
  <skos:altLabel>nuclear engines (spacecraft application)</skos:altLabel>
  <skos:altLabel>nuclear power sources (spacecraft application)</skos:altLabel>
  <skos:altLabel>nuclear propulsion systems (spacecraft application)</skos:altLabel>
  <skos:altLabel>nuclear rocket engines</skos:altLabel>
  <skos:altLabel>onboard solar arrays</skos:altLabel>
  <skos:altLabel>onboard solar generators</skos:altLabel>
  <skos:altLabel>plasma propulsion (spacecraft applications)</skos:altLabel>
  <skos:altLabel>pneumatic systems (spacecraft propulsion and power)</skos:altLabel>
  <skos:altLabel>propellant flow systems (spacecraft)</skos:altLabel>
  <skos:altLabel>propellant injectors, pumps, and tanks (spacecraft)</skos:altLabel>
  <skos:altLabel>propulsion system components (spacecraft)</skos:altLabel>
  <skos:altLabel>propulsion systems (spacecraft)</skos:altLabel>
  <skos:altLabel>pumps (spacecraft)</skos:altLabel>
  <skos:altLabel>refueling in orbit</skos:altLabel>
  <skos:altLabel>retrorockets</skos:altLabel>
  <skos:altLabel>rocket engine design</skos:altLabel>
  <skos:altLabel>rocket engine exhaust plumes</skos:altLabel>
  <skos:altLabel>rocket engine noise</skos:altLabel>
  <skos:altLabel>rocket engines (spacecraft)</skos:altLabel>
  <skos:altLabel>rocket throttling systems</skos:altLabel>
  <skos:altLabel>solar electric ion propulsion</skos:altLabel>
  <skos:altLabel>solar electric propulsion</skos:altLabel>
  <skos:altLabel>solar sails</skos:altLabel>
  <skos:altLabel>solid propellant rocket engines</skos:altLabel>
  <skos:altLabel>space power reactors (application)</skos:altLabel>
  <skos:altLabel>spacecraft auxiliary power sources</skos:altLabel>
  <skos:altLabel>spacecraft engine design</skos:altLabel>
  <skos:altLabel>spacecraft hydraulic systems (power)</skos:altLabel>
  <skos:altLabel>spacecraft pneumatic systems (power)</skos:altLabel>
  <skos:altLabel>spacecraft power systems</skos:altLabel>
  <skos:altLabel>spacecraft propulsion</skos:altLabel>
  <skos:altLabel>spacecraft vehicle booster engines</skos:altLabel>
  <skos:altLabel>systems for energy conversion (spacecraft)</skos:altLabel>
  <skos:altLabel>thrust vector control devices (spacecraft)</skos:altLabel>
  <skos:altLabel>turborocket engines (spacecraft)</skos:altLabel>
  <skos:altLabel>vector control engines (spacecraft)</skos:altLabel>
  <skos:altLabel>vernier engines (spacecraft)</skos:altLabel>
  <skos:broader rdf:resource='subj:578'/>
  <nt2:status>Approved</nt2:status>
  <nt2:type>Descriptor</nt2:type>
  <nt2:inputdate>2007-01-11</nt2:inputdate>
  <dcterms:dateAccepted>2006-12-01</dcterms:dateAccepted>
  <dcterms:modified>2007-01-11</dcterms:modified>
  <nt2:notValidDate></nt2:notValidDate>
  <nt2:code>20</nt2:code>
 </skos:Concept>
 <skos:Concept rdf:about='subj:17'>
  <skos:prefLabel>Space Communications, Spacecraft Communications, Command and Tracking</skos:prefLabel>
  <skos:scopeNote>Includes space systems telemetry; space communications
    networks; astronavigation and guidance; and spacecraft
    radio blackout. For related information see also 04
    Aircraft Communications and Navigation; and 32
    Communications and Radar.
  </skos:scopeNote>
  <skos:altLabel>astronavigation</skos:altLabel>
  <skos:altLabel>automatic picture transmission (APT)</skos:altLabel>
  <skos:altLabel>celestial navigation (spacecraft)</skos:altLabel>
  <skos:altLabel>collision avoidance (spacecraft)</skos:altLabel>
  <skos:altLabel>command and control of spacecraft</skos:altLabel>
  <skos:altLabel>communications blackouts (reentry)</skos:altLabel>
  <skos:altLabel>communications networks (space)</skos:altLabel>
  <skos:altLabel>communications systems (space)</skos:altLabel>
  <skos:altLabel>Deep Space Network</skos:altLabel>
  <skos:altLabel>digital communications systems (spacecraft)</skos:altLabel>
  <skos:altLabel>global positioning systems (spacecraft)</skos:altLabel>
  <skos:altLabel>ground based data acquisition stations</skos:altLabel>
  <skos:altLabel>ground based data acquisition systems</skos:altLabel>
  <skos:altLabel>ground based tracking stations</skos:altLabel>
  <skos:altLabel>ground based tracking systems</skos:altLabel>
  <skos:altLabel>guidance system design (spacecraft)</skos:altLabel>
  <skos:altLabel>inertial navigation systems (spacecraft)</skos:altLabel>
  <skos:altLabel>inertial sensors and measurement units (spacecraft)</skos:altLabel>
  <skos:altLabel>laser communications systems (spacecraft)</skos:altLabel>
  <skos:altLabel>laser tracking systems (spacecraft)</skos:altLabel>
  <skos:altLabel>launch vehicle navigation</skos:altLabel>
  <skos:altLabel>man-machine communications (spacecraft)</skos:altLabel>
  <skos:altLabel>manned space flight network</skos:altLabel>
  <skos:altLabel>microwave communications systems (spacecraft)</skos:altLabel>
  <skos:altLabel>microwave receivers (spacecraft)</skos:altLabel>
  <skos:altLabel>microwave transmitters (spacecraft)</skos:altLabel>
  <skos:altLabel>navigation computer systems (spacecraft)</skos:altLabel>
  <skos:altLabel>navigation display devices (spacecraft)</skos:altLabel>
  <skos:altLabel>navigation system design (spacecraft)</skos:altLabel>
  <skos:altLabel>navigation systems (spacecraft)</skos:altLabel>
  <skos:altLabel>optical communication (space)</skos:altLabel>
  <skos:altLabel>orbital maneuvers (control)</skos:altLabel>
  <skos:altLabel>radar communications systems (spacecraft)</skos:altLabel>
  <skos:altLabel>radar detection (spacecraft navigation)</skos:altLabel>
  <skos:altLabel>radar imagery (spacecraft navigation)</skos:altLabel>
  <skos:altLabel>radar tracking systems (spacecraft)</skos:altLabel>
  <skos:altLabel>radio blackout (loss of communications)</skos:altLabel>
  <skos:altLabel>radio communications systems (spacecraft)</skos:altLabel>
  <skos:altLabel>range and angle measurement (spacecraft)</skos:altLabel>
  <skos:altLabel>rendezvous guidance</skos:altLabel>
  <skos:altLabel>search and rescue operations (communications)</skos:altLabel>
  <skos:altLabel>Shuttle Imaging radar (theory and techniques)</skos:altLabel>
  <skos:altLabel>space based data acquisition stations</skos:altLabel>
  <skos:altLabel>space based data acquisition systems</skos:altLabel>
  <skos:altLabel>space communications</skos:altLabel>
  <skos:altLabel>space communications networks</skos:altLabel>
  <skos:altLabel>space flight communication techniques and theory</skos:altLabel>
  <skos:altLabel>space flight navigation techniques and theory</skos:altLabel>
  <skos:altLabel>space navigation</skos:altLabel>
  <skos:altLabel>Space Tracking and Data Acquisition Network (STADAN)</skos:altLabel>
  <skos:altLabel>spacecraft command</skos:altLabel>
  <skos:altLabel>spacecraft communications</skos:altLabel>
  <skos:altLabel>spacecraft control (communications)</skos:altLabel>
  <skos:altLabel>spacecraft navigation</skos:altLabel>
  <skos:altLabel>spacecraft tracking</skos:altLabel>
  <skos:altLabel>speech analysis (spacecraft voice communications)</skos:altLabel>
  <skos:altLabel>speech compression (spacecraft voice communications)</skos:altLabel>
  <skos:altLabel>station keeping</skos:altLabel>
  <skos:altLabel>target-signature modeling (spacecraft)</skos:altLabel>
  <skos:altLabel>telemetry (spacecraft applications)</skos:altLabel>
  <skos:altLabel>tracking and communications installations (spacecraft)</skos:altLabel>
  <skos:altLabel>tracking networks</skos:altLabel>
  <skos:altLabel>tracking stations</skos:altLabel>
  <skos:altLabel>voice communications systems (spacecraft)</skos:altLabel>
  <skos:altLabel>wave propagation (spacecraft communications effect)</skos:altLabel>
  <skos:broader rdf:resource='subj:578'/>
  <nt2:status>Approved</nt2:status>
  <nt2:type>Descriptor</nt2:type>
  <nt2:inputdate>2007-01-11</nt2:inputdate>
  <dcterms:dateAccepted>2006-12-01</dcterms:dateAccepted>
  <dcterms:modified>2007-01-11</dcterms:modified>
  <nt2:notValidDate></nt2:notValidDate>
  <nt2:code>17</nt2:code>
 </skos:Concept>
 <skos:Concept rdf:about='subj:82'>
  <skos:prefLabel>Documentation and Information Science</skos:prefLabel>
  <skos:scopeNote>Includes information management; information storage and
    retrieval technology; technical writing; graphic arts; and
    micrography. For computer program documentation see 61
    Computer Programming and Software.
  </skos:scopeNote>
  <skos:altLabel>copyright regulations</skos:altLabel>
  <skos:altLabel>databases</skos:altLabel>
  <skos:altLabel>document markup languages (information transfer)</skos:altLabel>
  <skos:altLabel>document miniaturization</skos:altLabel>
  <skos:altLabel>document processing</skos:altLabel>
  <skos:altLabel>documentation</skos:altLabel>
  <skos:altLabel>geographical information systems</skos:altLabel>
  <skos:altLabel>graphic arts</skos:altLabel>
  <skos:altLabel>information retrieval</skos:altLabel>
  <skos:altLabel>information science</skos:altLabel>
  <skos:altLabel>information storage</skos:altLabel>
  <skos:altLabel>information systems</skos:altLabel>
  <skos:altLabel>internet resources</skos:altLabel>
  <skos:altLabel>language translation</skos:altLabel>
  <skos:altLabel>lexicography</skos:altLabel>
  <skos:altLabel>library science</skos:altLabel>
  <skos:altLabel>manuals (refer to appropriate category for manuals)</skos:altLabel>
  <skos:altLabel>mechanical drawing</skos:altLabel>
  <skos:altLabel>microfiche techniques</skos:altLabel>
  <skos:altLabel>micrography</skos:altLabel>
  <skos:altLabel>project documentation</skos:altLabel>
  <skos:altLabel>reprography</skos:altLabel>
  <skos:altLabel>Space Station Information System</skos:altLabel>
  <skos:altLabel>technical writing</skos:altLabel>
  <skos:broader rdf:resource='subj:2767'/>
  <nt2:status>Approved</nt2:status>
  <nt2:type>Descriptor</nt2:type>
  <nt2:inputdate>2007-01-11</nt2:inputdate>
  <dcterms:dateAccepted>2006-12-01</dcterms:dateAccepted>
  <dcterms:modified>2007-01-11</dcterms:modified>
  <nt2:notValidDate></nt2:notValidDate>
  <nt2:code>82</nt2:code>
 </skos:Concept>
 <skos:Concept rdf:about='subj:91'>
  <skos:prefLabel>Lunar and Planetary Science and Exploration</skos:prefLabel>
  <skos:scopeNote>Includes planetology; selenology; meteorites; comets;
    craters; and manned and unmanned planetary and lunar
    flights. For spacecraft design or space stations see 18
    Spacecraft Design, Testing and Performance.
  </skos:scopeNote>
  <skos:altLabel>asteroids (characteristics and composition)</skos:altLabel>
  <skos:altLabel>comet exploration</skos:altLabel>
  <skos:altLabel>comets (characteristics and composition)</skos:altLabel>
  <skos:altLabel>composition)</skos:altLabel>
  <skos:altLabel>craters (extraterrestrial)</skos:altLabel>
  <skos:altLabel>dwarf planets</skos:altLabel>
  <skos:altLabel>Earth analogs</skos:altLabel>
  <skos:altLabel>extraterrestrial roving vehicles</skos:altLabel>
  <skos:altLabel>flyby missions</skos:altLabel>
  <skos:altLabel>gas giant planets</skos:altLabel>
  <skos:altLabel>lunar and planetary resource utilization</skos:altLabel>
  <skos:altLabel>lunar and planetary resources</skos:altLabel>
  <skos:altLabel>lunar exploration</skos:altLabel>
  <skos:altLabel>lunar landing sites</skos:altLabel>
  <skos:altLabel>lunar mapping</skos:altLabel>
  <skos:altLabel>lunar photography</skos:altLabel>
  <skos:altLabel>lunar regolith simulants</skos:altLabel>
  <skos:altLabel>lunar samples</skos:altLabel>
  <skos:altLabel>lunar structure</skos:altLabel>
  <skos:altLabel>manned flights (space exploration)</skos:altLabel>
  <skos:altLabel>manned lunar exploration</skos:altLabel>
  <skos:altLabel>manned Mars missions</skos:altLabel>
  <skos:altLabel>manned planetary exploration</skos:altLabel>
  <skos:altLabel>Mars exploration</skos:altLabel>
  <skos:altLabel>meteorites</skos:altLabel>
  <skos:altLabel>meteoroids</skos:altLabel>
  <skos:altLabel>meteors</skos:altLabel>
  <skos:altLabel>moons (characteristics and composition)</skos:altLabel>
  <skos:altLabel>natural satellites (characteristics and composition)</skos:altLabel>
  <skos:altLabel>planetary atmospheres</skos:altLabel>
  <skos:altLabel>planetary exploration</skos:altLabel>
  <skos:altLabel>planetary mapping</skos:altLabel>
  <skos:altLabel>planetary motion</skos:altLabel>
  <skos:altLabel>planetary photography</skos:altLabel>
  <skos:altLabel>planetary samples</skos:altLabel>
  <skos:altLabel>planetary satellites (characteristics)</skos:altLabel>
  <skos:altLabel>planetary structure</skos:altLabel>
  <skos:altLabel>planetology</skos:altLabel>
  <skos:altLabel>remote exploration of planets</skos:altLabel>
  <skos:altLabel>selenography</skos:altLabel>
  <skos:altLabel>selenology</skos:altLabel>
  <skos:altLabel>soil sampling and analysis (planetology)</skos:altLabel>
  <skos:altLabel>solar system bodies</skos:altLabel>
  <skos:altLabel>tektites</skos:altLabel>
  <skos:altLabel>terrestrial planets</skos:altLabel>
  <skos:altLabel>unmanned flights (space exploration)</skos:altLabel>
  <skos:altLabel>unmanned lunar exploration</skos:altLabel>
  <skos:altLabel>unmanned planetary exploration</skos:altLabel>
  <skos:broader rdf:resource='subj:2871'/>
  <nt2:status>Approved</nt2:status>
  <nt2:type>Descriptor</nt2:type>
  <nt2:inputdate>2007-01-11</nt2:inputdate>
  <dcterms:dateAccepted>2006-12-01</dcterms:dateAccepted>
  <dcterms:modified>2007-01-11</dcterms:modified>
  <nt2:notValidDate></nt2:notValidDate>
  <nt2:code>91</nt2:code>
 </skos:Concept>
 <skos:Concept rdf:about='subj:65'>
  <skos:prefLabel>Statistics and Probability</skos:prefLabel>
  <skos:scopeNote>Includes data sampling and smoothing; Monte Carlo method;
    time series analysis; and stochastic processes.
  </skos:scopeNote>
  <skos:altLabel>analysis of variance</skos:altLabel>
  <skos:altLabel>Bayesian statistics</skos:altLabel>
  <skos:altLabel>data sampling</skos:altLabel>
  <skos:altLabel>data smoothing</skos:altLabel>
  <skos:altLabel>error analysis (statistics)</skos:altLabel>
  <skos:altLabel>Markov processes</skos:altLabel>
  <skos:altLabel>martingales</skos:altLabel>
  <skos:altLabel>maximum likelihood estimation</skos:altLabel>
  <skos:altLabel>minimax techniques</skos:altLabel>
  <skos:altLabel>Monte Carlo method</skos:altLabel>
  <skos:altLabel>prediction analysis</skos:altLabel>
  <skos:altLabel>principal components analysis</skos:altLabel>
  <skos:altLabel>probability</skos:altLabel>
  <skos:altLabel>probability density functions</skos:altLabel>
  <skos:altLabel>random sampling</skos:altLabel>
  <skos:altLabel>regression analysis</skos:altLabel>
  <skos:altLabel>sampling techniques (statistics)</skos:altLabel>
  <skos:altLabel>statistical techniques</skos:altLabel>
  <skos:altLabel>statistics</skos:altLabel>
  <skos:altLabel>stochastic processes</skos:altLabel>
  <skos:altLabel>time series analysis</skos:altLabel>
  <skos:altLabel>Weilbull distributions</skos:altLabel>
  <skos:broader rdf:resource='subj:2321'/>
  <nt2:status>Approved</nt2:status>
  <nt2:type>Descriptor</nt2:type>
  <nt2:inputdate>2007-01-11</nt2:inputdate>
  <dcterms:dateAccepted>2006-12-01</dcterms:dateAccepted>
  <dcterms:modified>2007-01-11</dcterms:modified>
  <nt2:notValidDate></nt2:notValidDate>
  <nt2:code>65</nt2:code>
 </skos:Concept>
 <skos:Concept rdf:about='subj:3056'>
  <skos:prefLabel>General</skos:prefLabel>
  <skos:scopeNote>Includes aerospace related reports of a general or broad
    nature; histories, biographies, or overviews of aerospace
    programs.
  </skos:scopeNote>
  <skos:broader rdf:resource='subj:100'/>
  <skos:narrower rdf:resource='subj:99'/>
  <nt2:status>Approved</nt2:status>
  <nt2:type>Descriptor</nt2:type>
  <nt2:inputdate>2007-01-11</nt2:inputdate>
  <dcterms:dateAccepted>2006-12-01</dcterms:dateAccepted>
  <dcterms:modified>2007-01-11</dcterms:modified>
  <nt2:notValidDate></nt2:notValidDate>
  <nt2:code>3056</nt2:code>
 </skos:Concept>
 <skos:Concept rdf:about='subj:85'>
  <skos:prefLabel>Technology Utilization and Surface Transportation</skos:prefLabel>
  <skos:scopeNote>Includes aerospace technology transfer; urban technology;
    surface and mass transportation. For related information
    see also 03 Air Transportation and Safety; 16 Space
    Transportation and Safety; and 44 Energy Production and
    Conversion. For specific technology transfer applications
    see also the category where the subject is treated.
  </skos:scopeNote>
  <skos:altLabel>air cushion vehicles</skos:altLabel>
  <skos:altLabel>electric vehicles</skos:altLabel>
  <skos:altLabel>fresh water sources</skos:altLabel>
  <skos:altLabel>global position system (surface navigation)</skos:altLabel>
  <skos:altLabel>ground effect machines</skos:altLabel>
  <skos:altLabel>hybrid vehicles</skos:altLabel>
  <skos:altLabel>hydrofoil vehicles</skos:altLabel>
  <skos:altLabel>land transportation vehicles (development and</skos:altLabel>
  <skos:altLabel>maglev vehicles</skos:altLabel>
  <skos:altLabel>mass transportation</skos:altLabel>
  <skos:altLabel>rapid transit systems</skos:altLabel>
  <skos:altLabel>sewage disposal</skos:altLabel>
  <skos:altLabel>space technology applications to urban problems</skos:altLabel>
  <skos:altLabel>surface transportation</skos:altLabel>
  <skos:altLabel>technology transfer</skos:altLabel>
  <skos:altLabel>technology utilization</skos:altLabel>
  <skos:altLabel>technology</skos:altLabel>
  <skos:altLabel>urban technology</skos:altLabel>
  <skos:altLabel>urban transportation</skos:altLabel>
  <skos:altLabel>waste products conversion (urban technology)</skos:altLabel>
  <skos:altLabel>waste products disposal (urban technology)</skos:altLabel>
  <skos:altLabel>waste treatment (development and technology)</skos:altLabel>
  <skos:altLabel>water treatment (development and technology)</skos:altLabel>
  <skos:broader rdf:resource='subj:2767'/>
  <nt2:status>Approved</nt2:status>
  <nt2:type>Descriptor</nt2:type>
  <nt2:inputdate>2007-01-11</nt2:inputdate>
  <dcterms:dateAccepted>2006-12-01</dcterms:dateAccepted>
  <dcterms:modified>2007-01-11</dcterms:modified>
  <nt2:notValidDate></nt2:notValidDate>
  <nt2:code>85</nt2:code>
 </skos:Concept>
 <skos:Concept rdf:about='subj:2321'>
  <skos:prefLabel>Mathematical and Computer Sciences</skos:prefLabel>
  <skos:scopeNote>Includes mathematical and computer sciences (general);
    computer operations and hardware; computer programming and
    software; computer systems; cybernetics, artificial
    intelligence and robotics; numerical analysis; statistics
    and probability; systems analysis and operations research;
    and theoretical mathematics.
  </skos:scopeNote>
  <skos:broader rdf:resource='subj:100'/>
  <skos:narrower rdf:resource='subj:60'/>
  <skos:narrower rdf:resource='subj:61'/>
  <skos:narrower rdf:resource='subj:62'/>
  <skos:narrower rdf:resource='subj:63'/>
  <skos:narrower rdf:resource='subj:59'/>
  <skos:narrower rdf:resource='subj:64'/>
  <skos:narrower rdf:resource='subj:65'/>
  <skos:narrower rdf:resource='subj:66'/>
  <skos:narrower rdf:resource='subj:67'/>
  <nt2:status>Approved</nt2:status>
  <nt2:type>Descriptor</nt2:type>
  <nt2:inputdate>2007-01-11</nt2:inputdate>
  <dcterms:dateAccepted>2006-12-01</dcterms:dateAccepted>
  <dcterms:modified>2007-01-11</dcterms:modified>
  <nt2:notValidDate></nt2:notValidDate>
  <nt2:code>2321</nt2:code>
 </skos:Concept>
 <skos:Concept rdf:about='subj:32'>
  <skos:prefLabel>Communications and Radar</skos:prefLabel>
  <skos:scopeNote>Includes radar; radio, wire, and optical communications;
    land and global communications; communications theory. For
    related information see also 04 Aircraft Communications and
    Navigation; and 17 Space Communications, Spacecraft
    Communications, Command and Tracking; for search and
    rescue, see 03 Air Transportation and Safety; and 16 Space
    Transportation and Safety.
  </skos:scopeNote>
  <skos:altLabel>antenna design</skos:altLabel>
  <skos:altLabel>antenna radiation patterns</skos:altLabel>
  <skos:altLabel>antenna theory</skos:altLabel>
  <skos:altLabel>communications (general)</skos:altLabel>
  <skos:altLabel>communications blackouts (electromagnetic interference)</skos:altLabel>
  <skos:altLabel>communications coding</skos:altLabel>
  <skos:altLabel>communications equipment</skos:altLabel>
  <skos:altLabel>communications interference</skos:altLabel>
  <skos:altLabel>communications networks (theory and techniques)</skos:altLabel>
  <skos:altLabel>communications noise</skos:altLabel>
  <skos:altLabel>communications satellite operational problems</skos:altLabel>
  <skos:altLabel>communications systems (theory and techniques)</skos:altLabel>
  <skos:altLabel>communications techniques</skos:altLabel>
  <skos:altLabel>communications theory</skos:altLabel>
  <skos:altLabel>data transmission applications</skos:altLabel>
  <skos:altLabel>data transmission development</skos:altLabel>
  <skos:altLabel>data transmission equipment</skos:altLabel>
  <skos:altLabel>data transmission research</skos:altLabel>
  <skos:altLabel>data transmission techniques</skos:altLabel>
  <skos:altLabel>digital communications systems (theory and techniques)</skos:altLabel>
  <skos:altLabel>electromagnetic interference</skos:altLabel>
  <skos:altLabel>electromagnetic radiation (communications)</skos:altLabel>
  <skos:altLabel>electromagnetic wave propagation</skos:altLabel>
  <skos:altLabel>electronic countermeasures</skos:altLabel>
  <skos:altLabel>frequency assignment</skos:altLabel>
  <skos:altLabel>global communications</skos:altLabel>
  <skos:altLabel>ionospheric effects on radio transmission (communications)</skos:altLabel>
  <skos:altLabel>ionospheric propagation (communications)</skos:altLabel>
  <skos:altLabel>ionospheric scatter (communications)</skos:altLabel>
  <skos:altLabel>ladar (application)</skos:altLabel>
  <skos:altLabel>large deployable space antennas</skos:altLabel>
  <skos:altLabel>laser communications</skos:altLabel>
  <skos:altLabel>laser optical radar</skos:altLabel>
  <skos:altLabel>lidar</skos:altLabel>
  <skos:altLabel>man-machine communications (theory and techniques)</skos:altLabel>
  <skos:altLabel>microwave communications systems (applications)</skos:altLabel>
  <skos:altLabel>microwave radiation (properties)</skos:altLabel>
  <skos:altLabel>microwave receivers (theory and techniques)</skos:altLabel>
  <skos:altLabel>microwave techniques</skos:altLabel>
  <skos:altLabel>microwave theory</skos:altLabel>
  <skos:altLabel>microwave transmitters (theory and techniques)</skos:altLabel>
  <skos:altLabel>modulation (signals)</skos:altLabel>
  <skos:altLabel>networks (communications)</skos:altLabel>
  <skos:altLabel>optical communications (applications)</skos:altLabel>
  <skos:altLabel>phase shift keying (PSK)</skos:altLabel>
  <skos:altLabel>phased array radar</skos:altLabel>
  <skos:altLabel>radar (theory and techniques)</skos:altLabel>
  <skos:altLabel>radar absorbing materials</skos:altLabel>
  <skos:altLabel>radar antenna design</skos:altLabel>
  <skos:altLabel>radar antennas (theory and techniques)</skos:altLabel>
  <skos:altLabel>radar clutter</skos:altLabel>
  <skos:altLabel>radar communications systems (theory and techniques)</skos:altLabel>
  <skos:altLabel>radar detection (communications)</skos:altLabel>
  <skos:altLabel>radar imagery (communications)</skos:altLabel>
  <skos:altLabel>radar receivers (theory and techniques)</skos:altLabel>
  <skos:altLabel>radar scattering</skos:altLabel>
  <skos:altLabel>radar tracking systems (theory and techniques)</skos:altLabel>
  <skos:altLabel>radar transmitters (theory and techniques)</skos:altLabel>
  <skos:altLabel>radio (theory and techniques)</skos:altLabel>
  <skos:altLabel>radio antenna design</skos:altLabel>
  <skos:altLabel>radio antennas (theory and techniques)</skos:altLabel>
  <skos:altLabel>radio communication systems (theory and techniques)</skos:altLabel>
  <skos:altLabel>radomes (design)</skos:altLabel>
  <skos:altLabel>satellite communications (earth communications)</skos:altLabel>
  <skos:altLabel>satellite networks (earth communications)</skos:altLabel>
  <skos:altLabel>side looking radar (theory and techniques)</skos:altLabel>
  <skos:altLabel>signal analyzers</skos:altLabel>
  <skos:altLabel>signal decoding</skos:altLabel>
  <skos:altLabel>signal detection</skos:altLabel>
  <skos:altLabel>signal encoding</skos:altLabel>
  <skos:altLabel>signal generators (theory and techniques)</skos:altLabel>
  <skos:altLabel>signal modulators</skos:altLabel>
  <skos:altLabel>signal processing</skos:altLabel>
  <skos:altLabel>speech analysis (electromagnetic aspects)</skos:altLabel>
  <skos:altLabel>speech data compression (communications)</skos:altLabel>
  <skos:altLabel>synthetic aperture radar</skos:altLabel>
  <skos:altLabel>telemetry (theory and techniques)</skos:altLabel>
  <skos:altLabel>television systems (aerospace applications)</skos:altLabel>
  <skos:altLabel>transmitters (theory and techniques)</skos:altLabel>
  <skos:altLabel>tropospheric scatter (electromagnetic effects)</skos:altLabel>
  <skos:altLabel>voice communications</skos:altLabel>
  <skos:altLabel>wave propagation (electromagnetic)</skos:altLabel>
  <skos:altLabel>whistlers (electromagnetic)</skos:altLabel>
  <skos:broader rdf:resource='subj:1332'/>
  <nt2:status>Approved</nt2:status>
  <nt2:type>Descriptor</nt2:type>
  <nt2:inputdate>2007-01-11</nt2:inputdate>
  <dcterms:dateAccepted>2006-12-01</dcterms:dateAccepted>
  <dcterms:modified>2007-01-11</dcterms:modified>
  <nt2:notValidDate></nt2:notValidDate>
  <nt2:code>32</nt2:code>
 </skos:Concept>
 <skos:Concept rdf:about='subj:29'>
  <skos:prefLabel>Space Processing</skos:prefLabel>
  <skos:scopeNote>Includes space-based development of materials, compounds,
    and processes for research or commercial application. Also
    includes the development of materials and compounds in
    simulated reduced-gravity environments. For legal aspects
    of space commercialization see 84 Law, Political Science
    and Space Policy.
  </skos:scopeNote>
  <skos:altLabel>alloy formation (space processing)</skos:altLabel>
  <skos:altLabel>biological materials (space processing)</skos:altLabel>
  <skos:altLabel>composite material formation (space processing)</skos:altLabel>
  <skos:altLabel>containerless processing</skos:altLabel>
  <skos:altLabel>crystal growth (space processing)</skos:altLabel>
  <skos:altLabel>electrophoresis operations in space (EOS)</skos:altLabel>
  <skos:altLabel>fluids behavior (space processing)</skos:altLabel>
  <skos:altLabel>glass formation (space processing)</skos:altLabel>
  <skos:altLabel>macromolecular crystallography (space processing)</skos:altLabel>
  <skos:altLabel>materials processing in space</skos:altLabel>
  <skos:altLabel>materials separation in space</skos:altLabel>
  <skos:altLabel>microgravity (space processing)</skos:altLabel>
  <skos:altLabel>multiphase materials processing in space</skos:altLabel>
  <skos:altLabel>pharmaceutical preparation (space processing)</skos:altLabel>
  <skos:altLabel>polymers (space processing)</skos:altLabel>
  <skos:altLabel>reduced gravity effects (materials)</skos:altLabel>
  <skos:altLabel>space based equipment for space processing</skos:altLabel>
  <skos:altLabel>space commercialization (space processing)</skos:altLabel>
  <skos:altLabel>space processing of materials</skos:altLabel>
  <skos:broader rdf:resource='subj:1058'/>
  <nt2:status>Approved</nt2:status>
  <nt2:type>Descriptor</nt2:type>
  <nt2:inputdate>2007-01-11</nt2:inputdate>
  <dcterms:dateAccepted>2006-12-01</dcterms:dateAccepted>
  <dcterms:modified>2007-01-11</dcterms:modified>
  <nt2:notValidDate></nt2:notValidDate>
  <nt2:code>29</nt2:code>
 </skos:Concept>
 <skos:Concept rdf:about='subj:31'>
  <skos:prefLabel>Engineering (General)</skos:prefLabel>
  <skos:scopeNote>Includes general research topics related to engineering and
    applied physics, and particular areas of vacuum technology,
    industrial engineering, cryogenics, and fire prevention.
    For specific topics in engineering see categories 32
    through 39.
  </skos:scopeNote>
  <skos:altLabel>applied mechanics</skos:altLabel>
  <skos:altLabel>civil engineering</skos:altLabel>
  <skos:altLabel>computer aided manufacturing</skos:altLabel>
  <skos:altLabel>cryogenics</skos:altLabel>
  <skos:altLabel>display engineering</skos:altLabel>
  <skos:altLabel>fire prevention</skos:altLabel>
  <skos:altLabel>industrial process control</skos:altLabel>
  <skos:altLabel>industrial safety procedures</skos:altLabel>
  <skos:altLabel>liquefied gases (CAM)(Engineering)</skos:altLabel>
  <skos:altLabel>metrication</skos:altLabel>
  <skos:altLabel>metrology</skos:altLabel>
  <skos:altLabel>safety procedures (engineering)</skos:altLabel>
  <skos:altLabel>vacuum technology</skos:altLabel>
  <skos:broader rdf:resource='subj:1332'/>
  <nt2:status>Approved</nt2:status>
  <nt2:type>Descriptor</nt2:type>
  <nt2:inputdate>2007-01-11</nt2:inputdate>
  <dcterms:dateAccepted>2006-12-01</dcterms:dateAccepted>
  <dcterms:modified>2007-01-11</dcterms:modified>
  <nt2:notValidDate></nt2:notValidDate>
  <nt2:code>31</nt2:code>
 </skos:Concept>
 <skos:Concept rdf:about='subj:06'>
  <skos:prefLabel>Avionics and Aircraft Instrumentation</skos:prefLabel>
  <skos:scopeNote>Includes all avionics systems, cockpit and cabin display
    devices, and flight instruments intended for use in
    aircraft. For related information see also 04 Aircraft
    Communications and Navigation; 08 Aircraft Stability and
    Control; 19 Spacecraft Instrumentation and Astrionics; and
    35 Instrumentation and Photography.
  </skos:scopeNote>
  <skos:altLabel>airborne computers</skos:altLabel>
  <skos:altLabel>airborne radar displays</skos:altLabel>
  <skos:altLabel>aircraft control computer systems</skos:altLabel>
  <skos:altLabel>aircraft instrumentation</skos:altLabel>
  <skos:altLabel>aircraft systems monitoring instruments</skos:altLabel>
  <skos:altLabel>airspeed indicators</skos:altLabel>
  <skos:altLabel>alarm systems (aircraft)</skos:altLabel>
  <skos:altLabel>altimeters (aircraft)</skos:altLabel>
  <skos:altLabel>analyzing devices (aircraft)</skos:altLabel>
  <skos:altLabel>anticollision devices</skos:altLabel>
  <skos:altLabel>attitude indicators (aircraft)</skos:altLabel>
  <skos:altLabel>avionics</skos:altLabel>
  <skos:altLabel>blind flying instruments</skos:altLabel>
  <skos:altLabel>cathode ray tubes (aircraft systems)</skos:altLabel>
  <skos:altLabel>cockpit display devices</skos:altLabel>
  <skos:altLabel>compasses</skos:altLabel>
  <skos:altLabel>control position indicators (aircraft)</skos:altLabel>
  <skos:altLabel>detecting devices (aircraft)</skos:altLabel>
  <skos:altLabel>display devices (aircraft)</skos:altLabel>
  <skos:altLabel>engine fuel quantity gages</skos:altLabel>
  <skos:altLabel>engine oil pressure gages</skos:altLabel>
  <skos:altLabel>engine oil temperature gages</skos:altLabel>
  <skos:altLabel>engine propulsion system instruments and gages</skos:altLabel>
  <skos:altLabel>engine RPM indicators</skos:altLabel>
  <skos:altLabel>fire control radar</skos:altLabel>
  <skos:altLabel>fire warning systems</skos:altLabel>
  <skos:altLabel>flight control computer systems</skos:altLabel>
  <skos:altLabel>flight instruments (aircraft)</skos:altLabel>
  <skos:altLabel>flight recorders (aircraft)</skos:altLabel>
  <skos:altLabel>fluid flow sensors (aircraft)</skos:altLabel>
  <skos:altLabel>gyroscopes (aircraft)</skos:altLabel>
  <skos:altLabel>heads-up displays (aircraft)</skos:altLabel>
  <skos:altLabel>horizon sensors (aircraft)</skos:altLabel>
  <skos:altLabel>infrared sensors (aircraft)</skos:altLabel>
  <skos:altLabel>instrument arrangement (aircraft)</skos:altLabel>
  <skos:altLabel>instrument design (aircraft)</skos:altLabel>
  <skos:altLabel>instrument displays (aircraft)</skos:altLabel>
  <skos:altLabel>instrument installation (aircraft)</skos:altLabel>
  <skos:altLabel>instrument landing systems (ILS)</skos:altLabel>
  <skos:altLabel>landing gear position indicators (aircraft)</skos:altLabel>
  <skos:altLabel>laser altimeters (aircraft)</skos:altLabel>
  <skos:altLabel>laser instruments (aircraft)</skos:altLabel>
  <skos:altLabel>Mach meters</skos:altLabel>
  <skos:altLabel>navigation instruments (design and development)</skos:altLabel>
  <skos:altLabel>onboard computer systems for aircraft</skos:altLabel>
  <skos:altLabel>pilot support systems (aircraft)</skos:altLabel>
  <skos:altLabel>position indicators (aircraft)</skos:altLabel>
  <skos:altLabel>power plant instruments and gages (aircraft)</skos:altLabel>
  <skos:altLabel>propulsion system instruments and gages (aircraft)</skos:altLabel>
  <skos:altLabel>rate of climb indicators</skos:altLabel>
  <skos:altLabel>recording devices (aircraft)</skos:altLabel>
  <skos:altLabel>sensors for aircraft equipment and operation</skos:altLabel>
  <skos:altLabel>skin temperature indicators (aircraft)</skos:altLabel>
  <skos:altLabel>stall indicators</skos:altLabel>
  <skos:altLabel>target acquisition</skos:altLabel>
  <skos:altLabel>target-signature modeling (aircraft)</skos:altLabel>
  <skos:altLabel>telemetry devices (aircraft)</skos:altLabel>
  <skos:altLabel>terrain clearance indicators</skos:altLabel>
  <skos:altLabel>turn and bank indicators</skos:altLabel>
  <skos:altLabel>warning systems (aircraft)</skos:altLabel>
  <skos:broader rdf:resource='subj:101'/>
  <nt2:status>Approved</nt2:status>
  <nt2:type>Descriptor</nt2:type>
  <nt2:inputdate>2007-01-11</nt2:inputdate>
  <dcterms:dateAccepted>2006-12-01</dcterms:dateAccepted>
  <dcterms:modified>2007-01-11</dcterms:modified>
  <nt2:notValidDate></nt2:notValidDate>
  <nt2:code>06</nt2:code>
 </skos:Concept>
 <skos:Concept rdf:about='subj:64'>
  <skos:prefLabel>Numerical Analysis</skos:prefLabel>
  <skos:scopeNote>Includes iteration, differential and difference equations,
    and numerical approximation.
  </skos:scopeNote>
  <skos:altLabel>algorithms (mathematics)</skos:altLabel>
  <skos:altLabel>approximation</skos:altLabel>
  <skos:altLabel>boundary value problems</skos:altLabel>
  <skos:altLabel>calculus</skos:altLabel>
  <skos:altLabel>collocation methods</skos:altLabel>
  <skos:altLabel>computational grids</skos:altLabel>
  <skos:altLabel>convergence (mathematics)</skos:altLabel>
  <skos:altLabel>difference equations</skos:altLabel>
  <skos:altLabel>differential equations</skos:altLabel>
  <skos:altLabel>differentiation (mathematics)</skos:altLabel>
  <skos:altLabel>eigenvalues/eigenvectors</skos:altLabel>
  <skos:altLabel>finite difference methods</skos:altLabel>
  <skos:altLabel>finite element methods</skos:altLabel>
  <skos:altLabel>finite volume methods</skos:altLabel>
  <skos:altLabel>fourier analysis</skos:altLabel>
  <skos:altLabel>Galerkin method</skos:altLabel>
  <skos:altLabel>grid refinement (mathematics)</skos:altLabel>
  <skos:altLabel>harmonic analysis (mathematics)</skos:altLabel>
  <skos:altLabel>integral equations</skos:altLabel>
  <skos:altLabel>iteration</skos:altLabel>
  <skos:altLabel>mathematical analysis</skos:altLabel>
  <skos:altLabel>matrices</skos:altLabel>
  <skos:altLabel>mesh refinement (mathematics)</skos:altLabel>
  <skos:altLabel>multigrid methods</skos:altLabel>
  <skos:altLabel>numerical integration</skos:altLabel>
  <skos:altLabel>perturbation theory (mathematics)</skos:altLabel>
  <skos:altLabel>Rayleigh-Ritz method</skos:altLabel>
  <skos:altLabel>Runge-Kutta method</skos:altLabel>
  <skos:altLabel>spectral methods (mathematics)</skos:altLabel>
  <skos:altLabel>spline functions</skos:altLabel>
  <skos:altLabel>variational methods</skos:altLabel>
  <skos:broader rdf:resource='subj:2321'/>
  <nt2:status>Approved</nt2:status>
  <nt2:type>Descriptor</nt2:type>
  <nt2:inputdate>2007-01-11</nt2:inputdate>
  <dcterms:dateAccepted>2006-12-01</dcterms:dateAccepted>
  <dcterms:modified>2007-01-11</dcterms:modified>
  <nt2:notValidDate></nt2:notValidDate>
  <nt2:code>64</nt2:code>
 </skos:Concept>
 <skos:Concept rdf:about='subj:99'>
  <skos:prefLabel>General.</skos:prefLabel>
  <skos:scopeNote>Includes aeronautical, astronautical, and space science
    related histories, biographies, and pertinent reports too
    broad for categorization; histories or broad overviews of
    NASA programs such as Apollo, Gemini, and Mercury
    spacecraft, Earth Resources Technology Satellite (ERTS),
    and Skylab; NASA appropriations hearings.
  </skos:scopeNote>
  <skos:altLabel>aeronautical history</skos:altLabel>
  <skos:altLabel>appropriations hearings (NASA)</skos:altLabel>
  <skos:altLabel>astronautical history</skos:altLabel>
  <skos:altLabel>biographies of astronauts, aviation pioneers, pilots, and</skos:altLabel>
  <skos:altLabel>scientists</skos:altLabel>
  <skos:altLabel>histories of aeronautics and space programs</skos:altLabel>
  <skos:broader rdf:resource='subj:3056'/>
  <nt2:status>Approved</nt2:status>
  <nt2:type>Descriptor</nt2:type>
  <nt2:inputdate>2007-01-11</nt2:inputdate>
  <dcterms:dateAccepted>2006-12-01</dcterms:dateAccepted>
  <dcterms:modified>2007-01-11</dcterms:modified>
  <nt2:notValidDate></nt2:notValidDate>
  <nt2:code>99</nt2:code>
 </skos:Concept>
 <skos:Concept rdf:about='subj:66'>
  <skos:prefLabel>Systems Analysis and Operations Research</skos:prefLabel>
  <skos:scopeNote>Includes mathematical modeling of systems; network
    analysis; mathematical programming; decision theory; and
    game theory.
  </skos:scopeNote>
  <skos:altLabel>decision theory</skos:altLabel>
  <skos:altLabel>dynamic programming</skos:altLabel>
  <skos:altLabel>game theory</skos:altLabel>
  <skos:altLabel>linear programming</skos:altLabel>
  <skos:altLabel>mathematical modeling (systems analysis)</skos:altLabel>
  <skos:altLabel>mathematical programming</skos:altLabel>
  <skos:altLabel>network analysis</skos:altLabel>
  <skos:altLabel>operations research</skos:altLabel>
  <skos:altLabel>optimization (mathematics)</skos:altLabel>
  <skos:altLabel>queueing theory</skos:altLabel>
  <skos:altLabel>systems analysis</skos:altLabel>
  <skos:broader rdf:resource='subj:2321'/>
  <nt2:status>Approved</nt2:status>
  <nt2:type>Descriptor</nt2:type>
  <nt2:inputdate>2007-01-11</nt2:inputdate>
  <dcterms:dateAccepted>2006-12-01</dcterms:dateAccepted>
  <dcterms:modified>2007-01-11</dcterms:modified>
  <nt2:notValidDate></nt2:notValidDate>
  <nt2:code>66</nt2:code>
 </skos:Concept>
 <skos:Concept rdf:about='subj:74'>
  <skos:prefLabel>Optics</skos:prefLabel>
  <skos:scopeNote>Includes light phenomena and the theory of optical devices.
    For lasers see 36 Lasers and Masers.
  </skos:scopeNote>
  <skos:altLabel>Bragg cells (optical applications)</skos:altLabel>
  <skos:altLabel>Cassegrain optics</skos:altLabel>
  <skos:altLabel>coherent light</skos:altLabel>
  <skos:altLabel>electron optics theory</skos:altLabel>
  <skos:altLabel>fiber optics</skos:altLabel>
  <skos:altLabel>geometrical optics</skos:altLabel>
  <skos:altLabel>infrared optics</skos:altLabel>
  <skos:altLabel>infrared radiation effects (optical applications)</skos:altLabel>
  <skos:altLabel>infrared signatures (optical applications)</skos:altLabel>
  <skos:altLabel>infrared spectra</skos:altLabel>
  <skos:altLabel>lens theory</skos:altLabel>
  <skos:altLabel>lenses (optical properties)</skos:altLabel>
  <skos:altLabel>light absorption</skos:altLabel>
  <skos:altLabel>light reflection</skos:altLabel>
  <skos:altLabel>light scattering</skos:altLabel>
  <skos:altLabel>light transmission</skos:altLabel>
  <skos:altLabel>liquid optics</skos:altLabel>
  <skos:altLabel>luminescence (optics)</skos:altLabel>
  <skos:altLabel>mirror interference (optics)</skos:altLabel>
  <skos:altLabel>modulation (optics)</skos:altLabel>
  <skos:altLabel>nonlinear optics</skos:altLabel>
  <skos:altLabel>optical bistability</skos:altLabel>
  <skos:altLabel>optical coatings</skos:altLabel>
  <skos:altLabel>optical communications (theory)</skos:altLabel>
  <skos:altLabel>optical fibers</skos:altLabel>
  <skos:altLabel>optical imaging devices (theory)</skos:altLabel>
  <skos:altLabel>optical materials</skos:altLabel>
  <skos:altLabel>optical properties</skos:altLabel>
  <skos:altLabel>optical waveguides</skos:altLabel>
  <skos:altLabel>optoelectronics (optics)</skos:altLabel>
  <skos:altLabel>photon beams</skos:altLabel>
  <skos:altLabel>photonics</skos:altLabel>
  <skos:altLabel>polarization (optics)</skos:altLabel>
  <skos:altLabel>refraction (optics)</skos:altLabel>
  <skos:altLabel>Schlieren optics</skos:altLabel>
  <skos:altLabel>telescopes (optical properties)</skos:altLabel>
  <skos:altLabel>tomography (optics)</skos:altLabel>
  <skos:altLabel>ultraviolet radiation (optics)</skos:altLabel>
  <skos:altLabel>wave propagation (optics)</skos:altLabel>
  <skos:altLabel>x-ray optics</skos:altLabel>
  <skos:broader rdf:resource='subj:2528'/>
  <nt2:status>Approved</nt2:status>
  <nt2:type>Descriptor</nt2:type>
  <nt2:inputdate>2007-01-11</nt2:inputdate>
  <dcterms:dateAccepted>2006-12-01</dcterms:dateAccepted>
  <dcterms:modified>2007-01-11</dcterms:modified>
  <nt2:notValidDate></nt2:notValidDate>
  <nt2:code>74</nt2:code>
 </skos:Concept>
 <skos:Concept rdf:about='subj:73'>
  <skos:prefLabel>Nuclear Physics</skos:prefLabel>
  <skos:scopeNote>Includes nuclear particles; and reactor theory. For space
    radiation see 93 Space Radiation. For atomic and molecular
    physics see 72 Atomic and Molecular Physics. For elementary
    particle physics see 77 Physics of Elementary Particles and
    Fields. For nuclear astrophysics see 90 Astrophysics.
  </skos:scopeNote>
  <skos:altLabel>alpha rays (theory)</skos:altLabel>
  <skos:altLabel>beta rays (theory)</skos:altLabel>
  <skos:altLabel>electron beams</skos:altLabel>
  <skos:altLabel>gamma rays (theory)</skos:altLabel>
  <skos:altLabel>ion beams (nuclear interactions)</skos:altLabel>
  <skos:altLabel>nuclear decay</skos:altLabel>
  <skos:altLabel>nuclear engines (theory)</skos:altLabel>
  <skos:altLabel>nuclear fission</skos:altLabel>
  <skos:altLabel>nuclear fuels</skos:altLabel>
  <skos:altLabel>nuclear fusion (theory)</skos:altLabel>
  <skos:altLabel>nuclear magnetic resonance</skos:altLabel>
  <skos:altLabel>nuclear particles</skos:altLabel>
  <skos:altLabel>nuclear power sources (theory)</skos:altLabel>
  <skos:altLabel>nuclear propulsion systems (theory)</skos:altLabel>
  <skos:altLabel>nuclear reactions</skos:altLabel>
  <skos:altLabel>nuclear reactor theory</skos:altLabel>
  <skos:altLabel>nuclear reactors</skos:altLabel>
  <skos:altLabel>nuclear research equipment</skos:altLabel>
  <skos:altLabel>nuclear scattering</skos:altLabel>
  <skos:altLabel>nuclear structure</skos:altLabel>
  <skos:altLabel>nuclear test equipment</skos:altLabel>
  <skos:altLabel>proton beams (nuclear interactions)</skos:altLabel>
  <skos:altLabel>radioisotopes</skos:altLabel>
  <skos:altLabel>reactor radiation safety measures (space applications)</skos:altLabel>
  <skos:altLabel>reactor theory</skos:altLabel>
  <skos:altLabel>space-power reactors (theory)</skos:altLabel>
  <skos:altLabel>x-ray radiation (theory)</skos:altLabel>
  <skos:broader rdf:resource='subj:2528'/>
  <nt2:status>Approved</nt2:status>
  <nt2:type>Descriptor</nt2:type>
  <nt2:inputdate>2007-01-11</nt2:inputdate>
  <dcterms:dateAccepted>2006-12-01</dcterms:dateAccepted>
  <dcterms:modified>2007-01-11</dcterms:modified>
  <nt2:notValidDate></nt2:notValidDate>
  <nt2:code>73</nt2:code>
 </skos:Concept>
 <skos:Concept rdf:about='subj:63'>
  <skos:prefLabel>Cybernetics, Artificial Intelligence and Robotics</skos:prefLabel>
  <skos:scopeNote>Includes feedback and control theory, information theory,
    machine learning, and expert systems. For related
    information see also 54 Man/System Technology and Life
    Support.
  </skos:scopeNote>
  <skos:altLabel>adaptive control theory</skos:altLabel>
  <skos:altLabel>artificial intelligence</skos:altLabel>
  <skos:altLabel>automata theory</skos:altLabel>
  <skos:altLabel>automatic control optimal control</skos:altLabel>
  <skos:altLabel>computer vision</skos:altLabel>
  <skos:altLabel>control systems design</skos:altLabel>
  <skos:altLabel>control theory</skos:altLabel>
  <skos:altLabel>cybernetics</skos:altLabel>
  <skos:altLabel>expert systems</skos:altLabel>
  <skos:altLabel>feed forward control</skos:altLabel>
  <skos:altLabel>feedback control</skos:altLabel>
  <skos:altLabel>filter theory (control)</skos:altLabel>
  <skos:altLabel>information theory</skos:altLabel>
  <skos:altLabel>knowledge based systems</skos:altLabel>
  <skos:altLabel>knowledge representation</skos:altLabel>
  <skos:altLabel>machine learning</skos:altLabel>
  <skos:altLabel>model order reduction (control theory)</skos:altLabel>
  <skos:altLabel>multivariable control</skos:altLabel>
  <skos:altLabel>neural networks</skos:altLabel>
  <skos:altLabel>pattern recognition</skos:altLabel>
  <skos:altLabel>remote manipulator arms (robotics)</skos:altLabel>
  <skos:altLabel>robot control</skos:altLabel>
  <skos:altLabel>robot dynamics</skos:altLabel>
  <skos:altLabel>robot sensors</skos:altLabel>
  <skos:altLabel>robot vision</skos:altLabel>
  <skos:altLabel>robotics</skos:altLabel>
  <skos:altLabel>scene analysis (robotics)</skos:altLabel>
  <skos:altLabel>speech recognition</skos:altLabel>
  <skos:altLabel>support vector machines</skos:altLabel>
  <skos:altLabel>teleoperators (robotics)</skos:altLabel>
  <skos:broader rdf:resource='subj:2321'/>
  <nt2:status>Approved</nt2:status>
  <nt2:type>Descriptor</nt2:type>
  <nt2:inputdate>2007-01-11</nt2:inputdate>
  <dcterms:dateAccepted>2006-12-01</dcterms:dateAccepted>
  <dcterms:modified>2007-01-11</dcterms:modified>
  <nt2:notValidDate></nt2:notValidDate>
  <nt2:code>63</nt2:code>
 </skos:Concept>
 <skos:Concept rdf:about='subj:2767'>
  <skos:prefLabel>Social and Information Sciences</skos:prefLabel>
  <skos:scopeNote>Includes social and information sciences (general);
    administration and management; documentation and
    information science; economics and cost analysis; law,
    political science, and space policy; and technology
    utilization and surface transportation.
  </skos:scopeNote>
  <skos:broader rdf:resource='subj:100'/>
  <skos:narrower rdf:resource='subj:81'/>
  <skos:narrower rdf:resource='subj:82'/>
  <skos:narrower rdf:resource='subj:83'/>
  <skos:narrower rdf:resource='subj:84'/>
  <skos:narrower rdf:resource='subj:80'/>
  <skos:narrower rdf:resource='subj:85'/>
  <nt2:status>Approved</nt2:status>
  <nt2:type>Descriptor</nt2:type>
  <nt2:inputdate>2007-01-11</nt2:inputdate>
  <dcterms:dateAccepted>2006-12-01</dcterms:dateAccepted>
  <dcterms:modified>2007-01-11</dcterms:modified>
  <nt2:notValidDate></nt2:notValidDate>
  <nt2:code>2767</nt2:code>
 </skos:Concept>
 <skos:Concept rdf:about='subj:59'>
  <skos:prefLabel>Mathematical and Computer Sciences (General)</skos:prefLabel>
  <skos:scopeNote>Includes general topics and overviews related to
    mathematics and computer science. For specific topics in
    these areas see categories 60 through 67.
  </skos:scopeNote>
  <skos:altLabel>computer sciences (general)</skos:altLabel>
  <skos:altLabel>mathematical sciences (general)</skos:altLabel>
  <skos:broader rdf:resource='subj:2321'/>
  <nt2:status>Approved</nt2:status>
  <nt2:type>Descriptor</nt2:type>
  <nt2:inputdate>2007-01-11</nt2:inputdate>
  <dcterms:dateAccepted>2006-12-01</dcterms:dateAccepted>
  <dcterms:modified>2007-01-11</dcterms:modified>
  <nt2:notValidDate></nt2:notValidDate>
  <nt2:code>59</nt2:code>
 </skos:Concept>
 <skos:Concept rdf:about='subj:1332'>
  <skos:prefLabel>Engineering</skos:prefLabel>
  <skos:scopeNote>Includes engineering (general); communications and radar;
    electronics and electrical engineering; fluid mechanics and
    thermodynamics; instrumentation and photography; lasers and
    masers; mechanical engineering; quality assurance and
    reliability; and structural mechanics. For related
    information see also Physics (categories 70 through 77).
  </skos:scopeNote>
  <skos:broader rdf:resource='subj:100'/>
  <skos:narrower rdf:resource='subj:32'/>
  <skos:narrower rdf:resource='subj:33'/>
  <skos:narrower rdf:resource='subj:31'/>
  <skos:narrower rdf:resource='subj:34'/>
  <skos:narrower rdf:resource='subj:35'/>
  <skos:narrower rdf:resource='subj:36'/>
  <skos:narrower rdf:resource='subj:37'/>
  <skos:narrower rdf:resource='subj:38'/>
  <skos:narrower rdf:resource='subj:39'/>
  <nt2:status>Approved</nt2:status>
  <nt2:type>Descriptor</nt2:type>
  <nt2:inputdate>2007-01-11</nt2:inputdate>
  <dcterms:dateAccepted>2006-12-01</dcterms:dateAccepted>
  <dcterms:modified>2007-01-11</dcterms:modified>
  <nt2:notValidDate></nt2:notValidDate>
  <nt2:code>1332</nt2:code>
 </skos:Concept>
 <skos:Concept rdf:about='subj:23'>
  <skos:prefLabel>Chemistry and Materials (General)</skos:prefLabel>
  <skos:scopeNote>Includes general research topics related to the
    composition, properties, structure, and use of chemical
    compounds and materials as they relate to aircraft, launch
    vehicles, and spacecraft. For specific topics in chemistry
    and materials see categories 24 through 29. For
    astrochemistry see category 90 Astrophysics.
  </skos:scopeNote>
  <skos:altLabel>chemical analysis techniques</skos:altLabel>
  <skos:altLabel>chemical manufacturing</skos:altLabel>
  <skos:altLabel>chemical processing (general)</skos:altLabel>
  <skos:altLabel>chemistry (general)</skos:altLabel>
  <skos:altLabel>materials (general)</skos:altLabel>
  <skos:altLabel>separations chemistry</skos:altLabel>
  <skos:altLabel>spectroscopic analysis (chemistry)</skos:altLabel>
  <skos:broader rdf:resource='subj:1058'/>
  <nt2:status>Approved</nt2:status>
  <nt2:type>Descriptor</nt2:type>
  <nt2:inputdate>2007-01-11</nt2:inputdate>
  <dcterms:dateAccepted>2006-12-01</dcterms:dateAccepted>
  <dcterms:modified>2007-01-11</dcterms:modified>
  <nt2:notValidDate></nt2:notValidDate>
  <nt2:code>23</nt2:code>
 </skos:Concept>
 <skos:Concept rdf:about='subj:62'>
  <skos:prefLabel>Computer Systems</skos:prefLabel>
  <skos:scopeNote>Includes computer networks and distributed processing
    systems. For information systems see 82 Documentation and
    Information Science. For computer systems applied to
    specific applications, see the associated category.
  </skos:scopeNote>
  <skos:altLabel>communications computer systems</skos:altLabel>
  <skos:altLabel>computer networks</skos:altLabel>
  <skos:altLabel>computer systems engineering</skos:altLabel>
  <skos:altLabel>computer time sharing</skos:altLabel>
  <skos:altLabel>data compilation systems</skos:altLabel>
  <skos:altLabel>data management systems</skos:altLabel>
  <skos:altLabel>data processing systems</skos:altLabel>
  <skos:altLabel>distributed data processing</skos:altLabel>
  <skos:altLabel>internets</skos:altLabel>
  <skos:altLabel>local area networks (LAN)</skos:altLabel>
  <skos:altLabel>parallel processing</skos:altLabel>
  <skos:altLabel>self-repairing computer systems</skos:altLabel>
  <skos:altLabel>wide area networks (WAN)</skos:altLabel>
  <skos:broader rdf:resource='subj:2321'/>
  <nt2:status>Approved</nt2:status>
  <nt2:type>Descriptor</nt2:type>
  <nt2:inputdate>2007-01-11</nt2:inputdate>
  <dcterms:dateAccepted>2006-12-01</dcterms:dateAccepted>
  <dcterms:modified>2007-01-11</dcterms:modified>
  <nt2:notValidDate></nt2:notValidDate>
  <nt2:code>62</nt2:code>
 </skos:Concept>
 <skos:Concept rdf:about='subj:48'>
  <skos:prefLabel>Oceanography</skos:prefLabel>
  <skos:scopeNote>Includes the physical, chemical and biological aspects of
    oceans and seas; ocean dynamics; and marine resources. For
    related information see also 43 Earth Resources and Remote
    Sensing.
  </skos:scopeNote>
  <skos:altLabel>air-sea interactions</skos:altLabel>
  <skos:altLabel>biological oceanography</skos:altLabel>
  <skos:altLabel>biosphere (oceanography)</skos:altLabel>
  <skos:altLabel>chlorophyll concentration</skos:altLabel>
  <skos:altLabel>dynamic oceanography</skos:altLabel>
  <skos:altLabel>general circulation models (ocean)</skos:altLabel>
  <skos:altLabel>marine biology</skos:altLabel>
  <skos:altLabel>marine resources</skos:altLabel>
  <skos:altLabel>ocean circulation</skos:altLabel>
  <skos:altLabel>ocean currents</skos:altLabel>
  <skos:altLabel>ocean floor studies</skos:altLabel>
  <skos:altLabel>ocean wave studies</skos:altLabel>
  <skos:altLabel>physical oceanography</skos:altLabel>
  <skos:altLabel>phytoplankton concentration</skos:altLabel>
  <skos:altLabel>salinity (oceanography)</skos:altLabel>
  <skos:altLabel>sea ice</skos:altLabel>
  <skos:altLabel>sea water</skos:altLabel>
  <skos:altLabel>sediments (oceanography)</skos:altLabel>
  <skos:altLabel>swash zone (oceanography)</skos:altLabel>
  <skos:altLabel>temperature variations (oceanography)</skos:altLabel>
  <skos:altLabel>thermoclines (oceanography)</skos:altLabel>
  <skos:altLabel>wave phenomena (oceanography)</skos:altLabel>
  <skos:broader rdf:resource='subj:1874'/>
  <nt2:status>Approved</nt2:status>
  <nt2:type>Descriptor</nt2:type>
  <nt2:inputdate>2007-01-11</nt2:inputdate>
  <dcterms:dateAccepted>2006-12-01</dcterms:dateAccepted>
  <dcterms:modified>2007-01-11</dcterms:modified>
  <nt2:notValidDate></nt2:notValidDate>
  <nt2:code>48</nt2:code>
 </skos:Concept>
 <skos:Concept rdf:about='subj:37'>
  <skos:prefLabel>Mechanical Engineering</skos:prefLabel>
  <skos:scopeNote>Includes mechanical devices and equipment; machine elements
    and processes. For cases where the application of a device
    or the host vehicle is emphasized see also the specific
    category where the application or vehicle is treated. For
    robotics see 63 Cybernetics, Artificial Intelligence, and
    Robotics; and 54 Man/System Technology and Life Support.
  </skos:scopeNote>
  <skos:altLabel>airbreathing engines (non-aircraft)</skos:altLabel>
  <skos:altLabel>auxiliary systems (mechanical)</skos:altLabel>
  <skos:altLabel>bearings</skos:altLabel>
  <skos:altLabel>bonding</skos:altLabel>
  <skos:altLabel>Brayton cycle turbines (mechanical engineering)</skos:altLabel>
  <skos:altLabel>brazing</skos:altLabel>
  <skos:altLabel>cams</skos:altLabel>
  <skos:altLabel>centrifugal compressors (non-aircraft)</skos:altLabel>
  <skos:altLabel>centrifugal pumps</skos:altLabel>
  <skos:altLabel>ceramic engines</skos:altLabel>
  <skos:altLabel>cladding</skos:altLabel>
  <skos:altLabel>clutches</skos:altLabel>
  <skos:altLabel>coatings</skos:altLabel>
  <skos:altLabel>compression ignition engines (non-aircraft)</skos:altLabel>
  <skos:altLabel>containers</skos:altLabel>
  <skos:altLabel>dies</skos:altLabel>
  <skos:altLabel>diesel engines (non-aircraft)</skos:altLabel>
  <skos:altLabel>drives</skos:altLabel>
  <skos:altLabel>electrodeposition</skos:altLabel>
  <skos:altLabel>electron beam welding</skos:altLabel>
  <skos:altLabel>electroplating</skos:altLabel>
  <skos:altLabel>fasteners</skos:altLabel>
  <skos:altLabel>filters (mechanical)</skos:altLabel>
  <skos:altLabel>fittings</skos:altLabel>
  <skos:altLabel>fixtures</skos:altLabel>
  <skos:altLabel>flywheels</skos:altLabel>
  <skos:altLabel>friction measurement</skos:altLabel>
  <skos:altLabel>friction phenomena</skos:altLabel>
  <skos:altLabel>friction stir welding</skos:altLabel>
  <skos:altLabel>friction welding</skos:altLabel>
  <skos:altLabel>gaskets</skos:altLabel>
  <skos:altLabel>gasoline engines (non-aircraft)</skos:altLabel>
  <skos:altLabel>gears</skos:altLabel>
  <skos:altLabel>grinding</skos:altLabel>
  <skos:altLabel>heat pumps</skos:altLabel>
  <skos:altLabel>heating, ventilation, and air conditioning (HVAC)</skos:altLabel>
  <skos:altLabel>hydraulic systems (general)</skos:altLabel>
  <skos:altLabel>impact phenomena</skos:altLabel>
  <skos:altLabel>impact testing</skos:altLabel>
  <skos:altLabel>internal combustion engines (non-aircraft)</skos:altLabel>
  <skos:altLabel>joining</skos:altLabel>
  <skos:altLabel>laser welding</skos:altLabel>
  <skos:altLabel>lubrication</skos:altLabel>
  <skos:altLabel>machine elements</skos:altLabel>
  <skos:altLabel>machine processes</skos:altLabel>
  <skos:altLabel>machinery</skos:altLabel>
  <skos:altLabel>machining</skos:altLabel>
  <skos:altLabel>manufacturing processes</skos:altLabel>
  <skos:altLabel>materials fabrication</skos:altLabel>
  <skos:altLabel>materials forming</skos:altLabel>
  <skos:altLabel>materials handling</skos:altLabel>
  <skos:altLabel>materials manufacturing</skos:altLabel>
  <skos:altLabel>mechanical equipment</skos:altLabel>
  <skos:altLabel>mechanics (practical)</skos:altLabel>
  <skos:altLabel>metal forming</skos:altLabel>
  <skos:altLabel>micromachining</skos:altLabel>
  <skos:altLabel>mounts (supports)</skos:altLabel>
  <skos:altLabel>nanodevices (mechanical)</skos:altLabel>
  <skos:altLabel>packaging</skos:altLabel>
  <skos:altLabel>packing (machine elements)</skos:altLabel>
  <skos:altLabel>piston engines (non-aircraft)</skos:altLabel>
  <skos:altLabel>plasma spraying</skos:altLabel>
  <skos:altLabel>plating</skos:altLabel>
  <skos:altLabel>pneumatic systems (general)</skos:altLabel>
  <skos:altLabel>powertrains</skos:altLabel>
  <skos:altLabel>pressure vessels</skos:altLabel>
  <skos:altLabel>pumps (non-aircraft)</skos:altLabel>
  <skos:altLabel>reaction wheels</skos:altLabel>
  <skos:altLabel>reciprocating engines (non-aircraft)</skos:altLabel>
  <skos:altLabel>refrigeration</skos:altLabel>
  <skos:altLabel>robotics (hardware)</skos:altLabel>
  <skos:altLabel>rollers</skos:altLabel>
  <skos:altLabel>rotary engines (non-aircraft)</skos:altLabel>
  <skos:altLabel>seals (stoppers)</skos:altLabel>
  <skos:altLabel>servomechanisms (mechanical aspects)</skos:altLabel>
  <skos:altLabel>shafts (machine elements)</skos:altLabel>
  <skos:altLabel>spark ignition engines (non-aircraft)</skos:altLabel>
  <skos:altLabel>springs (mechanical)</skos:altLabel>
  <skos:altLabel>Stirling cycle engines (non-aircraft)</skos:altLabel>
  <skos:altLabel>throttle controls (non-aircraft)</skos:altLabel>
  <skos:altLabel>tools</skos:altLabel>
  <skos:altLabel>tribology</skos:altLabel>
  <skos:altLabel>turbine engines (non-aircraft)</skos:altLabel>
  <skos:altLabel>vacuum forming</skos:altLabel>
  <skos:altLabel>valves</skos:altLabel>
  <skos:altLabel>welding techniques</skos:altLabel>
  <skos:broader rdf:resource='subj:1332'/>
  <nt2:status>Approved</nt2:status>
  <nt2:type>Descriptor</nt2:type>
  <nt2:inputdate>2007-01-11</nt2:inputdate>
  <dcterms:dateAccepted>2006-12-01</dcterms:dateAccepted>
  <dcterms:modified>2007-01-11</dcterms:modified>
  <nt2:notValidDate></nt2:notValidDate>
  <nt2:code>37</nt2:code>
 </skos:Concept>
 <skos:Concept rdf:about='subj:04'>
  <skos:prefLabel>Aircraft Communications and Navigation</skos:prefLabel>
  <skos:scopeNote>Includes all modes of communication with and between
    aircraft; air navigation systems (satellite and ground
    based); and air traffic control. For related information
    see also 06 Avionics and Aircraft Instrumentation; 17 Space
    Communications, Spacecraft Communications, Command and
    Tracking; and 32 Communications and Radar.
  </skos:scopeNote>
  <skos:altLabel>air navigation</skos:altLabel>
  <skos:altLabel>air traffic control</skos:altLabel>
  <skos:altLabel>aircraft command and control</skos:altLabel>
  <skos:altLabel>aircraft communications</skos:altLabel>
  <skos:altLabel>aircraft tracking</skos:altLabel>
  <skos:altLabel>air-sea navigation</skos:altLabel>
  <skos:altLabel>all weather global position determination</skos:altLabel>
  <skos:altLabel>approach control (aircraft)</skos:altLabel>
  <skos:altLabel>celestial navigation (aircraft)</skos:altLabel>
  <skos:altLabel>collision avoidance (aircraft control)</skos:altLabel>
  <skos:altLabel>communications networks (aircraft)</skos:altLabel>
  <skos:altLabel>communications system (aircraft)</skos:altLabel>
  <skos:altLabel>Consol/Consolan navigation system</skos:altLabel>
  <skos:altLabel>Decca navigation system</skos:altLabel>
  <skos:altLabel>digital communications systems (aircraft)</skos:altLabel>
  <skos:altLabel>Doppler navigation systems</skos:altLabel>
  <skos:altLabel>electromagnetic devices (radiators, sensors and other</skos:altLabel>
  <skos:altLabel>equipment) for navigation systems</skos:altLabel>
  <skos:altLabel>global positioning systems (aircraft)</skos:altLabel>
  <skos:altLabel>ground based and space based radar for air navigation</skos:altLabel>
  <skos:altLabel>ground control approach (GCA) systems</skos:altLabel>
  <skos:altLabel>guidance system design (aircraft)</skos:altLabel>
  <skos:altLabel>inertial navigation systems (aircraft)</skos:altLabel>
  <skos:altLabel>inertial sensors and measurement units (aircraft)</skos:altLabel>
  <skos:altLabel>instrument navigation systems</skos:altLabel>
  <skos:altLabel>ionospheric effects on radio transmission (aircraft)</skos:altLabel>
  <skos:altLabel>laser communications systems (aircraft)</skos:altLabel>
  <skos:altLabel>laser tracking systems (aircraft)</skos:altLabel>
  <skos:altLabel>Long Range Navigation System (LORAN)</skos:altLabel>
  <skos:altLabel>man-machine communications (aircraft)</skos:altLabel>
  <skos:altLabel>microwave communications systems (aircraft)</skos:altLabel>
  <skos:altLabel>Microwave Landing System (MLS)</skos:altLabel>
  <skos:altLabel>microwave receivers (aircraft)</skos:altLabel>
  <skos:altLabel>microwave transmitters (aircraft)</skos:altLabel>
  <skos:altLabel>navigation computer systems (aircraft)</skos:altLabel>
  <skos:altLabel>navigation display devices (aircraft)</skos:altLabel>
  <skos:altLabel>navigation system design (aircraft)</skos:altLabel>
  <skos:altLabel>navigation systems (aircraft)</skos:altLabel>
  <skos:altLabel>Omega navigation system</skos:altLabel>
  <skos:altLabel>Omnidirectional Radio Range System (OMNI)</skos:altLabel>
  <skos:altLabel>passive sensors, trackers, and references (aircraft)</skos:altLabel>
  <skos:altLabel>radar communications systems (aircraft)</skos:altLabel>
  <skos:altLabel>radar detection (aircraft navigation)</skos:altLabel>
  <skos:altLabel>radar imagery (aircraft navigation)</skos:altLabel>
  <skos:altLabel>radar tracking systems (aircraft)</skos:altLabel>
  <skos:altLabel>radio communications system (aircraft)</skos:altLabel>
  <skos:altLabel>range and angle measurement (aircraft)</skos:altLabel>
  <skos:altLabel>sea navigation (aircraft related)</skos:altLabel>
  <skos:altLabel>speech analysis (aircraft voice communication)</skos:altLabel>
  <skos:altLabel>speech compression (aircraft voice communication)</skos:altLabel>
  <skos:altLabel>systems for adverse weather avoidance</skos:altLabel>
  <skos:altLabel>systems for collision avoidance</skos:altLabel>
  <skos:altLabel>TACAN</skos:altLabel>
  <skos:altLabel>telemetry (aircraft applications)</skos:altLabel>
  <skos:altLabel>terrain avoidance systems</skos:altLabel>
  <skos:altLabel>terrain following</skos:altLabel>
  <skos:altLabel>tropospheric scatter (aircraft communications/ navigation</skos:altLabel>
  <skos:altLabel>disruption)</skos:altLabel>
  <skos:altLabel>very high frequency omnirange (VOR) navigation</skos:altLabel>
  <skos:altLabel>voice communications systems (aircraft)</skos:altLabel>
  <skos:altLabel>wave propagation (aircraft communications effects)</skos:altLabel>
  <skos:broader rdf:resource='subj:101'/>
  <nt2:status>Approved</nt2:status>
  <nt2:type>Descriptor</nt2:type>
  <nt2:inputdate>2007-01-11</nt2:inputdate>
  <dcterms:dateAccepted>2006-12-01</dcterms:dateAccepted>
  <dcterms:modified>2007-01-11</dcterms:modified>
  <nt2:notValidDate></nt2:notValidDate>
  <nt2:code>04</nt2:code>
 </skos:Concept>
 <skos:Concept rdf:about='subj:71'>
  <skos:prefLabel>Acoustics</skos:prefLabel>
  <skos:scopeNote>Includes sound generation, transmission, and attenuation.
    For noise pollution see 45 Environment Pollution. For
    aircraft noise see also 02 Aerodynamics; and 07 Aircraft
    Propulsion and Power.
  </skos:scopeNote>
  <skos:altLabel>acoustic scattering</skos:altLabel>
  <skos:altLabel>acoustic theory</skos:altLabel>
  <skos:altLabel>acoustics (general)</skos:altLabel>
  <skos:altLabel>aeroacoustics</skos:altLabel>
  <skos:altLabel>aerodynamic noise (general)</skos:altLabel>
  <skos:altLabel>Doppler effect (acoustics)</skos:altLabel>
  <skos:altLabel>noise attenuation</skos:altLabel>
  <skos:altLabel>noise generation</skos:altLabel>
  <skos:altLabel>noise measurement</skos:altLabel>
  <skos:altLabel>noise propagation</skos:altLabel>
  <skos:altLabel>noise reduction (general)</skos:altLabel>
  <skos:altLabel>sodar (sound detection and ranging)</skos:altLabel>
  <skos:altLabel>sonic boom (theory)</skos:altLabel>
  <skos:altLabel>sound absorption</skos:altLabel>
  <skos:altLabel>sound attenuation</skos:altLabel>
  <skos:altLabel>sound generation</skos:altLabel>
  <skos:altLabel>sound generation in ducts</skos:altLabel>
  <skos:altLabel>sound propagation</skos:altLabel>
  <skos:altLabel>sound transmission</skos:altLabel>
  <skos:altLabel>surface acoustic wave devices (theory)</skos:altLabel>
  <skos:altLabel>ultrasonic applications</skos:altLabel>
  <skos:altLabel>ultrasonic theory</skos:altLabel>
  <skos:altLabel>underwater acoustics</skos:altLabel>
  <skos:altLabel>wave propagation (acoustic)</skos:altLabel>
  <skos:broader rdf:resource='subj:2528'/>
  <nt2:status>Approved</nt2:status>
  <nt2:type>Descriptor</nt2:type>
  <nt2:inputdate>2007-01-11</nt2:inputdate>
  <dcterms:dateAccepted>2006-12-01</dcterms:dateAccepted>
  <dcterms:modified>2007-01-11</dcterms:modified>
  <nt2:notValidDate></nt2:notValidDate>
  <nt2:code>71</nt2:code>
 </skos:Concept>
 <skos:Concept rdf:about='subj:35'>
  <skos:prefLabel>Instrumentation and Photography</skos:prefLabel>
  <skos:scopeNote>Includes remote sensors; measuring instruments and gages;
    detectors; cameras and photographic supplies; and
    holography. For aerial photography see 43 Earth Resources
    and Remote Sensing. For related information see also 06
    Avionics and Aircraft Instrumentation; and 19 Spacecraft
    Instrumentation.
  </skos:scopeNote>
  <skos:altLabel>ablation sensors (design and techniques)</skos:altLabel>
  <skos:altLabel>accelerometers</skos:altLabel>
  <skos:altLabel>alarm systems (design and techniques)</skos:altLabel>
  <skos:altLabel>analyzing devices (design and techniques)</skos:altLabel>
  <skos:altLabel>anemometers (design and techniques)</skos:altLabel>
  <skos:altLabel>atomic clocks (design and techniques)</skos:altLabel>
  <skos:altLabel>attitude indicators (design and techniques)</skos:altLabel>
  <skos:altLabel>bioelectronic instruments (theory and techniques)</skos:altLabel>
  <skos:altLabel>bioinstrumentation (theory and techniques)</skos:altLabel>
  <skos:altLabel>biomedical instruments (theory and techniques)</skos:altLabel>
  <skos:altLabel>Bragg cells (design and techniques)</skos:altLabel>
  <skos:altLabel>cameras</skos:altLabel>
  <skos:altLabel>coronagraphs</skos:altLabel>
  <skos:altLabel>darkroom equipment</skos:altLabel>
  <skos:altLabel>detectors</skos:altLabel>
  <skos:altLabel>Earth sensors</skos:altLabel>
  <skos:altLabel>electron microscopes</skos:altLabel>
  <skos:altLabel>electro-optical systems (instrumentation)</skos:altLabel>
  <skos:altLabel>emissivity measurements</skos:altLabel>
  <skos:altLabel>filters (photographic)</skos:altLabel>
  <skos:altLabel>flow visualization (instrumentation)</skos:altLabel>
  <skos:altLabel>fluid flow sensors (general)</skos:altLabel>
  <skos:altLabel>gages (general)</skos:altLabel>
  <skos:altLabel>geophysical sensors (design and techniques)</skos:altLabel>
  <skos:altLabel>gyroscopes (design and operation)</skos:altLabel>
  <skos:altLabel>holography</skos:altLabel>
  <skos:altLabel>image enhancement</skos:altLabel>
  <skos:altLabel>infrared sensors</skos:altLabel>
  <skos:altLabel>instrument design (theory and techniques)</skos:altLabel>
  <skos:altLabel>instrumentation</skos:altLabel>
  <skos:altLabel>interferometers</skos:altLabel>
  <skos:altLabel>ion mass spectrometers</skos:altLabel>
  <skos:altLabel>laser Doppler velocimeters</skos:altLabel>
  <skos:altLabel>laser instruments (design and operation)</skos:altLabel>
  <skos:altLabel>lenses (photographic)</skos:altLabel>
  <skos:altLabel>mass spectrometers</skos:altLabel>
  <skos:altLabel>measuring instruments</skos:altLabel>
  <skos:altLabel>micrometeoroid sensors (instrumentation)</skos:altLabel>
  <skos:altLabel>microscopes</skos:altLabel>
  <skos:altLabel>multimode sensors</skos:altLabel>
  <skos:altLabel>multispectral sensors</skos:altLabel>
  <skos:altLabel>nondestructive testing instruments</skos:altLabel>
  <skos:altLabel>optical imaging devices (design and techniques)</skos:altLabel>
  <skos:altLabel>optical measuring instruments (design and techniques)</skos:altLabel>
  <skos:altLabel>oscilloscopes</skos:altLabel>
  <skos:altLabel>ozonesondes</skos:altLabel>
  <skos:altLabel>photographic processing equipment</skos:altLabel>
  <skos:altLabel>photographic supplies</skos:altLabel>
  <skos:altLabel>photography</skos:altLabel>
  <skos:altLabel>photometry</skos:altLabel>
  <skos:altLabel>phototheodolites</skos:altLabel>
  <skos:altLabel>physiological monitoring devices (theory and techniques)</skos:altLabel>
  <skos:altLabel>position sensors</skos:altLabel>
  <skos:altLabel>precision time and time interval (PTTI)</skos:altLabel>
  <skos:altLabel>pressure transducers</skos:altLabel>
  <skos:altLabel>radiation instruments</skos:altLabel>
  <skos:altLabel>radiography</skos:altLabel>
  <skos:altLabel>recording devices</skos:altLabel>
  <skos:altLabel>remote sensors</skos:altLabel>
  <skos:altLabel>scatterometers (design and techniques)</skos:altLabel>
  <skos:altLabel>sensors</skos:altLabel>
  <skos:altLabel>shock tube instruments</skos:altLabel>
  <skos:altLabel>spectral analysis instruments</skos:altLabel>
  <skos:altLabel>spectrometers</skos:altLabel>
  <skos:altLabel>spectrophotometers</skos:altLabel>
  <skos:altLabel>spectroscopes</skos:altLabel>
  <skos:altLabel>strain gags</skos:altLabel>
  <skos:altLabel>tape recorders</skos:altLabel>
  <skos:altLabel>temperature measuring instruments</skos:altLabel>
  <skos:altLabel>test facility instruments</skos:altLabel>
  <skos:altLabel>thermocouples (design and techniques)</skos:altLabel>
  <skos:altLabel>time measurement equipment</skos:altLabel>
  <skos:altLabel>tomography (design and techniques)</skos:altLabel>
  <skos:altLabel>transducers (applications)</skos:altLabel>
  <skos:altLabel>two-gas sensors (general)</skos:altLabel>
  <skos:altLabel>ultrasonic testing equipment</skos:altLabel>
  <skos:altLabel>vidicon cameras</skos:altLabel>
  <skos:altLabel>wind tunnel instruments</skos:altLabel>
  <skos:broader rdf:resource='subj:1332'/>
  <nt2:status>Approved</nt2:status>
  <nt2:type>Descriptor</nt2:type>
  <nt2:inputdate>2007-01-11</nt2:inputdate>
  <dcterms:dateAccepted>2006-12-01</dcterms:dateAccepted>
  <dcterms:modified>2007-01-11</dcterms:modified>
  <nt2:notValidDate></nt2:notValidDate>
  <nt2:code>35</nt2:code>
 </skos:Concept>
 <skos:Concept rdf:about='subj:38'>
  <skos:prefLabel>Quality Assurance and Reliability</skos:prefLabel>
  <skos:scopeNote>Includes approaches to, and methods for reliability
    analysis and control, quality control, inspection,
    maintainability, and standardization.
  </skos:scopeNote>
  <skos:altLabel>accelerated life testing</skos:altLabel>
  <skos:altLabel>clean rooms (general)</skos:altLabel>
  <skos:altLabel>environmental test facilities</skos:altLabel>
  <skos:altLabel>environmental testing</skos:altLabel>
  <skos:altLabel>failure rates</skos:altLabel>
  <skos:altLabel>fault detection (quality control)</skos:altLabel>
  <skos:altLabel>inspection</skos:altLabel>
  <skos:altLabel>inspection methods</skos:altLabel>
  <skos:altLabel>life prediction</skos:altLabel>
  <skos:altLabel>life testing</skos:altLabel>
  <skos:altLabel>maintainability (procedures and theory)</skos:altLabel>
  <skos:altLabel>nondestructive testing</skos:altLabel>
  <skos:altLabel>quality assurance</skos:altLabel>
  <skos:altLabel>quality control</skos:altLabel>
  <skos:altLabel>radiography (quality control)</skos:altLabel>
  <skos:altLabel>redundancy systems</skos:altLabel>
  <skos:altLabel>reliability (procedures and theory)</skos:altLabel>
  <skos:altLabel>reliability criteria</skos:altLabel>
  <skos:altLabel>sampling techniques (quality control)</skos:altLabel>
  <skos:altLabel>service life</skos:altLabel>
  <skos:altLabel>shock testing (quality control)</skos:altLabel>
  <skos:altLabel>ultrasonic testing (quality control)</skos:altLabel>
  <skos:broader rdf:resource='subj:1332'/>
  <nt2:status>Approved</nt2:status>
  <nt2:type>Descriptor</nt2:type>
  <nt2:inputdate>2007-01-11</nt2:inputdate>
  <dcterms:dateAccepted>2006-12-01</dcterms:dateAccepted>
  <dcterms:modified>2007-01-11</dcterms:modified>
  <nt2:notValidDate></nt2:notValidDate>
  <nt2:code>38</nt2:code>
 </skos:Concept>
 <skos:Concept rdf:about='subj:07'>
  <skos:prefLabel>Aircraft Propulsion and Power</skos:prefLabel>
  <skos:scopeNote>Includes primary propulsion systems and related systems and
    components, e.g., gas turbine engines, compressors, and
    fuel systems; and onboard auxiliary power plants for
    aircraft. For related information see also 20 Spacecraft
    Propulsion and Power; 28 Propellants and Fuels; and 44
    Energy Production and Conversion.
  </skos:scopeNote>
  <skos:altLabel>aerodynamic noise (propulsion systems)</skos:altLabel>
  <skos:altLabel>afterburner controls</skos:altLabel>
  <skos:altLabel>afterburners (aircraft engines)</skos:altLabel>
  <skos:altLabel>airbreathing engines (aircraft)</skos:altLabel>
  <skos:altLabel>aircraft engine design</skos:altLabel>
  <skos:altLabel>aircraft engine maintenance</skos:altLabel>
  <skos:altLabel>aircraft engine performance</skos:altLabel>
  <skos:altLabel>aircraft engine simulation</skos:altLabel>
  <skos:altLabel>aircraft engine testing</skos:altLabel>
  <skos:altLabel>aircraft engines</skos:altLabel>
  <skos:altLabel>aircraft fuel systems</skos:altLabel>
  <skos:altLabel>aircraft hydraulic systems (power)</skos:altLabel>
  <skos:altLabel>aircraft pneumatic systems (power)</skos:altLabel>
  <skos:altLabel>aircraft power systems</skos:altLabel>
  <skos:altLabel>aircraft propellers</skos:altLabel>
  <skos:altLabel>aircraft propulsion system components</skos:altLabel>
  <skos:altLabel>aircraft propulsion systems</skos:altLabel>
  <skos:altLabel>auxiliary power systems (aircraft)</skos:altLabel>
  <skos:altLabel>auxiliary power units (APU) (aircraft)</skos:altLabel>
  <skos:altLabel>bird ingestion (aircraft engines)</skos:altLabel>
  <skos:altLabel>bypass jet engines</skos:altLabel>
  <skos:altLabel>carburetors (aircraft engines)</skos:altLabel>
  <skos:altLabel>centrifugal compressors (aircraft)</skos:altLabel>
  <skos:altLabel>chemical propulsion engines (aircraft)</skos:altLabel>
  <skos:altLabel>combustors (aircraft)</skos:altLabel>
  <skos:altLabel>compression ignition engines (aircraft)</skos:altLabel>
  <skos:altLabel>compressors (aircraft engines)</skos:altLabel>
  <skos:altLabel>cooling systems (aircraft engines)</skos:altLabel>
  <skos:altLabel>diesel engines (aircraft)</skos:altLabel>
  <skos:altLabel>diffusers (aircraft engines)</skos:altLabel>
  <skos:altLabel>ejectors (aircraft)</skos:altLabel>
  <skos:altLabel>electric power systems (aircraft)</skos:altLabel>
  <skos:altLabel>electric power units (aircraft)</skos:altLabel>
  <skos:altLabel>electric propulsion systems (aircraft)</skos:altLabel>
  <skos:altLabel>engine control systems (aircraft)</skos:altLabel>
  <skos:altLabel>engine ingestion</skos:altLabel>
  <skos:altLabel>engine noise (aircraft)</skos:altLabel>
  <skos:altLabel>engine noise suppressors (aircraft)</skos:altLabel>
  <skos:altLabel>exhaust systems (aircraft engines)</skos:altLabel>
  <skos:altLabel>exit controls (aircraft engines)</skos:altLabel>
  <skos:altLabel>fan jet engines</skos:altLabel>
  <skos:altLabel>foreign object ingestion (aircraft engines)</skos:altLabel>
  <skos:altLabel>fuel distribution pumps (aircraft)</skos:altLabel>
  <skos:altLabel>fuel distribution systems (aircraft)</skos:altLabel>
  <skos:altLabel>fuel injection systems (aircraft)</skos:altLabel>
  <skos:altLabel>fuel system components (aircraft)</skos:altLabel>
  <skos:altLabel>fuel systems (aircraft)</skos:altLabel>
  <skos:altLabel>fuel tanks (aircraft)</skos:altLabel>
  <skos:altLabel>gas turbine engines (aircraft)</skos:altLabel>
  <skos:altLabel>gasoline engines (aircraft)</skos:altLabel>
  <skos:altLabel>injection systems (aircraft engines)</skos:altLabel>
  <skos:altLabel>inlet controls (aircraft engines)</skos:altLabel>
  <skos:altLabel>inlets (aircraft)</skos:altLabel>
  <skos:altLabel>internal combustion engines (aircraft)</skos:altLabel>
  <skos:altLabel>jet engines</skos:altLabel>
  <skos:altLabel>noise reduction (aircraft engines)</skos:altLabel>
  <skos:altLabel>nozzles (aircraft)</skos:altLabel>
  <skos:altLabel>nuclear engines (aircraft)</skos:altLabel>
  <skos:altLabel>nuclear propulsion systems (aircraft)</skos:altLabel>
  <skos:altLabel>piston engines (aircraft)</skos:altLabel>
  <skos:altLabel>pneumatic systems (aircraft propulsion and power)</skos:altLabel>
  <skos:altLabel>propellers (tractor, pusher, contrarotating, propfan)</skos:altLabel>
  <skos:altLabel>propulsion system components (aircraft)</skos:altLabel>
  <skos:altLabel>propulsion systems (aircraft)</skos:altLabel>
  <skos:altLabel>pulse detonation engines</skos:altLabel>
  <skos:altLabel>pulsejet engines</skos:altLabel>
  <skos:altLabel>pumps (aircraft engines and fuel systems)</skos:altLabel>
  <skos:altLabel>quiet engines (aircraft)</skos:altLabel>
  <skos:altLabel>ramjet engines (aircraft)</skos:altLabel>
  <skos:altLabel>reciprocating engines (aircraft)</skos:altLabel>
  <skos:altLabel>rocket engines (aircraft)</skos:altLabel>
  <skos:altLabel>rotary engines (aircraft)</skos:altLabel>
  <skos:altLabel>scramjet engines (aircraft)</skos:altLabel>
  <skos:altLabel>spark ignition engines (aircraft)</skos:altLabel>
  <skos:altLabel>Stirling cycle engines (aircraft)</skos:altLabel>
  <skos:altLabel>superchargers (aircraft engines)</skos:altLabel>
  <skos:altLabel>throttle controls (aircraft)</skos:altLabel>
  <skos:altLabel>thrust reverser controls</skos:altLabel>
  <skos:altLabel>thrust reversers (aircraft engines)</skos:altLabel>
  <skos:altLabel>turbine blade cooling</skos:altLabel>
  <skos:altLabel>turbine blade vibration</skos:altLabel>
  <skos:altLabel>turbines (aircraft engines)</skos:altLabel>
  <skos:altLabel>turbofan engines</skos:altLabel>
  <skos:altLabel>turboprop engines</skos:altLabel>
  <skos:altLabel>turborocket engines (aircraft)</skos:altLabel>
  <skos:altLabel>wind tunnel tests (propulsion systems)</skos:altLabel>
  <skos:broader rdf:resource='subj:101'/>
  <nt2:status>Approved</nt2:status>
  <nt2:type>Descriptor</nt2:type>
  <nt2:inputdate>2007-01-11</nt2:inputdate>
  <dcterms:dateAccepted>2006-12-01</dcterms:dateAccepted>
  <dcterms:modified>2007-01-11</dcterms:modified>
  <nt2:notValidDate></nt2:notValidDate>
  <nt2:code>07</nt2:code>
 </skos:Concept>
 <skos:Concept rdf:about='subj:36'>
  <skos:prefLabel>Lasers and Masers</skos:prefLabel>
  <skos:scopeNote>Includes lasing theory, laser pumping techniques, maser
    amplifiers, laser materials, and the assessment of laser
    and maser outputs. For cases where the application of the
    laser or maser is emphasized see also the specific category
    where the application is treated. For related information
    see also 76 Solid-State Physics.
  </skos:scopeNote>
  <skos:altLabel>chemical lasers</skos:altLabel>
  <skos:altLabel>dye lasers</skos:altLabel>
  <skos:altLabel>gas lasers</skos:altLabel>
  <skos:altLabel>glass lasers</skos:altLabel>
  <skos:altLabel>ladar (design)</skos:altLabel>
  <skos:altLabel>laser amplifiers</skos:altLabel>
  <skos:altLabel>laser Applications</skos:altLabel>
  <skos:altLabel>laser beams</skos:altLabel>
  <skos:altLabel>laser cavities</skos:altLabel>
  <skos:altLabel>laser damage</skos:altLabel>
  <skos:altLabel>laser drilling (theory and techniques)</skos:altLabel>
  <skos:altLabel>laser materials</skos:altLabel>
  <skos:altLabel>laser modulators</skos:altLabel>
  <skos:altLabel>laser optics</skos:altLabel>
  <skos:altLabel>laser radiation effects</skos:altLabel>
  <skos:altLabel>laser radiation hazards</skos:altLabel>
  <skos:altLabel>laser research</skos:altLabel>
  <skos:altLabel>laser theory</skos:altLabel>
  <skos:altLabel>laser tracking systems (general)</skos:altLabel>
  <skos:altLabel>lasers</skos:altLabel>
  <skos:altLabel>lasertrons</skos:altLabel>
  <skos:altLabel>liquid lasers</skos:altLabel>
  <skos:altLabel>masers</skos:altLabel>
  <skos:altLabel>orotrons</skos:altLabel>
  <skos:altLabel>parametric amplifiers</skos:altLabel>
  <skos:altLabel>quantum generators</skos:altLabel>
  <skos:altLabel>semiconductor lasers</skos:altLabel>
  <skos:altLabel>short pulsed lasers</skos:altLabel>
  <skos:altLabel>solid state lasers</skos:altLabel>
  <skos:altLabel>tunable lasers</skos:altLabel>
  <skos:broader rdf:resource='subj:1332'/>
  <nt2:status>Approved</nt2:status>
  <nt2:type>Descriptor</nt2:type>
  <nt2:inputdate>2007-01-11</nt2:inputdate>
  <dcterms:dateAccepted>2006-12-01</dcterms:dateAccepted>
  <dcterms:modified>2007-01-11</dcterms:modified>
  <nt2:notValidDate></nt2:notValidDate>
  <nt2:code>36</nt2:code>
 </skos:Concept>
 <skos:Concept rdf:about='subj:93'>
  <skos:prefLabel>Space Radiation</skos:prefLabel>
  <skos:scopeNote>Includes cosmic radiation; and inner and outer Earth
    radiation belts. For biological effects of radiation on
    plants and animals see 51 Life Sciences; on human beings
    see 52 Aerospace Medicine. For theory see 73 Nuclear
    Physics.
  </skos:scopeNote>
  <skos:altLabel>alpha rays (space)</skos:altLabel>
  <skos:altLabel>beta rays (space)</skos:altLabel>
  <skos:altLabel>cosmic radiation</skos:altLabel>
  <skos:altLabel>galactic radiation</skos:altLabel>
  <skos:altLabel>gamma rays (space)</skos:altLabel>
  <skos:altLabel>inner Earth radiation belts</skos:altLabel>
  <skos:altLabel>intergalactic radiation</skos:altLabel>
  <skos:altLabel>interstellar radiation</skos:altLabel>
  <skos:altLabel>outer Earth radiation belts</skos:altLabel>
  <skos:altLabel>radiation belts</skos:altLabel>
  <skos:altLabel>stellar radiation</skos:altLabel>
  <skos:altLabel>ultraviolet radiation (space)</skos:altLabel>
  <skos:altLabel>Van Allen belts</skos:altLabel>
  <skos:altLabel>x-ray radiation (space)</skos:altLabel>
  <skos:broader rdf:resource='subj:2871'/>
  <nt2:status>Approved</nt2:status>
  <nt2:type>Descriptor</nt2:type>
  <nt2:inputdate>2007-01-11</nt2:inputdate>
  <dcterms:dateAccepted>2006-12-01</dcterms:dateAccepted>
  <dcterms:modified>2007-01-11</dcterms:modified>
  <nt2:notValidDate></nt2:notValidDate>
  <nt2:code>93</nt2:code>
 </skos:Concept>
 <skos:Concept rdf:about='subj:34'>
  <skos:prefLabel>Fluid Mechanics and Thermodynamics</skos:prefLabel>
  <skos:scopeNote>Includes fluid dynamics and kinematics and all forms of
    heat transfer; boundary layer flow; hydrodynamics;
    hydraulics; fluidics; mass transfer and ablation cooling.
    For related information see also 02 Aerodynamics.
  </skos:scopeNote>
  <skos:altLabel>ablation</skos:altLabel>
  <skos:altLabel>ablation cooling</skos:altLabel>
  <skos:altLabel>atomizers</skos:altLabel>
  <skos:altLabel>boiling</skos:altLabel>
  <skos:altLabel>Boltzmann transport theory</skos:altLabel>
  <skos:altLabel>boundary layer flow (general)</skos:altLabel>
  <skos:altLabel>cavitation</skos:altLabel>
  <skos:altLabel>compressible flow (general)</skos:altLabel>
  <skos:altLabel>computational fluid dynamics</skos:altLabel>
  <skos:altLabel>convection</skos:altLabel>
  <skos:altLabel>enthalpy</skos:altLabel>
  <skos:altLabel>entropy</skos:altLabel>
  <skos:altLabel>equations of state</skos:altLabel>
  <skos:altLabel>flow (general)</skos:altLabel>
  <skos:altLabel>flow characteristics</skos:altLabel>
  <skos:altLabel>flow equations</skos:altLabel>
  <skos:altLabel>flow measurement</skos:altLabel>
  <skos:altLabel>flow visualization (general applications)</skos:altLabel>
  <skos:altLabel>flow with heat addition</skos:altLabel>
  <skos:altLabel>fluerics</skos:altLabel>
  <skos:altLabel>fluid dynamics</skos:altLabel>
  <skos:altLabel>fluid flow</skos:altLabel>
  <skos:altLabel>fluid forces</skos:altLabel>
  <skos:altLabel>fluid heat transfer</skos:altLabel>
  <skos:altLabel>fluid kinematics</skos:altLabel>
  <skos:altLabel>fluid mechanics</skos:altLabel>
  <skos:altLabel>fluidics</skos:altLabel>
  <skos:altLabel>free energy</skos:altLabel>
  <skos:altLabel>gas dynamics</skos:altLabel>
  <skos:altLabel>gas flow</skos:altLabel>
  <skos:altLabel>gas forces</skos:altLabel>
  <skos:altLabel>gas heat transfer</skos:altLabel>
  <skos:altLabel>gas mechanics</skos:altLabel>
  <skos:altLabel>gaseous film cooling</skos:altLabel>
  <skos:altLabel>heat exchangers (aerospace applications)</skos:altLabel>
  <skos:altLabel>heat pipes (aerospace applications)</skos:altLabel>
  <skos:altLabel>heat shields (aerospace applications)</skos:altLabel>
  <skos:altLabel>heat sinks (aerospace applications)</skos:altLabel>
  <skos:altLabel>heat transfer</skos:altLabel>
  <skos:altLabel>hydraulics</skos:altLabel>
  <skos:altLabel>hydrodynamics</skos:altLabel>
  <skos:altLabel>hydrostatics</skos:altLabel>
  <skos:altLabel>incompressible flow</skos:altLabel>
  <skos:altLabel>induction heating</skos:altLabel>
  <skos:altLabel>internal flow in ducts (applications)</skos:altLabel>
  <skos:altLabel>internal flow in turbomachinery (applications)</skos:altLabel>
  <skos:altLabel>inviscid flow</skos:altLabel>
  <skos:altLabel>laminar flow (general)</skos:altLabel>
  <skos:altLabel>liquid settling</skos:altLabel>
  <skos:altLabel>liquid sloshing</skos:altLabel>
  <skos:altLabel>mass transfer</skos:altLabel>
  <skos:altLabel>mixing of gases</skos:altLabel>
  <skos:altLabel>mixing of liquids</skos:altLabel>
  <skos:altLabel>multiphase flow</skos:altLabel>
  <skos:altLabel>Navier-Stokes equations</skos:altLabel>
  <skos:altLabel>pneumatics</skos:altLabel>
  <skos:altLabel>radiative transfer</skos:altLabel>
  <skos:altLabel>radiators (aerospace applications)</skos:altLabel>
  <skos:altLabel>rheology</skos:altLabel>
  <skos:altLabel>shock waves</skos:altLabel>
  <skos:altLabel>skin friction</skos:altLabel>
  <skos:altLabel>sprays</skos:altLabel>
  <skos:altLabel>temperature-pressure phenomena</skos:altLabel>
  <skos:altLabel>thermal radiation</skos:altLabel>
  <skos:altLabel>thermodynamic cycles</skos:altLabel>
  <skos:altLabel>thermodynamic properties</skos:altLabel>
  <skos:altLabel>thermodynamics</skos:altLabel>
  <skos:altLabel>transitional flow (general)</skos:altLabel>
  <skos:altLabel>transpiration cooling</skos:altLabel>
  <skos:altLabel>turbulence models</skos:altLabel>
  <skos:altLabel>turbulent flow (general)</skos:altLabel>
  <skos:altLabel>unsteady flow (general)</skos:altLabel>
  <skos:altLabel>viscous flow</skos:altLabel>
  <skos:altLabel>vortices (general)</skos:altLabel>
  <skos:broader rdf:resource='subj:1332'/>
  <nt2:status>Approved</nt2:status>
  <nt2:type>Descriptor</nt2:type>
  <nt2:inputdate>2007-01-11</nt2:inputdate>
  <dcterms:dateAccepted>2006-12-01</dcterms:dateAccepted>
  <dcterms:modified>2007-01-11</dcterms:modified>
  <nt2:notValidDate></nt2:notValidDate>
  <nt2:code>34</nt2:code>
 </skos:Concept>
 <skos:Concept rdf:about='subj:12'>
  <skos:prefLabel>Astronautics (General)</skos:prefLabel>
  <skos:scopeNote>Includes general research topics related to space flight
    and manned and unmanned space vehicles, platforms or
    objects launched into, or assembled in, outer space; and
    related components and equipment. Also includes
    manufacturing and maintenance of such vehicles or
    platforms. For specific topics in astronautics see
    categories 13 through 20. For extraterrestrial exploration
    see 91 Lunar and Planetary Science and Exploration.
  </skos:scopeNote>
  <skos:altLabel>in-orbit maintenance, servicing and refueling</skos:altLabel>
  <skos:altLabel>launch vehicle maintenance</skos:altLabel>
  <skos:altLabel>launch vehicle manufacturing</skos:altLabel>
  <skos:altLabel>launch vehicle production</skos:altLabel>
  <skos:altLabel>maintenance (spacecraft)</skos:altLabel>
  <skos:altLabel>mission planning (space)</skos:altLabel>
  <skos:altLabel>space based maintenance and servicing;</skos:altLabel>
  <skos:altLabel>space colonies</skos:altLabel>
  <skos:altLabel>space colonization</skos:altLabel>
  <skos:altLabel>space exploration (mission planning)</skos:altLabel>
  <skos:altLabel>space manufacturing and assembly</skos:altLabel>
  <skos:altLabel>space programs</skos:altLabel>
  <skos:altLabel>space station assembly</skos:altLabel>
  <skos:altLabel>space station maintenance</skos:altLabel>
  <skos:altLabel>space vehicle maintenance</skos:altLabel>
  <skos:altLabel>space vehicle manufacturing</skos:altLabel>
  <skos:altLabel>space vehicle production</skos:altLabel>
  <skos:altLabel>spacecraft maintenance</skos:altLabel>
  <skos:altLabel>spacecraft manufacturing</skos:altLabel>
  <skos:altLabel>spacecraft production</skos:altLabel>
  <skos:broader rdf:resource='subj:578'/>
  <nt2:status>Approved</nt2:status>
  <nt2:type>Descriptor</nt2:type>
  <nt2:inputdate>2007-01-11</nt2:inputdate>
  <dcterms:dateAccepted>2006-12-01</dcterms:dateAccepted>
  <dcterms:modified>2007-01-11</dcterms:modified>
  <nt2:notValidDate></nt2:notValidDate>
  <nt2:code>12</nt2:code>
 </skos:Concept>
 <skos:Concept rdf:about='subj:39'>
  <skos:prefLabel>Structural Mechanics</skos:prefLabel>
  <skos:scopeNote>Includes structural element design, analysis and testing;
    dynamic responses of structures; weight analysis; fatigue
    and other structural properties; and mechanical and thermal
    stresses in structures. For applications see 05 Aircraft
    Design, Testing and Performance; and 18 Spacecraft Design,
    Testing and Performance.
  </skos:scopeNote>
  <skos:altLabel>acoustoelasticity</skos:altLabel>
  <skos:altLabel>adhesive joints (structural stability)</skos:altLabel>
  <skos:altLabel>aeroelasticity (structural flexibility)</skos:altLabel>
  <skos:altLabel>beams (structures)</skos:altLabel>
  <skos:altLabel>bending</skos:altLabel>
  <skos:altLabel>bolted joints</skos:altLabel>
  <skos:altLabel>bonded structures</skos:altLabel>
  <skos:altLabel>buckling</skos:altLabel>
  <skos:altLabel>columns</skos:altLabel>
  <skos:altLabel>combined loads</skos:altLabel>
  <skos:altLabel>compression</skos:altLabel>
  <skos:altLabel>compression loads</skos:altLabel>
  <skos:altLabel>compression strength (structural)</skos:altLabel>
  <skos:altLabel>cones (structures)</skos:altLabel>
  <skos:altLabel>crack propagation</skos:altLabel>
  <skos:altLabel>cracks</skos:altLabel>
  <skos:altLabel>cylinders (structures)</skos:altLabel>
  <skos:altLabel>dynamic structural analysis</skos:altLabel>
  <skos:altLabel>elasticity</skos:altLabel>
  <skos:altLabel>energy</skos:altLabel>
  <skos:altLabel>energy absorption (structures)</skos:altLabel>
  <skos:altLabel>fatigue (structural)</skos:altLabel>
  <skos:altLabel>filament wound structures (design and tests)</skos:altLabel>
  <skos:altLabel>flutter (structural)</skos:altLabel>
  <skos:altLabel>fracture mechanics</skos:altLabel>
  <skos:altLabel>honeycomb structures</skos:altLabel>
  <skos:altLabel>lightweight structural elements</skos:altLabel>
  <skos:altLabel>lightweight structures</skos:altLabel>
  <skos:altLabel>panels (structures)</skos:altLabel>
  <skos:altLabel>photoelasticity</skos:altLabel>
  <skos:altLabel>plasticity</skos:altLabel>
  <skos:altLabel>plates (structural elements)</skos:altLabel>
  <skos:altLabel>rings (structures)</skos:altLabel>
  <skos:altLabel>riveted joints</skos:altLabel>
  <skos:altLabel>sandwich structures</skos:altLabel>
  <skos:altLabel>shear loads</skos:altLabel>
  <skos:altLabel>shear strength (structures)</skos:altLabel>
  <skos:altLabel>shells (structures)</skos:altLabel>
  <skos:altLabel>shock testing (structural analysis)</skos:altLabel>
  <skos:altLabel>stress (structural)</skos:altLabel>
  <skos:altLabel>stress analysis</skos:altLabel>
  <skos:altLabel>structural analysis</skos:altLabel>
  <skos:altLabel>structural design</skos:altLabel>
  <skos:altLabel>structural elements</skos:altLabel>
  <skos:altLabel>structural fatigue</skos:altLabel>
  <skos:altLabel>structural testing</skos:altLabel>
  <skos:altLabel>structural theory</skos:altLabel>
  <skos:altLabel>structural vibration effects</skos:altLabel>
  <skos:altLabel>tensile strength (structures)</skos:altLabel>
  <skos:altLabel>tension loads</skos:altLabel>
  <skos:altLabel>thermal stress</skos:altLabel>
  <skos:altLabel>thermoelasticity (structural materials)</skos:altLabel>
  <skos:altLabel>trusses</skos:altLabel>
  <skos:altLabel>vibration (structures)</skos:altLabel>
  <skos:altLabel>vibration testing</skos:altLabel>
  <skos:altLabel>viscoelasticity (structural materials)</skos:altLabel>
  <skos:altLabel>wave propagation (structural response)</skos:altLabel>
  <skos:altLabel>weight analysis</skos:altLabel>
  <skos:altLabel>weld strength</skos:altLabel>
  <skos:altLabel>welded structures</skos:altLabel>
  <skos:broader rdf:resource='subj:1332'/>
  <nt2:status>Approved</nt2:status>
  <nt2:type>Descriptor</nt2:type>
  <nt2:inputdate>2007-01-11</nt2:inputdate>
  <dcterms:dateAccepted>2006-12-01</dcterms:dateAccepted>
  <dcterms:modified>2007-01-11</dcterms:modified>
  <nt2:notValidDate></nt2:notValidDate>
  <nt2:code>39</nt2:code>
 </skos:Concept>
 <skos:Concept rdf:about='subj:28'>
  <skos:prefLabel>Propellants and Fuels</skos:prefLabel>
  <skos:scopeNote>Includes rocket propellants, igniters, and oxidizers; their
    storage and handling procedures; and aircraft fuels. For
    nuclear fuels see 73 Nuclear Physics. For related
    information see also 07 Aircraft Propulsion and Power; 20
    Spacecraft Propulsion and Power; and 44 Energy Production
    and Conversion.
  </skos:scopeNote>
  <skos:altLabel>aircraft fuels</skos:altLabel>
  <skos:altLabel>boiloff</skos:altLabel>
  <skos:altLabel>boron-based fuels</skos:altLabel>
  <skos:altLabel>burning rates</skos:altLabel>
  <skos:altLabel>catalysts (propellants)</skos:altLabel>
  <skos:altLabel>chemical properties of propellants and fuels</skos:altLabel>
  <skos:altLabel>combustion characteristics (propellants and fuels)</skos:altLabel>
  <skos:altLabel>combustion controllability (propellants and fuels)</skos:altLabel>
  <skos:altLabel>combustion in microgravity (propellants and fuels)</skos:altLabel>
  <skos:altLabel>combustion instability (propellants and fuels)</skos:altLabel>
  <skos:altLabel>combustion kinetics (propellants and fuels)</skos:altLabel>
  <skos:altLabel>combustion of propellants and fuels</skos:altLabel>
  <skos:altLabel>combustion products</skos:altLabel>
  <skos:altLabel>cryogenic propellants</skos:altLabel>
  <skos:altLabel>decomposition (propellants and fuels)</skos:altLabel>
  <skos:altLabel>development of propellants and fuels</skos:altLabel>
  <skos:altLabel>evaluation of propellants and fuels</skos:altLabel>
  <skos:altLabel>exotic propellants and fuels</skos:altLabel>
  <skos:altLabel>explosives</skos:altLabel>
  <skos:altLabel>flames and flame propagation (propellants and fuels)</skos:altLabel>
  <skos:altLabel>fluorine/oxygen propellants</skos:altLabel>
  <skos:altLabel>fuels</skos:altLabel>
  <skos:altLabel>gelled propellants and fuels</skos:altLabel>
  <skos:altLabel>handling of propellants and fuels</skos:altLabel>
  <skos:altLabel>high energy propellants and fuels</skos:altLabel>
  <skos:altLabel>hybrid propellants and fuels</skos:altLabel>
  <skos:altLabel>hydrazine propellants</skos:altLabel>
  <skos:altLabel>hydrides</skos:altLabel>
  <skos:altLabel>hydrogen propellants and fuels</skos:altLabel>
  <skos:altLabel>hypergolic propellants</skos:altLabel>
  <skos:altLabel>igniters (propellants)</skos:altLabel>
  <skos:altLabel>ignition studies (propellants and fuels)</skos:altLabel>
  <skos:altLabel>jet engine fuels</skos:altLabel>
  <skos:altLabel>kerosene based fuels</skos:altLabel>
  <skos:altLabel>liquid fuels</skos:altLabel>
  <skos:altLabel>liquid hydrogen (propellants and fuels)</skos:altLabel>
  <skos:altLabel>liquid oxygen (propellants and fuels)</skos:altLabel>
  <skos:altLabel>liquid petroleum gas (LPG)</skos:altLabel>
  <skos:altLabel>liquid propellants</skos:altLabel>
  <skos:altLabel>lithergolic propellants</skos:altLabel>
  <skos:altLabel>manufacture of propellants</skos:altLabel>
  <skos:altLabel>mechanical properties of propellants and fuels</skos:altLabel>
  <skos:altLabel>metal based propellants and fuels</skos:altLabel>
  <skos:altLabel>monopropellants</skos:altLabel>
  <skos:altLabel>nitrate based propellants and fuels</skos:altLabel>
  <skos:altLabel>oxidizers</skos:altLabel>
  <skos:altLabel>physical properties of propellants and fuels</skos:altLabel>
  <skos:altLabel>piston engine fuels</skos:altLabel>
  <skos:altLabel>propellant grains</skos:altLabel>
  <skos:altLabel>propellants</skos:altLabel>
  <skos:altLabel>pyrotechnics</skos:altLabel>
  <skos:altLabel>rocket propellants</skos:altLabel>
  <skos:altLabel>service life of propellants and fuels</skos:altLabel>
  <skos:altLabel>solid propellant curing</skos:altLabel>
  <skos:altLabel>solid propellants</skos:altLabel>
  <skos:altLabel>space storable propellants</skos:altLabel>
  <skos:altLabel>storage of propellants and fuels</skos:altLabel>
  <skos:altLabel>testing of propellants and fuels</skos:altLabel>
  <skos:altLabel>thermal characteristics</skos:altLabel>
  <skos:altLabel>thixotropic propellants</skos:altLabel>
  <skos:altLabel>vaporization of propellants and fuels</skos:altLabel>
  <skos:broader rdf:resource='subj:1058'/>
  <nt2:status>Approved</nt2:status>
  <nt2:type>Descriptor</nt2:type>
  <nt2:inputdate>2007-01-11</nt2:inputdate>
  <dcterms:dateAccepted>2006-12-01</dcterms:dateAccepted>
  <dcterms:modified>2007-01-11</dcterms:modified>
  <nt2:notValidDate></nt2:notValidDate>
  <nt2:code>28</nt2:code>
 </skos:Concept>
 <skos:Concept rdf:about='subj:101'>
  <skos:prefLabel>Aeronautics</skos:prefLabel>
  <skos:scopeNote>Includes aeronautics (general); aerodynamics; air
    transportation and safety; aircraft communications and
    navigation; aircraft design, testing and performance;
    avionics and aircraft instrumentation; aircraft propulsion
    and power; aircraft stability and control; and research and
    support facilities (air). For related information see also
    Astronautics (categories 12 through 20).
  </skos:scopeNote>
  <skos:broader rdf:resource='subj:100'/>
  <skos:narrower rdf:resource='subj:02'/>
  <skos:narrower rdf:resource='subj:01'/>
  <skos:narrower rdf:resource='subj:03'/>
  <skos:narrower rdf:resource='subj:04'/>
  <skos:narrower rdf:resource='subj:05'/>
  <skos:narrower rdf:resource='subj:07'/>
  <skos:narrower rdf:resource='subj:08'/>
  <skos:narrower rdf:resource='subj:06'/>
  <skos:narrower rdf:resource='subj:09'/>
  <nt2:status>Approved</nt2:status>
  <nt2:type>Descriptor</nt2:type>
  <nt2:inputdate>2007-01-11</nt2:inputdate>
  <dcterms:dateAccepted>2006-12-01</dcterms:dateAccepted>
  <dcterms:modified>2007-01-11</dcterms:modified>
  <nt2:notValidDate></nt2:notValidDate>
  <nt2:code>101</nt2:code>
 </skos:Concept>
 <skos:Concept rdf:about='subj:02'>
  <skos:prefLabel>Aerodynamics</skos:prefLabel>
  <skos:scopeNote>Includes aerodynamics of flight vehicles, test bodies,
    airframe components and combinations, wings, and control
    surfaces. Also includes aerodynamics of rotors, stators,
    fans, and other elements of turbomachinery. For related
    information see also 34 Fluid Mechanics and Thermodynamics.
  </skos:scopeNote>
  <skos:altLabel>aerodynamic derivatives</skos:altLabel>
  <skos:altLabel>aerodynamic flow fields</skos:altLabel>
  <skos:altLabel>aerodynamic heating</skos:altLabel>
  <skos:altLabel>aerodynamic noise (airframe generated)</skos:altLabel>
  <skos:altLabel>aerodynamic studies of skin friction</skos:altLabel>
  <skos:altLabel>aerodynamic wakes</skos:altLabel>
  <skos:altLabel>aerodynamics of protuberances and substructures</skos:altLabel>
  <skos:altLabel>aeroelasticity (theory)</skos:altLabel>
  <skos:altLabel>aerothermodynamics</skos:altLabel>
  <skos:altLabel>air cushion vehicle aerodynamics</skos:altLabel>
  <skos:altLabel>air flow separation</skos:altLabel>
  <skos:altLabel>air launched weapons (aerodynamics)</skos:altLabel>
  <skos:altLabel>aircraft aerodynamics</skos:altLabel>
  <skos:altLabel>airfoil aerodynamics</skos:altLabel>
  <skos:altLabel>airship aerodynamics</skos:altLabel>
  <skos:altLabel>autogyro aerodynamics</skos:altLabel>
  <skos:altLabel>balloon aerodynamics</skos:altLabel>
  <skos:altLabel>boundary layer aerodynamics</skos:altLabel>
  <skos:altLabel>boundary layer flow (aerodynamics)</skos:altLabel>
  <skos:altLabel>buffeting</skos:altLabel>
  <skos:altLabel>canard aerodynamics</skos:altLabel>
  <skos:altLabel>cascade aerodynamics</skos:altLabel>
  <skos:altLabel>compressible flow (aerodynamics)</skos:altLabel>
  <skos:altLabel>control surface aerodynamics</skos:altLabel>
  <skos:altLabel>Coriolis forces (aerodynamics)</skos:altLabel>
  <skos:altLabel>drag reduction (effects and techniques)</skos:altLabel>
  <skos:altLabel>exit aerodynamics</skos:altLabel>
  <skos:altLabel>glider aerodynamics</skos:altLabel>
  <skos:altLabel>ground effect machine aerodynamics</skos:altLabel>
  <skos:altLabel>helicopter aerodynamics</skos:altLabel>
  <skos:altLabel>high speed aerodynamics</skos:altLabel>
  <skos:altLabel>hovercraft aerodynamics</skos:altLabel>
  <skos:altLabel>hypersonic aerodynamics</skos:altLabel>
  <skos:altLabel>inlet aerodynamics</skos:altLabel>
  <skos:altLabel>internal flow in turbomachinery (theory)</skos:altLabel>
  <skos:altLabel>laminar flow (aerodynamics)</skos:altLabel>
  <skos:altLabel>land transportation vehicles (aerodynamics)</skos:altLabel>
  <skos:altLabel>launch vehicle aerodynamics</skos:altLabel>
  <skos:altLabel>lifting body aerodynamics</skos:altLabel>
  <skos:altLabel>lighter-than-air craft (balloons, airships) aerodynamics</skos:altLabel>
  <skos:altLabel>low speed aerodynamics</skos:altLabel>
  <skos:altLabel>missile aerodynamics</skos:altLabel>
  <skos:altLabel>parachute aerodynamics</skos:altLabel>
  <skos:altLabel>propeller aerodynamics</skos:altLabel>
  <skos:altLabel>reentry vehicle aerodynamics</skos:altLabel>
  <skos:altLabel>riblets (aerodynamics)</skos:altLabel>
  <skos:altLabel>rocket aerodynamics</skos:altLabel>
  <skos:altLabel>Rogallo wing aerodynamics</skos:altLabel>
  <skos:altLabel>rotary wing aircraft aerodynamics</skos:altLabel>
  <skos:altLabel>rotor aerodynamics</skos:altLabel>
  <skos:altLabel>sailplane aerodynamics</skos:altLabel>
  <skos:altLabel>sonic boom (aerodynamically generated)</skos:altLabel>
  <skos:altLabel>spacecraft aerodynamics</skos:altLabel>
  <skos:altLabel>stabilization surfaces (aerodynamics)</skos:altLabel>
  <skos:altLabel>STOL aerodynamics</skos:altLabel>
  <skos:altLabel>subsonic aerodynamics</skos:altLabel>
  <skos:altLabel>supercritical airfoils</skos:altLabel>
  <skos:altLabel>supercritical wings</skos:altLabel>
  <skos:altLabel>supersonic aerodynamics</skos:altLabel>
  <skos:altLabel>transitional flow (aerodynamics)</skos:altLabel>
  <skos:altLabel>transonic aerodynamics</skos:altLabel>
  <skos:altLabel>turbulent flow (aerodynamics)</skos:altLabel>
  <skos:altLabel>ultralight aircraft (aerodynamics)</skos:altLabel>
  <skos:altLabel>unsteady flow (aerodynamics)</skos:altLabel>
  <skos:altLabel>VSTOL aerodynamics</skos:altLabel>
  <skos:altLabel>VTOL aerodynamics</skos:altLabel>
  <skos:altLabel>wakes (effects of turbulent flow behind aircraft)</skos:altLabel>
  <skos:altLabel>wind tunnel tests (aerodynamics)</skos:altLabel>
  <skos:altLabel>wing aerodynamics</skos:altLabel>
  <skos:broader rdf:resource='subj:101'/>
  <nt2:status>Approved</nt2:status>
  <nt2:type>Descriptor</nt2:type>
  <nt2:inputdate>2007-01-11</nt2:inputdate>
  <dcterms:dateAccepted>2006-12-01</dcterms:dateAccepted>
  <dcterms:modified>2007-01-11</dcterms:modified>
  <nt2:notValidDate></nt2:notValidDate>
  <nt2:code>02</nt2:code>
 </skos:Concept>
 <skos:Concept rdf:about='subj:03'>
  <skos:prefLabel>Air Transportation and Safety</skos:prefLabel>
  <skos:scopeNote>Includes passenger and cargo air transport operations;
    airport ground operations; flight safety and hazards; and
    aircraft accidents. Systems and hardware specific to ground
    operations of aircraft and to airport construction are
    covered in 09 Research and Support Facilities (Air). Air
    traffic control is covered in 04 Aircraft Communications
    and Navigation. For related information see also 16 Space
    Transportation and Safety; and 85 Technology Utilization
    and Surface Transportation.
  </skos:scopeNote>
  <skos:altLabel>accidents and emergencies (aircraft)</skos:altLabel>
  <skos:altLabel>air piracy (incident or safety aspects)</skos:altLabel>
  <skos:altLabel>air safety</skos:altLabel>
  <skos:altLabel>air transportation</skos:altLabel>
  <skos:altLabel>aircraft accidents</skos:altLabel>
  <skos:altLabel>aircraft aging (safety)</skos:altLabel>
  <skos:altLabel>aircraft ditching</skos:altLabel>
  <skos:altLabel>aircraft durability</skos:altLabel>
  <skos:altLabel>aircraft emergencies</skos:altLabel>
  <skos:altLabel>aircraft health management</skos:altLabel>
  <skos:altLabel>aircraft in-flight collision</skos:altLabel>
  <skos:altLabel>aircraft licensing</skos:altLabel>
  <skos:altLabel>aircraft near miss</skos:altLabel>
  <skos:altLabel>aircraft operating problems</skos:altLabel>
  <skos:altLabel>aircraft safety</skos:altLabel>
  <skos:altLabel>aircraft search and rescue operations</skos:altLabel>
  <skos:altLabel>aircrew licensing</skos:altLabel>
  <skos:altLabel>aircrew training</skos:altLabel>
  <skos:altLabel>airport noise</skos:altLabel>
  <skos:altLabel>airport operations</skos:altLabel>
  <skos:altLabel>airport security</skos:altLabel>
  <skos:altLabel>airworthiness</skos:altLabel>
  <skos:altLabel>baggage handling (aircraft)</skos:altLabel>
  <skos:altLabel>bird collision (air transportation and safety)</skos:altLabel>
  <skos:altLabel>bird ingestion (air transportation and safety)</skos:altLabel>
  <skos:altLabel>cargo air transport operations</skos:altLabel>
  <skos:altLabel>cargo handling (aircraft)</skos:altLabel>
  <skos:altLabel>cargo transportation (aircraft)</skos:altLabel>
  <skos:altLabel>clear air turbulence (aircraft safety)</skos:altLabel>
  <skos:altLabel>collision avoidance (aircraft safety)</skos:altLabel>
  <skos:altLabel>crashworthiness (aircraft)</skos:altLabel>
  <skos:altLabel>ejection systems and seats (air transportation and safety)</skos:altLabel>
  <skos:altLabel>emergency locater transmitters</skos:altLabel>
  <skos:altLabel>escape systems (aircraft)</skos:altLabel>
  <skos:altLabel>explosions (aircraft)</skos:altLabel>
  <skos:altLabel>fail safety systems (aircraft)</skos:altLabel>
  <skos:altLabel>fire (aircraft)</skos:altLabel>
  <skos:altLabel>flight hazards (aircraft)</skos:altLabel>
  <skos:altLabel>flight safety (aircraft)</skos:altLabel>
  <skos:altLabel>flotation devices</skos:altLabel>
  <skos:altLabel>foreign object damage (FOD)</skos:altLabel>
  <skos:altLabel>foreign object ingestion (air transportation and safety)</skos:altLabel>
  <skos:altLabel>icing (aircraft)</skos:altLabel>
  <skos:altLabel>inspection (aircraft safety)</skos:altLabel>
  <skos:altLabel>lightning discharge on aircraft</skos:altLabel>
  <skos:altLabel>parachutes (personal and aircraft applications)</skos:altLabel>
  <skos:altLabel>passenger air transport operations</skos:altLabel>
  <skos:altLabel>passenger handling (air transportation)</skos:altLabel>
  <skos:altLabel>passenger transportation (air)</skos:altLabel>
  <skos:altLabel>public nuisance implications</skos:altLabel>
  <skos:altLabel>restraint harness (aircraft)</skos:altLabel>
  <skos:altLabel>runway safety</skos:altLabel>
  <skos:altLabel>safety systems (aircraft)</skos:altLabel>
  <skos:altLabel>search and rescue operations (air)</skos:altLabel>
  <skos:altLabel>seat belts (aircraft)</skos:altLabel>
  <skos:altLabel>severe storms (aircraft safety)</skos:altLabel>
  <skos:altLabel>shoulder harness (aircraft)</skos:altLabel>
  <skos:altLabel>survival (aircraft operations)</skos:altLabel>
  <skos:altLabel>taxiing (aircraft)</skos:altLabel>
  <skos:broader rdf:resource='subj:101'/>
  <nt2:status>Approved</nt2:status>
  <nt2:type>Descriptor</nt2:type>
  <nt2:inputdate>2007-01-11</nt2:inputdate>
  <dcterms:dateAccepted>2006-12-01</dcterms:dateAccepted>
  <dcterms:modified>2007-01-11</dcterms:modified>
  <nt2:notValidDate></nt2:notValidDate>
  <nt2:code>03</nt2:code>
 </skos:Concept>
 <skos:Concept rdf:about='subj:46'>
  <skos:prefLabel>Geophysics</skos:prefLabel>
  <skos:scopeNote>Includes earth structure and dynamics, aeronomy; upper and
    lower atmosphere studies; ionospheric and magnetospheric
    physics; and geomagnetism. For related information see 47
    Meteorology and Climatology; and 93 Space Radiation.
  </skos:scopeNote>
  <skos:altLabel>aeronomy</skos:altLabel>
  <skos:altLabel>aerosols (atmospheric physics )</skos:altLabel>
  <skos:altLabel>air glow</skos:altLabel>
  <skos:altLabel>atmospheric boundary layers (atmospheric physics)</skos:altLabel>
  <skos:altLabel>atmospheric circulation (atmospheric physics)</skos:altLabel>
  <skos:altLabel>atmospheric density</skos:altLabel>
  <skos:altLabel>atmospheric electricity</skos:altLabel>
  <skos:altLabel>atmospheric optics</skos:altLabel>
  <skos:altLabel>atmospheric physics</skos:altLabel>
  <skos:altLabel>atmospheric radiation</skos:altLabel>
  <skos:altLabel>atmospheric scattering</skos:altLabel>
  <skos:altLabel>atmospheric structure</skos:altLabel>
  <skos:altLabel>atmospheric studies (physical processes)</skos:altLabel>
  <skos:altLabel>atmospherics</skos:altLabel>
  <skos:altLabel>aurora</skos:altLabel>
  <skos:altLabel>biosphere (physical processes)</skos:altLabel>
  <skos:altLabel>continental drift</skos:altLabel>
  <skos:altLabel>Earth magnetic field</skos:altLabel>
  <skos:altLabel>Earth origins</skos:altLabel>
  <skos:altLabel>Earth structure</skos:altLabel>
  <skos:altLabel>Earth-reflected radiation</skos:altLabel>
  <skos:altLabel>fault detection (geological)</skos:altLabel>
  <skos:altLabel>general circulation models (atmosphere)</skos:altLabel>
  <skos:altLabel>geochemistry</skos:altLabel>
  <skos:altLabel>geodesy (physics)</skos:altLabel>
  <skos:altLabel>geological surveys</skos:altLabel>
  <skos:altLabel>geology (Earth structure)</skos:altLabel>
  <skos:altLabel>geomagnetism</skos:altLabel>
  <skos:altLabel>geomorphology</skos:altLabel>
  <skos:altLabel>geophysical sensors (applications)</skos:altLabel>
  <skos:altLabel>glaciology</skos:altLabel>
  <skos:altLabel>gravitational anomalies (terrestrial)</skos:altLabel>
  <skos:altLabel>gravitational theory (terrestrial)</skos:altLabel>
  <skos:altLabel>gravitational waves (terrestrial)</skos:altLabel>
  <skos:altLabel>greenhouse effect (atmospheric physics)</skos:altLabel>
  <skos:altLabel>hydrosphere studies</skos:altLabel>
  <skos:altLabel>infrared spectrometry (atmosphere)</skos:altLabel>
  <skos:altLabel>ionosphere (Earth)</skos:altLabel>
  <skos:altLabel>ionospheric electron density</skos:altLabel>
  <skos:altLabel>ionospheric physics</skos:altLabel>
  <skos:altLabel>ionospheric plasmas</skos:altLabel>
  <skos:altLabel>ionospheric scintillation</skos:altLabel>
  <skos:altLabel>lithology</skos:altLabel>
  <skos:altLabel>lower atmosphere studies</skos:altLabel>
  <skos:altLabel>magnetism (terrestrial)</skos:altLabel>
  <skos:altLabel>magnetosphere (Earth)</skos:altLabel>
  <skos:altLabel>noctilucent clouds</skos:altLabel>
  <skos:altLabel>ozone depletion (atmospheric physics)</skos:altLabel>
  <skos:altLabel>plate tectonics</skos:altLabel>
  <skos:altLabel>rocket/balloon geophysical studies</skos:altLabel>
  <skos:altLabel>seismology</skos:altLabel>
  <skos:altLabel>soil mechanics</skos:altLabel>
  <skos:altLabel>soil sampling</skos:altLabel>
  <skos:altLabel>solar-atmosphere interactions</skos:altLabel>
  <skos:altLabel>space geodesy</skos:altLabel>
  <skos:altLabel>stratosphere</skos:altLabel>
  <skos:altLabel>stratospheric circulation</skos:altLabel>
  <skos:altLabel>tectonics</skos:altLabel>
  <skos:altLabel>upper atmosphere studies</skos:altLabel>
  <skos:altLabel>very long baseline interferometry (geophysics applications)</skos:altLabel>
  <skos:altLabel>volcanoes</skos:altLabel>
  <skos:altLabel>whistlers (upper atmosphere)</skos:altLabel>
  <skos:broader rdf:resource='subj:1874'/>
  <nt2:status>Approved</nt2:status>
  <nt2:type>Descriptor</nt2:type>
  <nt2:inputdate>2007-01-11</nt2:inputdate>
  <dcterms:dateAccepted>2006-12-01</dcterms:dateAccepted>
  <dcterms:modified>2007-01-11</dcterms:modified>
  <nt2:notValidDate></nt2:notValidDate>
  <nt2:code>46</nt2:code>
 </skos:Concept>
 <skos:Concept rdf:about='subj:1874'>
  <skos:prefLabel>Geosciences</skos:prefLabel>
  <skos:scopeNote>Includes geosciences (general); earth resources and remote
    sensing; energy production and conversion; environment
    pollution; geophysics; meteorology and climatology; and
    oceanography. For related information see also Space
    Sciences (categories 88 through 93).
  </skos:scopeNote>
  <skos:broader rdf:resource='subj:100'/>
  <skos:narrower rdf:resource='subj:43'/>
  <skos:narrower rdf:resource='subj:44'/>
  <skos:narrower rdf:resource='subj:45'/>
  <skos:narrower rdf:resource='subj:46'/>
  <skos:narrower rdf:resource='subj:42'/>
  <skos:narrower rdf:resource='subj:47'/>
  <skos:narrower rdf:resource='subj:48'/>
  <nt2:status>Approved</nt2:status>
  <nt2:type>Descriptor</nt2:type>
  <nt2:inputdate>2007-01-11</nt2:inputdate>
  <dcterms:dateAccepted>2006-12-01</dcterms:dateAccepted>
  <dcterms:modified>2007-01-11</dcterms:modified>
  <nt2:notValidDate></nt2:notValidDate>
  <nt2:code>1874</nt2:code>
 </skos:Concept>
 <skos:Concept rdf:about='subj:61'>
  <skos:prefLabel>Computer Programming and Software</skos:prefLabel>
  <skos:scopeNote>Includes software engineering, computer programs, routines,
    algorithms, and specific applications, e.g., CAD/CAM. For
    computer software applied to specific applications, see
    also the associated category.
  </skos:scopeNote>
  <skos:altLabel>algorithms (computer operations)</skos:altLabel>
  <skos:altLabel>CAD (computer aided design)</skos:altLabel>
  <skos:altLabel>CAM (computer aided manufacturing)</skos:altLabel>
  <skos:altLabel>coding techniques (computer programming)</skos:altLabel>
  <skos:altLabel>compilers (software)</skos:altLabel>
  <skos:altLabel>computer aided design (CAD)</skos:altLabel>
  <skos:altLabel>computer aided manufacturing (CAM)</skos:altLabel>
  <skos:altLabel>computer architecture</skos:altLabel>
  <skos:altLabel>computer graphics (software)</skos:altLabel>
  <skos:altLabel>computer programming</skos:altLabel>
  <skos:altLabel>computer routines</skos:altLabel>
  <skos:altLabel>computer software</skos:altLabel>
  <skos:altLabel>computerized simulation (general)</skos:altLabel>
  <skos:altLabel>data acquisition programs</skos:altLabel>
  <skos:altLabel>debugging programs</skos:altLabel>
  <skos:altLabel>diagnostic procedures (software)</skos:altLabel>
  <skos:altLabel>document markup languages (computer programming)</skos:altLabel>
  <skos:altLabel>error correction codes</skos:altLabel>
  <skos:altLabel>fault tolerant software</skos:altLabel>
  <skos:altLabel>flight computer software</skos:altLabel>
  <skos:altLabel>formalism (computer programming)</skos:altLabel>
  <skos:altLabel>interpreters (software)</skos:altLabel>
  <skos:altLabel>object oriented programming</skos:altLabel>
  <skos:altLabel>operating systems (computers)</skos:altLabel>
  <skos:altLabel>programming (computers)</skos:altLabel>
  <skos:altLabel>programming languages</skos:altLabel>
  <skos:altLabel>protocol checking</skos:altLabel>
  <skos:altLabel>software debugging</skos:altLabel>
  <skos:altLabel>software engineering</skos:altLabel>
  <skos:altLabel>software reuse</skos:altLabel>
  <skos:broader rdf:resource='subj:2321'/>
  <nt2:status>Approved</nt2:status>
  <nt2:type>Descriptor</nt2:type>
  <nt2:inputdate>2007-01-11</nt2:inputdate>
  <dcterms:dateAccepted>2006-12-01</dcterms:dateAccepted>
  <dcterms:modified>2007-01-11</dcterms:modified>
  <nt2:notValidDate></nt2:notValidDate>
  <nt2:code>61</nt2:code>
 </skos:Concept>
 <skos:Concept rdf:about='subj:14'>
  <skos:prefLabel>Ground Support Systems and Facilities (Space)</skos:prefLabel>
  <skos:scopeNote>Includes launch complexes, research and production
    facilities; ground support equipment, e.g., mobile
    transporters; and test chambers and simulators. Also
    includes extraterrestrial bases and supporting equipment.
    For related information see also 09 Research and Support
    Facilities (Air).
  </skos:scopeNote>
  <skos:altLabel>accelerators (aerospace)</skos:altLabel>
  <skos:altLabel>assembly buildings</skos:altLabel>
  <skos:altLabel>astronaut training facilities</skos:altLabel>
  <skos:altLabel>automatic picture transmission (APT) ground stations</skos:altLabel>
  <skos:altLabel>block houses</skos:altLabel>
  <skos:altLabel>checkout facilities (space)</skos:altLabel>
  <skos:altLabel>checkout systems (space)</skos:altLabel>
  <skos:altLabel>clean rooms (space)</skos:altLabel>
  <skos:altLabel>deep space instrumentation facilities</skos:altLabel>
  <skos:altLabel>development facilities (space)</skos:altLabel>
  <skos:altLabel>electromagnetic launchers (facilities)</skos:altLabel>
  <skos:altLabel>engine test blocks (space)</skos:altLabel>
  <skos:altLabel>engine test stands (space)</skos:altLabel>
  <skos:altLabel>extraterrestrial bases</skos:altLabel>
  <skos:altLabel>flight simulators (space)</skos:altLabel>
  <skos:altLabel>gravity simulators</skos:altLabel>
  <skos:altLabel>ground support equipment (space)</skos:altLabel>
  <skos:altLabel>ground support facilities (space)</skos:altLabel>
  <skos:altLabel>ground support systems (space)</skos:altLabel>
  <skos:altLabel>ground support vehicles (space)</skos:altLabel>
  <skos:altLabel>high temperature test facilities (space)</skos:altLabel>
  <skos:altLabel>laser range finder facilities</skos:altLabel>
  <skos:altLabel>laser space communications facilities</skos:altLabel>
  <skos:altLabel>launch complexes</skos:altLabel>
  <skos:altLabel>launch facilities</skos:altLabel>
  <skos:altLabel>launch pads and bases</skos:altLabel>
  <skos:altLabel>launch towers</skos:altLabel>
  <skos:altLabel>launch vehicle simulators</skos:altLabel>
  <skos:altLabel>light gas guns (launch facilities)</skos:altLabel>
  <skos:altLabel>low temperature test facilities (space)</skos:altLabel>
  <skos:altLabel>lunar and planetary bases</skos:altLabel>
  <skos:altLabel>lunar gravity simulators</skos:altLabel>
  <skos:altLabel>lunar roving vehicles</skos:altLabel>
  <skos:altLabel>maintenance facilities (space based, ground based)</skos:altLabel>
  <skos:altLabel>mobile lunar laboratories</skos:altLabel>
  <skos:altLabel>mobile planetary laboratories</skos:altLabel>
  <skos:altLabel>mobile transporters</skos:altLabel>
  <skos:altLabel>optical tracking stations</skos:altLabel>
  <skos:altLabel>overhaul facilities (space)</skos:altLabel>
  <skos:altLabel>payload operations and support</skos:altLabel>
  <skos:altLabel>planetary roving vehicles</skos:altLabel>
  <skos:altLabel>pressure test facilities (space)</skos:altLabel>
  <skos:altLabel>rail accelerators, railguns, launchers (applications)</skos:altLabel>
  <skos:altLabel>range safety</skos:altLabel>
  <skos:altLabel>recovery equipment and vehicles</skos:altLabel>
  <skos:altLabel>remote launch monitoring facilities</skos:altLabel>
  <skos:altLabel>repair facilities (space based, ground based)</skos:altLabel>
  <skos:altLabel>research facilities (space)</skos:altLabel>
  <skos:altLabel>rocket engine test pads</skos:altLabel>
  <skos:altLabel>rocket sleds</skos:altLabel>
  <skos:altLabel>rocket test facilities</skos:altLabel>
  <skos:altLabel>rover vehicles</skos:altLabel>
  <skos:altLabel>shuttlecraft landing facilities</skos:altLabel>
  <skos:altLabel>simulators (space)</skos:altLabel>
  <skos:altLabel>solar heating simulators</skos:altLabel>
  <skos:altLabel>solar simulators</skos:altLabel>
  <skos:altLabel>space facility for cryogenic materials</skos:altLabel>
  <skos:altLabel>space research facilities</skos:altLabel>
  <skos:altLabel>space simulators</skos:altLabel>
  <skos:altLabel>space vacuum simulators</skos:altLabel>
  <skos:altLabel>spacecraft maintenance facilities</skos:altLabel>
  <skos:altLabel>spacecraft production facilities</skos:altLabel>
  <skos:altLabel>spacecraft simulators</skos:altLabel>
  <skos:altLabel>spaceport planning</skos:altLabel>
  <skos:altLabel>spaceports</skos:altLabel>
  <skos:altLabel>special vehicles (land, sea, air)</skos:altLabel>
  <skos:altLabel>transportation or rescue of astronautics or</skos:altLabel>
  <skos:altLabel>astronautic-oriented equipment)</skos:altLabel>
  <skos:altLabel>storage facilities for propellants and cryogenics</skos:altLabel>
  <skos:altLabel>structures test facilities (space)</skos:altLabel>
  <skos:altLabel>support facilities</skos:altLabel>
  <skos:altLabel>surface exploration vehicles</skos:altLabel>
  <skos:altLabel>temperature test facilities (space)</skos:altLabel>
  <skos:altLabel>test facilities (space)</skos:altLabel>
  <skos:altLabel>test range facilities</skos:altLabel>
  <skos:altLabel>test ranges</skos:altLabel>
  <skos:altLabel>umbilical towers</skos:altLabel>
  <skos:altLabel>vacuum test facilities</skos:altLabel>
  <skos:altLabel>wind tunnel test facilities (launch and space vehicles)</skos:altLabel>
  <skos:altLabel>wind tunnel tests (launch and space vehicles)</skos:altLabel>
  <skos:broader rdf:resource='subj:578'/>
  <nt2:status>Approved</nt2:status>
  <nt2:type>Descriptor</nt2:type>
  <nt2:inputdate>2007-01-11</nt2:inputdate>
  <dcterms:dateAccepted>2006-12-01</dcterms:dateAccepted>
  <dcterms:modified>2007-01-11</dcterms:modified>
  <nt2:notValidDate></nt2:notValidDate>
  <nt2:code>14</nt2:code>
 </skos:Concept>
 <skos:Concept rdf:about='subj:53'>
  <skos:prefLabel>Behavioral Sciences</skos:prefLabel>
  <skos:scopeNote>Includes psychological factors; individual and group
    behavior; crew training and evaluation; and psychiatric
    research.
  </skos:scopeNote>
  <skos:altLabel>astronaut health (psychological)</skos:altLabel>
  <skos:altLabel>aviation psychology</skos:altLabel>
  <skos:altLabel>confinement (psychological effects, human)</skos:altLabel>
  <skos:altLabel>crew evaluation</skos:altLabel>
  <skos:altLabel>crew training</skos:altLabel>
  <skos:altLabel>effects of radiation (psychological, human)</skos:altLabel>
  <skos:altLabel>effects of stress (psychological, human)</skos:altLabel>
  <skos:altLabel>fatigue (psychological, human)</skos:altLabel>
  <skos:altLabel>flying training</skos:altLabel>
  <skos:altLabel>group behavior</skos:altLabel>
  <skos:altLabel>human behavior</skos:altLabel>
  <skos:altLabel>isolation effects (psychological, human)</skos:altLabel>
  <skos:altLabel>mental adaptation to flight</skos:altLabel>
  <skos:altLabel>perception (psychological, human)</skos:altLabel>
  <skos:altLabel>pilot performance</skos:altLabel>
  <skos:altLabel>psychological effects of flight</skos:altLabel>
  <skos:altLabel>psychological factors</skos:altLabel>
  <skos:altLabel>sensory deprivation (psychological effects, human)</skos:altLabel>
  <skos:altLabel>sleep deprivation (psychological effects, human)</skos:altLabel>
  <skos:altLabel>social interaction</skos:altLabel>
  <skos:altLabel>sociological research (psychology, human)</skos:altLabel>
  <skos:altLabel>space adaptation (psychological effects, human)</skos:altLabel>
  <skos:altLabel>space flight effects (psychological, human)</skos:altLabel>
  <skos:altLabel>stress (psychological effects, human)</skos:altLabel>
  <skos:altLabel>weightlessness effects (psychological, human)</skos:altLabel>
  <skos:broader rdf:resource='subj:2127'/>
  <nt2:status>Approved</nt2:status>
  <nt2:type>Descriptor</nt2:type>
  <nt2:inputdate>2007-01-11</nt2:inputdate>
  <dcterms:dateAccepted>2006-12-01</dcterms:dateAccepted>
  <dcterms:modified>2007-01-11</dcterms:modified>
  <nt2:notValidDate></nt2:notValidDate>
  <nt2:code>53</nt2:code>
 </skos:Concept>
 <skos:Concept rdf:about='subj:27'>
  <skos:prefLabel>Nonmetallic Materials</skos:prefLabel>
  <skos:scopeNote>Includes physical, chemical, and mechanical properties of
    plastics, elastomers, lubricants, polymers, textiles,
    adhesives, and ceramic materials. For composite materials
    see 24 Composite Materials.
  </skos:scopeNote>
  <skos:altLabel>ablative materials (nonmetallic)</skos:altLabel>
  <skos:altLabel>adhesives</skos:altLabel>
  <skos:altLabel>cements</skos:altLabel>
  <skos:altLabel>ceramic materials</skos:altLabel>
  <skos:altLabel>chemical properties of nonmetallic materials</skos:altLabel>
  <skos:altLabel>cleaners</skos:altLabel>
  <skos:altLabel>compression strength (nonmetallic materials)</skos:altLabel>
  <skos:altLabel>creep strength (nonmetallic materials)</skos:altLabel>
  <skos:altLabel>crystal structure (nonmetallic materials)</skos:altLabel>
  <skos:altLabel>crystals (nonmetallic)</skos:altLabel>
  <skos:altLabel>development of nonmetallic materials</skos:altLabel>
  <skos:altLabel>elastomers</skos:altLabel>
  <skos:altLabel>evaluation of nonmetallic materials</skos:altLabel>
  <skos:altLabel>fabrics (nonmetallic materials)</skos:altLabel>
  <skos:altLabel>fatigue (nonmetallic materials)</skos:altLabel>
  <skos:altLabel>ferrofluids</skos:altLabel>
  <skos:altLabel>fibers (nonmetallic materials)</skos:altLabel>
  <skos:altLabel>film strength</skos:altLabel>
  <skos:altLabel>flammability (nonmetallic materials)</skos:altLabel>
  <skos:altLabel>foam materials</skos:altLabel>
  <skos:altLabel>glass materials</skos:altLabel>
  <skos:altLabel>glues</skos:altLabel>
  <skos:altLabel>graphite</skos:altLabel>
  <skos:altLabel>greases</skos:altLabel>
  <skos:altLabel>hydraulic fluids</skos:altLabel>
  <skos:altLabel>hydrogels</skos:altLabel>
  <skos:altLabel>insulation (nonmetallic materials)</skos:altLabel>
  <skos:altLabel>lubricants</skos:altLabel>
  <skos:altLabel>lubrication properties of nonmetallic materials</skos:altLabel>
  <skos:altLabel>mechanical properties of nonmetallic materials</skos:altLabel>
  <skos:altLabel>nonmetallic fibers</skos:altLabel>
  <skos:altLabel>offgassing/outgassing (nonmetallic materials)</skos:altLabel>
  <skos:altLabel>packing (nonmetallic materials)</skos:altLabel>
  <skos:altLabel>paints</skos:altLabel>
  <skos:altLabel>paper</skos:altLabel>
  <skos:altLabel>patching compounds</skos:altLabel>
  <skos:altLabel>physical properties of nonmetallic materials</skos:altLabel>
  <skos:altLabel>plastics</skos:altLabel>
  <skos:altLabel>plywoods</skos:altLabel>
  <skos:altLabel>polymers</skos:altLabel>
  <skos:altLabel>protection of materials (nonmetallic)</skos:altLabel>
  <skos:altLabel>protective coatings (nonmetallic)</skos:altLabel>
  <skos:altLabel>radomes (nonmetallic materials)</skos:altLabel>
  <skos:altLabel>reinforcing filaments (nonmetallic)</skos:altLabel>
  <skos:altLabel>research on nonmetallic materials</skos:altLabel>
  <skos:altLabel>rubber</skos:altLabel>
  <skos:altLabel>sealants (nonmetallic materials)</skos:altLabel>
  <skos:altLabel>sheer strength (nonmetallic materials)</skos:altLabel>
  <skos:altLabel>silicon materials</skos:altLabel>
  <skos:altLabel>solvents</skos:altLabel>
  <skos:altLabel>surface properties (nonmetallic materials)</skos:altLabel>
  <skos:altLabel>tensile strength (nonmetallic materials)</skos:altLabel>
  <skos:altLabel>testing of materials (nonmetallic)</skos:altLabel>
  <skos:altLabel>textiles</skos:altLabel>
  <skos:altLabel>whiskers (nonmetallic materials)</skos:altLabel>
  <skos:altLabel>woods</skos:altLabel>
  <skos:broader rdf:resource='subj:1058'/>
  <nt2:status>Approved</nt2:status>
  <nt2:type>Descriptor</nt2:type>
  <nt2:inputdate>2007-01-11</nt2:inputdate>
  <dcterms:dateAccepted>2006-12-01</dcterms:dateAccepted>
  <dcterms:modified>2007-01-11</dcterms:modified>
  <nt2:notValidDate></nt2:notValidDate>
  <nt2:code>27</nt2:code>
 </skos:Concept>
 <skos:Concept rdf:about='subj:80'>
  <skos:prefLabel>Social and Information Sciences (General)</skos:prefLabel>
  <skos:scopeNote>Includes general research topics related to sociology;
    educational programs and curricula.
  </skos:scopeNote>
  <skos:altLabel>educational curricula</skos:altLabel>
  <skos:altLabel>educational programs</skos:altLabel>
  <skos:altLabel>social sciences</skos:altLabel>
  <skos:altLabel>sociological research (humanities)</skos:altLabel>
  <skos:broader rdf:resource='subj:2767'/>
  <nt2:status>Approved</nt2:status>
  <nt2:type>Descriptor</nt2:type>
  <nt2:inputdate>2007-01-11</nt2:inputdate>
  <dcterms:dateAccepted>2006-12-01</dcterms:dateAccepted>
  <dcterms:modified>2007-01-11</dcterms:modified>
  <nt2:notValidDate></nt2:notValidDate>
  <nt2:code>80</nt2:code>
 </skos:Concept>
 <skos:Concept rdf:about='subj:2871'>
  <skos:prefLabel>Space Sciences</skos:prefLabel>
  <skos:scopeNote>Includes space sciences (general); astronomy; astrophysics;
    lunar and planetary science and exploration; solar physics;
    and space radiation. For related information see also
    Geosciences (categories 42 through 48).
  </skos:scopeNote>
  <skos:broader rdf:resource='subj:100'/>
  <skos:narrower rdf:resource='subj:89'/>
  <skos:narrower rdf:resource='subj:90'/>
  <skos:narrower rdf:resource='subj:91'/>
  <skos:narrower rdf:resource='subj:92'/>
  <skos:narrower rdf:resource='subj:93'/>
  <skos:narrower rdf:resource='subj:88'/>
  <nt2:status>Approved</nt2:status>
  <nt2:type>Descriptor</nt2:type>
  <nt2:inputdate>2007-01-11</nt2:inputdate>
  <dcterms:dateAccepted>2006-12-01</dcterms:dateAccepted>
  <dcterms:modified>2007-01-11</dcterms:modified>
  <nt2:notValidDate></nt2:notValidDate>
  <nt2:code>2871</nt2:code>
 </skos:Concept>
 <skos:Concept rdf:about='subj:76'>
  <skos:prefLabel>Solid-State Physics</skos:prefLabel>
  <skos:scopeNote>Includes condensed matter physics, crystallography, and
    superconductivity. For related information see also 33
    Electronics and Electrical Engineering; and 36 Lasers and
    Masers.
  </skos:scopeNote>
  <skos:altLabel>acceptors (solid state)</skos:altLabel>
  <skos:altLabel>band structure of solids</skos:altLabel>
  <skos:altLabel>condensed matter physics</skos:altLabel>
  <skos:altLabel>conductivity (solid state)</skos:altLabel>
  <skos:altLabel>critical field curves of superconducting materials</skos:altLabel>
  <skos:altLabel>critical temperatures of superconducting materials</skos:altLabel>
  <skos:altLabel>crystal defects</skos:altLabel>
  <skos:altLabel>crystal growth (general)</skos:altLabel>
  <skos:altLabel>crystal structure (semiconductors)</skos:altLabel>
  <skos:altLabel>crystallography</skos:altLabel>
  <skos:altLabel>dielectric materials properties</skos:altLabel>
  <skos:altLabel>donors (solid state)</skos:altLabel>
  <skos:altLabel>electrical transport properties in solids</skos:altLabel>
  <skos:altLabel>electron energy bands</skos:altLabel>
  <skos:altLabel>electron motion in conductors</skos:altLabel>
  <skos:altLabel>electron paramagnetic resonance (solid state)</skos:altLabel>
  <skos:altLabel>energy gaps in semiconductors</skos:altLabel>
  <skos:altLabel>epitaxy</skos:altLabel>
  <skos:altLabel>holes (electron deficiencies)</skos:altLabel>
  <skos:altLabel>lattice vibrations</skos:altLabel>
  <skos:altLabel>liquid crystals</skos:altLabel>
  <skos:altLabel>Mossbauer effect</skos:altLabel>
  <skos:altLabel>piezoelectricity</skos:altLabel>
  <skos:altLabel>radiation effects in semiconductors</skos:altLabel>
  <skos:altLabel>semiconductor materials</skos:altLabel>
  <skos:altLabel>solid state physics</skos:altLabel>
  <skos:altLabel>solidification (solid state)</skos:altLabel>
  <skos:altLabel>superconducting materials</skos:altLabel>
  <skos:altLabel>superconductivity (theory)</skos:altLabel>
  <skos:altLabel>thermoelectric materials</skos:altLabel>
  <skos:altLabel>thin films (theory, deposition and growth)</skos:altLabel>
  <skos:broader rdf:resource='subj:2528'/>
  <nt2:status>Approved</nt2:status>
  <nt2:type>Descriptor</nt2:type>
  <nt2:inputdate>2007-01-11</nt2:inputdate>
  <dcterms:dateAccepted>2006-12-01</dcterms:dateAccepted>
  <dcterms:modified>2007-01-11</dcterms:modified>
  <nt2:notValidDate></nt2:notValidDate>
  <nt2:code>76</nt2:code>
 </skos:Concept>
 <skos:Concept rdf:about='subj:16'>
  <skos:prefLabel>Space Transportation and Safety</skos:prefLabel>
  <skos:scopeNote>Includes passenger and cargo space transportation, e.g.,
    shuttle operations; and space rescue techniques. For
    related information see also 03 Air Transportation and
    Safety; 15 Launch Vehicles and Launch Operations; and 18
    Spacecraft Design, Testing and Performance. For space suits
    see 54 Man/System Technology and Life Support.
  </skos:scopeNote>
  <skos:altLabel>accidents and emergencies (spacecraft)</skos:altLabel>
  <skos:altLabel>cargo handling (spacecraft)</skos:altLabel>
  <skos:altLabel>cargo transportation (spacecraft)</skos:altLabel>
  <skos:altLabel>escape systems (spacecraft)</skos:altLabel>
  <skos:altLabel>explosions (spacecraft)</skos:altLabel>
  <skos:altLabel>extravehicular activity (EVA) (operations)</skos:altLabel>
  <skos:altLabel>fire (spacecraft)</skos:altLabel>
  <skos:altLabel>flight safety (spacecraft)</skos:altLabel>
  <skos:altLabel>orbiting maneuvering vehicles</skos:altLabel>
  <skos:altLabel>parachutes (spacecraft applications)</skos:altLabel>
  <skos:altLabel>passenger handling (space transportation)</skos:altLabel>
  <skos:altLabel>passenger transportation (space)</skos:altLabel>
  <skos:altLabel>Payload Assist Module (PAM) assist</skos:altLabel>
  <skos:altLabel>payload delivery (space transportation)</skos:altLabel>
  <skos:altLabel>payload handling (space transportation)</skos:altLabel>
  <skos:altLabel>payload retrieval (space transportation)</skos:altLabel>
  <skos:altLabel>recovery of spacecraft</skos:altLabel>
  <skos:altLabel>restraint harness (spacecraft)</skos:altLabel>
  <skos:altLabel>safety systems (spacecraft)</skos:altLabel>
  <skos:altLabel>search and rescue operations (space)</skos:altLabel>
  <skos:altLabel>shoulder harness (spacecraft)</skos:altLabel>
  <skos:altLabel>space debris (spaceflight hazard)</skos:altLabel>
  <skos:altLabel>space flight commercialization</skos:altLabel>
  <skos:altLabel>space flight hazards</skos:altLabel>
  <skos:altLabel>space operation emergencies</skos:altLabel>
  <skos:altLabel>space rescue</skos:altLabel>
  <skos:altLabel>space shuttle operations</skos:altLabel>
  <skos:altLabel>space transportation</skos:altLabel>
  <skos:altLabel>spacecraft ditching</skos:altLabel>
  <skos:altLabel>spacecraft health management</skos:altLabel>
  <skos:altLabel>spacecraft retrieval</skos:altLabel>
  <skos:altLabel>survival (space operations)</skos:altLabel>
  <skos:broader rdf:resource='subj:578'/>
  <nt2:status>Approved</nt2:status>
  <nt2:type>Descriptor</nt2:type>
  <nt2:inputdate>2007-01-11</nt2:inputdate>
  <dcterms:dateAccepted>2006-12-01</dcterms:dateAccepted>
  <dcterms:modified>2007-01-11</dcterms:modified>
  <nt2:notValidDate></nt2:notValidDate>
  <nt2:code>16</nt2:code>
 </skos:Concept>
 <skos:Concept rdf:about='subj:05'>
  <skos:prefLabel>Aircraft Design, Testing and Performance</skos:prefLabel>
  <skos:scopeNote>Includes all stages of design of aircraft and aircraft
    structures and systems. Also includes aircraft testing,
    performance, and evaluation, and aircraft and flight
    simulation technology. For related information see also 18
    Spacecraft Design, Testing and Performance; and 39
    Structural Mechanics. For land transportation vehicles see
    85 Technology Utilization and Surface Transportation.
  </skos:scopeNote>
  <skos:altLabel>aeroelasticity (property)</skos:altLabel>
  <skos:altLabel>aircraft components</skos:altLabel>
  <skos:altLabel>aircraft configurations</skos:altLabel>
  <skos:altLabel>aircraft descriptions (types/names/designations)</skos:altLabel>
  <skos:altLabel>aircraft design</skos:altLabel>
  <skos:altLabel>aircraft development</skos:altLabel>
  <skos:altLabel>aircraft evaluation</skos:altLabel>
  <skos:altLabel>aircraft flight tests</skos:altLabel>
  <skos:altLabel>aircraft performance</skos:altLabel>
  <skos:altLabel>aircraft simulation</skos:altLabel>
  <skos:altLabel>aircraft structures</skos:altLabel>
  <skos:altLabel>aircraft testing</skos:altLabel>
  <skos:altLabel>airship performance</skos:altLabel>
  <skos:altLabel>body-tail combinations (aircraft design)</skos:altLabel>
  <skos:altLabel>cabin pressurization (aircraft)</skos:altLabel>
  <skos:altLabel>deicing systems (aircraft)</skos:altLabel>
  <skos:altLabel>depressurization systems (aircraft)</skos:altLabel>
  <skos:altLabel>ejection systems and seats (design)</skos:altLabel>
  <skos:altLabel>expandable structures (aircraft)</skos:altLabel>
  <skos:altLabel>fins (aircraft)</skos:altLabel>
  <skos:altLabel>fuselages</skos:altLabel>
  <skos:altLabel>gliders (sailplanes, hang gliders)</skos:altLabel>
  <skos:altLabel>helicopter design</skos:altLabel>
  <skos:altLabel>helicopter ground resonance</skos:altLabel>
  <skos:altLabel>helicopter performance</skos:altLabel>
  <skos:altLabel>helicopter rotor dynamics</skos:altLabel>
  <skos:altLabel>Highly Maneuverable Aircraft Technology (HiMAT)</skos:altLabel>
  <skos:altLabel>hydraulic system (aircraft)</skos:altLabel>
  <skos:altLabel>inflatable structures (aircraft)</skos:altLabel>
  <skos:altLabel>in-flight simulation (aircraft)</skos:altLabel>
  <skos:altLabel>landing gear (aircraft)</skos:altLabel>
  <skos:altLabel>lifting bodies</skos:altLabel>
  <skos:altLabel>lighter-than-air craft (balloons, airships) design</skos:altLabel>
  <skos:altLabel>models (aircraft)</skos:altLabel>
  <skos:altLabel>noise reduction</skos:altLabel>
  <skos:altLabel>noise reduction (aircraft structures)</skos:altLabel>
  <skos:altLabel>or are affected by design, development, testing,</skos:altLabel>
  <skos:altLabel>pneumatic systems (aircraft)</skos:altLabel>
  <skos:altLabel>powerlift technology</skos:altLabel>
  <skos:altLabel>pressurization systems (aircraft)</skos:altLabel>
  <skos:altLabel>pressurized cabins</skos:altLabel>
  <skos:altLabel>remotely piloted vehicles (RPV)</skos:altLabel>
  <skos:altLabel>tail surfaces</skos:altLabel>
  <skos:altLabel>TAV (transatmospheric vehicles) (aircraft)</skos:altLabel>
  <skos:altLabel>tilt rotor aircraft</skos:altLabel>
  <skos:altLabel>tires (aircraft)</skos:altLabel>
  <skos:altLabel>transatmospheric vehicles (TAV) (aircraft)</skos:altLabel>
  <skos:altLabel>transition flight</skos:altLabel>
  <skos:altLabel>wheels (aircraft)</skos:altLabel>
  <skos:altLabel>wind tunnel tests (aircraft and components)</skos:altLabel>
  <skos:altLabel>wing-body combinations (aircraft design)</skos:altLabel>
  <skos:altLabel>wing-nacelle combinations (aircraft design)</skos:altLabel>
  <skos:altLabel>wings</skos:altLabel>
  <skos:broader rdf:resource='subj:101'/>
  <nt2:status>Approved</nt2:status>
  <nt2:type>Descriptor</nt2:type>
  <nt2:inputdate>2007-01-11</nt2:inputdate>
  <dcterms:dateAccepted>2006-12-01</dcterms:dateAccepted>
  <dcterms:modified>2007-01-11</dcterms:modified>
  <nt2:notValidDate></nt2:notValidDate>
  <nt2:code>05</nt2:code>
 </skos:Concept>
 <skos:Concept rdf:about='subj:52'>
  <skos:prefLabel>Aerospace Medicine</skos:prefLabel>
  <skos:scopeNote>Includes the biological and physiological effects of
    atmospheric and space flight (weightlessness, space
    radiation, acceleration, and altitude stress) on the human
    being; and the prevention of adverse effects of those
    environments. For psychological and behavioral effects of
    aerospace environments see 53 Behavioral Science. For the
    effects of space on animals and plants see 51 Life Sciences.
  </skos:scopeNote>
  <skos:altLabel>acceleration effects (biological, human)</skos:altLabel>
  <skos:altLabel>altitude effects (biological, human)</skos:altLabel>
  <skos:altLabel>anthropometry</skos:altLabel>
  <skos:altLabel>astronaut health (physical)</skos:altLabel>
  <skos:altLabel>atmospheric pressure effects (human)</skos:altLabel>
  <skos:altLabel>bioastronautics</skos:altLabel>
  <skos:altLabel>bioelectronic instruments (aerospace medicine)</skos:altLabel>
  <skos:altLabel>bioengineering (aerospace medicine)</skos:altLabel>
  <skos:altLabel>biomedical instruments (aerospace medicine)</skos:altLabel>
  <skos:altLabel>bone mass</skos:altLabel>
  <skos:altLabel>cardiac physiology (human)</skos:altLabel>
  <skos:altLabel>centrifugal motion effects</skos:altLabel>
  <skos:altLabel>circadian rhythm (human)</skos:altLabel>
  <skos:altLabel>clinical chemistry</skos:altLabel>
  <skos:altLabel>confinement (effects, human)</skos:altLabel>
  <skos:altLabel>Coriolis forces (physiological effects, human)</skos:altLabel>
  <skos:altLabel>deceleration effects (human)</skos:altLabel>
  <skos:altLabel>decompression sickness</skos:altLabel>
  <skos:altLabel>diurnal effects (human)</skos:altLabel>
  <skos:altLabel>dysbarism</skos:altLabel>
  <skos:altLabel>effects of atmospheric flight (human)</skos:altLabel>
  <skos:altLabel>effects of radiation (human)</skos:altLabel>
  <skos:altLabel>effects of space flight (human)</skos:altLabel>
  <skos:altLabel>effects of stress (human)</skos:altLabel>
  <skos:altLabel>electromagnetic field effects (physiological, human)</skos:altLabel>
  <skos:altLabel>environmental effects (human)</skos:altLabel>
  <skos:altLabel>exercise</skos:altLabel>
  <skos:altLabel>extravehicular activity (physiological effects)</skos:altLabel>
  <skos:altLabel>fatigue (physiological, human)</skos:altLabel>
  <skos:altLabel>genetics (human)</skos:altLabel>
  <skos:altLabel>gravitational effects (biological, human)</skos:altLabel>
  <skos:altLabel>high temperature effects (human)</skos:altLabel>
  <skos:altLabel>hypoxia (human)</skos:altLabel>
  <skos:altLabel>low temperature effects (human)</skos:altLabel>
  <skos:altLabel>magnetic field effects (human)</skos:altLabel>
  <skos:altLabel>microgravity effects (human)</skos:altLabel>
  <skos:altLabel>motion sickness</skos:altLabel>
  <skos:altLabel>neuroendocrinology</skos:altLabel>
  <skos:altLabel>orthostatic tolerance</skos:altLabel>
  <skos:altLabel>oxygen generation</skos:altLabel>
  <skos:altLabel>pathology (human)</skos:altLabel>
  <skos:altLabel>perception (biological, human)</skos:altLabel>
  <skos:altLabel>pharmacology</skos:altLabel>
  <skos:altLabel>physiological effects of flight (human)</skos:altLabel>
  <skos:altLabel>physiological factors (human)</skos:altLabel>
  <skos:altLabel>physiological monitoring devices (human)</skos:altLabel>
  <skos:altLabel>physiology (human)</skos:altLabel>
  <skos:altLabel>quarantine (human)</skos:altLabel>
  <skos:altLabel>radiation effects (human)</skos:altLabel>
  <skos:altLabel>radiobiography (human)</skos:altLabel>
  <skos:altLabel>reduced gravity effects (physiological, human)</skos:altLabel>
  <skos:altLabel>sensory deprivation (physiological effects, human)</skos:altLabel>
  <skos:altLabel>sensory organs (human)</skos:altLabel>
  <skos:altLabel>sleep apnea</skos:altLabel>
  <skos:altLabel>sleep deprivation (physiological effects, human)</skos:altLabel>
  <skos:altLabel>space adaptation (physiological, human)</skos:altLabel>
  <skos:altLabel>space environment effects (physiological, human)</skos:altLabel>
  <skos:altLabel>space flight effects (physiological, human)</skos:altLabel>
  <skos:altLabel>stress (physiological effects, human)</skos:altLabel>
  <skos:altLabel>stress effects of atmospheric flight (physiological, human)</skos:altLabel>
  <skos:altLabel>stress effects of space flight (physiological, human)</skos:altLabel>
  <skos:altLabel>temperature effects (human)</skos:altLabel>
  <skos:altLabel>tomography (medical applications)</skos:altLabel>
  <skos:altLabel>toxicology (human)</skos:altLabel>
  <skos:altLabel>vestibular effects (human)</skos:altLabel>
  <skos:altLabel>visual acuity</skos:altLabel>
  <skos:altLabel>weightlessness effects (physiological, human)</skos:altLabel>
  <skos:altLabel>zero gravity effects (physiological, human)</skos:altLabel>
  <skos:broader rdf:resource='subj:2127'/>
  <nt2:status>Approved</nt2:status>
  <nt2:type>Descriptor</nt2:type>
  <nt2:inputdate>2007-01-11</nt2:inputdate>
  <dcterms:dateAccepted>2006-12-01</dcterms:dateAccepted>
  <dcterms:modified>2007-01-11</dcterms:modified>
  <nt2:notValidDate></nt2:notValidDate>
  <nt2:code>52</nt2:code>
 </skos:Concept>
 <skos:Concept rdf:about='subj:67'>
  <skos:prefLabel>Theoretical Mathematics</skos:prefLabel>
  <skos:scopeNote>Includes algebra, functional analysis, geometry, topology,
    set theory, group theory and number theory.
  </skos:scopeNote>
  <skos:altLabel>Abelian groups</skos:altLabel>
  <skos:altLabel>algebraic systems</skos:altLabel>
  <skos:altLabel>Banach spaces</skos:altLabel>
  <skos:altLabel>Boolean algebra</skos:altLabel>
  <skos:altLabel>differential geometry</skos:altLabel>
  <skos:altLabel>field theory (mathematics)</skos:altLabel>
  <skos:altLabel>fractals</skos:altLabel>
  <skos:altLabel>functional analysis</skos:altLabel>
  <skos:altLabel>fuzzy sets</skos:altLabel>
  <skos:altLabel>geometry</skos:altLabel>
  <skos:altLabel>graph theory</skos:altLabel>
  <skos:altLabel>group theory</skos:altLabel>
  <skos:altLabel>Hamiltonian functions</skos:altLabel>
  <skos:altLabel>Hilbert spaces</skos:altLabel>
  <skos:altLabel>mathematical logic</skos:altLabel>
  <skos:altLabel>mathematical theories</skos:altLabel>
  <skos:altLabel>number theory</skos:altLabel>
  <skos:altLabel>operator theory (mathematics)</skos:altLabel>
  <skos:altLabel>parentology</skos:altLabel>
  <skos:altLabel>Riemann surfaces</skos:altLabel>
  <skos:altLabel>set theory</skos:altLabel>
  <skos:broader rdf:resource='subj:2321'/>
  <nt2:status>Approved</nt2:status>
  <nt2:type>Descriptor</nt2:type>
  <nt2:inputdate>2007-01-11</nt2:inputdate>
  <dcterms:dateAccepted>2006-12-01</dcterms:dateAccepted>
  <dcterms:modified>2007-01-11</dcterms:modified>
  <nt2:notValidDate></nt2:notValidDate>
  <nt2:code>67</nt2:code>
 </skos:Concept>
 <skos:Concept rdf:about='subj:90'>
  <skos:prefLabel>Astrophysics</skos:prefLabel>
  <skos:scopeNote>Includes cosmology; celestial mechanics; space plasmas; and
    interstellar and interplanetary gases and dust.
  </skos:scopeNote>
  <skos:altLabel>astrochemistry</skos:altLabel>
  <skos:altLabel>binaries (astrophysics)</skos:altLabel>
  <skos:altLabel>black holes (astrophysics)</skos:altLabel>
  <skos:altLabel>celestial body orbits</skos:altLabel>
  <skos:altLabel>celestial body physical properties</skos:altLabel>
  <skos:altLabel>celestial body trajectories</skos:altLabel>
  <skos:altLabel>celestial mechanics</skos:altLabel>
  <skos:altLabel>cosmic dust</skos:altLabel>
  <skos:altLabel>cosmic noise</skos:altLabel>
  <skos:altLabel>cosmology</skos:altLabel>
  <skos:altLabel>dark energy</skos:altLabel>
  <skos:altLabel>dark matter</skos:altLabel>
  <skos:altLabel>expansion of the universe</skos:altLabel>
  <skos:altLabel>galactic evolution</skos:altLabel>
  <skos:altLabel>galactic structure</skos:altLabel>
  <skos:altLabel>galaxies (astrophysics)</skos:altLabel>
  <skos:altLabel>galaxy clusters</skos:altLabel>
  <skos:altLabel>gravitational collapse (astrophysics)</skos:altLabel>
  <skos:altLabel>gravitational theory (astrophysics)</skos:altLabel>
  <skos:altLabel>gravitational waves (astrophysics)</skos:altLabel>
  <skos:altLabel>hydromagnetics (astrophysics)</skos:altLabel>
  <skos:altLabel>intergalactic dust</skos:altLabel>
  <skos:altLabel>intergalactic gases</skos:altLabel>
  <skos:altLabel>intergalactic matter</skos:altLabel>
  <skos:altLabel>interplanetary dust</skos:altLabel>
  <skos:altLabel>interplanetary gases</skos:altLabel>
  <skos:altLabel>interplanetary matter</skos:altLabel>
  <skos:altLabel>interplanetary shock waves</skos:altLabel>
  <skos:altLabel>interstellar dust</skos:altLabel>
  <skos:altLabel>interstellar gases</skos:altLabel>
  <skos:altLabel>interstellar matter</skos:altLabel>
  <skos:altLabel>Magellanic clouds</skos:altLabel>
  <skos:altLabel>magnetism (extraterrestrial)</skos:altLabel>
  <skos:altLabel>nebulae (astrophysics)</skos:altLabel>
  <skos:altLabel>novae (astrophysics)</skos:altLabel>
  <skos:altLabel>nuclear astrophysics</skos:altLabel>
  <skos:altLabel>physical properties of celestial bodies</skos:altLabel>
  <skos:altLabel>pulsars (astrophysics)</skos:altLabel>
  <skos:altLabel>quasars (astrophysics)</skos:altLabel>
  <skos:altLabel>solar system evolution</skos:altLabel>
  <skos:altLabel>space plasmas</skos:altLabel>
  <skos:altLabel>stars (astrophysics)</skos:altLabel>
  <skos:altLabel>stellar evolution</skos:altLabel>
  <skos:altLabel>stellar luminosity</skos:altLabel>
  <skos:altLabel>stellar magnetic fields</skos:altLabel>
  <skos:altLabel>stellar mass accretion</skos:altLabel>
  <skos:altLabel>stellar physics</skos:altLabel>
  <skos:altLabel>stellar systems</skos:altLabel>
  <skos:altLabel>supernovae (astrophysics)</skos:altLabel>
  <skos:altLabel>universe</skos:altLabel>
  <skos:broader rdf:resource='subj:2871'/>
  <nt2:status>Approved</nt2:status>
  <nt2:type>Descriptor</nt2:type>
  <nt2:inputdate>2007-01-11</nt2:inputdate>
  <dcterms:dateAccepted>2006-12-01</dcterms:dateAccepted>
  <dcterms:modified>2007-01-11</dcterms:modified>
  <nt2:notValidDate></nt2:notValidDate>
  <nt2:code>90</nt2:code>
 </skos:Concept>
 <skos:Concept rdf:about='subj:54'>
  <skos:prefLabel>Man/System Technology and Life Support</skos:prefLabel>
  <skos:scopeNote>Includes human factors engineering, bionics, man-machine
    systems, life support, space suits and protective clothing.
    For related information see also 16 Space Transportation;
    and 52 Aerospace Medicine.
  </skos:scopeNote>
  <skos:altLabel>bioengineering (man-machine systems)</skos:altLabel>
  <skos:altLabel>bioinstrumentation (physiological monitoring)</skos:altLabel>
  <skos:altLabel>bionics</skos:altLabel>
  <skos:altLabel>cabin pressurization (life support)</skos:altLabel>
  <skos:altLabel>closed ecological systems</skos:altLabel>
  <skos:altLabel>diets (space missions)</skos:altLabel>
  <skos:altLabel>extravehicular activity (EVA) (equipment)</skos:altLabel>
  <skos:altLabel>farming in space (life support)</skos:altLabel>
  <skos:altLabel>flight suits</skos:altLabel>
  <skos:altLabel>food (space missions)</skos:altLabel>
  <skos:altLabel>food preparation (space missions)</skos:altLabel>
  <skos:altLabel>food storage (space missions)</skos:altLabel>
  <skos:altLabel>helmets</skos:altLabel>
  <skos:altLabel>human factors engineering</skos:altLabel>
  <skos:altLabel>human productivity in space</skos:altLabel>
  <skos:altLabel>life support</skos:altLabel>
  <skos:altLabel>man-machine systems</skos:altLabel>
  <skos:altLabel>manned maneuvering units</skos:altLabel>
  <skos:altLabel>man-system interfaces</skos:altLabel>
  <skos:altLabel>oxygen systems (life support)</skos:altLabel>
  <skos:altLabel>pressurized cabins (life support)</skos:altLabel>
  <skos:altLabel>protection measures (human)</skos:altLabel>
  <skos:altLabel>protective clothing</skos:altLabel>
  <skos:altLabel>quarantine procedures</skos:altLabel>
  <skos:altLabel>radiation safety measures (physiological)</skos:altLabel>
  <skos:altLabel>remote manipulator arms (human interface)</skos:altLabel>
  <skos:altLabel>space cabin atmosphere</skos:altLabel>
  <skos:altLabel>space cabin oxygen supplies</skos:altLabel>
  <skos:altLabel>space cabin water supplies</skos:altLabel>
  <skos:altLabel>space flight feeding</skos:altLabel>
  <skos:altLabel>space hygiene</skos:altLabel>
  <skos:altLabel>space sanitation</skos:altLabel>
  <skos:altLabel>space suits</skos:altLabel>
  <skos:altLabel>spacecraft sterilization (interior)</skos:altLabel>
  <skos:altLabel>teleoperators (human interface)</skos:altLabel>
  <skos:altLabel>waste products conversion (aerospace vehicles)</skos:altLabel>
  <skos:altLabel>waste products disposal (aerospace vehicles)</skos:altLabel>
  <skos:altLabel>waste products storage (aerospace vehicles)</skos:altLabel>
  <skos:altLabel>work place design</skos:altLabel>
  <skos:broader rdf:resource='subj:2127'/>
  <nt2:status>Approved</nt2:status>
  <nt2:type>Descriptor</nt2:type>
  <nt2:inputdate>2007-01-11</nt2:inputdate>
  <dcterms:dateAccepted>2006-12-01</dcterms:dateAccepted>
  <dcterms:modified>2007-01-11</dcterms:modified>
  <nt2:notValidDate></nt2:notValidDate>
  <nt2:code>54</nt2:code>
 </skos:Concept>
 <skos:Concept rdf:about='subj:100'>
  <skos:prefLabel>NASA STINASA STI Subject Categories</skos:prefLabel>
  <skos:scopeNote>This Facet is created from NASA/SP-2006-7603, the "NASA
    Scientific and Technical Information Scope and Subject
    Category Guide", published in December 2006.  See
    http://www.sti.nasa.gov/ for copies.
  </skos:scopeNote>
  <skos:narrower rdf:resource='subj:101'/>
  <skos:narrower rdf:resource='subj:578'/>
  <skos:narrower rdf:resource='subj:1058'/>
  <skos:narrower rdf:resource='subj:1332'/>
  <skos:narrower rdf:resource='subj:3056'/>
  <skos:narrower rdf:resource='subj:1874'/>
  <skos:narrower rdf:resource='subj:2127'/>
  <skos:narrower rdf:resource='subj:2321'/>
  <skos:narrower rdf:resource='subj:2528'/>
  <skos:narrower rdf:resource='subj:2767'/>
  <skos:narrower rdf:resource='subj:2871'/>
  <nt2:status>Approved</nt2:status>
  <nt2:type>Descriptor</nt2:type>
  <nt2:inputdate>2007-01-11</nt2:inputdate>
  <dcterms:dateAccepted></dcterms:dateAccepted>
  <dcterms:modified>2007-06-04</dcterms:modified>
  <nt2:notValidDate></nt2:notValidDate>
  <nt2:code>100</nt2:code>
 </skos:Concept>
 <skos:Concept rdf:about='subj:01'>
  <skos:prefLabel>Aeronautics (General)</skos:prefLabel>
  <skos:scopeNote>Includes general research topics related to manned and
    unmanned aircraft and the problems of flight within the
    Earths atmosphere. Also includes manufacturing,
    maintenance, and repair of aircraft. For specific topics in
    aeronautics see categories 02 through 09. For information
    related to space vehicles see 12 Astronautics.
  </skos:scopeNote>
  <skos:altLabel>aircraft maintenance</skos:altLabel>
  <skos:altLabel>aircraft manufacturing</skos:altLabel>
  <skos:altLabel>aircraft production</skos:altLabel>
  <skos:altLabel>aircraft repair</skos:altLabel>
  <skos:altLabel>maintenance (aircraft)</skos:altLabel>
  <skos:broader rdf:resource='subj:101'/>
  <nt2:status>Approved</nt2:status>
  <nt2:type>Descriptor</nt2:type>
  <nt2:inputdate>2007-01-11</nt2:inputdate>
  <dcterms:dateAccepted>2006-12-01</dcterms:dateAccepted>
  <dcterms:modified>2007-01-11</dcterms:modified>
  <nt2:notValidDate></nt2:notValidDate>
  <nt2:code>01</nt2:code>
 </skos:Concept>
 <skos:Concept rdf:about='subj:42'>
  <skos:prefLabel>Geosciences (General)</skos:prefLabel>
  <skos:scopeNote>Includes general research topics related to the Earth
    sciences, and the specific areas of petrology, minerology,
    and general geology. For other specific topics in
    geosciences see categories 42 through 48.
  </skos:scopeNote>
  <skos:altLabel>craters (Earth)</skos:altLabel>
  <skos:altLabel>Earth sciences</skos:altLabel>
  <skos:altLabel>geology (general)</skos:altLabel>
  <skos:altLabel>minerals (petrology)</skos:altLabel>
  <skos:altLabel>petrography</skos:altLabel>
  <skos:altLabel>petrology</skos:altLabel>
  <skos:broader rdf:resource='subj:1874'/>
  <nt2:status>Approved</nt2:status>
  <nt2:type>Descriptor</nt2:type>
  <nt2:inputdate>2007-01-11</nt2:inputdate>
  <dcterms:dateAccepted>2006-12-01</dcterms:dateAccepted>
  <dcterms:modified>2007-01-11</dcterms:modified>
  <nt2:notValidDate></nt2:notValidDate>
  <nt2:code>42</nt2:code>
 </skos:Concept>
 <skos:Concept rdf:about='subj:2528'>
  <skos:prefLabel>Physics</skos:prefLabel>
  <skos:scopeNote>Includes physics (general); acoustics; atomic and molecular
    physics; nuclear physics; optics; plasma physics;
    solid-state physics; and physics of elementary particles
    and fields. For related information see also Engineering
    (categories 31 through 39).
  </skos:scopeNote>
  <skos:broader rdf:resource='subj:100'/>
  <skos:narrower rdf:resource='subj:71'/>
  <skos:narrower rdf:resource='subj:72'/>
  <skos:narrower rdf:resource='subj:73'/>
  <skos:narrower rdf:resource='subj:74'/>
  <skos:narrower rdf:resource='subj:70'/>
  <skos:narrower rdf:resource='subj:77'/>
  <skos:narrower rdf:resource='subj:75'/>
  <skos:narrower rdf:resource='subj:76'/>
  <nt2:status>Approved</nt2:status>
  <nt2:type>Descriptor</nt2:type>
  <nt2:inputdate>2007-01-11</nt2:inputdate>
  <dcterms:dateAccepted>2006-12-01</dcterms:dateAccepted>
  <dcterms:modified>2007-01-11</dcterms:modified>
  <nt2:notValidDate></nt2:notValidDate>
  <nt2:code>2528</nt2:code>
 </skos:Concept>
 <skos:Concept rdf:about='subj:55'>
  <skos:prefLabel>Exobiology</skos:prefLabel>
  <skos:scopeNote>Includes astrobiology; planetary biology; and
    extraterrestrial life. For the biological effects of
    aerospace environments on humans see 52 Aerospace Medicine;
    on animals and plants see 51 Life Sciences. For
    psychological and behavioral effects of aerospace
    environments see 53 Behavioral Science.
  </skos:scopeNote>
  <skos:altLabel>abiogenesis</skos:altLabel>
  <skos:altLabel>amino acid analysis (extraterrestrial)</skos:altLabel>
  <skos:altLabel>astrobiology</skos:altLabel>
  <skos:altLabel>biochemical detection of life</skos:altLabel>
  <skos:altLabel>bioinstrumentation (extraterrestrial life)</skos:altLabel>
  <skos:altLabel>biology (extraterrestrial)</skos:altLabel>
  <skos:altLabel>biomarkers (exobiology)</skos:altLabel>
  <skos:altLabel>chemical evolution</skos:altLabel>
  <skos:altLabel>culturing, cell (exobiology)</skos:altLabel>
  <skos:altLabel>enzyme analysis (extraterrestrial)</skos:altLabel>
  <skos:altLabel>extraterrestrial biochemistry</skos:altLabel>
  <skos:altLabel>extraterrestrial biology</skos:altLabel>
  <skos:altLabel>extraterrestrial environment effect (exobiology)</skos:altLabel>
  <skos:altLabel>extraterrestrial life</skos:altLabel>
  <skos:altLabel>extraterrestrial water</skos:altLabel>
  <skos:altLabel>extreme temperature effects (exobiology)</skos:altLabel>
  <skos:altLabel>gravitational effects (exobiology)</skos:altLabel>
  <skos:altLabel>life detection</skos:altLabel>
  <skos:altLabel>magnetic field effects</skos:altLabel>
  <skos:altLabel>nature of life</skos:altLabel>
  <skos:altLabel>origin of life (extraterrestrial)</skos:altLabel>
  <skos:altLabel>planetary biology</skos:altLabel>
  <skos:altLabel>protobiological evolution</skos:altLabel>
  <skos:altLabel>reproduction of extraterrestrial life</skos:altLabel>
  <skos:altLabel>soil sampling and analysis (extraterrestrial life)</skos:altLabel>
  <skos:altLabel>space biology</skos:altLabel>
  <skos:altLabel>spontaneous generation of life</skos:altLabel>
  <skos:broader rdf:resource='subj:2127'/>
  <nt2:status>Approved</nt2:status>
  <nt2:type>Descriptor</nt2:type>
  <nt2:inputdate>2007-01-11</nt2:inputdate>
  <dcterms:dateAccepted>2006-12-01</dcterms:dateAccepted>
  <dcterms:modified>2007-01-11</dcterms:modified>
  <nt2:notValidDate></nt2:notValidDate>
  <nt2:code>55</nt2:code>
 </skos:Concept>
 <skos:Concept rdf:about='subj:43'>
  <skos:prefLabel>Earth Resources and Remote Sensing</skos:prefLabel>
  <skos:scopeNote>Includes remote sensing of earth features, phenomena and
    resources by aircraft, balloon, rocket, and spacecraft;
    analysis of remote sensing data and imagery; development of
    remote sensing products; photogrammetry; aerial
    photography; and hydrology. For related instrumentation see
    35 Instrumentation and Photography.
  </skos:scopeNote>
  <skos:altLabel>aerial photography</skos:altLabel>
  <skos:altLabel>cartography</skos:altLabel>
  <skos:altLabel>computer processing of Earth resources data</skos:altLabel>
  <skos:altLabel>crop disease detection</skos:altLabel>
  <skos:altLabel>crop forecasts</skos:altLabel>
  <skos:altLabel>desertification</skos:altLabel>
  <skos:altLabel>Earth resources</skos:altLabel>
  <skos:altLabel>foliage sensing</skos:altLabel>
  <skos:altLabel>forest fire detection applications)</skos:altLabel>
  <skos:altLabel>geodesy (remote sensing)</skos:altLabel>
  <skos:altLabel>geological exploration</skos:altLabel>
  <skos:altLabel>geological survey</skos:altLabel>
  <skos:altLabel>geothermal resources</skos:altLabel>
  <skos:altLabel>ground truth</skos:altLabel>
  <skos:altLabel>hydrology</skos:altLabel>
  <skos:altLabel>infrared imagery (remote sensing)</skos:altLabel>
  <skos:altLabel>infrared signatures (earth resources)</skos:altLabel>
  <skos:altLabel>LANDSAT (remote sensing applications)</skos:altLabel>
  <skos:altLabel>limnology</skos:altLabel>
  <skos:altLabel>littoral regions</skos:altLabel>
  <skos:altLabel>mapping</skos:altLabel>
  <skos:altLabel>mineral deposits</skos:altLabel>
  <skos:altLabel>multispectral band scanners (remote sensing</skos:altLabel>
  <skos:altLabel>ocean color (remote sensing)</skos:altLabel>
  <skos:altLabel>orography</skos:altLabel>
  <skos:altLabel>petroleum deposits</skos:altLabel>
  <skos:altLabel>photogrammetry</skos:altLabel>
  <skos:altLabel>radar detection (earth resources)</skos:altLabel>
  <skos:altLabel>radar imagery (remote sensing)</skos:altLabel>
  <skos:altLabel>remote sensing of earth resources</skos:altLabel>
  <skos:altLabel>satellite derived atmospheric profiles</skos:altLabel>
  <skos:altLabel>satellite observation (remote sensing applications)</skos:altLabel>
  <skos:altLabel>scatterometers (remote sensing applications)</skos:altLabel>
  <skos:altLabel>SEASAT (remote sensing applications)</skos:altLabel>
  <skos:altLabel>Shuttle Imaging Radar (earth resources)</skos:altLabel>
  <skos:altLabel>side looking radar (earth resources)</skos:altLabel>
  <skos:altLabel>signature analysis (earth resources)</skos:altLabel>
  <skos:altLabel>snow and ice observations</skos:altLabel>
  <skos:altLabel>soil identification</skos:altLabel>
  <skos:altLabel>thematic mapping</skos:altLabel>
  <skos:altLabel>timber inventory</skos:altLabel>
  <skos:altLabel>very long base interferometry (applications)</skos:altLabel>
  <skos:altLabel>water resources</skos:altLabel>
  <skos:broader rdf:resource='subj:1874'/>
  <nt2:status>Approved</nt2:status>
  <nt2:type>Descriptor</nt2:type>
  <nt2:inputdate>2007-01-11</nt2:inputdate>
  <dcterms:dateAccepted>2006-12-01</dcterms:dateAccepted>
  <dcterms:modified>2007-01-11</dcterms:modified>
  <nt2:notValidDate></nt2:notValidDate>
  <nt2:code>43</nt2:code>
 </skos:Concept>
 <skos:Concept rdf:about='subj:13'>
  <skos:prefLabel>Astrodynamics</skos:prefLabel>
  <skos:scopeNote>Includes powered and free-flight trajectories; orbital and
    launching dynamics.
  </skos:scopeNote>
  <skos:altLabel>aerobraking</skos:altLabel>
  <skos:altLabel>astroballistics</skos:altLabel>
  <skos:altLabel>atmospheric entry effects</skos:altLabel>
  <skos:altLabel>ballistic trajectories</skos:altLabel>
  <skos:altLabel>free-flight trajectories</skos:altLabel>
  <skos:altLabel>gravitational effects (orbital effects on launch vehicles</skos:altLabel>
  <skos:altLabel>interplanetary trajectories</skos:altLabel>
  <skos:altLabel>launch vehicle trajectories</skos:altLabel>
  <skos:altLabel>launching dynamics</skos:altLabel>
  <skos:altLabel>orbit dynamics of spacecraft</skos:altLabel>
  <skos:altLabel>orbital maneuvers (trajectories)</skos:altLabel>
  <skos:altLabel>orbital rendezvous</skos:altLabel>
  <skos:altLabel>powered trajectories</skos:altLabel>
  <skos:altLabel>projectile trajectories</skos:altLabel>
  <skos:altLabel>propulsion effects on launching, trajectories, and orbits</skos:altLabel>
  <skos:altLabel>reentry dynamics</skos:altLabel>
  <skos:altLabel>reentry trajectories</skos:altLabel>
  <skos:altLabel>space flight dynamics (theory)</skos:altLabel>
  <skos:altLabel>spacecraft orbits</skos:altLabel>
  <skos:altLabel>spacecraft trajectories</skos:altLabel>
  <skos:altLabel>swingby maneuver</skos:altLabel>
  <skos:altLabel>trajectory analysis</skos:altLabel>
  <skos:altLabel>trajectory optimization</skos:altLabel>
  <skos:altLabel>two-and three-body problems (trajectory analysis)</skos:altLabel>
  <skos:broader rdf:resource='subj:578'/>
  <nt2:status>Approved</nt2:status>
  <nt2:type>Descriptor</nt2:type>
  <nt2:inputdate>2007-01-11</nt2:inputdate>
  <dcterms:dateAccepted>2006-12-01</dcterms:dateAccepted>
  <dcterms:modified>2007-01-11</dcterms:modified>
  <nt2:notValidDate></nt2:notValidDate>
  <nt2:code>13</nt2:code>
 </skos:Concept>
 <skos:Concept rdf:about='subj:19'>
  <skos:prefLabel>Spacecraft Instrumentation and Astrionics</skos:prefLabel>
  <skos:scopeNote>Includes the design, manufacture, or use of devices for the
    purpose of measuring, detecting, controlling, computing,
    recording, or processing data related to the operation of
    space vehicles or platforms. For related information see
    also 06 Aircraft Instrumentation and Avionics; For
    spaceborne instruments not integral to the vehicle itself
    see 35 Instrumentation and Photography; For spaceborne
    telescopes and other astronomical instruments see 89
    Astronomy.
  </skos:scopeNote>
  <skos:altLabel>ablation sensors (spacecraft)</skos:altLabel>
  <skos:altLabel>alarm systems (spacecraft)</skos:altLabel>
  <skos:altLabel>altimeters (spacecraft)</skos:altLabel>
  <skos:altLabel>analyzing devices (spacecraft)</skos:altLabel>
  <skos:altLabel>astrionics</skos:altLabel>
  <skos:altLabel>attitude indicators (spacecraft)</skos:altLabel>
  <skos:altLabel>bioelectronic instruments (spacecraft)</skos:altLabel>
  <skos:altLabel>biomedical instruments (spacecraft)</skos:altLabel>
  <skos:altLabel>cabin display devices (spacecraft)</skos:altLabel>
  <skos:altLabel>cathode ray tubes (spacecraft systems)</skos:altLabel>
  <skos:altLabel>control position indicators (spacecraft)</skos:altLabel>
  <skos:altLabel>detecting devices (spacecraft)</skos:altLabel>
  <skos:altLabel>display devices (spacecraft)</skos:altLabel>
  <skos:altLabel>flight instruments (spacecraft)</skos:altLabel>
  <skos:altLabel>flight recorders (spacecraft)</skos:altLabel>
  <skos:altLabel>fluid flow sensors (spacecraft)</skos:altLabel>
  <skos:altLabel>gyroscopes (spacecraft)</skos:altLabel>
  <skos:altLabel>heads-up displays (spacecraft)</skos:altLabel>
  <skos:altLabel>horizon sensors (spacecraft)</skos:altLabel>
  <skos:altLabel>infrared sensors (spacecraft)</skos:altLabel>
  <skos:altLabel>instrument arrangement (spacecraft)</skos:altLabel>
  <skos:altLabel>instrument design (spacecraft)</skos:altLabel>
  <skos:altLabel>instrument displays (spacecraft)</skos:altLabel>
  <skos:altLabel>instrument installation (spacecraft)</skos:altLabel>
  <skos:altLabel>instrument pointing systems (IPS)</skos:altLabel>
  <skos:altLabel>landing gear position indicators (spacecraft)</skos:altLabel>
  <skos:altLabel>laser altimeters (spacecraft)</skos:altLabel>
  <skos:altLabel>laser instruments (spacecraft)</skos:altLabel>
  <skos:altLabel>micrometeoroid sensors (spacecraft)</skos:altLabel>
  <skos:altLabel>navigation display devices (design and development)</skos:altLabel>
  <skos:altLabel>onboard computer systems for spacecraft</skos:altLabel>
  <skos:altLabel>onboard instrument systems for spacecraft</skos:altLabel>
  <skos:altLabel>onboard sensors and recorders for spacecraft</skos:altLabel>
  <skos:altLabel>passive sensors, trackers, and references (spacecraft)</skos:altLabel>
  <skos:altLabel>pointing systems</skos:altLabel>
  <skos:altLabel>position indicators (spacecraft)</skos:altLabel>
  <skos:altLabel>propulsion system instruments and gages (spacecraft)</skos:altLabel>
  <skos:altLabel>recording devices (spacecraft)</skos:altLabel>
  <skos:altLabel>sensors for spacecraft equipment</skos:altLabel>
  <skos:altLabel>skin temperature indicators (spacecraft)</skos:altLabel>
  <skos:altLabel>space cabin atmosphere sensors</skos:altLabel>
  <skos:altLabel>spacecraft control computer systems</skos:altLabel>
  <skos:altLabel>spacecraft instruments</skos:altLabel>
  <skos:altLabel>spacecraft systems monitoring instruments</skos:altLabel>
  <skos:altLabel>star trackers (navigation)</skos:altLabel>
  <skos:altLabel>telemetry devices (spacecraft)</skos:altLabel>
  <skos:altLabel>thermal protection sensors</skos:altLabel>
  <skos:altLabel>two-gas sensors (spacecraft)</skos:altLabel>
  <skos:altLabel>warning lights (spacecraft)</skos:altLabel>
  <skos:broader rdf:resource='subj:578'/>
  <nt2:status>Approved</nt2:status>
  <nt2:type>Descriptor</nt2:type>
  <nt2:inputdate>2007-01-11</nt2:inputdate>
  <dcterms:dateAccepted>2006-12-01</dcterms:dateAccepted>
  <dcterms:modified>2007-01-11</dcterms:modified>
  <nt2:notValidDate></nt2:notValidDate>
  <nt2:code>19</nt2:code>
 </skos:Concept>
 <skos:Concept rdf:about='subj:08'>
  <skos:prefLabel>Aircraft Stability and Control</skos:prefLabel>
  <skos:scopeNote>Includes flight dynamics, aircraft handling qualities,
    piloting, flight controls, and autopilots. For related
    information see also 05 Aircraft Design, Testing and
    Performance; and 06 Avionics and Aircraft Instrumentation.
  </skos:scopeNote>
  <skos:altLabel>air launched weapons (stability)</skos:altLabel>
  <skos:altLabel>aircraft control</skos:altLabel>
  <skos:altLabel>aircraft stability</skos:altLabel>
  <skos:altLabel>aircraft trim</skos:altLabel>
  <skos:altLabel>attitude control (aircraft)</skos:altLabel>
  <skos:altLabel>automatic pilots (aircraft)</skos:altLabel>
  <skos:altLabel>body-tail combinations (stability and control)</skos:altLabel>
  <skos:altLabel>control effectiveness (aircraft)</skos:altLabel>
  <skos:altLabel>control surface interactions (aircraft)</skos:altLabel>
  <skos:altLabel>dutch roll</skos:altLabel>
  <skos:altLabel>dynamic stability (aircraft)</skos:altLabel>
  <skos:altLabel>flight control (aircraft)</skos:altLabel>
  <skos:altLabel>flight dynamics (aircraft)</skos:altLabel>
  <skos:altLabel>flight management systems</skos:altLabel>
  <skos:altLabel>flight path control (aircraft)</skos:altLabel>
  <skos:altLabel>flutter (aircraft)</skos:altLabel>
  <skos:altLabel>fly-by-light control (FBL)</skos:altLabel>
  <skos:altLabel>fly-by-wire control (FBW)</skos:altLabel>
  <skos:altLabel>flying qualities (aircraft)</skos:altLabel>
  <skos:altLabel>handling qualities (aircraft)</skos:altLabel>
  <skos:altLabel>lateral control (aircraft)</skos:altLabel>
  <skos:altLabel>lateral stability (aircraft)</skos:altLabel>
  <skos:altLabel>longitudinal control (aircraft)</skos:altLabel>
  <skos:altLabel>longitudinal stability (aircraft)</skos:altLabel>
  <skos:altLabel>maneuvering (aircraft)</skos:altLabel>
  <skos:altLabel>missiles (performance)</skos:altLabel>
  <skos:altLabel>operational effects of atmospheric variables</skos:altLabel>
  <skos:altLabel>pitch control (aircraft)</skos:altLabel>
  <skos:altLabel>pitch stability (aircraft)</skos:altLabel>
  <skos:altLabel>roll control (aircraft)</skos:altLabel>
  <skos:altLabel>roll stability (aircraft)</skos:altLabel>
  <skos:altLabel>spin recovery</skos:altLabel>
  <skos:altLabel>stability (aircraft)</skos:altLabel>
  <skos:altLabel>stability augmentation (aircraft)</skos:altLabel>
  <skos:altLabel>stability derivatives (aircraft)</skos:altLabel>
  <skos:altLabel>stabilization surfaces (aircraft)</skos:altLabel>
  <skos:altLabel>static stability (aircraft)</skos:altLabel>
  <skos:altLabel>vibration (aircraft)</skos:altLabel>
  <skos:altLabel>voice command for aircraft</skos:altLabel>
  <skos:altLabel>wind tunnel tests (stability and control)</skos:altLabel>
  <skos:altLabel>wing rock</skos:altLabel>
  <skos:altLabel>wing-body combinations (stability and control)</skos:altLabel>
  <skos:altLabel>wing-nacelle combinations (stability and control)</skos:altLabel>
  <skos:altLabel>yaw control (aircraft)</skos:altLabel>
  <skos:altLabel>yaw stability (aircraft)</skos:altLabel>
  <skos:broader rdf:resource='subj:101'/>
  <nt2:status>Approved</nt2:status>
  <nt2:type>Descriptor</nt2:type>
  <nt2:inputdate>2007-01-11</nt2:inputdate>
  <dcterms:dateAccepted>2006-12-01</dcterms:dateAccepted>
  <dcterms:modified>2007-01-11</dcterms:modified>
  <nt2:notValidDate></nt2:notValidDate>
  <nt2:code>08</nt2:code>
 </skos:Concept>
 <skos:Concept rdf:about='subj:47'>
  <skos:prefLabel>Meteorology and Climatology</skos:prefLabel>
  <skos:scopeNote>Includes weather observation forecasting and modification.
  </skos:scopeNote>
  <skos:altLabel>anabatic winds</skos:altLabel>
  <skos:altLabel>anemometers (applications)</skos:altLabel>
  <skos:altLabel>atmospheric boundary layer (climatology)</skos:altLabel>
  <skos:altLabel>atmospheric circulation (meteorology)</skos:altLabel>
  <skos:altLabel>atmospheric cloud physics</skos:altLabel>
  <skos:altLabel>atmospheric energy exchanges</skos:altLabel>
  <skos:altLabel>atmospheric interactions</skos:altLabel>
  <skos:altLabel>atmospheric studies (meteorological)</skos:altLabel>
  <skos:altLabel>atmospheric turbulence</skos:altLabel>
  <skos:altLabel>barometric pressure</skos:altLabel>
  <skos:altLabel>catabatic winds (also katabatic)</skos:altLabel>
  <skos:altLabel>clear air turbulence (meteorology)</skos:altLabel>
  <skos:altLabel>climate change</skos:altLabel>
  <skos:altLabel>climate models</skos:altLabel>
  <skos:altLabel>climate prediction</skos:altLabel>
  <skos:altLabel>climate variability</skos:altLabel>
  <skos:altLabel>climatology</skos:altLabel>
  <skos:altLabel>cloud cover analysis</skos:altLabel>
  <skos:altLabel>cloud patterns</skos:altLabel>
  <skos:altLabel>cloud seeding</skos:altLabel>
  <skos:altLabel>clouds (meteorology)</skos:altLabel>
  <skos:altLabel>Coriolis forces (meteorology)</skos:altLabel>
  <skos:altLabel>cyclones</skos:altLabel>
  <skos:altLabel>diurnal effects (meteorology)</skos:altLabel>
  <skos:altLabel>el Nino</skos:altLabel>
  <skos:altLabel>energy exchanges in the atmosphere</skos:altLabel>
  <skos:altLabel>fog dissipation and formation</skos:altLabel>
  <skos:altLabel>fronts (meteorology)</skos:altLabel>
  <skos:altLabel>global meteorology</skos:altLabel>
  <skos:altLabel>global warming</skos:altLabel>
  <skos:altLabel>hurricanes</skos:altLabel>
  <skos:altLabel>ice cover (climatology)</skos:altLabel>
  <skos:altLabel>ice crystals (meteorology)</skos:altLabel>
  <skos:altLabel>jet streams (meteorology)</skos:altLabel>
  <skos:altLabel>katabatic winds (also catabatic)</skos:altLabel>
  <skos:altLabel>la Nina</skos:altLabel>
  <skos:altLabel>lightning</skos:altLabel>
  <skos:altLabel>macrometeorology</skos:altLabel>
  <skos:altLabel>meteorological anomalies</skos:altLabel>
  <skos:altLabel>meteorological parameters</skos:altLabel>
  <skos:altLabel>meteorological satellite studies</skos:altLabel>
  <skos:altLabel>meteorological sounding rocket studies</skos:altLabel>
  <skos:altLabel>meteorology</skos:altLabel>
  <skos:altLabel>microbursts</skos:altLabel>
  <skos:altLabel>micrometeorology</skos:altLabel>
  <skos:altLabel>monsoons</skos:altLabel>
  <skos:altLabel>precipitation (meteorology)</skos:altLabel>
  <skos:altLabel>rain</skos:altLabel>
  <skos:altLabel>seasonal variations</skos:altLabel>
  <skos:altLabel>snow</skos:altLabel>
  <skos:altLabel>snow cover</skos:altLabel>
  <skos:altLabel>solar-atmospheric interactions</skos:altLabel>
  <skos:altLabel>storm cells</skos:altLabel>
  <skos:altLabel>synoptic meteorology</skos:altLabel>
  <skos:altLabel>temperature variations (meteorology)</skos:altLabel>
  <skos:altLabel>thunderstorms</skos:altLabel>
  <skos:altLabel>tornadoes</skos:altLabel>
  <skos:altLabel>typhoons</skos:altLabel>
  <skos:altLabel>weather forecasting</skos:altLabel>
  <skos:altLabel>weather modification</skos:altLabel>
  <skos:altLabel>wind</skos:altLabel>
  <skos:altLabel>wind shear</skos:altLabel>
  <skos:broader rdf:resource='subj:1874'/>
  <nt2:status>Approved</nt2:status>
  <nt2:type>Descriptor</nt2:type>
  <nt2:inputdate>2007-01-11</nt2:inputdate>
  <dcterms:dateAccepted>2006-12-01</dcterms:dateAccepted>
  <dcterms:modified>2007-01-11</dcterms:modified>
  <nt2:notValidDate></nt2:notValidDate>
  <nt2:code>47</nt2:code>
 </skos:Concept>
 <skos:Concept rdf:about='subj:2127'>
  <skos:prefLabel>Life Sciences</skos:prefLabel>
  <skos:scopeNote>Includes life sciences (general); aerospace medicine;
    behavioral sciences; man/system technology and life
    support; and exobiology.
  </skos:scopeNote>
  <skos:broader rdf:resource='subj:100'/>
  <skos:narrower rdf:resource='subj:52'/>
  <skos:narrower rdf:resource='subj:53'/>
  <skos:narrower rdf:resource='subj:55'/>
  <skos:narrower rdf:resource='subj:51'/>
  <skos:narrower rdf:resource='subj:54'/>
  <nt2:status>Approved</nt2:status>
  <nt2:type>Descriptor</nt2:type>
  <nt2:inputdate>2007-01-11</nt2:inputdate>
  <dcterms:dateAccepted>2006-12-01</dcterms:dateAccepted>
  <dcterms:modified>2007-01-11</dcterms:modified>
  <nt2:notValidDate></nt2:notValidDate>
  <nt2:code>2127</nt2:code>
 </skos:Concept>
 <skos:Concept rdf:about='subj:33'>
  <skos:prefLabel>Electronics and Electrical Engineering</skos:prefLabel>
  <skos:scopeNote>Includes development, performance, and maintainability of
    electrical/electronic devices and components; related test
    equipment; and microelectronics and integrated circuitry.
    For related information see also 60 Computer Operations and
    Hardware; and 76 Solid-State Physics. For communications
    equipment and devices see 32 Communications and Radar.
  </skos:scopeNote>
  <skos:altLabel>amplifiers</skos:altLabel>
  <skos:altLabel>audio amplifiers</skos:altLabel>
  <skos:altLabel>batteries (electrical design)</skos:altLabel>
  <skos:altLabel>bridge circuits</skos:altLabel>
  <skos:altLabel>capacitors</skos:altLabel>
  <skos:altLabel>cathode ray tubes (electrical design)</skos:altLabel>
  <skos:altLabel>charge-coupled devices</skos:altLabel>
  <skos:altLabel>chips (integrated circuits)</skos:altLabel>
  <skos:altLabel>chokes (electric, electronic)</skos:altLabel>
  <skos:altLabel>circuit simulation (integrated circuits)</skos:altLabel>
  <skos:altLabel>circuit theory</skos:altLabel>
  <skos:altLabel>converters</skos:altLabel>
  <skos:altLabel>crystals (electronic applications)</skos:altLabel>
  <skos:altLabel>dielectrics (electronic application)</skos:altLabel>
  <skos:altLabel>diodes</skos:altLabel>
  <skos:altLabel>dividers (electric)</skos:altLabel>
  <skos:altLabel>electric circuits</skos:altLabel>
  <skos:altLabel>electric filters</skos:altLabel>
  <skos:altLabel>electric motors</skos:altLabel>
  <skos:altLabel>electric power units (electrical design)</skos:altLabel>
  <skos:altLabel>electrical components</skos:altLabel>
  <skos:altLabel>electrical engineering</skos:altLabel>
  <skos:altLabel>electrical relays</skos:altLabel>
  <skos:altLabel>electromechanics</skos:altLabel>
  <skos:altLabel>electron beam devices</skos:altLabel>
  <skos:altLabel>electron tubes</skos:altLabel>
  <skos:altLabel>electronic circuits</skos:altLabel>
  <skos:altLabel>electronic components</skos:altLabel>
  <skos:altLabel>electronic packaging</skos:altLabel>
  <skos:altLabel>electronic test equipment</skos:altLabel>
  <skos:altLabel>electronics</skos:altLabel>
  <skos:altLabel>field effect transistors (FET)</skos:altLabel>
  <skos:altLabel>field programmable gate arrays</skos:altLabel>
  <skos:altLabel>filters (electric, electronic)</skos:altLabel>
  <skos:altLabel>fuses (electric)</skos:altLabel>
  <skos:altLabel>generators (electrical design)</skos:altLabel>
  <skos:altLabel>inductors (electric)</skos:altLabel>
  <skos:altLabel>insulation (electric, electronic)</skos:altLabel>
  <skos:altLabel>integrated circuits</skos:altLabel>
  <skos:altLabel>inverters</skos:altLabel>
  <skos:altLabel>Kalman filters</skos:altLabel>
  <skos:altLabel>klystrons</skos:altLabel>
  <skos:altLabel>light emitting diodes (LED)</skos:altLabel>
  <skos:altLabel>lithography (circuit fabrication)</skos:altLabel>
  <skos:altLabel>magnets (electrical, electronics application)</skos:altLabel>
  <skos:altLabel>microcircuits</skos:altLabel>
  <skos:altLabel>microelectronics</skos:altLabel>
  <skos:altLabel>microminiaturization</skos:altLabel>
  <skos:altLabel>modulators (electric, electronic devices)</skos:altLabel>
  <skos:altLabel>nanodevices (electronic)</skos:altLabel>
  <skos:altLabel>networks (circuitry)</skos:altLabel>
  <skos:altLabel>opto-acoustic electronics</skos:altLabel>
  <skos:altLabel>optoelectronics (applications)</skos:altLabel>
  <skos:altLabel>oscillators</skos:altLabel>
  <skos:altLabel>photoelectric devices</skos:altLabel>
  <skos:altLabel>photomultipliers</skos:altLabel>
  <skos:altLabel>power amplifiers</skos:altLabel>
  <skos:altLabel>power packs (electric)</skos:altLabel>
  <skos:altLabel>power supplies electric)</skos:altLabel>
  <skos:altLabel>printed circuits</skos:altLabel>
  <skos:altLabel>programmable logic devices</skos:altLabel>
  <skos:altLabel>radomes (electrical properties)</skos:altLabel>
  <skos:altLabel>rail accelerators, railguns, launchers (theory)</skos:altLabel>
  <skos:altLabel>reconfigurable hardware</skos:altLabel>
  <skos:altLabel>rectifiers</skos:altLabel>
  <skos:altLabel>regulators (voltage, current)</skos:altLabel>
  <skos:altLabel>resistors</skos:altLabel>
  <skos:altLabel>semiconductor devices</skos:altLabel>
  <skos:altLabel>servomechanisms (electrical aspects)</skos:altLabel>
  <skos:altLabel>signal generators (applications)</skos:altLabel>
  <skos:altLabel>silicon cells (electrical properties)</skos:altLabel>
  <skos:altLabel>single event transients</skos:altLabel>
  <skos:altLabel>single event upsets</skos:altLabel>
  <skos:altLabel>sneak circuit analysis</skos:altLabel>
  <skos:altLabel>solar cells (electrical design)</skos:altLabel>
  <skos:altLabel>solar state circuitry</skos:altLabel>
  <skos:altLabel>solid state devices</skos:altLabel>
  <skos:altLabel>superconductivity (applications)</skos:altLabel>
  <skos:altLabel>surface wave acoustic devices (electronic design)</skos:altLabel>
  <skos:altLabel>switches</skos:altLabel>
  <skos:altLabel>switching circuits</skos:altLabel>
  <skos:altLabel>switching theory</skos:altLabel>
  <skos:altLabel>test equipment (electrical properties)</skos:altLabel>
  <skos:altLabel>thyratrons</skos:altLabel>
  <skos:altLabel>transducers</skos:altLabel>
  <skos:altLabel>transformers</skos:altLabel>
  <skos:altLabel>transistors</skos:altLabel>
  <skos:altLabel>transmission lines</skos:altLabel>
  <skos:altLabel>traveling wave tubes</skos:altLabel>
  <skos:altLabel>triodes</skos:altLabel>
  <skos:altLabel>tunnel diodes</skos:altLabel>
  <skos:altLabel>vacuum tubes</skos:altLabel>
  <skos:altLabel>very large scale integration (VLSI)</skos:altLabel>
  <skos:altLabel>VHSIC</skos:altLabel>
  <skos:altLabel>waveguides</skos:altLabel>
  <skos:broader rdf:resource='subj:1332'/>
  <nt2:status>Approved</nt2:status>
  <nt2:type>Descriptor</nt2:type>
  <nt2:inputdate>2007-01-11</nt2:inputdate>
  <dcterms:dateAccepted>2006-12-01</dcterms:dateAccepted>
  <dcterms:modified>2007-01-11</dcterms:modified>
  <nt2:notValidDate></nt2:notValidDate>
  <nt2:code>33</nt2:code>
 </skos:Concept>
 <skos:Concept rdf:about='subj:15'>
  <skos:prefLabel>Launch Vehicles and Launch Operations</skos:prefLabel>
  <skos:scopeNote>Includes all classes of launch vehicles, launch/space
    vehicle systems, and boosters; and launch operations. For
    related information see also 18 Spacecraft Design, Testing,
    and Performance; and 20 Spacecraft Propulsion and Power.
  </skos:scopeNote>
  <skos:altLabel>boosters (launch vehicles)</skos:altLabel>
  <skos:altLabel>combinations of launch vehicles and space vehicles</skos:altLabel>
  <skos:altLabel>commercial launch vehicles</skos:altLabel>
  <skos:altLabel>countdown</skos:altLabel>
  <skos:altLabel>design of launch vehicles, tanks, components, systems</skos:altLabel>
  <skos:altLabel>electromagnetic launchers (operations)</skos:altLabel>
  <skos:altLabel>launch operations</skos:altLabel>
  <skos:altLabel>launch vehicle auxiliary systems</skos:altLabel>
  <skos:altLabel>launch vehicle configurations</skos:altLabel>
  <skos:altLabel>launch vehicle design</skos:altLabel>
  <skos:altLabel>launch vehicle dynamics</skos:altLabel>
  <skos:altLabel>launch vehicle performance</skos:altLabel>
  <skos:altLabel>launch vehicle preparation</skos:altLabel>
  <skos:altLabel>launch vehicle stability</skos:altLabel>
  <skos:altLabel>launch vehicle testing</skos:altLabel>
  <skos:altLabel>launch vehicles</skos:altLabel>
  <skos:altLabel>light gas guns (operations)</skos:altLabel>
  <skos:altLabel>multistage launch vehicles</skos:altLabel>
  <skos:altLabel>nose cones</skos:altLabel>
  <skos:altLabel>orbit-on-demand vehicles</skos:altLabel>
  <skos:altLabel>reentry launch vehicles</skos:altLabel>
  <skos:altLabel>reusable vehicles</skos:altLabel>
  <skos:altLabel>rocket launchers</skos:altLabel>
  <skos:altLabel>rockets</skos:altLabel>
  <skos:altLabel>satellite launching dynamics</skos:altLabel>
  <skos:altLabel>separation and staging techniques (for stages of launch</skos:altLabel>
  <skos:altLabel>vehicles)</skos:altLabel>
  <skos:altLabel>single-stage launch vehicles</skos:altLabel>
  <skos:altLabel>sounding rockets</skos:altLabel>
  <skos:broader rdf:resource='subj:578'/>
  <nt2:status>Approved</nt2:status>
  <nt2:type>Descriptor</nt2:type>
  <nt2:inputdate>2007-01-11</nt2:inputdate>
  <dcterms:dateAccepted>2006-12-01</dcterms:dateAccepted>
  <dcterms:modified>2007-01-11</dcterms:modified>
  <nt2:notValidDate></nt2:notValidDate>
  <nt2:code>15</nt2:code>
 </skos:Concept>
 <skos:Concept rdf:about='subj:84'>
  <skos:prefLabel>Law, Political Science and Space Policy</skos:prefLabel>
  <skos:scopeNote>Includes; aviation law; space law and policy; international
    law; international cooperation; and patent policy.
  </skos:scopeNote>
  <skos:altLabel>aerospace agreements</skos:altLabel>
  <skos:altLabel>air piracy (legal aspects)</skos:altLabel>
  <skos:altLabel>air transport regulations</skos:altLabel>
  <skos:altLabel>civil aeronautical law</skos:altLabel>
  <skos:altLabel>congressional legislation</skos:altLabel>
  <skos:altLabel>federal aviation laws</skos:altLabel>
  <skos:altLabel>government/industry relationships</skos:altLabel>
  <skos:altLabel>international cooperation</skos:altLabel>
  <skos:altLabel>international law</skos:altLabel>
  <skos:altLabel>law</skos:altLabel>
  <skos:altLabel>legal liability of commercial aviation</skos:altLabel>
  <skos:altLabel>legal liability of general aviation</skos:altLabel>
  <skos:altLabel>legal liability of manned space flight</skos:altLabel>
  <skos:altLabel>legal liability of unmanned space flight</skos:altLabel>
  <skos:altLabel>patent law</skos:altLabel>
  <skos:altLabel>patent policy</skos:altLabel>
  <skos:altLabel>political science</skos:altLabel>
  <skos:altLabel>space commercialization (legal aspects)</skos:altLabel>
  <skos:altLabel>space law</skos:altLabel>
  <skos:altLabel>space policy</skos:altLabel>
  <skos:altLabel>transfer of responsibility (space applications)</skos:altLabel>
  <skos:altLabel>treaties</skos:altLabel>
  <skos:broader rdf:resource='subj:2767'/>
  <nt2:status>Approved</nt2:status>
  <nt2:type>Descriptor</nt2:type>
  <nt2:inputdate>2007-01-11</nt2:inputdate>
  <dcterms:dateAccepted>2006-12-01</dcterms:dateAccepted>
  <dcterms:modified>2007-01-11</dcterms:modified>
  <nt2:notValidDate></nt2:notValidDate>
  <nt2:code>84</nt2:code>
 </skos:Concept>
 <skos:Concept rdf:about='subj:26'>
  <skos:prefLabel>Metals and Metallic Materials</skos:prefLabel>
  <skos:scopeNote>Includes physical, chemical, and mechanical properties of
    metals and metallic materials; and metallurgy.
  </skos:scopeNote>
  <skos:altLabel>alloys</skos:altLabel>
  <skos:altLabel>anodizing</skos:altLabel>
  <skos:altLabel>cermets</skos:altLabel>
  <skos:altLabel>chemical properties of alloys</skos:altLabel>
  <skos:altLabel>chemical properties of metals</skos:altLabel>
  <skos:altLabel>compression strength (metallic materials)</skos:altLabel>
  <skos:altLabel>corrosion</skos:altLabel>
  <skos:altLabel>creep strength (metallic materials)</skos:altLabel>
  <skos:altLabel>crystal structure (metallic materials)</skos:altLabel>
  <skos:altLabel>crystals (metallic)</skos:altLabel>
  <skos:altLabel>development of alloys</skos:altLabel>
  <skos:altLabel>eutectics</skos:altLabel>
  <skos:altLabel>eutectoids</skos:altLabel>
  <skos:altLabel>evaluation of alloys</skos:altLabel>
  <skos:altLabel>evaluation of metals</skos:altLabel>
  <skos:altLabel>fatigue (metallic materials)</skos:altLabel>
  <skos:altLabel>ferrites</skos:altLabel>
  <skos:altLabel>fibers (metallic materials)</skos:altLabel>
  <skos:altLabel>flammability (metallic materials)</skos:altLabel>
  <skos:altLabel>heat treatment of metals</skos:altLabel>
  <skos:altLabel>hydrogen embrittlement</skos:altLabel>
  <skos:altLabel>intermetallics</skos:altLabel>
  <skos:altLabel>mechanical properties of alloys</skos:altLabel>
  <skos:altLabel>mechanical properties of metals</skos:altLabel>
  <skos:altLabel>metal crystals</skos:altLabel>
  <skos:altLabel>metallic fibers</skos:altLabel>
  <skos:altLabel>metallic materials</skos:altLabel>
  <skos:altLabel>metallography</skos:altLabel>
  <skos:altLabel>metallurgy</skos:altLabel>
  <skos:altLabel>metals</skos:altLabel>
  <skos:altLabel>microstructure of welded joints</skos:altLabel>
  <skos:altLabel>offgassing/outgassing (metallic materials)</skos:altLabel>
  <skos:altLabel>packing (metallic materials)</skos:altLabel>
  <skos:altLabel>phase equilibrium</skos:altLabel>
  <skos:altLabel>physical properties of alloys</skos:altLabel>
  <skos:altLabel>physical properties of metals</skos:altLabel>
  <skos:altLabel>powder metallurgy</skos:altLabel>
  <skos:altLabel>protection of alloys</skos:altLabel>
  <skos:altLabel>protection of materials (metallic)</skos:altLabel>
  <skos:altLabel>protective coatings (metallic materials)</skos:altLabel>
  <skos:altLabel>refractory materials</skos:altLabel>
  <skos:altLabel>reinforcing filaments (metallic materials)</skos:altLabel>
  <skos:altLabel>research on metallic materials</skos:altLabel>
  <skos:altLabel>sealants (metallic materials)</skos:altLabel>
  <skos:altLabel>shear strength (metallic materials)</skos:altLabel>
  <skos:altLabel>sintering (metallic materials)</skos:altLabel>
  <skos:altLabel>stress corrosion cracking</skos:altLabel>
  <skos:altLabel>surface hardening of metals</skos:altLabel>
  <skos:altLabel>surface properties (metallic materials)</skos:altLabel>
  <skos:altLabel>tensile strength (metallic materials)</skos:altLabel>
  <skos:altLabel>testing of alloys</skos:altLabel>
  <skos:altLabel>testing of materials (metallic materials)</skos:altLabel>
  <skos:altLabel>vacuum arc melting</skos:altLabel>
  <skos:altLabel>welded joints (microstructure)</skos:altLabel>
  <skos:altLabel>whiskers (metallic materials)</skos:altLabel>
  <skos:broader rdf:resource='subj:1058'/>
  <nt2:status>Approved</nt2:status>
  <nt2:type>Descriptor</nt2:type>
  <nt2:inputdate>2007-01-11</nt2:inputdate>
  <dcterms:dateAccepted>2006-12-01</dcterms:dateAccepted>
  <dcterms:modified>2007-01-11</dcterms:modified>
  <nt2:notValidDate></nt2:notValidDate>
  <nt2:code>26</nt2:code>
 </skos:Concept>
 <skos:Concept rdf:about='subj:72'>
  <skos:prefLabel>Atomic and Molecular Physics</skos:prefLabel>
  <skos:scopeNote>Includes atomic and molecular structure, electron
    properties, and atomic and molecular spectra. For
    elementary particle physics see 77 Physics of Elementary
    Particles and Fields; for nuclear physics see 73 Nuclear
    Physics.
  </skos:scopeNote>
  <skos:altLabel>absorption of radiation by atoms</skos:altLabel>
  <skos:altLabel>activation analysis</skos:altLabel>
  <skos:altLabel>atomic beam measurements</skos:altLabel>
  <skos:altLabel>atomic collisions</skos:altLabel>
  <skos:altLabel>atomic electron properties</skos:altLabel>
  <skos:altLabel>atomic energy levels</skos:altLabel>
  <skos:altLabel>atomic frequency standards</skos:altLabel>
  <skos:altLabel>atomic fuels (space applications)</skos:altLabel>
  <skos:altLabel>atomic nuclei</skos:altLabel>
  <skos:altLabel>atomic physics</skos:altLabel>
  <skos:altLabel>atomic reactions</skos:altLabel>
  <skos:altLabel>atomic spectra</skos:altLabel>
  <skos:altLabel>atomic structure</skos:altLabel>
  <skos:altLabel>electron collisions</skos:altLabel>
  <skos:altLabel>electron scattering</skos:altLabel>
  <skos:altLabel>emission of radiation by atoms</skos:altLabel>
  <skos:altLabel>fluorescence</skos:altLabel>
  <skos:altLabel>intermolecular forces</skos:altLabel>
  <skos:altLabel>ion beams (theory)</skos:altLabel>
  <skos:altLabel>ion dynamics</skos:altLabel>
  <skos:altLabel>ion exchange</skos:altLabel>
  <skos:altLabel>luminescence (atomic physics)</skos:altLabel>
  <skos:altLabel>molecular beams</skos:altLabel>
  <skos:altLabel>molecular collision theory</skos:altLabel>
  <skos:altLabel>molecular energy</skos:altLabel>
  <skos:altLabel>molecular interactions</skos:altLabel>
  <skos:altLabel>molecular physics</skos:altLabel>
  <skos:altLabel>molecular properties</skos:altLabel>
  <skos:altLabel>molecular spectra</skos:altLabel>
  <skos:altLabel>molecular spectroscopy</skos:altLabel>
  <skos:altLabel>molecular structure</skos:altLabel>
  <skos:altLabel>photon interactions with atoms and molecules</skos:altLabel>
  <skos:altLabel>radiation absorption by atoms</skos:altLabel>
  <skos:altLabel>theories of atomic physics</skos:altLabel>
  <skos:altLabel>theories of molecular physics</skos:altLabel>
  <skos:broader rdf:resource='subj:2528'/>
  <nt2:status>Approved</nt2:status>
  <nt2:type>Descriptor</nt2:type>
  <nt2:inputdate>2007-01-11</nt2:inputdate>
  <dcterms:dateAccepted>2006-12-01</dcterms:dateAccepted>
  <dcterms:modified>2007-01-11</dcterms:modified>
  <nt2:notValidDate></nt2:notValidDate>
  <nt2:code>72</nt2:code>
 </skos:Concept>
 <skos:Concept rdf:about='subj:81'>
  <skos:prefLabel>Administration and Management</skos:prefLabel>
  <skos:scopeNote>Includes management planning and research.
  </skos:scopeNote>
  <skos:altLabel>administration</skos:altLabel>
  <skos:altLabel>administrative planning</skos:altLabel>
  <skos:altLabel>budgeting (management)</skos:altLabel>
  <skos:altLabel>contract procurement</skos:altLabel>
  <skos:altLabel>contract supervision</skos:altLabel>
  <skos:altLabel>critical path method</skos:altLabel>
  <skos:altLabel>decision making</skos:altLabel>
  <skos:altLabel>management</skos:altLabel>
  <skos:altLabel>management planning</skos:altLabel>
  <skos:altLabel>management research</skos:altLabel>
  <skos:altLabel>management tools</skos:altLabel>
  <skos:altLabel>PERT (Program Evaluation and Review Technique)</skos:altLabel>
  <skos:altLabel>program management</skos:altLabel>
  <skos:altLabel>project management</skos:altLabel>
  <skos:altLabel>research management</skos:altLabel>
  <skos:altLabel>research planning</skos:altLabel>
  <skos:altLabel>space commercialization (management)</skos:altLabel>
  <skos:broader rdf:resource='subj:2767'/>
  <nt2:status>Approved</nt2:status>
  <nt2:type>Descriptor</nt2:type>
  <nt2:inputdate>2007-01-11</nt2:inputdate>
  <dcterms:dateAccepted>2006-12-01</dcterms:dateAccepted>
  <dcterms:modified>2007-01-11</dcterms:modified>
  <nt2:notValidDate></nt2:notValidDate>
  <nt2:code>81</nt2:code>
 </skos:Concept>
 <skos:Concept rdf:about='subj:1058'>
  <skos:prefLabel>Chemistry and Materials</skos:prefLabel>
  <skos:scopeNote>Includes chemistry and materials (general); composite
    materials; inorganic, organic and physical chemistry;
    metals and metallic materials; nonmetallic materials;
    propellants and fuels; and space processing.
  </skos:scopeNote>
  <skos:broader rdf:resource='subj:100'/>
  <skos:narrower rdf:resource='subj:23'/>
  <skos:narrower rdf:resource='subj:24'/>
  <skos:narrower rdf:resource='subj:25'/>
  <skos:narrower rdf:resource='subj:26'/>
  <skos:narrower rdf:resource='subj:27'/>
  <skos:narrower rdf:resource='subj:28'/>
  <skos:narrower rdf:resource='subj:29'/>
  <nt2:status>Approved</nt2:status>
  <nt2:type>Descriptor</nt2:type>
  <nt2:inputdate>2007-01-11</nt2:inputdate>
  <dcterms:dateAccepted>2006-12-01</dcterms:dateAccepted>
  <dcterms:modified>2007-01-11</dcterms:modified>
  <nt2:notValidDate></nt2:notValidDate>
  <nt2:code>1058</nt2:code>
 </skos:Concept>
 <skos:Concept rdf:about='subj:77'>
  <skos:prefLabel>Physics of Elementary Particles and Fields</skos:prefLabel>
  <skos:scopeNote>Includes quantum mechanics; theoretical physics; and
    statistical mechanics. For related information see also 72
    Atomic and Molecular Physics; 73 Nuclear Physics; and 25
    Inorganic, Organic and Physical Chemistry.
  </skos:scopeNote>
  <skos:altLabel>annihilation reactions</skos:altLabel>
  <skos:altLabel>antimatter</skos:altLabel>
  <skos:altLabel>antiparticles</skos:altLabel>
  <skos:altLabel>baryons</skos:altLabel>
  <skos:altLabel>Boltzmann statistics</skos:altLabel>
  <skos:altLabel>Bose and Fermi statistics quantum mechanics</skos:altLabel>
  <skos:altLabel>bosons quarks</skos:altLabel>
  <skos:altLabel>elementary particle interactions</skos:altLabel>
  <skos:altLabel>elementary particles</skos:altLabel>
  <skos:altLabel>fermions</skos:altLabel>
  <skos:altLabel>Feynman diagrams</skos:altLabel>
  <skos:altLabel>gauge field theory</skos:altLabel>
  <skos:altLabel>high energy physics</skos:altLabel>
  <skos:altLabel>kaons</skos:altLabel>
  <skos:altLabel>leptons</skos:altLabel>
  <skos:altLabel>mesons</skos:altLabel>
  <skos:altLabel>momentum transfer (particle interactions)</skos:altLabel>
  <skos:altLabel>neutrinos</skos:altLabel>
  <skos:altLabel>neutron properties</skos:altLabel>
  <skos:altLabel>neutron sources</skos:altLabel>
  <skos:altLabel>neutron spectra</skos:altLabel>
  <skos:altLabel>particle physics</skos:altLabel>
  <skos:altLabel>pions</skos:altLabel>
  <skos:altLabel>quantum chromodynamics (QCD)</skos:altLabel>
  <skos:altLabel>quantum electrodynamics (QED)</skos:altLabel>
  <skos:altLabel>standard model (particle physics)</skos:altLabel>
  <skos:altLabel>statistical physics</skos:altLabel>
  <skos:altLabel>string theory</skos:altLabel>
  <skos:altLabel>strong interactions (field theory)</skos:altLabel>
  <skos:altLabel>supergravity</skos:altLabel>
  <skos:altLabel>superstring theory</skos:altLabel>
  <skos:altLabel>supersymmetry</skos:altLabel>
  <skos:altLabel>symmetry breaking</skos:altLabel>
  <skos:altLabel>theoretical physics</skos:altLabel>
  <skos:altLabel>theory of relativity</skos:altLabel>
  <skos:altLabel>unified field theory</skos:altLabel>
  <skos:altLabel>weak interactions (field theory)</skos:altLabel>
  <skos:broader rdf:resource='subj:2528'/>
  <nt2:status>Approved</nt2:status>
  <nt2:type>Descriptor</nt2:type>
  <nt2:inputdate>2007-01-11</nt2:inputdate>
  <dcterms:dateAccepted>2006-12-01</dcterms:dateAccepted>
  <dcterms:modified>2007-01-11</dcterms:modified>
  <nt2:notValidDate></nt2:notValidDate>
  <nt2:code>77</nt2:code>
 </skos:Concept>
 <skos:Concept rdf:about='subj:24'>
  <skos:prefLabel>Composite Materials</skos:prefLabel>
  <skos:scopeNote>Includes physical, chemical, and mechanical properties of
    laminates and other composite materials.
  </skos:scopeNote>
  <skos:altLabel>ablative materials (composite)</skos:altLabel>
  <skos:altLabel>boron fiber materials</skos:altLabel>
  <skos:altLabel>carbon fiber materials</skos:altLabel>
  <skos:altLabel>ceramic matrix composites</skos:altLabel>
  <skos:altLabel>epoxy matrix composites</skos:altLabel>
  <skos:altLabel>fatigue (composite materials)</skos:altLabel>
  <skos:altLabel>fiber composites</skos:altLabel>
  <skos:altLabel>fiber-matrix interfaces</skos:altLabel>
  <skos:altLabel>filament materials</skos:altLabel>
  <skos:altLabel>filament wound structures (composite materials)</skos:altLabel>
  <skos:altLabel>filament-matrix materials</skos:altLabel>
  <skos:altLabel>flammability (composite materials)</skos:altLabel>
  <skos:altLabel>glass fiber reinforced plastics</skos:altLabel>
  <skos:altLabel>honeycomb materials</skos:altLabel>
  <skos:altLabel>insulation (composite materials)</skos:altLabel>
  <skos:altLabel>laminates</skos:altLabel>
  <skos:altLabel>mechanical properties (composite materials)</skos:altLabel>
  <skos:altLabel>metal filament systems</skos:altLabel>
  <skos:altLabel>metal matrix composites (MMC)</skos:altLabel>
  <skos:altLabel>nanocomposites</skos:altLabel>
  <skos:altLabel>offgassing/outgassing (composite materials)</skos:altLabel>
  <skos:altLabel>polymer matrix composites</skos:altLabel>
  <skos:altLabel>reinforcing fibers (composite materials)</skos:altLabel>
  <skos:altLabel>shear strength (composite materials)</skos:altLabel>
  <skos:altLabel>stacking sequence (composite materials)</skos:altLabel>
  <skos:altLabel>surface properties (composite materials)</skos:altLabel>
  <skos:altLabel>tensile strength (composite materials)</skos:altLabel>
  <skos:altLabel>testing of materials (composite materials)</skos:altLabel>
  <skos:altLabel>whisker composites</skos:altLabel>
  <skos:altLabel>whiskers (composite materials)</skos:altLabel>
  <skos:altLabel>woven composites</skos:altLabel>
  <skos:broader rdf:resource='subj:1058'/>
  <nt2:status>Approved</nt2:status>
  <nt2:type>Descriptor</nt2:type>
  <nt2:inputdate>2007-01-11</nt2:inputdate>
  <dcterms:dateAccepted>2006-12-01</dcterms:dateAccepted>
  <dcterms:modified>2007-01-11</dcterms:modified>
  <nt2:notValidDate></nt2:notValidDate>
  <nt2:code>24</nt2:code>
 </skos:Concept>
 <skos:Concept rdf:about='subj:51'>
  <skos:prefLabel>Life Sciences (General)</skos:prefLabel>
  <skos:scopeNote>Includes general research topics related to plant and
    animal biology (non-human); ecology; microbiology; and also
    the origin, development, structure, and maintenance, of
    animals and plants in space and related environmental
    conditions. For specific topics in life sciences see
    categories 52 through 55.
  </skos:scopeNote>
  <skos:altLabel>acceleration effects (biological, animal and plant)</skos:altLabel>
  <skos:altLabel>altitude effects (biological, animal and plant)</skos:altLabel>
  <skos:altLabel>animal biology</skos:altLabel>
  <skos:altLabel>atmospheric pressure effects (biological, animal and plant)</skos:altLabel>
  <skos:altLabel>biochemistry</skos:altLabel>
  <skos:altLabel>bioelectronic instruments (applications, animal and plant)</skos:altLabel>
  <skos:altLabel>bioengineering (general)</skos:altLabel>
  <skos:altLabel>biological evolution (terrestrial)</skos:altLabel>
  <skos:altLabel>biology (general)</skos:altLabel>
  <skos:altLabel>botany</skos:altLabel>
  <skos:altLabel>chronobiology (animal and plant)</skos:altLabel>
  <skos:altLabel>circadian rhythm (animal and plant)</skos:altLabel>
  <skos:altLabel>diurnal effects (biological, animal and plant)</skos:altLabel>
  <skos:altLabel>electromagnetic field effects (biological, animal and plant)</skos:altLabel>
  <skos:altLabel>environmental effects (biological, animal and plant)</skos:altLabel>
  <skos:altLabel>estivation</skos:altLabel>
  <skos:altLabel>farming in space (general)</skos:altLabel>
  <skos:altLabel>genetics (animal and plant)</skos:altLabel>
  <skos:altLabel>gravitational effects (biological, animal and plant)</skos:altLabel>
  <skos:altLabel>hibernation</skos:altLabel>
  <skos:altLabel>magnetic field effects (biological, animal and plant)</skos:altLabel>
  <skos:altLabel>microbiology</skos:altLabel>
  <skos:altLabel>microgravity effects (biological, animal and plant)</skos:altLabel>
  <skos:altLabel>origin of life (terrestrial)</skos:altLabel>
  <skos:altLabel>osmosis (biological)</skos:altLabel>
  <skos:altLabel>plants</skos:altLabel>
  <skos:altLabel>quarantine (animal and plant)</skos:altLabel>
  <skos:altLabel>radiation effects (biological, animal and plant)</skos:altLabel>
  <skos:altLabel>reduced gravity effects (biological, animal and plant)</skos:altLabel>
  <skos:altLabel>space environment effects (biological, animal and plant)</skos:altLabel>
  <skos:altLabel>telemedicine</skos:altLabel>
  <skos:altLabel>temperature effects (biological, animal and plant)</skos:altLabel>
  <skos:altLabel>weightlessness effects (biological, animal and plant)</skos:altLabel>
  <skos:altLabel>zero gravity effects (biological, animal and plant)</skos:altLabel>
  <skos:broader rdf:resource='subj:2127'/>
  <nt2:status>Approved</nt2:status>
  <nt2:type>Descriptor</nt2:type>
  <nt2:inputdate>2007-01-11</nt2:inputdate>
  <dcterms:dateAccepted>2006-12-01</dcterms:dateAccepted>
  <dcterms:modified>2007-01-11</dcterms:modified>
  <nt2:notValidDate></nt2:notValidDate>
  <nt2:code>51</nt2:code>
 </skos:Concept>
 <skos:Concept rdf:about='subj:88'>
  <skos:prefLabel>Space Sciences (General)</skos:prefLabel>
  <skos:scopeNote>Includes general research topics related to the natural
    space sciences. For specific topics in Space Sciences see
    categories 89 through 93.
  </skos:scopeNote>
  <skos:broader rdf:resource='subj:2871'/>
  <nt2:status>Approved</nt2:status>
  <nt2:type>Descriptor</nt2:type>
  <nt2:inputdate>2007-01-11</nt2:inputdate>
  <dcterms:dateAccepted>2006-12-01</dcterms:dateAccepted>
  <dcterms:modified>2007-01-11</dcterms:modified>
  <nt2:notValidDate></nt2:notValidDate>
  <nt2:code>88</nt2:code>
 </skos:Concept>
 <skos:Concept rdf:about='subj:60'>
  <skos:prefLabel>Computer Operations and Hardware</skos:prefLabel>
  <skos:scopeNote>Includes hardware for computer graphics, firmware and data
    processing. For components see 33 Electronics and
    Electrical Engineering. For computer vision see 63
    Cybernetics, Artificial Intelligence and Robotics.
  </skos:scopeNote>
  <skos:altLabel>analog computers</skos:altLabel>
  <skos:altLabel>architecture (computers)</skos:altLabel>
  <skos:altLabel>automatic data processors (ADP)</skos:altLabel>
  <skos:altLabel>central processing unit (CPU)</skos:altLabel>
  <skos:altLabel>computer buffers</skos:altLabel>
  <skos:altLabel>computer display devices</skos:altLabel>
  <skos:altLabel>computer graphics (hardware)</skos:altLabel>
  <skos:altLabel>computer hardware</skos:altLabel>
  <skos:altLabel>computer hardware design</skos:altLabel>
  <skos:altLabel>computer interfacing equipment</skos:altLabel>
  <skos:altLabel>computer manufacturing</skos:altLabel>
  <skos:altLabel>computer memory devices</skos:altLabel>
  <skos:altLabel>computer operations</skos:altLabel>
  <skos:altLabel>computer peripheral equipment</skos:altLabel>
  <skos:altLabel>computer printers</skos:altLabel>
  <skos:altLabel>computer storage devices</skos:altLabel>
  <skos:altLabel>computer storage techniques</skos:altLabel>
  <skos:altLabel>computers (hardware)</skos:altLabel>
  <skos:altLabel>data input devices</skos:altLabel>
  <skos:altLabel>data processing</skos:altLabel>
  <skos:altLabel>digital computers</skos:altLabel>
  <skos:altLabel>digital storage devices</skos:altLabel>
  <skos:altLabel>digital storage techniques</skos:altLabel>
  <skos:altLabel>firmware</skos:altLabel>
  <skos:altLabel>hybrid computers</skos:altLabel>
  <skos:altLabel>input devices</skos:altLabel>
  <skos:altLabel>mainframes</skos:altLabel>
  <skos:altLabel>mechanical computers</skos:altLabel>
  <skos:altLabel>memory devices (computer)</skos:altLabel>
  <skos:altLabel>microcomputers</skos:altLabel>
  <skos:altLabel>minicomputers</skos:altLabel>
  <skos:altLabel>modems</skos:altLabel>
  <skos:altLabel>multiprocessors (hardware)</skos:altLabel>
  <skos:altLabel>optical scanners (computer, peripheral equipment)</skos:altLabel>
  <skos:altLabel>output devices (computers)</skos:altLabel>
  <skos:altLabel>parallel processing (hardware)</skos:altLabel>
  <skos:altLabel>personal computers</skos:altLabel>
  <skos:altLabel>plotters</skos:altLabel>
  <skos:altLabel>processors (hardware)</skos:altLabel>
  <skos:altLabel>random access memories</skos:altLabel>
  <skos:altLabel>read-only memories</skos:altLabel>
  <skos:altLabel>remote input equipment</skos:altLabel>
  <skos:altLabel>remote readout equipment</skos:altLabel>
  <skos:altLabel>remote terminals</skos:altLabel>
  <skos:altLabel>spaceborne computers</skos:altLabel>
  <skos:altLabel>supercomputers</skos:altLabel>
  <skos:broader rdf:resource='subj:2321'/>
  <nt2:status>Approved</nt2:status>
  <nt2:type>Descriptor</nt2:type>
  <nt2:inputdate>2007-01-11</nt2:inputdate>
  <dcterms:dateAccepted>2006-12-01</dcterms:dateAccepted>
  <dcterms:modified>2007-01-11</dcterms:modified>
  <nt2:notValidDate></nt2:notValidDate>
  <nt2:code>60</nt2:code>
 </skos:Concept>
</rdf:RDF>


"""

################################################
'''
from pprint import pprint

soup = BeautifulSoup(jpl_skos_xml)

results = {}

for obj in soup.find_all("skos:concept"):
    for broad in obj.find_all('skos:broader'):
        c = [s for s in broad["rdf:resource"] if s.isdigit()]
        code = int(str.join('', c))
        print(broad['rdf:resource'], code)
        for obj in soup.find_all("skos:concept")

        # obj = broad.find('rdf:about'='subj:' + str(code))


    obj_code = str(obj.find("nt2:code").string)
    print(obj_code)
    results[obj_code] = { 'label': obj.find("skos:preflabel").string,
                          'res': "" }


pprint(results)
'''

if __name__ == "__main__":
    print("This is a useful collection of data, not a stand-alone script")