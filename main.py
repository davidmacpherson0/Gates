import datetime
import threading, time



def timer_start():
	
	
	Running = True
	count = 10

	i = 0 

	Start_Time = time.monotonic() #int(round(time.time() * 100000 ))

	while Running:
		End_Time = time.monotonic()
		time_elasped = End_Time - Start_Time # int(round(time.time() * 100000 )) - Start_Time	
		#print(time_elasped / 100000 , end = '\r')
		print(time_elasped, end = '\r')
		time.sleep(0.01)
		
		

		if (i == 100):
			Running = False 
	
	
		i = i + 1 


	print()	

	print('All Done')
	
	


	
	
	
	
	
start = time.monotonic()
print('start: ',start)
timer_start()

end = time.monotonic()
print('end: ',end)
time_taken =  end - start
print()
print('Time Taken:',time_taken)
print()

