import pyttsx3;
import time
engine = pyttsx3.init();
engine.setProperty('voice', 'english+f2')

ex_n=int(input("Enter numbr of exercises:"))
rep_n=int(input("Enter number of repetitions in tha exercise:"))

Exercise=[i for i in range(1,ex_n+1)]

Reps=[i for i in range(1,rep_n+1)]

for E in Exercise:
	for R in Reps:

		message="Exercise no ",str(E),"Rep number",str(R)
		message = ''.join(message)
		print(message) 
		
		for i in range(1,11):
			print(i)
			engine.say(str(i));
			engine.runAndWait() ;
			#Time between 1-2, 2-3, etc.
			time.sleep(0.2)


		#time between two repetitions
		time.sleep(2)

	#time between two exercises
	time.sleep(10)







