# gpm2spotify
Google Play Music to Spotify Library Exporter

Something I made in a couple of hours to celebrate Spotify's launch in India. The scripts is able to Migrate GPM library to Spotify. Without paying for any money or sharing your credential with shady third party. Just follow the instructions below

All credits to creators of who made the amazing libraries which even made it possible for me to do something like this 

Spotipy [https://spotipy.readthedocs.io/en/latest/]

GMusicApi [https://unofficial-google-music-api.readthedocs.io/en/latest/]


1. 	Download and Install Python from https://www.python.org/downloads/release/python-372/  (x86-64 Installer)

        a. Select Add Python 3.7 to Path Option	
        b. Select Install Now
        c. Close the installer
        d. Open powershell and enter following command
           python -V
           If version is displayed we are good to go.
        e. Update pip
           python -m pip install --upgrade pip
	   
2.  Install Python Libraries required for scripts to work
        
        a. pip install spotipy
        b. pip install gmusicapi

3.	Next we want to register our script as an application on spotify developer account. This will help us use Spotify Web Apis

        a. Goto https://developer.spotify.com/dashboard/
        b. Log In
        c. Accept Developer Terms
        d. Create ClientId
        e. Input a Name and Description for your app (I Used GPM2Spotify)
        f. Select "I don't know" in the What are you building section. This doesn't allow you to use this application commercially which isn't our purpose anyway.
        g. Accept Terms
        h. Edit Setings
        i. Add "http://localhost:8080/" to the Redirect URI
        j. Copy ClientId and ClientSecret to Config.txt
        k. Goto "https://www.spotify.com/in/account/overview/" Copy Username to Config.txt

4.  Copy the script to local Machine. Go to the previous folder
	
        a. Execute "python gpm.py" and follow instructions
    This should create a file GPMLibraryParsed.txt containing Your GPM library with eachline describing [Artist Song Title]
        
        b. Execute "python spotify.py" and follow instructions
    This will import all songs from GPMLibraryParsed.txt, look up each song on Spotify and add the ones it finds to your library. Also it will ask you to provide URL to playlist where it can add all the songs it has added to your library. In my case it looks like this "https://open.spotify.com/playlist/3TXAVQywYUgvhllirL3mqM"
	   
That's it. Sit back and enjoy your library being populated! Yay!
