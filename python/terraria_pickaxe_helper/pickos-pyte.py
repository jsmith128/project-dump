from __future__ import unicode_literals
import pyte as p
import pickCon as pc

screen = p.Screen(80,24)
stream = p.Stream(screen)
stream.feed("Hello World!")
screen.display