# microcontroller_aggregated_stuff

Hosting some microcontroller related stuff

# Setup of Jukebox

Assuming you have a recent Python installed:

```
python -m venv venv
venv/Scripts/activate
pip install -r requirements.txt
pdm update
pdm run thonny
```

* This should open the Thonny IDE.
* Now connect to your prepared RaspberryPi Pico Controller as usual
* Open the file in jukebox/jukebox.py
* When starting it from inside Thonny the onboard LED of your Pico should start flashing with 20Hz
* If a passive buzzer is connected as described in jukebox/jukebox.py you should here a scale played
* See jukebox/main.py on usage and how to play the included songs
    * Song files need to be transferred to your Pico, too, such that these can be imported.
* Starting jukebox/main.py obviously starts playing the song files
* Enjoy...
