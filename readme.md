# Update - Please note:
**My rewrite is now oficially merged with the [original Versions](https://github.com/unibonn/physics-labclasses-fits) of University Bonn.**  
So this project is no longer supported. I'll leave it here for documentation reasons.  
Please visit my [fork](https://github.com/ceron21/physics-labclasses-fits) or the [original](https://github.com/unibonn/physics-labclasses-fits) for the latest version.   

## This is a better version of the scripts `chiFit.py` and `chi2FitXYErr.py` used in physics at university bonn.

### Notes for `chi2Fit.py`  
The script is more modular and usable than before.  
I included the old version in the history of my commits for better comparison.  
The feature is that all settings are bundled at the top of the code, so that everybody can understand what is to set and where. 

The input way data is put in has also changed. There is now a file input from the terminal instead of entering all values in the script itself.  

Both scripts are compaltible according to input-file structure.     

Please note that I did take a pervious version of one script and combined it with code from an other script as a startingpoint.  
But there are also many changes and additions in the code written by myself.  

The intention of that project is to make the script more accessible especially for the prospective physics teachers who have to use the script too without hearing the EDV Modulue which prepares the physics students for using such scripts.  

**Please don't forget to read and understand the code eventhough it isnt't needed anymore (because I did that work for you).  
You can't trust me or any other code you can find on the internet if you don't understand whats happening!**

The original Versions are publicly avaibale on the website of [university-bonn](https://www.praktika.physik.uni-bonn.de/module/physik261).  
`chi2Fit.py` is from an unknown user, i did also copy code from [Thomas Erben](https://github.com/terben)  
`chi2FitXYErr.py` was written by [Thomas Erben](https://github.com/terben) and modified by me.  

### Notes for `chi2FitXYErr.py`
I din't add any functions, I just modified the settings for labeling so that it is more accessible for everybody.  
My Version is also out of the box compatible with the other scripts needed file-structure.  

## How to use:
Just enter `python3 chi2Fit,py -h` / `python3 chi2FitXYErr.py -h` in the terminal, this should explain everything. If you don't understand how it's used you shouldn't use it without proper knowlede!


