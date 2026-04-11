!define PROJECT_NAME "StaffCAD"
!define PROJECT_VERSION "1.0.0"
!define GITHUB_ZIP_URL "https://github.com/CodeBullet23/StaffCAD/archive/refs/heads/main.zip"
!define INSTALL_EXE_NAME "${PROJECT_NAME}_Setup_${PROJECT_VERSION}.exe"

!include "MUI2.nsh"

!define MUI_ICON "${NSISDIR}\Contrib\Graphics\Icons\modern-install.ico"
!define MUI_UNICON "${NSISDIR}\Contrib\Graphics\Icons\modern-uninstall.ico"
!define MUI_HEADERIMAGE
!define MUI_HEADERIMAGE_RIGHT
!define MUI_HEADERIMAGE_BITMAP "${NSISDIR}\Contrib\Graphics\Header\win.bmp"
!define MUI_ABORTWARNING

!define MUI_FINISHPAGE_RUN
!define MUI_FINISHPAGE_RUN_TEXT "Launch StaffCAD now"
!define MUI_FINISHPAGE_RUN_FUNCTION "LaunchStaffCAD"

OutFile "${INSTALL_EXE_NAME}"
InstallDir "$PROGRAMFILES\${PROJECT_NAME}"
RequestExecutionLevel admin

Var StartMenuFolder

!insertmacro MUI_PAGE_WELCOME
!insertmacro MUI_PAGE_DIRECTORY
!insertmacro MUI_PAGE_INSTFILES
!insertmacro MUI_PAGE_FINISH

!insertmacro MUI_UNPAGE_CONFIRM
!insertmacro MUI_UNPAGE_INSTFILES

!insertmacro MUI_LANGUAGE "English"

Section "Install"
  SetOutPath "$INSTDIR"
  StrCpy $StartMenuFolder "${PROJECT_NAME}"

  DetailPrint "Downloading StaffCAD..."
  ExecWait 'powershell -Command "Invoke-WebRequest -Uri \"${GITHUB_ZIP_URL}\" -OutFile \"$INSTDIR\repo.zip\""'

  DetailPrint "Extracting..."
  ExecWait 'powershell -Command "Expand-Archive -Path \"$INSTDIR\repo.zip\" -DestinationPath \"$INSTDIR\repo\" -Force"'

  DetailPrint "Organizing files..."
  FindFirst $0 $1 "$INSTDIR\repo\*.*"
  loop:
    StrCmp $1 "" done
    IfFileExists "$INSTDIR\repo\$1\*.*" 0 +3
      CopyFiles /SILENT "$INSTDIR\repo\$1\*.*" "$INSTDIR"
      Goto next
    CopyFiles /SILENT "$INSTDIR\repo\$1" "$INSTDIR"
  next:
    FindNext $0 $1
    Goto loop
  done:
  FindClose $0

  RMDir /r "$INSTDIR\repo"
  Delete "$INSTDIR\repo.zip"

  DetailPrint "Creating smart launcher..."
  FileOpen $0 "$INSTDIR\run_app.bat" w
  FileWrite $0 '@echo off$\r$\n'
  FileWrite $0 'cd /d "%~dp0"$\r$\n'
  FileWrite $0 'echo Checking Python...$\r$\n'
  FileWrite $0 'python --version >nul 2>&1$\r$\n'
  FileWrite $0 'if errorlevel 1 (echo Python not installed. Install Python 3.10+ and try again.& pause & exit /b)$\r$\n'
  FileWrite $0 'echo Checking virtual environment...$\r$\n'
  FileWrite $0 'if not exist ".venv" (echo Creating venv... & python -m venv .venv)$\r$\n'
  FileWrite $0 'echo Checking Flask...$\r$\n'
  FileWrite $0 '"%~dp0\.venv\Scripts\python.exe" -c "import flask" >nul 2>&1$\r$\n'
  FileWrite $0 'if errorlevel 1 (echo Installing Flask... & "%~dp0\.venv\Scripts\python.exe" -m pip install --upgrade pip & "%~dp0\.venv\Scripts\python.exe" -m pip install flask flask_sqlalchemy flask_login)$\r$\n'
  FileWrite $0 'echo Starting StaffCAD...$\r$\n'
  FileWrite $0 '"%~dp0\.venv\Scripts\python.exe" "%~dp0\app.py"$\r$\n'
  FileWrite $0 'echo.$\r$\n'
  FileWrite $0 'echo Server stopped. Press any key to close...$\r$\n'
  FileWrite $0 'pause >nul$\r$\n'
  FileClose $0

  CreateDirectory "$SMPROGRAMS\$StartMenuFolder"
  CreateShortCut "$SMPROGRAMS\$StartMenuFolder\${PROJECT_NAME}.lnk" "$INSTDIR\run_app.bat"
  CreateShortCut "$DESKTOP\${PROJECT_NAME}.lnk" "$INSTDIR\run_app.bat"

  WriteUninstaller "$INSTDIR\Uninstall.exe"
SectionEnd

Section "Uninstall"
  Delete "$DESKTOP\${PROJECT_NAME}.lnk"
  RMDir /r "$SMPROGRAMS\$StartMenuFolder"
  RMDir /r "$INSTDIR"
SectionEnd

Function LaunchStaffCAD
  Exec '"$INSTDIR\run_app.bat"'
  ExecShell "open" "http://127.0.0.1:5000/login"
FunctionEnd
