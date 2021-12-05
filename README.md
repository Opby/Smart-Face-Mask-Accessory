# Problem: 
Due to the covid-19 outbreak, wearing masks is becoming a new norm. Masks protect people from virus but, at the same time, muffle people's voice and make it harder for people to communicate

# Objectives: 
The solution is to design a smart voice amplifying accessory that can clip onto any face mask. In this project, I use Raspberry PI and sensor/audio EVBs to demonstrate the key functions of this smart accessory and identify the key engineering problems with solutions.

# Constraints:
* The maximum cost of the accessory is around $30 -Need to select components fit into budget. 
* The time limit to provide a prototype is a week - Raspberry PI and market available EVBs are used to construct the prototype.

# Methods:
* Design: 
    * Amplify the voice with a microphone, amplifier and a speaker.
    * Use a humidity sensor to control the on/off so that users do not have to manually turn it on/off before using while maximizing the battery life
* Prototype build:
    * Raspberry PI is used to run Python program that will control humidity sensor
    * Silicon Lab multi-sensor EVB is used to provide the humidity sensing
    * A Voice bonnet with MEMS microphone and voice amplifier with two external speakers are used
* Prototype testing:
    * A voice volume meter APP on smartphone is used to measure voice volume

# Design Diagram
![Diagram](https://github.com/Opby/Smart-Face-Mask-Accessory/blob/main/Design%20Diagram.png)

# Prototype 
![Prototype](https://github.com/Opby/Smart-Face-Mask-Accessory/blob/main/Prototype.jpeg)

# Results
Voice Amplification
* Using voice volume meter, we baselined the typical voice volume with a face mask is 57dB over noise floor
* By adjusting the volume gain with Python code, we determine the optimal gain for the Amp is -16 to -18: Original voice get amplified by 10dB w/o noticeable echo

![Results](https://github.com/Opby/Smart-Face-Mask-Accessory/blob/main/results.png)

