@echo off
cls

rem  ****************************************************************************
rem  * Name:    GitCompress                                                     *
rem  * Desc:    Compress Local GIT Repository.                                  *
rem  *                                                                          *
rem  * This script will compress the local GIT repository in order to conserve  *
rem  * disk space.                                                              *
rem  *                                                                          *
rem  ****************************************************************************


:Confirm
echo This script will compress the local GIT repository in order to conserve
echo disk space.
echo.
echo Press Control-C to terminate this process, or 
pause


@echo.
rem  ****************************************************************************
rem  * Compress Local GIT Repository.
rem  ****************************************************************************
echo *** Compressing Local GIT Repository ...

git gc


@echo.
rem  ****************************************************************************
rem  * Script complete.
rem  ****************************************************************************
echo Script complete!
@echo.
pause
exit
