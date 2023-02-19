from psychopy import locale_setup
from psychopy import prefs

from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding
import random

import psutil, platform
p = psutil.Process(os.getpid())

if platform.system() == 'Darwin' or platform.system() == 'Linux':
    p.nice(20)
else:
    p.nice(psutil.HIGH_PRIORITY_CLASS)

import psychopy.iohub as io
from psychopy.hardware import keyboard

# Store info about the experiment session
psychopyVersion = '2022.2.4'
expName = 'TEST2 version2'  # from the Builder filename that created this script
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1920, 1080], fullscr=True, screen=1, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[-1.0000, -1.0000, -1.0000], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = False
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize all components

# --- Initialize components for Routine "Bienvenida" ---
mensajeBienvenida = visual.TextStim(win=win, name='mensajeBienvenida',
    text='Bienvenido, participante',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
mensajeExplicacion = visual.TextStim(win=win, name='mensajeExplicacion',
    text='En el siguiente experimento se presentarán 4 figuras, colocadas en los extremos de la pantalla, las cuales parpadearán a diferentes frecuencias.\n\nEl experimento durará alrededor de 10 minutos, por lo que busque adoptar una posición cómoda. Cualquier inconveniente comuníquelo al investigador\n',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
text_4 = visual.TextStim(win=win, name='text_4',
    text='Por favor, mantenga la concentración durante toda la sesión, evite hacer movimientos bruscos y permanezca en una postura relajada',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
incioTeclado1 = keyboard.Keyboard()

# --- Initialize components for Routine "Pausa" ---
incioTeclado2 = keyboard.Keyboard()
mensajeAviso = visual.TextStim(win=win, name='mensajeAviso',
    text='Vamos a comprobar que todo este funcionando correctamente antes de iniciar el experimento',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
mensajeAviso2 = visual.TextStim(win=win, name='mensajeAviso2',
    text='Cuente hasta 20 mentalmente, con los ojos cerrados',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# --- Initialize components for Routine "BASELINE" ---
baseline_Image = visual.ImageStim(
    win=win,
    name='baseline_Image', 
    image='DRAW.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0), size=(0.35, 0.35),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# --- Initialize components for Routine "routine_6_6HZ" ---
BLANCO = visual.ImageStim(
    win=win,
    name='BLANCO', 
    image='C:/Users/jarv_/OneDrive/Desktop/BLANCO.png', mask=None, anchor='center',
    ori=0.0, pos=(0.72, 0), size=(0.35, 0.35),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# --- Initialize components for Routine "routine_7_5HZ" ---
BLANCO_2 = visual.ImageStim(
    win=win,
    name='BLANCO_2', 
    image='C:/Users/jarv_/OneDrive/Desktop/BLANCO.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0.32), size=(0.35, 0.35),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# --- Initialize components for Routine "routine_8_57HZ" ---
BLANCO_3 = visual.ImageStim(
    win=win,
    name='BLANCO_3', 
    image='C:/Users/jarv_/OneDrive/Desktop/BLANCO.png', mask=None, anchor='center',
    ori=0.0, pos=(-0.72, 0), size=(0.35, 0.35),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# --- Initialize components for Routine "routine_10HZ" ---
BLANCO_4 = visual.ImageStim(
    win=win,
    name='BLANCO_4', 
    image='C:/Users/jarv_/OneDrive/Desktop/BLANCO.png', mask=None, anchor='center',
    ori=0.0, pos=(0,-0.32), size=(0.35, 0.35),
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)

# --- Initialize components for Routine "Final" ---
mensajeSalida = visual.TextStim(win=win, name='mensajeSalida',
    text='La sesión ha finalizado\n\nPor favor, permanezca quieto hasta que el investigador entre a la sala',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
teclaSalida = keyboard.Keyboard()



# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 



# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "Bienvenida" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
incioTeclado1.keys = []
incioTeclado1.rt = []
_incioTeclado1_allKeys = []
# keep track of which components have finished
BienvenidaComponents = [mensajeBienvenida, mensajeExplicacion, text_4, incioTeclado1]
for thisComponent in BienvenidaComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Bienvenida" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *mensajeBienvenida* updates
    if mensajeBienvenida.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mensajeBienvenida.frameNStart = frameN  # exact frame index
        mensajeBienvenida.tStart = t  # local t and not account for scr refresh
        mensajeBienvenida.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mensajeBienvenida, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        #thisExp.timestampOnFlip(win, 'mensajeBienvenida.started')
        mensajeBienvenida.setAutoDraw(True)
    if mensajeBienvenida.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mensajeBienvenida.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            mensajeBienvenida.tStop = t  # not accounting for scr refresh
            mensajeBienvenida.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            #thisExp.timestampOnFlip(win, 'mensajeBienvenida.stopped')
            mensajeBienvenida.setAutoDraw(False)
    
    # *mensajeExplicacion* updates
    if mensajeExplicacion.status == NOT_STARTED and tThisFlip >= 5-frameTolerance:
        # keep track of start time/frame for later
        mensajeExplicacion.frameNStart = frameN  # exact frame index
        mensajeExplicacion.tStart = t  # local t and not account for scr refresh
        mensajeExplicacion.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mensajeExplicacion, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        #thisExp.timestampOnFlip(win, 'mensajeExplicacion.started')
        mensajeExplicacion.setAutoDraw(True)
    if mensajeExplicacion.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mensajeExplicacion.tStartRefresh + 18-frameTolerance:
            # keep track of stop time/frame for later
            mensajeExplicacion.tStop = t  # not accounting for scr refresh
            mensajeExplicacion.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            #thisExp.timestampOnFlip(win, 'mensajeExplicacion.stopped')
            mensajeExplicacion.setAutoDraw(False)
    
    # *text_4* updates
    if text_4.status == NOT_STARTED and tThisFlip >= 23-frameTolerance:
        # keep track of start time/frame for later
        text_4.frameNStart = frameN  # exact frame index
        text_4.tStart = t  # local t and not account for scr refresh
        text_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        #thisExp.timestampOnFlip(win, 'text_4.started')
        text_4.setAutoDraw(True)
    if text_4.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_4.tStartRefresh + 6-frameTolerance:
            # keep track of stop time/frame for later
            text_4.tStop = t  # not accounting for scr refresh
            text_4.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            #thisExp.timestampOnFlip(win, 'text_4.stopped')
            text_4.setAutoDraw(False)
    
    # *incioTeclado1* updates
    waitOnFlip = False
    if incioTeclado1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        incioTeclado1.frameNStart = frameN  # exact frame index
        incioTeclado1.tStart = t  # local t and not account for scr refresh
        incioTeclado1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(incioTeclado1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        #thisExp.timestampOnFlip(win, 'incioTeclado1.started')
        incioTeclado1.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(incioTeclado1.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(incioTeclado1.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if incioTeclado1.status == STARTED and not waitOnFlip:
        theseKeys = incioTeclado1.getKeys(keyList=['y','n','left','right','space'], waitRelease=False)
        _incioTeclado1_allKeys.extend(theseKeys)
        if len(_incioTeclado1_allKeys):
            incioTeclado1.keys = _incioTeclado1_allKeys[-1].name  # just the last key pressed
            incioTeclado1.rt = _incioTeclado1_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in BienvenidaComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Bienvenida" ---
for thisComponent in BienvenidaComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# the Routine "Bienvenida" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "Pausa" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
incioTeclado2.keys = []
incioTeclado2.rt = []
_incioTeclado2_allKeys = []
# keep track of which components have finished
PausaComponents = [incioTeclado2, mensajeAviso, mensajeAviso2]
for thisComponent in PausaComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Pausa" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *incioTeclado2* updates
    waitOnFlip = False
    if incioTeclado2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        incioTeclado2.frameNStart = frameN  # exact frame index
        incioTeclado2.tStart = t  # local t and not account for scr refresh
        incioTeclado2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(incioTeclado2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        #thisExp.timestampOnFlip(win, 'incioTeclado2.started')
        incioTeclado2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(incioTeclado2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(incioTeclado2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if incioTeclado2.status == STARTED and not waitOnFlip:
        theseKeys = incioTeclado2.getKeys(keyList=['a','space'], waitRelease=False)
        _incioTeclado2_allKeys.extend(theseKeys)
        if len(_incioTeclado2_allKeys):
            incioTeclado2.keys = _incioTeclado2_allKeys[-1].name  # just the last key pressed
            incioTeclado2.rt = _incioTeclado2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *mensajeAviso* updates
    if mensajeAviso.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        mensajeAviso.frameNStart = frameN  # exact frame index
        mensajeAviso.tStart = t  # local t and not account for scr refresh
        mensajeAviso.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mensajeAviso, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        #thisExp.timestampOnFlip(win, 'mensajeAviso.started')
        mensajeAviso.setAutoDraw(True)
    if mensajeAviso.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mensajeAviso.tStartRefresh + 5-frameTolerance:
            # keep track of stop time/frame for later
            mensajeAviso.tStop = t  # not accounting for scr refresh
            mensajeAviso.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            #thisExp.timestampOnFlip(win, 'mensajeAviso.stopped')
            mensajeAviso.setAutoDraw(False)
    
    # *mensajeAviso2* updates
    if mensajeAviso2.status == NOT_STARTED and tThisFlip >= 7-frameTolerance:
        # keep track of start time/frame for later
        mensajeAviso2.frameNStart = frameN  # exact frame index
        mensajeAviso2.tStart = t  # local t and not account for scr refresh
        mensajeAviso2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mensajeAviso2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        #thisExp.timestampOnFlip(win, 'mensajeAviso2.started')
        mensajeAviso2.setAutoDraw(True)
    if mensajeAviso2.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mensajeAviso2.tStartRefresh + 7-frameTolerance:
            # keep track of stop time/frame for later
            mensajeAviso2.tStop = t  # not accounting for scr refresh
            mensajeAviso2.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            #thisExp.timestampOnFlip(win, 'mensajeAviso2.stopped')
            mensajeAviso2.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in PausaComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Pausa" ---
for thisComponent in PausaComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses

#thisExp.nextEntry()
# the Routine "Pausa" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()





#STIMULI FUNCTIONS

def baseline():
    
    # --- Prepare to start Routine "BASELINE" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    BASELINEComponents = [baseline_Image]
    for thisComponent in BASELINEComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *baseline_Image* updates
        if baseline_Image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            baseline_Image.frameNStart = frameN  # exact frame index
            baseline_Image.tStart = t  # local t and not account for scr refresh
            baseline_Image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(baseline_Image, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            #thisExp.timestampOnFlip(win, 'baseline_Image.started')
            baseline_Image.setAutoDraw(True)
        if baseline_Image.status == STARTED:
            if frameN >= 240:
                # keep track of stop time/frame for later
                baseline_Image.tStop = t  # not accounting for scr refresh
                baseline_Image.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                #thisExp.timestampOnFlip(win, 'baseline_Image.stopped')
                baseline_Image.setAutoDraw(False)
    # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in BASELINEComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "BASELINE" ---
    for thisComponent in BASELINEComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "BASELINE" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()




def freq6_6():
    # --- Prepare to start Routine "routine_6_6HZ" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    routine_6_6HZComponents = [BLANCO]
    for thisComponent in routine_6_6HZComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "routine_6_6HZ" ---
    while continueRoutine and routineTimer.getTime() < 4:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *BLANCO* updates
        if BLANCO.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            BLANCO.frameNStart = frameN  # exact frame index
            BLANCO.tStart = t  # local t and not account for scr refresh
            BLANCO.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(BLANCO, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            #thisExp.timestampOnFlip(win, 'BLANCO.started')
            BLANCO.setAutoDraw(True)
        if BLANCO.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > BLANCO.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                BLANCO.tStop = t  # not accounting for scr refresh
                BLANCO.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                #thisExp.timestampOnFlip(win, 'BLANCO.stopped')
                BLANCO.setAutoDraw(False)
        if BLANCO.status == STARTED:  # only update if drawing
            BLANCO.setOpacity(frameN%9 >= 4, log=False)
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in routine_6_6HZComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "routine_6_6HZ" ---
    for thisComponent in routine_6_6HZComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-4.00000)


def freq7_5():
    # --- Prepare to start Routine "routine_7_5HZ" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    routine_7_5HZComponents = [BLANCO_2]
    for thisComponent in routine_7_5HZComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "routine_7_5HZ" ---
    while continueRoutine and routineTimer.getTime() < 4:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *BLANCO_2* updates
        if BLANCO_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            BLANCO_2.frameNStart = frameN  # exact frame index
            BLANCO_2.tStart = t  # local t and not account for scr refresh
            BLANCO_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(BLANCO_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            #thisExp.timestampOnFlip(win, 'BLANCO_2.started')
            BLANCO_2.setAutoDraw(True)
        if BLANCO_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > BLANCO_2.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                BLANCO_2.tStop = t  # not accounting for scr refresh
                BLANCO_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                #thisExp.timestampOnFlip(win, 'BLANCO_2.stopped')
                BLANCO_2.setAutoDraw(False)
        if BLANCO_2.status == STARTED:  # only update if drawing
            BLANCO_2.setOpacity(frameN%8 >= 4, log=False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in routine_7_5HZComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "routine_7_5HZ" ---
    for thisComponent in routine_7_5HZComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-4.00000)



def freq8_57():
    
    # --- Prepare to start Routine "routine_8_57HZ" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    routine_8_57HZComponents = [BLANCO_3]
    for thisComponent in routine_8_57HZComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "routine_8_57HZ" ---
    while continueRoutine and routineTimer.getTime() < 4:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *BLANCO_3* updates
        if BLANCO_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            BLANCO_3.frameNStart = frameN  # exact frame index
            BLANCO_3.tStart = t  # local t and not account for scr refresh
            BLANCO_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(BLANCO_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            #thisExp.timestampOnFlip(win, 'BLANCO_3.started')
            BLANCO_3.setAutoDraw(True)
        if BLANCO_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > BLANCO_3.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                BLANCO_3.tStop = t  # not accounting for scr refresh
                BLANCO_3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                #thisExp.timestampOnFlip(win, 'BLANCO_3.stopped')
                BLANCO_3.setAutoDraw(False)
        if BLANCO_3.status == STARTED:  # only update if drawing
            BLANCO_3.setOpacity(frameN%7 >= 3 , log=False)
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in routine_8_57HZComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "routine_8_57HZ" ---
    for thisComponent in routine_8_57HZComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-4.00000)



def freq10():
    
    # --- Prepare to start Routine "routine_10HZ" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    routine_10HZComponents = [BLANCO_4]
    for thisComponent in routine_10HZComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "routine_10HZ" ---
    while continueRoutine and routineTimer.getTime() < 4:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *BLANCO_4* updates
        if BLANCO_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            BLANCO_4.frameNStart = frameN  # exact frame index
            BLANCO_4.tStart = t  # local t and not account for scr refresh
            BLANCO_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(BLANCO_4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            #thisExp.timestampOnFlip(win, 'BLANCO_4.started')
            BLANCO_4.setAutoDraw(True)
        if BLANCO_4.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 4-frameTolerance:
                # keep track of stop time/frame for later
                BLANCO_4.tStop = t  # not accounting for scr refresh
                BLANCO_4.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                #thisExp.timestampOnFlip(win, 'BLANCO_4.stopped')
                BLANCO_4.setAutoDraw(False)
        if BLANCO_4.status == STARTED:  # only update if drawing
            BLANCO_4.setOpacity(frameN%6 >= 3, log=False)
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in routine_10HZComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "routine_10HZ" ---
    for thisComponent in routine_10HZComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-4.00000)


stimuli_list = [freq6_6,freq7_5,freq8_57,freq10]

stimuli_sequence = [baseline]
for j in range(0,20):
  for i in range(0,4):
    stimuli_sequence.append(stimuli_list[i])

  stimuli_sequence.append(baseline)
  random.shuffle(stimuli_list)


for stim in stimuli_sequence:
    stim()

for i in range(len(stimuli_sequence)):
    if stimuli_sequence[i]==freq6_6:
        stimuli_sequence[i]=1
    
    if stimuli_sequence[i]==freq7_5:
        stimuli_sequence[i]=2
    
    if stimuli_sequence[i]==freq8_57:
        stimuli_sequence[i]=3
    
    if stimuli_sequence[i]==freq10:
        stimuli_sequence[i]=4
    
    if stimuli_sequence[i]==baseline:
        stimuli_sequence[i]=5

print(stimuli_sequence)
print(len(stimuli_sequence))


# --- Prepare to start Routine "Final" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
teclaSalida.keys = []
teclaSalida.rt = []
_teclaSalida_allKeys = []
# keep track of which components have finished
FinalComponents = [mensajeSalida, teclaSalida]
for thisComponent in FinalComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Final" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *mensajeSalida* updates
    if mensajeSalida.status == NOT_STARTED and tThisFlip >= 10.0-frameTolerance:
        # keep track of start time/frame for later
        mensajeSalida.frameNStart = frameN  # exact frame index
        mensajeSalida.tStart = t  # local t and not account for scr refresh
        mensajeSalida.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(mensajeSalida, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        #thisExp.timestampOnFlip(win, 'mensajeSalida.started')
        mensajeSalida.setAutoDraw(True)
    if mensajeSalida.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > mensajeSalida.tStartRefresh + 6.0-frameTolerance:
            # keep track of stop time/frame for later
            mensajeSalida.tStop = t  # not accounting for scr refresh
            mensajeSalida.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            #thisExp.timestampOnFlip(win, 'mensajeSalida.stopped')
            mensajeSalida.setAutoDraw(False)
    
    # *teclaSalida* updates
    waitOnFlip = False
    if teclaSalida.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        teclaSalida.frameNStart = frameN  # exact frame index
        teclaSalida.tStart = t  # local t and not account for scr refresh
        teclaSalida.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(teclaSalida, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        #thisExp.timestampOnFlip(win, 'teclaSalida.started')
        teclaSalida.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(teclaSalida.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(teclaSalida.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if teclaSalida.status == STARTED and not waitOnFlip:
        theseKeys = teclaSalida.getKeys(keyList=['y','n','left','right','space'], waitRelease=False)
        _teclaSalida_allKeys.extend(theseKeys)
        if len(_teclaSalida_allKeys):
            teclaSalida.keys = _teclaSalida_allKeys[-1].name  # just the last key pressed
            teclaSalida.rt = _teclaSalida_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in FinalComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Final" ---
for thisComponent in FinalComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)


#thisExp.nextEntry()
# the Routine "Final" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()


# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
#thisExp.abort()  # or data files will save again on exit
win.close()


core.quit()
