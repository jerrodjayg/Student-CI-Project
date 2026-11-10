@echo off
setlocal

echo === CI Build Started ===
echo Checking Python installation...
python --version
if errorlevel 1 exit /b 1

echo Checking source files...
dir

echo === Running Application Tests ===
python -m unittest discover -s tests -v
if errorlevel 1 (
    echo TESTS FAILED
    exit /b 1
)

echo === Running Application ===
python app.py
if errorlevel 1 exit /b 1

echo === CI Build Completed Successfully ===
exit /b 0
