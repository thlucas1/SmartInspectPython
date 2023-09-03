@echo off
cls

rem  ****************************************************************************
rem  * Name:    GitCommitUpdates                                                *
rem  * Desc:    Commit All Changes to Local GIT Repository.                     *
rem  *                                                                          *
rem  * This script will commit all source file changes in this folder to a      *
rem  * Local GIT Repository.                                                    *
rem  *                                                                          *
rem  ****************************************************************************


:Confirm
echo This script will commit all source file changes in this folder to a
echo Local GIT Repository.
echo.
echo Press Control-C to terminate this process, or 
pause


@echo.
rem  ****************************************************************************
rem  * Commit changes to Local GIT Repository.
rem  ****************************************************************************
echo *** Committing changes to Local GIT Repository ...

git add .
git commit -m "Updated via command file"


@echo.
rem  ****************************************************************************
rem  * Compress Local GIT Repository.
rem  ****************************************************************************
echo *** Compressing Local GIT Repository ...

git gc --auto


@echo.
rem  ****************************************************************************
rem  * Script complete.
rem  ****************************************************************************
echo Script complete!
@echo.
pause
exit
