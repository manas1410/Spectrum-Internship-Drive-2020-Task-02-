import cx_Freeze
import json
executables=[cx_Freeze.Executable(
	"D:/college/Internship(Spectrum)/3/welcome.py",
	base="Win32GUI",
	icon='D:/college/Internship(Spectrum)/3/logo/spectrumlogo.ico')]
cx_Freeze.setup(
	name='Students Mark Entry',
	options={"build_exe":{"packages":['tkinter','webbrowser','sqlite3','PIL','os'],"include_files":['D:/college/Internship(Spectrum)/3/mark_list.db','D:/college/Internship(Spectrum)/3/user_pas.db','D:/college/Internship(Spectrum)/3/logo/spectrumlogo.ico']}},
	executables=executables)
