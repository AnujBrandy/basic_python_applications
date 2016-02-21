import urllib

def read_text( ) :
	file_handle = open( r"twilio_sending_text.py" )
	contents = file_handle.read( )
	print contents
	profanity_check( contents )

def profanity_check( text_to_check ) :
	connection_handle = urllib.urlopen( "http://www.wdyl.com/profanity?q=" + text_to_check )
	output = connection_handle.read( )
	print output

read_text( )