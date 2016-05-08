####################################################################
##
## This is a list of known issues and future implmentation items 
##
####################################################################

#################################################################
## Needed Features

1) History Database
This will enable the learning feature to truly view past data 
and make informed future decisions

2) Improved UI
Currently the UI is bland and unusable on small screens. Make it
more clearly represent the information through color/font changes.

3) SMART Mode
Recognise our phones connecting to WiFi and change tempurature 
preferences accordingly

6) LEARNING Mode
Research machine learning algorithms to determine what might be
benificial. This would include a database setup to record past
data and analysis

5) Outdoor Tempurature Check
This can start as a ping to weather.com or some service for my 
zip code but ideally I could ping an outdoor tempurature sensor
at some point

#################################################################
## Future Improvments

1) More Responsive Thread Control Class
This would make controlling the recurring threads easier and more 
elegant. This could still be an area of improvement but now after cancel()
is called the function will not run but the timer will still stall closing the
program. 

##############################################################
## Know Issues

1) Upon exit a thread does not exit. This forces a Ctrl-c to exit fully.
This is not a huge issue as one shouldn't be opening and closing this program
at a regular interval but it could be an issue with lack on control over
seperate thread and timing in future items.

