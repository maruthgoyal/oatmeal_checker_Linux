This is a fan-made program that checks for a new Oatmeal comic every 30 minutes.
It will create a desktop notification to notify you if it finds a new comic.

To use:

Clone this repository to your location of choice
• To clone to the desktop: 
Open Terminal 
cd Desktop 
git clone https://github.com/maruthgoyal/oatmeal_checker.git 

Run the install.sh script 
• Open Terminal 
• cd /wherever/you/have/cloned/the/project 
• source install.sh 
• Enter your password when prompted to do so 
• Wait for the installation to finish 
• Close the terminal 

Run the run.sh script to run the program 
• Open Terminal 
• cd /wherever/you/have/cloned/the/project 
• screen -S oatmeal_screen 
• source run.sh 
• Press ctrl + a 
• Press d 
• Close the terminal 

To terminate the program (if you want to) 
• Open Terminal 
• screen -X -S oatmeal_screen kill 
• Close the terminal 

And that's it! Enjoy your Oatmeal! 

NOTE: If your computer ever shuts down or you terminate the program, just execute the run.sh script again as specified above. 
No need to run install.sh again though.
