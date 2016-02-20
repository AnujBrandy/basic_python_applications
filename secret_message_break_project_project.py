import os

file_names = os.listdir( r"/home/anuj/Desktop/python_projects/break_time" )

for file_name in file_names :
	if file_name.endswith( ".py" ) :
		os.rename( file_name , file_name[ : -3 ]  + "_project" + ".py" )


