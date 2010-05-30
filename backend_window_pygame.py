"""
Myrmidon
Copyright (c) 2010 Fiona Burrows
 
Permission is hereby granted, free of charge, to any person
obtaining a copy of this software and associated documentation
files (the "Software"), to deal in the Software without
restriction, including without limitation the rights to use,
copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following
conditions:
 
The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.
 
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.
 
---------------------

- BACKEND FILE -
- WINDOW       -

A pygame-based window creation and handling backend.

"""

import os, pygame
from myrmidon import MyrmidonGame

class MyrmidonWindowPygame(object):
	def __init__(self):
		os.environ['SDL_VIDEO_CENTERED'] = '1'
		pygame.init()

		pygame.display.gl_set_attribute(pygame.locals.GL_MULTISAMPLEBUFFERS,1)

		if MyrmidonGame.full_screen:
			pygame.display.set_mode(MyrmidonGame.screen_resolution, pygame.OPENGL | pygame.DOUBLEBUF | pygame.FULLSCREEN | pygame.HWSURFACE)
		else:
			pygame.display.set_mode(MyrmidonGame.screen_resolution, pygame.OPENGL | pygame.DOUBLEBUF)

	def Clock(self):
		return pygame.time.Clock()

	def change_resolution(self, resolution):
		pygame.display.quit()
		"""
		pygame.display.init()
		if MyrmidonGame.full_screen:
			pygame.display.set_mode(resolution, pygame.OPENGL | pygame.DOUBLEBUF | pygame.FULLSCREEN | pygame.HWSURFACE)
		else:
			pygame.display.set_mode(resolution, pygame.OPENGL | pygame.DOUBLEBUF)
		"""
		self.__init__()


	# TEXT HANDLING
	@classmethod	
	def load_font(cls, filename = None, size = 20):
		return pygame.font.Font(filename, size)
	 
