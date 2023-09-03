@echo off
cls

rem  ****************************************************************************
rem  * Name:    GitInit                                                         *
rem  * Desc:    Initialize Local GIT Repository.                                *
rem  *                                                                          *
rem  * This script file will initialize a new Local GIT Repository.  It will    *
rem  * also add all source files in this folder to the newly created repository.*
rem  *                                                                          *
rem  ****************************************************************************


:Confirm
echo This script file will initialize a new Local GIT Repository.  It will 
echo also add all source files in this folder to the newly created repository. 
echo.
echo *** IMPORTANT ***
echo This script should only be ran once, which will create the repository.
echo After that, run the "GitCommitUpdates.cmd" script to commit changes.
echo *** IMPORTANT ***
echo.
echo Press Control-C to terminate this batch process, or 
pause


@echo.
rem  ****************************************************************************
rem  * Add files to Local GIT Repository.
rem  ****************************************************************************
echo *** Adding all files to Local GIT Repository ...

git init
git add --all
git commit -m "Initial Commit"


@echo.
rem  ****************************************************************************
rem  * Script complete.
rem  ****************************************************************************
echo Script complete!
@echo.
pause
exit
