from gpiozero import Motor, OutputDevice
from time import sleep

motor1 = Motor(27, 24)
motor1_enable = OutputDevice(5, initial_value=1)
motor2 = Motor(6, 22)
motor2_enable = OutputDevice(17, initial_value=1)
motor3 = Motor(23, 16)
motor3_enable = OutputDevice(12, initial_value=1)
motor4 = Motor(13, 18)
motor4_enable = OutputDevice(25, initial_value=1) 

my_speed = 1

while (1):

	motor1.value = my_speed #  speed forwards
	motor2.value = my_speed #  speed forwards
	motor3.value = -my_speed #  speed backwards
	motor4.value = -my_speed #  speed backwards
	
	
	# Leave the motor on for 3 seconds
	sleep(0.2)
	
	motor1.stop() # stop the motor
	motor2.stop() # stop the motor
	motor3.stop() # stop the motor
	motor4.stop() # stop the motor
	
	# Leave the motor off for 2 seconds
	sleep(2)
	
	motor1.value = -my_speed #  speed backwards
	motor2.value = -my_speed #  speed backwards
	motor3.value = my_speed #  speed forwards
	motor4.value = my_speed #  speed forwards
	
	
	sleep(0.2)
	
	motor1.stop() # stop the motor
	motor2.stop() # stop the motor
	motor3.stop() # stop the motor
	motor4.stop() # stop the motor
	
	# Leave the motor off for 2 seconds
	sleep(2)




#motor1.forward() # full speed forwards

#motor.backward() # full speed backwards
#motor.backward(0.5) # half speed backwards

#motor.stop() # stop the motor

#motor.value = 0.5 # half speed forwards
#motor.value = -0.5 # half speed backwards
#motor.value = 0 # stop

#motor.reverse() # reverse direction at same speed, e.g...

#motor.forward(0.5) # going forward at half speed
#motor.reverse() # now going backwards at half speed 
