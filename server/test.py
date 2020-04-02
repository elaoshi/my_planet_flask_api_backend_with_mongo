import os, pathlib
import pytest

os.chdir( pathlib.Path.cwd() / 'server' )

pytest.main()