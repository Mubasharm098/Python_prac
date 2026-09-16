print('''Twinkle, twinkle, little star,
How I wonder what you are!Up above the world so high,
Like a diamond in the sky.Twinkle,
twinkle, little star,
How I wonder what you are!''')

try:
	import pyttsx3
except ImportError:
	pyttsx3 = None

if pyttsx3 is not None:
	engine = pyttsx3.init()
	engine.say("Hi, I'm your assistant")
	engine.runAndWait()