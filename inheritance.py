class Parent( ) :
	def __init__( self, last_name, eye_color ) :
		print "Parent constructor called"
		self.last_name = last_name
		self.eye_color = eye_color

	def show_info( self ) :
		print "Last Name: " + str( self.last_name ) + "Eye Color: " + str( self.eye_color )
parent = Parent( "Baranwal", "black" )

class Child( Parent ) :
	def __init__( self, last_name, eye_color, number_of_toys ) :
		print "Child constructor called"
		Parent.__init__( self, last_name, eye_color )
		self.number_of_toys = number_of_toys

	def show_info( self ) :
		print "Last Name: " + str( self.last_name ) + " Eye Color: " + str( self.eye_color ) + " Number of Toys: " + str( self.number_of_toys )
child = Child( "Baranwal", "black", 10 )
child.show_info( )
