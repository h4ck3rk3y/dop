The project folder contains the cloud server code, android studio project and android apk file.

The apk file provided can be installed in any mobile device.

You can also get the apk file from the folder 
	C:\Users\username\AndroidStudioProjects\projectname\app\build\outputs\apk

Import android project and make your changes.

App contains three activities

MainActivity : It interacts with the cloud server.

MapsActivity : Displaying the map and locations of hospitals with routes.

GPSTracker : To get our location

Note:: Obtain the key for Google Maps. And change it in AndroidManifest.xml
		android:name="com.google.android.geo.API_KEY"
            	android:value="@string/google_maps_key" 

	In function updateplaces() of MapsActivity, change the key tag to your browser key in placesSearchStr string.

