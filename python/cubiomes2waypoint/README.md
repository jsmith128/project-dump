## Cubiomes to Waypoint
### 2/20/2023

Takes the structure export output from cubiomes viewer analysis
and turns it into a waypoint file for xaeros mini/worldmap.

To use, first [download cubiomes-viewer](https://github.com/Cubitect/cubiomes-viewer/releases), then launch and enter a seed. Go to the `Structures` tab and click `Analyze`. Then you'll get a list of structure locations, which I believe are _only_ the ones visible in the viewport. Now click `Export...` and save it somewhere useful. 

Now that you have the structure list, go into the `cubiomes2wp.py` file and change the `infile` and `outfile` variables so that `infile` is directed towards the structure file you just saved, and outfile can be whatever you want. 

You can then configure the `colors` dictionary to specify what colors each waypoint should be, and then `disabled_structs` to disable a structure; meaning that it will not be in the resulting waypoint file. This can be useful for disabling mineshafts (which are off by default) because they will quickly clutter your waypoints menu and HUD.

Now everything is setup, the program should be ready to run. If the output file has text in it and nothing looks broken, then perfect! Now you can save this file as `.minecraft\XaeroWaypoints\--mapname--\dim%0\mw$default_1.txt`, or whatever you think will work. At the time of writing I see there is a map folder with a `dim%0\waypoints.txt`, so maybe that works too! 

Backup and experiment.