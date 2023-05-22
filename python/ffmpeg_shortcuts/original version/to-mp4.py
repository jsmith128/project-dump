#!/usr/bin/python
import ffmpy
input = input("Full name of file(.extension): ")

ff = ffmpy.FFmpeg(
	inputs={input: None},
	outputs={"output.mp4": None}
)
ff.run()