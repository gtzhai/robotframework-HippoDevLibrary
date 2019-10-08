Creating distributions
----------------------
pip install -r requirements-build.txt

1. Cleanup (again). This removes temporary files as well as ``build`` and
   ``dist`` directories::

      invoke clean

2. Create source distribution and universal (i.e. Python 2 and 3 compatible)::

      invoke pack
      ls -l dist

