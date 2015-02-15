__author__ = 'lorenzo'

components = [
  {
    "id": 15,
    "pbtype": [
      "bus attitude orbit determination control"
    ],
    "name": "AODCS Simple",
    "description": "Use gravity and spinning to stabilize your spacecraft for free. Pointing is not that accurate.",
    "slug": "aodcs_simple",
    "link": "",
    "category": "bus"
  },
  {
    "id": 14,
    "pbtype": [
      "bus attitude orbit determination control"
    ],
    "name": "AODCS Robust",
    "description": "You wanna point an ant 1000 km away? You can, but is resource-consuming.",
    "slug": "aodcs_robust",
    "link": "",
    "category": "bus"
  },
  {
    "id": 10,
    "pbtype": [
      "bus backup power"
    ],
    "name": "Backup Power Batteries",
    "description": "Always good and cheap, but low specific energy.",
    "slug": "pow_sec_batt",
    "link": "",
    "category": "bus"
  },
  {
    "id": 11,
    "pbtype": [
      "bus backup power"
    ],
    "name": "Backup Power Fuel Cells",
    "description": "Always good and good specific energy, but not that cheap.",
    "slug": "pow_sec_fc",
    "link": "",
    "category": "bus"
  },
  {
    "id": 18,
    "pbtype": [
      "bus command and data handling"
    ],
    "name": "Command and Data Handling Standard",
    "description": "\"Low\"cost protocols that are not optimized.",
    "slug": "cdh_standard",
    "link": "",
    "category": "bus"
  },
  {
    "id": 19,
    "pbtype": [
      "bus command and data handling"
    ],
    "name": "Command and Data Handling Optimized",
    "description": "Optimized high-cost protocols and algorithms for a proper data handling.",
    "slug": "cdh_optim",
    "link": "",
    "category": "bus"
  },
  {
    "id": 12,
    "pbtype": [
      "bus communications"
    ],
    "name": "Communication Monodirectional",
    "description": "Consumes less power, but it must be pointed.",
    "slug": "comm_mono",
    "link": "",
    "category": "bus"
  },
  {
    "id": 13,
    "pbtype": [
      "bus communications"
    ],
    "name": "Communication Omnidirectional",
    "description": "No pointing needed! Higher power required though...",
    "slug": "comm_omni",
    "link": "",
    "category": "bus"
  },
  {
    "id": 9,
    "pbtype": [
      "bus primary power"
    ],
    "name": "Primary Power RTG",
    "description": "Works everywhere, but it is radioactive.",
    "slug": "pow_prim_rtg",
    "link": "",
    "category": "bus"
  },
  {
    "id": 8,
    "pbtype": [
      "bus primary power"
    ],
    "name": "Primary Power Solar Arrays",
    "description": "The closer to the Sun, the better! But, they work even quite far away.",
    "slug": "pow_prim_panels",
    "link": "",
    "category": "bus"
  },
  {
    "id": 16,
    "pbtype": [
      "bus propulsion"
    ],
    "name": "Propulsion Electric",
    "description": "Super cool, but right now it works good only if you accept long mission times or high power.",
    "slug": "prop_electr",
    "link": "",
    "category": "bus"
  },
  {
    "id": 17,
    "pbtype": [
      "bus propulsion"
    ],
    "name": "Propulsion Chemical",
    "description": "Impulsive propulsion that always works, but costs more for long missions.",
    "slug": "prop_chem",
    "link": "",
    "category": "bus"
  },
  {
    "id": 23,
    "pbtype": [
      "payload remote sensing"
    ],
    "name": "Microwave sensor",
    "description": "Seize microwave section of EM-spectre",
    "slug": "microwave",
    "link": "",
    "category": "payload"
  },
  {
    "id": 26,
    "pbtype": [
      "payload remote sensing"
    ],
    "name": "X-rays sensor",
    "description": "Seize X-rays ",
    "slug": "x_rays",
    "link": "",
    "category": "payload"
  },
  {
    "id": 2,
    "pbtype": [
      "payload remote sensing"
    ],
    "name": "Radio Sensor",
    "description": "Similar to the optical sensor, but on different wavelenghts.",
    "slug": "radio_sensor",
    "link": "",
    "category": "payload"
  },
  {
    "id": 1,
    "pbtype": [
      "payload remote sensing"
    ],
    "name": "Visible Light Sensor",
    "description": "It's like a camera, but in space! Seize the visible light. ",
    "slug": "opt_sensor",
    "link": "",
    "category": "payload"
  },
  {
    "id": 32,
    "pbtype": [
      "payload remote sensing"
    ],
    "name": "Magnetic fields metrics",
    "description": "Instruments used  to measure the magnetization of a magnetic material or to measure the strength and the direction of the magnetic field.",
    "slug": "mag",
    "link": "",
    "category": "payload"
  },
  {
    "id": 31,
    "pbtype": [
      "payload remote sensing"
    ],
    "name": "Altitude metrics (laser)",
    "description": "A laser altimeter is an instrument that measures the distance from an orbiting spacecraft to the surface of the planet or asteroid.",
    "slug": "laser_alt",
    "link": "",
    "category": "payload"
  },
  {
    "id": 5,
    "pbtype": [
      "payload remote sensing"
    ],
    "name": "Amplifier",
    "description": "Whenever you need to amplify a signal, whichever it is.",
    "slug": "amplifier",
    "link": "",
    "category": "payload"
  },
  {
    "id": 27,
    "pbtype": [
      "payload remote sensing"
    ],
    "name": "Gamma-rays sensor",
    "description": "Seize Gamma-rays",
    "slug": "gamma_rays",
    "link": "",
    "category": "payload"
  },
  {
    "id": 33,
    "pbtype": [
      "payload remote sensing"
    ],
    "name": "Gravitational wave detector",
    "description": "A gravitational-wave detector is any device designed to measure gravitational waves, tiny distortions of spacetime.",
    "slug": "grav",
    "link": "",
    "category": "payload"
  },
  {
    "id": 24,
    "pbtype": [
      "payload remote sensing"
    ],
    "name": "Infrared sensor",
    "description": "Seize infrared",
    "slug": "infrared",
    "link": "",
    "category": "payload"
  },
  {
    "id": 25,
    "pbtype": [
      "payload remote sensing"
    ],
    "name": "Ultraviolet sensor",
    "description": "Seizeultraviolet",
    "slug": "ultraviolet",
    "link": "",
    "category": "payload"
  },
  {
    "id": 38,
    "pbtype": [
      "payload scientific"
    ],
    "name": "Microdust Particles Analyzer",
    "description": "Scan dust particles ranging from nanometers to micrometers and imaging their surface",
    "slug": "microdust",
    "link": "",
    "category": "payload"
  },
  {
    "id": 36,
    "pbtype": [
      "payload scientific"
    ],
    "name": "Light polarization metrics",
    "description": "Measures light polarization",
    "slug": "photopolarimeter",
    "link": "",
    "category": "payload"
  },
  {
    "id": 35,
    "pbtype": [
      "payload scientific"
    ],
    "name": "Plasma Analyzer",
    "description": "Analyze and collect data about ionized gases.",
    "slug": "plasma",
    "link": "",
    "category": "payload"
  },
  {
    "id": 34,
    "pbtype": [
      "payload scientific"
    ],
    "name": "Particles Detector",
    "description": "Collect Data about different kinds of particles, from protons to smaller ones.",
    "slug": "particles",
    "link": "",
    "category": "payload"
  },
  {
    "id": 4,
    "pbtype": [
      "payload scientific"
    ],
    "name": "Surface & atmosphere probe",
    "description": "It can be sent on celestial bodies to collect samples and analyze them.",
    "slug": "probe",
    "link": "",
    "category": "payload"
  },
  {
    "id": 37,
    "pbtype": [
      "payload scientific"
    ],
    "name": "Ion Mass Analyzer",
    "description": "The mass spectrometer measures the charge to mass ratio and abundance of gas-phase ions",
    "slug": "ion_mass",
    "link": "",
    "category": "payload"
  },
  {
    "id": 21,
    "pbtype": [
      "bus structure"
    ],
    "name": "High Resistance Structure",
    "description": "It's like a bunker, but much more lighter and in space (so it is expensive)!",
    "slug": "struct_high_resist",
    "link": "",
    "category": "bus"
  },
  {
    "id": 20,
    "pbtype": [
      "bus structure"
    ],
    "name": "Standard Structure",
    "description": "Keeps it all together at a \"low\" cost, but might not be enough for highly-debris-populated zones. Radiation shielding might be a problem.",
    "slug": "struct_stand",
    "link": "",
    "category": "bus"
  },
  {
    "id": 6,
    "pbtype": [
      "bus thermal"
    ],
    "name": "Thermal Active",
    "description": "It allows a wider temperature range, but it needs power.",
    "slug": "therm_active",
    "link": "",
    "category": "bus"
  },
  {
    "id": 7,
    "pbtype": [
      "bus thermal"
    ],
    "name": "Thermal Passive",
    "description": "Doesn't consume any power, but cannot be used everywhere.",
    "slug": "therm_passive",
    "link": "",
    "category": "bus"
  }
]


print([c["id"] for c in components])
