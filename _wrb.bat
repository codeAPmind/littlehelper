IF DEFINED c (ECHO %c%) ELSE (set c=c:\3)
ECHO %c%
set p=%c%\python.exe
set d=%cd%
rd /s /q %d%\dist\
cd /D %c%
%p% -m pip install -U pip nuitka  wmi imageio simpleaudio  pillow   airtest pywinauto pynput pywin32
@REM %p% -m pip install -U pip nuitka  wmi    airtest pywinauto pynput
@REM %p% -m nuitka --onefile --disable-console --windows-icon-from-ico=%d%\0up.png --include-data-files=%d%\*.png=.\ --include-data-files=%d%\*.wav=.\ --include-data-dir=%d%\AutoTest=.\AutoTest\ --enable-plugin=tk-inter %d%\UnityHelper.py  --include-data-files=%d%\AutoTest\*.png=.\AutoTest\
%p% -m nuitka --onefile --windows-icon-from-ico=%d%\0up.png --include-data-files=%d%\*.png=.\ --include-data-files=%d%\*.wav=.\ --include-data-dir=%d%\AutoTest=.\AutoTest\ --enable-plugin=tk-inter --include-module=tkinter --include-module=airtest --include-module=comtypes.stream --include-module=pywinauto  %d%\UnityHelper.py
xcopy /f/y %c%\UnityHelper.dist\UnityHelper.exe %d%\dist\
cd /D %d%
robocopy . dist\ /xf .gitignore *.py *.md *.bat /xd .git .vscode __pycache__ examples
pause