# Python
## Exercise 1.1
Task Requirements:
  - Install Python 3.8.7 
  - Set up a new virtual environment
  - Install Visual Studio Code
  - Set up an IPython shell
  - Export a requirements file
  - Create a Github repo for this course

Task Directions: 
  - Install Python 3.8.7 on your system.  Verify you’re able to access the correct Python installation from your terminal and check that it’s running the correct version by using the python --version command.
  - Set up a new virtual environment with command "mkvirtualenv" and name it “cf-python-base”.
  - Install Visual Studio Code and make a script called “add.py” that adds two numbers that the user enters. Input from a user can be stored into a variable with the following syntax (don’t include < and > in your code): variable_name = int(input("<any prompt you'd like to give to the user>")).
Store two values a and b from the user and add them to a variable c.
Finally, print the value of c to the screen. The print() function can be used to print variable values with the following syntax: print(<variable name>).
  - Set up an IPython shell in the virtual environment “cf-python-base”. The name of the package to be installed is “ipython,” via command "pip install ipython".  Verify your installation by launching an IPython shell with the command ipython.
  - Export a requirements file. 
First, generate a “requirements.txt” file from your source environment. To do this, you use the pip freeze command and all packages (including version numbers) installed in the currently activated environment will be compiled: > pip freeze > requirements.txt.
Next, create a new environment called “cf-python-copy”. In this new environment, install packages from the “requirements.txt” file that you generated earlier. To install the packages from this file in any other environment, you run the pip install command with the extra -r argument, followed by the name of your requirements file: > pip install -r requirements.txt.
  - Create a Github repo for this course. In this Github repo, you’ll make separate folders for each Exercise. You’ll upload any deliverables from an Exercise to its designated folder, so, for example, you’ll add the deliverables specified in the final step here to a folder named “Exercise 1.1.” This way, you can keep all your work properly arranged. Keep your mentor informed about this arrangement.
