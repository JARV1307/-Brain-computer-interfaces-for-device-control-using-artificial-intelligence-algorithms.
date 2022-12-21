# -Brain-computer-interfaces-for-device-control-using-artificial-intelligence-algorithms.
Development of a Brain - Computer Interface (BCI) based on artificial intelligence algorithms to classify patterns of experiments using Steady State Visually Evoked Potentials (SSVEP) 

this project aims to design and implement a brain-computer interface with steady-state visual stimuli (SSVEP) for the control of the displacement of a device. 

For now, Python has been used for the development of both the experiment and the data processing. We are also looking to implement the system in real time ensuring high accuracy with low computational cost.

The interface of the experiment was made using PSYCHOPY: https://www.psychopy.org/

For the data adquisition we are using the Ultracortex MK IV from OpenBCI and also we are using the GUI from the manufacturer: https://openbci.com/#gsc.tab=0

For the experiment we set 4 stimuli frecuencies: 6.6 Hz, 7.5Hz, 8.57Hz and 10Hz with a white square. Those stimulies are presented on a screen with a refresh rate of 60Hz, and they appear pseudorandomly at intervals of 3.5 seconds for each stimuli.

![image](https://user-images.githubusercontent.com/59260995/209015875-72eccc05-3e44-48af-9516-8ac86af9b075.png)


'''We are currently trying to synchronize the visual stimuli with the acquisition of the data to be able to label them correctly.'''
