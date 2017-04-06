import sublime
import sublime_plugin
import os
import os.path
import platform
import subprocess

PLUGIN_DIR = os.getcwd() if int(sublime.version()) < 3000 else os.path.dirname(__file__)
SUBL_ASYNC = callable(getattr(sublime, 'set_timeout_async', None))
USE_SHELL  = sublime.platform() == 'windows'
DIV        = '\\' if sublime.platform() == 'windows' else '/'
POPEN_ENV  = ({'PATH': ':'.join(['/usr/local/bin', os.environ['PATH']])}) if sublime.platform() == 'osx' and os.path.isdir('/usr/local/bin') else None


class LessBuilderFileClass():
	def datasFile(self, dados):
		settings          = sublime.load_settings('LessBuilder.sublime-settings')
		inputfile         = dados.file_name()
		fileName          = os.path.basename(inputfile)

		retorno           = DataFile()
		retorno.settings  = settings
		retorno.folder    = os.path.dirname(inputfile)
		retorno.extension = fileName.split(".")[-1]
		retorno.file      = fileName.replace('.'+retorno.extension, '')

		return retorno

	def buildLess(self, minify, prefix, folder, file):
		less      = folder+DIV+file+'.less'
		css       = folder+DIV+file+prefix+'.css'
		strMinify = '--clean-css ' if minify else ''

		cmd       = 'lessc '+strMinify+less+' '+css
		p         = subprocess.Popen(cmd, stderr=subprocess.PIPE, shell=USE_SHELL, env=POPEN_ENV)

		print('LESS: '+less)
		print('CSS: '+css)

class DataFile(object):
  settings  = ""
  folder    = ""
  file      = ""
  extension = ""

# Commando Base
class LessBuilderCommand(sublime_plugin.TextCommand, LessBuilderFileClass):
	def run(self, view=None):
		view     = self.view
		fileData = self.datasFile(view)
		minify   = fileData.settings.get('minify')
		prefix   = fileData.settings.get('prefixMinify') if minify else ''

		if(fileData.extension=='less'):
			self.buildLess(minify, prefix, fileData.folder, fileData.file)

class EventDump(sublime_plugin.EventListener, LessBuilderFileClass):
	def on_post_save(self, edit):
		fileData = self.datasFile(edit)
		minify   = fileData.settings.get('minify')
		prefix   = fileData.settings.get('prefixMinify') if minify else ''

		if fileData.settings.get('onSave') and fileData.extension=='less':
			self.buildLess(minify, prefix, fileData.folder, fileData.file)
		elif fileData.settings.get('onSave')==False and fileData.extension=='less':
			print('Não permitido transforma ao salvar')