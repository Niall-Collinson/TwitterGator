import tkinter as tk
from PIL import ImageTk, Image
import requests
from generate import generate
from generate import graph_generator


def gui():
	"""
	GUI function, runs from TKInter library

	:return:
	"""

	def call_generate():
		"""
		Gets data sample

		:return:
		"""
		vocab, bow_shape = generate(size.get(), entry.get(), time_choices.get())

		info_label['text'] = bow_shape

	def generate_graph():
		"""
		Calls event detection and returns graph

		:return:
		"""
		terms = graph_generator(k_number.get(), scale_widget.get(), algo)
		label_receiver['text'] = terms

	def call_help():
		"""
		Returns help window

		:return:
		"""
		from PIL import ImageTk, Image
		window = tk.Tk()

		window.title("Help")

		canvas1 = tk.Canvas(window, height=800, width=800)
		canvas1.configure(bg='blue')
		canvas1.pack()

		lbl = tk.Label(canvas1, font=40,  text="HELPFUL INFORMATION")
		lbl.place(relx=0.4, rely=0.1)

		lbl = tk.Label(canvas1, font=8,text="Step 1: Get sample of data from Twitter\n\n"
									"Enter phrase: Will return results containing any of the words\n"
									"Sample size: Maximum number of tweets to return\n"
									"Time period: Period of time the sample is taken from\n\n"
									"Bag of Words shape:\n Shows the shape of the sample data, "
									"the first number being the number of words\n "
									"and the second being the features of these words.\n"
									"A sample where the number of words is greater "
									"than the featues indicates low value. \n"
									"Vice versa indicates a large aount of high value terms\n\n\n"
									"Step 2: Find events in the sample data\n\n"
									"Vertices: Number of words in graph\n"
									"Word frequency: Minimum number of words must appear in sample,"
									"a low word frequency will allow lower value words through\n\n"
									"Algorithm Method: Choose which method to run\n"
									"BFS: Returns heaviest set of connected K-subgraphs\n"
									"DFS: Returns the heaviest subgraph\n"
									"HYBRID: A mix between these two methods\n\n"
									"For further help or if you have any bugs to report \n"
									"email: help@twittergator.com")
		lbl.place(relx=0.025, rely=0.25)
		#lbl.configure(bg='blue')
		window.mainloop()


	"""
	The code below is the TKInter framework
	"""


	#Sets out window frame and sets size and height
	HEIGHT = 700
	WIDTH = 800

	root = tk.Tk()

	#Creates canvas
	canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
	canvas.pack()

	#Path to background image
	path1 = "jungle.png"

	#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
	img2 = ImageTk.PhotoImage(Image.open(path1))

	#The Label widget is a standard Tkinter widget used to display a text or image on the screen.
	panel = tk.Label(root, image=img2)

	#The Pack geometry manager packs widgets in rows or columns.
	panel.place(relwidth=1, relheight=1)

	#Help button
	button = tk.Button(root, text="HELP", font=40, command=lambda: call_help())
	button.place(relx=0.945, rely=0.01, relheight=0.05, relwidth=0.05)

	#Header frame
	header_frame = tk.Frame(root, bg='#80c1ff', bd=1)
	header_frame.place(relx=0.5, rely=0, relwidth=0.125, relheight=0.2, anchor='n')

	#Icon image
	path = "gator.png"
	img = Image.open(path)
	img = img.resize((100, 75), Image.ANTIALIAS)

	#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
	img = ImageTk.PhotoImage(img)

	#The Label widget is a standard Tkinter widget used to display a text or image on the screen.
	panel = tk.Label(header_frame, image = img)

	#The Pack geometry manager packs widgets in rows or columns.
	panel.place(rely=-0.25, relwidth=1, relheight=1)

	#Upper frame
	upper_frame = tk.Frame(root, bg='#80c1ff', bd=5)
	upper_frame.place(relx=0.5, rely=0.1, relwidth=0.8, relheight=0.1, anchor='n')

	#Header title
	label = tk.Label(upper_frame, text="TWITTER GATOR")
	label.config(font=("Courier", 20))
	label.place(relwidth=1, relheight=1)

	#Main frame
	frame = tk.Frame(root, bg='#80c1ff', bd=5)
	frame.place(relx=0.5, rely=0.25, relwidth=0.8, relheight=0.65, anchor='n')

	#Step one framework
	label = tk.Label(frame, bg='#80c1ff', text="STEP 1:")
	label.place(rely=-0.025, relx=0.45, relheight=0.1)

	label = tk.Label(frame, text="ENTER PHRASE TO QUERY:")
	label.place(rely=0.05, relwidth=0.4, relheight=0.1)

	entry = tk.Entry(frame, font=40)
	entry.place(rely=0.15, relwidth=0.4, relheight=0.1)

	#Sample size
	label = tk.Label(frame, bg='#80c1ff', text="Sample size:")
	label.config(font=("Courier", 12))
	label.place(relx=0.425, rely=0.075)

	choices = ['500', '1000', '5000', '10000']
	size = tk.StringVar(root)
	size.set('10000')
	selector = tk.OptionMenu(frame, size, *choices)
	selector.place(relx=0.425, rely=0.125,  relheight=0.1, relwidth=0.15)

	#Time period
	label = tk.Label(frame, bg='#80c1ff', text="Time period:")
	label.config(font=("Courier", 12))
	label.place(relx=0.6, rely=0.075 )

	time_choices = "All time"
	time_request = ['Last 15 minutes', 'Last 30 minutes', 'Last 6 hours', 'Last day', 'Last week', 'Last month',
					'Last year']
	time_choices = tk.StringVar(root)
	time_choices.set('Last year')
	selector = tk.OptionMenu(frame, time_choices, *time_request)
	selector.place(relx=0.6, rely=0.125, relheight=0.1, relwidth=0.15)

	#Generate sample data
	button = tk.Button(frame, text="SEND\nQUERY", font=40, command=lambda: call_generate())
	button.place(rely=0.05, relx=0.8, relheight=0.2, relwidth=0.2)

	#Main box which displays results
	label_receiver = tk.Label(frame)
	label_receiver.config(font=("Courier", 15))
	label_receiver.place(rely=0.27, relwidth=1, relheight=0.5)

	#Lower frame
	lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
	lower_frame.place(relx=0.5, rely=0.75, relwidth=0.8, relheight=0.2, anchor='n')

	#Step 2 framework
	label = tk.Label(lower_frame, bg='#80c1ff', text="STEP 2:")
	label.place(relx=0.375, rely=-0.1, relwidth=0.25, relheight=0.2)

	label = tk.Label(lower_frame, bg='#80c1ff', text="Bag of Words shape:")
	label.config(font=("Courier", 12))
	label.place(relx=-0.025, rely=-0.1, relwidth=0.25, relheight=0.2)

	info_label = tk.Label(lower_frame)
	info_label.config(font=("Courier", 15))
	info_label.place(rely=0.05, relwidth=0.15, relheight=1)

	#Generate graph
	button = tk.Button(lower_frame, text="GENERATE\nGRAPH", font=40, command=lambda: generate_graph())
	button.place(relx=0.825, relheight=1, relwidth=0.175)

	#Vertices selector
	label = tk.Label(lower_frame, bg='#80c1ff', text="Vertices:")
	label.config(font=("Courier", 12))
	label.place(relx=0.15, rely=0.1, relwidth=0.2, relheight=0.2)

	choices = ['1', '2', '3']
	k_number = tk.StringVar(root)
	k_number.set('1')
	selector = tk.OptionMenu(lower_frame, k_number, *choices)
	selector.place(relx=0.2, rely=0.4, relheight=0.4, relwidth=0.1)

	#Word frequency
	label = tk.Label(lower_frame, bg='#80c1ff', text="Word frequency")
	label.config(font=("Courier", 12))
	label.place(relx=0.325, rely=0.05, relwidth=0.2, relheight=0.3)

	scale_widget = tk.Scale(lower_frame, from_=1, to=10,
								 orient=tk.HORIZONTAL)
	scale_widget.set(3)
	scale_widget.place(relx=0.325, rely=0.35, relwidth=0.2, relheight=0.5)

	#Algorithm method
	label = tk.Label(lower_frame, text="ALGORITHM METHOD")
	label.config(font=("Courier", 12))
	label.place(relx=0.55, rely=0.1, relwidth=0.25, relheight=0.25)

	algo = 'DFS'

	r1 = tk.Radiobutton(lower_frame, text="DFS", variable=algo, value='DFS')
	r1.place(relx=0.55, rely=0.3, relwidth=0.25, relheight=0.25)

	r2 = tk.Radiobutton(lower_frame, text="BFS", variable=algo, value='BFS')
	r2.place(relx=0.55, rely=0.55, relwidth=0.25, relheight=0.25)

	r3 = tk.Radiobutton(lower_frame, text="HYBRID", variable=algo, value='HYBRID')
	r3.place(relx=0.55, rely=0.8, relwidth=0.25, relheight=0.25)

	root.wm_title("Twitter Gator")
	root.mainloop()
