python:
------
install python for the respective OS at https://www.python.org/downloads/
Make sure to update the path variable to point to the python installation folder.

pip:
----
get get-pip.py from below link to your folder
https://bootstrap.pypa.io/get-pip.py
Open a command prompt and navigate to the folder containing get-pip.py.
Run the following command:

pylint:
-------
pip install -U pylint

mutmut:
------
pip install mutmut

pytest:
------
pip install pytest

unittest:
---------
pip install unittest

Other topics uderdiscussion
---------------------------
Make sure the tools are also available in your editor (mine is visual studio code), editor is your choice 
https://code.visualstudio.com/download (choose defaults)

Install jscpd:
install node from https://nodejs.org/en/download/
npm install -g jscpd
make sure package is available npm list -g --depth=0
for details: https://www.npmjs.com/package/jscpd

JSCPD for edittor:
https://marketplace.visualstudio.com/items?itemName=paulhoughton.vscode-jscpd


Commands
--------

Outputting pylint
=================
$pyfiles = Get-ChildItem -Path .\ -Filter *.py -Recurse -File -Name
pylint -E $pyfiles

Copy paste detection:
=====================
jscpd -r "html" -o "repo_location" "report_location"

pytest execution
================
pytest -v -s

Coverage for all files in a folder
=========================
pytest --cov-report html --cov="code_path"

unit testing coverage
=====================
python -m unittest -v
coverage run fine_name
coverage html

pydoc creation
==============
python -m pydoc -w module_name

Mutation testing commands:
=========================
mutmut run
mutmut show


