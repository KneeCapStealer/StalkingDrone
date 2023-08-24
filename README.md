##### --------- School project ---------
# StalkingDrone
This drone will stalk you into your nightmares.

## The Plan
### OpenCV
We will make a drone that follows people around using it's camera. This is achieved using the open source library [OpenCV](https://opencv.org/).
OpenCV means 'Open Computer Vision', Computer vision is a term used to describe a computer reacting to input from a camera. We can use OpenCV to find human figures, faces, shapes and colours. Using this information we can track people and follow them.

### The Drone
The drone will be programmed using the library [DjiTelloPy](https://github.com/damiafuentes/DJITelloPy) with this library we can connect to the drone using wi-fi. From the library we can oder the drone to move, turn, start and stop. Furthermore we can get input from it's camera. We can then use this input together with OpenCV and then tell the drone where to fly via the output from OpenCV.

## Further Research

### Hvad giver den af muligheder og begrænsninger?
- Mulighed for remote styring med controller eller gennem selvskrevet kode.
- Utrolig stabil flyvning i 13 minutters intervaller før batteriet går tør.
- 720P live camera feed der kan tilgås med kode.
![image](https://github.com/KneeCapStealer/StalkingDrone/assets/104348534/20f25577-dc77-46e5-a904-ca567fc93f76)

### Hvilke teknologier sidder i dronen?
- Intel 14-core processor
- Onboard Movidius Myriad 2 VPU (Video Processing Unit) til avanceret imaging og vision processing.
- Optical flow sensor
- Barometrisk tryk sensor
- 6-akse gyro og accelerometer system.
- 720p 5MP kamera

### Hvordan holder den sig i luften?
Propeller og motorere 🙂

### Hvordan holder den sin position?
https://www.compsmag.com/reviews/dji-ryze-tello-review/

- #### Electronic Image Stabilization (EIS):
  The Tello drone is equipped with a 6-axis gyro and accelerometer system that helps stabilize its flight by measuring its orientation and movement
  in real-time. This information is used to adjust the motor speeds and control surfaces to maintain stability.
  https://en.techreviewer.de/dji-ryze-tello/

- #### Optical Flow Sensor:
  The drone is equipped with an optical flow sensor on its underside. This sensor captures images of the ground and analyzes the patterns of
  movement to determine the drone's position relative to the ground. This is particularly useful for maintaining stability when flying at lower
  altitudes where GPS signals might be weaker or less accurate.
  https://www.compsmag.com/reviews/dji-ryze-tello-review/
  ![Stavbility picture](https://github.com/KneeCapStealer/StalkingDrone/blob/main/pictures/GitHUB%20pictures/DJI_tello_stability.png?raw=true)

- #### Barometric Pressure Sensor:
  The drone also has a barometric pressure sensor that measures the air pressure at its current altitude. By using this information, the drone can
  adjust its altitude to maintain a stable height above the ground.
  https://www.eduporium.com/tello-edu-programmable-drone.html

- #### Flight Controller:
  The Tello drone's flight controller processes the data from all the sensors and adjusts the motor speeds and control surfaces to ensure stable
  flight. It uses algorithms to interpret the sensor data and make real-time adjustments.

- #### Software Algorithms:
  DJI has developed advanced flight control algorithms that help the drone make rapid adjustments to its position and orientation. These algorithms
  take into account various sensor inputs to correct for any deviations from the desired flight path.

### Hvordan kobler man til den?
- Gennem WiFi
- Gennem deres app

### Hvordan kan man programmere den? – Og med hvilke værktøjer/sprog?
- Dronen kan progammeres normalt med python eller swift eller med visual scripting i scratch.

#### Hvad skal der til for at komme i gang med python?
I python skal man installere et library kaldet DjiTelloPy, hvilket giver os en masse indbygget kommandoer til at få dronen til at flyve som vi vil.


[Slides](https://docs.google.com/presentation/d/1WnB7Oa8djt5TXJY0MSV2IE0C44vwi-oS0N73car16F8/edit?usp=sharing)

[Docs](https://docs.google.com/document/d/1SxukPcr4lkwFjZu1Y7ejZoejWrY_VKYavuYP73BwPDw/edit?usp=sharing)
