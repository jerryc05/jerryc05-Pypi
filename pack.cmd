@rmdir dist  /s /q
@rmdir build /s /q
@py setup.py bdist_wheel
@REM @py setup.py sdist bdist_wheel
@rmdir build /s /q
@twine upload -u jerryc05 dist\*
@pause