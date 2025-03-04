# # ---------CHAPTER 13 – ADVANCED PYTHON 2--------

# # VIRTUAL ENVIRIONMENT
# # An environment which is same as the system interpreter but is isolated from 
# # the other Python environments on the system.

# # --------INSTALLATION--------

# # To use virtual environments, we write:
# # pip install virtualenv # Install the package
# # We create a new environment using:
# # virtualenv myprojectenv # Creates a new venv
# # The next step after creating the virtual environment is to activate it.
# # We can now use this virtual environment as a separate Python installation.

#        ---------PIP FREEZE COMMAND -----------
# ‘pip freeze’ returns all the package installed in a given python 
# environment along with  the versions.
# pip freeze > requirements .txt

# The above command creates a file named ‘requirements.txt’ 
# in the same directory containing the output of ‘pip freeze’.

# We can distribute this file to other users, and they can
#  recreate the same environment  using:
# pip install –r requirements.txt