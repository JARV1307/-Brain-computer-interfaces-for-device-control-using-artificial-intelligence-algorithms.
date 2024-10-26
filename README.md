# -Brain-computer-interfaces-for-device-control-using-artificial-intelligence-algorithms.
Development of a Brain - Computer Interface (BCI) based on artificial intelligence algorithms to classify patterns of experiments using Steady State Visually Evoked Potentials (SSVEP) 

this project aims to design and implement a brain-computer interface with steady-state visual stimuli (SSVEP) for the control of the displacement of a device. 

For now, Python has been used for the development of both the experiment and the data processing. We are also looking to implement the system in real time ensuring high accuracy with low computational cost.

The interface of the experiment was made using PSYCHOPY: https://www.psychopy.org/

For the data adquisition we are using the Ultracortex MK IV from OpenBCI and also we are using the GUI from the manufacturer: https://openbci.com/#gsc.tab=0

For the experiment we set 4 stimuli frecuencies: 6.6 Hz, 7.5Hz, 8.57Hz and 10Hz with a white square. Those stimulies are presented on a screen with a refresh rate of 60Hz, and they appear pseudorandomly at intervals of 4 seconds for each stimuli.


![209015875-72eccc05-3e44-48af-9516-8ac86af9b075](https://user-images.githubusercontent.com/59260995/219917356-0e06dd98-d843-4054-b997-72a4985fd897.png)


4 seconds for each stimuli shows better responses than using 3.5 seconds


'''We are currently trying to synchronize the visual stimuli with the acquisition of the data to be able to label them correctly.'''

One solution - preload a list with the sequence that the experiment will follow and then add the events manually in the python script for data processing with the MNE library. Knowing that every single one of the events have a duration of 4 seconds




So far, using 18 features, some classification results have been achieved of between 80 to 70 % accuracy. But mostly we have encountered a classification percentage between 40 to 60%.


# Experimentation design:

Materials:
| Materials | Description |
| --- | --- |
| cyton board | From OpenBCI |
| PC | with graphics card at least RTX-3050 |
| Screen | with a stable refresh rate of 60 Hz  |

The user must first undergo a routine checkup to determine that he/she does not have any medical condition, must not have a history of epilepsy, his/her blood pressure is measured, his/her sex and age are noted, and the experiment is mainly carried out with people who have good eyesight and are able to maintain concentration.

the experimentation area must be divided in two: one where the data acquisition system is, in our case the PC with the OpenBCI software, and the other area where the only electronic devices present must be the screen where the visual stimuli will be displayed and the other device is the OpenBCI Cyton board, which is where the brainwave sensor is mounted.
