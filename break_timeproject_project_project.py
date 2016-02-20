import webbrowser
import time

break_count = 0
total_count = 3

print "The program started at " + str( time.ctime( ) )
while break_count < total_count :
	time.sleep( 5 )
	print "The Program has waited till " + str( time.ctime( ) )
	webbrowser.open( "https://www.youtube.com/watch?v=5klXx8cZbsk" )
	break_count = break_count + 1