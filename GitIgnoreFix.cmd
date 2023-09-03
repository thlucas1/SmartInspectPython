@echo off
cls

rem  ****************************************************************************
rem  * Name:    GitIgnoreFix                                                    *
rem  * Desc:    Fixes Local GIT Repository when adding entries to .gitignore.   *
rem  *                                                                          *
rem  * Each time I start a project and do the first commit, I ALWAYS forget to  *
rem  * add/change/create the ".gitignore" file.  This will remove any files     *
rem  * that are still being tracked after making changes to ".gitignore".       *
rem  *                                                                          *
rem  ****************************************************************************


:Confirm
echo This will remove files from the Local GIT Repository HEAD that should be
echo ignored after modifying the ".gitignore" file.
echo.
echo *** NOTE - ONLY RUN THIS if you have changed ".gitignore"!
echo.
echo When you add/modify the .gitignore file and then try to commit the changes,
echo you will see that the files you asked git to ignore are still being flagged
echo as changed.  The reason for this is that the files are still on the HEAD
echo index, and are still being tracked as you have not told GIT to remove them
echo from the index.
echo.
echo The following commands will be executed to remove the files no longer
echo tracked (as controlled by .gitignore) from the HEAD index:
echo.
echo git rm -rf --cached .
echo git add . 
echo git commit -m 'fixed gitignore'
echo.
echo Press Control-C to terminate this process, or 
pause


@echo.
rem  ****************************************************************************
rem  * Commit changes to Local GIT Repository.
rem  ****************************************************************************
echo *** Committing changes to Local GIT Repository ...

rem Remove the files completely from the index.
git rm -rf --cached .

rem Add all of the files (the dot means all).
git add . 

rem Commit the changes with the label of:  “fixed gitignore”
git commit -m "fixed gitignore"

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
