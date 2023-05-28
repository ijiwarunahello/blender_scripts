@echo off
set BLENDER_PATH="C:\Program Files\Blender Foundation\Blender 3.3\blender.exe"
set PYTHON_SCRIPT=%1

shift
set ARGS=
@REM 第1引数以降を処理
:loop
if "%1"=="" goto end
set ARGS=%ARGS% %1
shift
goto loop
:end

%BLENDER_PATH% --background --python %PYTHON_SCRIPT% -- %ARGS%
