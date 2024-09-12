import pygame
import mido
from mido import Message
import time



# down = index 1 - c - 48
# down2 = index 1 - c - 60
# left_down = index 8 - c# - 49
# left_down2 = index 8 - c# - 61
# left = index 2 - d - 50
# left2 = index 2 - d - 62
# left_up = index 6 - e - 52
# left_up = index 6 - e - 64
# up = index 0 - f - 53
# up = index 0 - f - 65
# right_up = index 7 - g - 55
# right_up = index 7 - g - 67
# right = index 3 - a - 57
# right = index 3 - a - 69
# right_down = index 5 - b - 59
# right_down = index 5 - b - 71
# select = index 9 - d# - 63
# back = index none - f# - 66
notes1 = { 0:53, 1:48, 2:50, 3:57, 4:0, 5:59, 6:52, 7:55, 8:49, 9:100}
notes2 = { 0:65, 1:60, 2:62, 3:69, 4:0, 5:71, 6:64, 7:67, 8:61, 9:100 }

# Initialize Pygame and Joystick
pygame.init()
pygame.joystick.init()

# Create a joystick object
joystick1 = pygame.joystick.Joystick(0)
joystick1.init()

# Create a second joystick object
joystick2 = pygame.joystick.Joystick(1)
joystick2.init()

# Initialize MIDI 1
port_name1 = 'Pad1 1' 
outport1 = mido.open_output(port_name1)

# Initialize MIDI 2
port_name2 = 'Pad2 2' 
outport2 = mido.open_output(port_name2)

# Define MIDI note values
velocity = 64  # Velocity of the note

def send_midi_message(outport, message_type, note, velocity1):
    """Send MIDI message."""
    try:
        message = Message(message_type, note=note, velocity=velocity)
        outport.send(message)
        print(f"Sent MIDI message: {message}")
    except Exception as e:
        print(f"Error sending MIDI message: {e}")

# Main loop
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.JOYBUTTONDOWN:
            if event.joy == 0:  # Joystick 1
                if event.button == 4: velocity = 0
                else: velocity = 64
                send_midi_message(outport1, 'note_on', notes1[event.button], velocity)
                print(event.button)
            elif event.joy == 1:  # Joystick 2
                if event.button == 4: velocity = 0
                else: velocity = 64
                send_midi_message(outport2, 'note_on', notes2[event.button], velocity)
        elif event.type == pygame.JOYBUTTONUP:
            if event.joy == 0:  # Joystick 1
                send_midi_message(outport1, 'note_off', notes1[event.button], 0)  # Note-off message with zero velocity
            elif event.joy == 1:  # Joystick 2
                send_midi_message(outport2, 'note_off', notes2[event.button], 0)  # Note-off message with zero velocity

pygame.quit()

