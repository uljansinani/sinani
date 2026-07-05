# DCAM — Dynamic Coating Application Module

## Role and deployment

Senior Mechatronics Engineer leading the Dynamic Coating Application Module (DCAM) project. The DCAM was an electro-mechanical module that applies protective coatings onto power-grid conductors. Its purpose was to automate the work — previously done by lineman — of manually connecting and disconnecting the Coating Application Module (CAM), thus automating its deployment remotely from the base station.

The automation of the Coating Module deployment via DCAM was initially done for the base robotics platforms (at our test facility), and later on the DCAM V1 moved to V2 whereby it was optimised to be used for UAV deployed, which was tested and pilot-run in Canada in a decommissioned line at Hydro-Québec Canada, with no line operators at height involved during this deployment of the module via LineDrone.

## Mechanism

I designed the mechanism in Fusion 360, chose the actuation method, and linkage configuration that made possible the locking feature of the module's arms. Essentially the module was using over-centre configuration to have its arms locked without requiring actuator assistance to retain the max clamping forces needed to apply the coating uniformly on the conductor, while it was pulled along the conductor from the drone. This made it possible to free linemen from many hours of the mundane tasks of installing and uninstalling the module every time the module had to be used, and it unlocked for us to move from the concept stage to manufacturing stage.

## Did NOT do (binding)

No embedded electronics designed or built. No sensing. No closed-loop control — actuators driven open-loop by external PWM from BRP/UAV. "Full stack" claim not permitted. Concept unit required no electronics beyond the actuators' integrated drivers. Pilot conductor was decommissioned/de-energized — "live" / "live-line" / "energized conductor" claims not permitted.

## Media (binding)

- Field photo (`assets/dcam-linedrone-hydroquebec.jpg`): from AssetCool Ltd. public trial / press material — [Hydro-Québec partnership announcement, Jan 2026](https://www.assetcool.com/post/assetcool-announces-strategic-partnership-with-hydro-qu%C3%A9bec-to-advance-successfully-piloted-drone-ba). Published on sinani.ai with visible company credit; image is employer press material, not personal portfolio IP.

## Card copy (compressed from above)

Paragraph 1: Senior Mechatronics Engineer leading DCAM — an electro-mechanical module that automates the deployment of a coating application module onto power-grid conductors, replacing the manual connect/disconnect work previously done by linemen at height. V1 deployed from a robotic base platform at the test facility; V2 optimised for UAV deployment and pilot-run on a decommissioned Hydro-Québec line via LineDrone — no operators at height.

Paragraph 2: Designed the mechanism in Fusion 360: an over-centre linkage that locks the module's arms closed without actuator assistance, retaining full clamping force as the module is pulled along the conductor. Actuation by Actuonix L12 linear actuators with integrated drivers, driven open-loop by external PWM from the platform or UAV — no onboard electronics. Took the module from concept to manufacture.
