#Using BeautifulSoup to scrape data from websites


##Pre-requisites - Environment Preparation:
###1. Which Python version to use? Python 2.7 (which is the default installed on Mac OS X) or Python 3?
>[Python wiki advice](https://wiki.python.org/moin/Python2orPython3)  
>[June 2014 Blog post from Learn to Code with Me](http://learntocodewith.me/programming/python/python-2-vs-python-3/)  
>[June 2014 Blog post from SEBASTIANRASCHKA](http://sebastianraschka.com/Articles/2014_python_2_3_key_diff.html#Comparing-unorderable-types)  

>For my immediate goals of building some simple web scrapers, I decided to follow [Quora response from Yilun Zhang](https://www.quora.com/What-should-I-use-for-data-science-Python-2-7-x-or-Python-3-4-x/answer/Yilun-Tom-Zhang?srid=zU1D)  
>taking into account that there seems to be lower adoption of Python 3.x (I need to verify this with more research though)  
>It is possible to maintain multiple Python environments on the same OS though - so I will be installing latest build of Python 3 at some point.


###2. Install pip
```
sudo easy_install pip
Password:
Searching for pip
Reading http://pypi.python.org/simple/pip/
Best match: pip 7.1.2
Downloading https://pypi.python.org/packages/source/p/pip/pip-7.1.2.tar.gz#md5=3823d2343d9f3aaab21cf9c917710196
Processing pip-7.1.2.tar.gz
Running pip-7.1.2/setup.py -q bdist_egg --dist-dir /tmp/easy_install-_JQGv9/pip-7.1.2/egg-dist-tmp-0ncQap
warning: no previously-included files found matching '.coveragerc'
warning: no previously-included files found matching '.mailmap'
warning: no previously-included files found matching '.travis.yml'
warning: no previously-included files found matching 'pip/_vendor/Makefile'
warning: no previously-included files found matching 'tox.ini'
warning: no previously-included files found matching 'dev-requirements.txt'
no previously-included directories found matching '.travis'
no previously-included directories found matching 'docs/_build'
no previously-included directories found matching 'contrib'
no previously-included directories found matching 'tasks'
no previously-included directories found matching 'tests'
Adding pip 7.1.2 to easy-install.pth file
Installing pip script to /usr/local/bin
Installing pip2.7 script to /usr/local/bin
Installing pip2 script to /usr/local/bin
	
Installed /Library/Python/2.7/site-packages/pip-7.1.2-py2.7.egg
Processing dependencies for pip
Finished processing dependencies for pip
```

```
which pip
/usr/local/bin/pip
```

```
pip --version
pip 7.1.2 from /Library/Python/2.7/site-packages/pip-7.1.2-py2.7.egg (python 2.7)
```


###3. Install virtualenv
> virtualenv is necessary for project encapsulation.   
> virtualenvwrapper is useful for ease of use of virtual environments.  
> autoenv for automatic env detection when changing to a directory  
> Reference: [Python virtualenv & virtualenvwrapper Guides](http://docs.python-guide.org/en/latest/dev/virtualenvs/)  

```
sudo pip install virtualenv
Password:
The directory '/Users/praneshabunsee/Library/Caches/pip/http' or its parent directory is not owned by the current user and the cache has been disabled. Please check the permissions and owner of that directory. If executing pip with sudo, you may want sudo's -H flag.
The directory '/Users/praneshabunsee/Library/Caches/pip' or its parent directory is not owned by the current user and caching wheels has been disabled. check the permissions and owner of that directory. If executing pip with sudo, you may want sudo's -H flag.
Collecting virtualenv
  Retrying (Retry(total=4, connect=None, read=None, redirect=None)) after connection broken by 'ReadTimeoutError("HTTPSConnectionPool(host='pypi.python.org', port=443): Read timed out. (read timeout=15)",)': /simple/virtualenv/
  Downloading virtualenv-13.1.2-py2.py3-none-any.whl (1.7MB)
    100% |████████████████████████████████| 1.7MB 282kB/s 
Installing collected packages: virtualenv
Successfully installed virtualenv-13.1.2
```


```
sudo pip install virtualenvwrapper
The directory '/Users/praneshabunsee/Library/Caches/pip/http' or its parent directory is not owned by the current user and the cache has been disabled. Please check the permissions and owner of that directory. If executing pip with sudo, you may want sudo's -H flag.
The directory '/Users/praneshabunsee/Library/Caches/pip' or its parent directory is not owned by the current user and caching wheels has been disabled. check the permissions and owner of that directory. If executing pip with sudo, you may want sudo's -H flag.
Collecting virtualenvwrapper
  Downloading virtualenvwrapper-4.7.1-py2.py3-none-any.whl
Requirement already satisfied (use --upgrade to upgrade): virtualenv in /Library/Python/2.7/site-packages (from virtualenvwrapper)
Collecting virtualenv-clone (from virtualenvwrapper)
  Downloading virtualenv-clone-0.2.6.tar.gz
Collecting stevedore (from virtualenvwrapper)
  Downloading stevedore-1.8.0-py2.py3-none-any.whl
Collecting argparse (from stevedore->virtualenvwrapper)
  Downloading argparse-1.4.0-py2.py3-none-any.whl
Requirement already satisfied (use --upgrade to upgrade): six>=1.9.0 in /Library/Python/2.7/site-packages (from stevedore->virtualenvwrapper)
Requirement already satisfied (use --upgrade to upgrade): pbr<2.0,>=1.6 in /Library/Python/2.7/site-packages (from stevedore->virtualenvwrapper)
Installing collected packages: virtualenv-clone, argparse, stevedore, virtualenvwrapper
  Running setup.py install for virtualenv-clone
Successfully installed argparse-1.4.0 stevedore-1.8.0 virtualenv-clone-0.2.6 virtualenvwrapper-4.7.1
```

```
export WORKON_HOME=~/Envs
```

```
source /usr/local/bin/virtualenvwrapper.sh
```

```
brew install autoenv
==> Downloading https://github.com/kennethreitz/autoenv/archive/v0.1.0.tar.gz
######################################################################## 100.0%
==> Caveats
To finish the installation, source activate.sh in your shell:
  source /usr/local/opt/autoenv/activate.sh
==> Summary
🍺  /usr/local/Cellar/autoenv/0.1.0: 4 files, 16K, built in 2 seconds
```

###4. Create your new virtual environment - I called my env 'soupy'. Then activate the env.
```
 virtualenv soupy
New python executable in soupy/bin/python
Installing setuptools, pip, wheel...done.
```

```
cd soupy  
source bin/activate
```

###5. Install iPython
>This is an optional installation. Use whichever IDE you are most comfortable with.  
>iPython provides a better IDE for developers than the default python IDE.   
>It provides helpful features like auto-complete and context-sensitive method selection.

```
sudo pip install ipython[all]
Password:
The directory '/Users/praneshabunsee/Library/Caches/pip/http' or its parent directory is not owned by the current user and the cache has been disabled. Please check the permissions and owner of that directory. If executing pip with sudo, you may want sudo's -H flag.
The directory '/Users/praneshabunsee/Library/Caches/pip' or its parent directory is not owned by the current user and caching wheels has been disabled. check the permissions and owner of that directory. If executing pip with sudo, you may want sudo's -H flag.
Collecting ipython[all]
/Library/Python/2.7/site-packages/pip-7.1.2-py2.7.egg/pip/_vendor/requests/packages/urllib3/util/ssl_.py:90: InsecurePlatformWarning: A true SSLContext object is not available. This prevents urllib3 from configuring SSL appropriately and may cause certain SSL connections to fail. For more information, see https://urllib3.readthedocs.org/en/latest/security.html#insecureplatformwarning.
InsecurePlatformWarning
Downloading ipython-4.0.0-py2-none-any.whl (730kB)
100% |████████████████████████████████| 733kB 654kB/s 
Collecting traitlets (from ipython[all])
Downloading traitlets-4.0.0-py2.py3-none-any.whl (56kB)
100% |████████████████████████████████| 57kB 5.4MB/s 
Collecting pickleshare (from ipython[all])
Downloading pickleshare-0.5.tar.gz
Collecting simplegeneric>0.8 (from ipython[all])
Downloading simplegeneric-0.8.1.zip
	
Collecting gnureadline (from ipython[all])
Downloading gnureadline-6.3.3-cp27-none-macosx_10_6_intel.whl (262kB)
100% |████████████████████████████████| 262kB 1.5MB/s 
Collecting appnope (from ipython[all])
Downloading appnope-0.1.0-py2.py3-none-any.whl
Collecting pexpect (from ipython[all])
Downloading pexpect-3.3.tar.gz (132kB)
100% |████████████████████████████████| 135kB 3.3MB/s 
Collecting nose>=0.10.1 (from ipython[all])
Downloading nose-1.3.7-py2-none-any.whl (154kB)
100% |████████████████████████████████| 155kB 2.9MB/s 
Collecting ipyparallel (from ipython[all])
Downloading ipyparallel-4.0.2-py2.py3-none-any.whl (164kB)
100% |████████████████████████████████| 167kB 2.5MB/s 
Collecting notebook (from ipython[all])
Downloading notebook-4.0.5-py2.py3-none-any.whl (5.5MB)
100% |████████████████████████████████| 5.5MB 89kB/s 
Collecting requests (from ipython[all])
Downloading requests-2.7.0-py2.py3-none-any.whl (470kB)
100% |████████████████████████████████| 471kB 836kB/s 
Collecting nbformat (from ipython[all])
Downloading nbformat-4.0.0-py2.py3-none-any.whl (138kB)
100% |████████████████████████████████| 139kB 2.1MB/s 
Collecting pyreadline>=2 (from ipython[all])
Downloading pyreadline-2.1.zip (109kB)
100% |████████████████████████████████| 110kB 3.1MB/s 
Collecting nbconvert (from ipython[all])
Downloading nbconvert-4.0.0-py2.py3-none-any.whl (278kB)
100% |████████████████████████████████| 278kB 1.4MB/s 
Collecting testpath (from ipython[all])
Downloading testpath-0.2-py2.py3-none-any.whl
Collecting ipykernel (from ipython[all])
Downloading ipykernel-4.0.3-py2.py3-none-any.whl (89kB)
100% |████████████████████████████████| 90kB 4.2MB/s 
Collecting numpydoc (from ipython[all])
Downloading numpydoc-0.5.tar.gz
Collecting qtconsole (from ipython[all])
	
Downloading numpydoc-0.5.tar.gz
Collecting qtconsole (from ipython[all])
Downloading qtconsole-4.0.1-py2.py3-none-any.whl (98kB)
100% |████████████████████████████████| 102kB 4.1MB/s 
Collecting Sphinx>=1.1 (from ipython[all])
Downloading Sphinx-1.3.1-py2.py3-none-any.whl (1.3MB)
100% |████████████████████████████████| 1.3MB 368kB/s 
Collecting mock (from ipython[all])
Downloading mock-1.3.0-py2.py3-none-any.whl (56kB)
100% |████████████████████████████████| 57kB 6.3MB/s 
Collecting ipython-genutils (from traitlets->ipython[all])
Downloading ipython_genutils-0.1.0-py2.py3-none-any.whl
Collecting path.py (from pickleshare->ipython[all])
Downloading path.py-8.1.1-py2.py3-none-any.whl
Collecting jupyter-client (from ipyparallel->ipython[all])
Downloading jupyter_client-4.0.0-py2.py3-none-any.whl (70kB)
100% |████████████████████████████████| 73kB 6.1MB/s 
Collecting pyzmq>=13 (from ipyparallel->ipython[all])
Downloading pyzmq-14.7.0-cp27-none-macosx_10_6_intel.whl (1.2MB)
100% |████████████████████████████████| 1.2MB 394kB/s 
Collecting tornado>=4 (from notebook->ipython[all])
Downloading tornado-4.2.1.tar.gz (434kB)
100% |████████████████████████████████| 438kB 1.1MB/s 
Collecting jupyter-core (from notebook->ipython[all])
Downloading jupyter_core-4.0.6-py2.py3-none-any.whl (74kB)
100% |████████████████████████████████| 77kB 5.4MB/s 
Collecting terminado>=0.3.3 (from notebook->ipython[all])
Downloading terminado-0.5.tar.gz
Collecting jinja2 (from notebook->ipython[all])
Downloading Jinja2-2.8-py2.py3-none-any.whl (263kB)
100% |████████████████████████████████| 266kB 2.0MB/s 
Collecting jsonschema!=2.5.0,>=2.0 (from nbformat->ipython[all])
Downloading jsonschema-2.5.1-py2.py3-none-any.whl
Collecting pygments (from nbconvert->ipython[all])
Downloading Pygments-2.0.2-py2-none-any.whl (672kB)
100% |████████████████████████████████| 675kB 700kB/s 
	
100% |████████████████████████████████| 675kB 700kB/s 
Collecting mistune!=0.6 (from nbconvert->ipython[all])
Downloading mistune-0.7.1-cp27-none-macosx_10_6_intel.macosx_10_9_intel.macosx_10_9_x86_64.macosx_10_10_intel.macosx_10_10_x86_64.whl (418kB)
100% |████████████████████████████████| 421kB 1.0MB/s 
Collecting sphinx-rtd-theme<0.2,>=0.1 (from Sphinx>=1.1->ipython[all])
Downloading sphinx_rtd_theme-0.1.9-py2-none-any.whl (693kB)
100% |████████████████████████████████| 696kB 711kB/s 
Collecting snowballstemmer>=1.1 (from Sphinx>=1.1->ipython[all])
Downloading snowballstemmer-1.2.0.tar.gz (49kB)
100% |████████████████████████████████| 53kB 6.0MB/s 
Collecting six>=1.4 (from Sphinx>=1.1->ipython[all])
Downloading six-1.9.0-py2.py3-none-any.whl
Collecting docutils>=0.11 (from Sphinx>=1.1->ipython[all])
Downloading docutils-0.12.tar.gz (1.6MB)
100% |████████████████████████████████| 1.6MB 303kB/s 
Collecting babel>=1.3 (from Sphinx>=1.1->ipython[all])
Downloading Babel-2.1.1-py2.py3-none-any.whl (3.6MB)
100% |████████████████████████████████| 3.6MB 134kB/s 
Collecting alabaster<0.8,>=0.7 (from Sphinx>=1.1->ipython[all])
Downloading alabaster-0.7.6-py2-none-any.whl
Collecting funcsigs (from mock->ipython[all])
Downloading funcsigs-0.4-py2.py3-none-any.whl
Collecting pbr>=0.11 (from mock->ipython[all])
Downloading pbr-1.8.0-py2.py3-none-any.whl (87kB)
100% |████████████████████████████████| 90kB 4.4MB/s 
Collecting backports.ssl-match-hostname (from tornado>=4->notebook->ipython[all])
Downloading backports.ssl_match_hostname-3.4.0.2.tar.gz
Collecting certifi (from tornado>=4->notebook->ipython[all])
Downloading certifi-2015.9.6.2-py2.py3-none-any.whl (371kB)
100% |████████████████████████████████| 372kB 805kB/s 
Collecting ptyprocess (from terminado>=0.3.3->notebook->ipython[all])
Downloading ptyprocess-0.5.tar.gz
Collecting MarkupSafe (from jinja2->notebook->ipython[all])
Downloading MarkupSafe-0.23.tar.gz
Collecting functools32 (from jsonschema!=2.5.0,>=2.0->nbformat->ipython[all])
Downloading functools32-3.2.3-2.tar.gz
Collecting pytz>=0a (from babel>=1.3->Sphinx>=1.1->ipython[all])
Downloading pytz-2015.6-py2.py3-none-any.whl (475kB)
100% |████████████████████████████████| 475kB 1.0MB/s 
Installing collected packages: decorator, ipython-genutils, traitlets, path.py, pickleshare, simplegeneric, gnureadline, appnope, pexpect, nose, jupyter-core, pyzmq, jupyter-client, ipykernel, ipyparallel, backports.ssl-match-hostname, certifi, tornado, functools32, jsonschema, nbformat, pygments, mistune, MarkupSafe, jinja2, nbconvert, ptyprocess, terminado, notebook, requests, pyreadline, testpath, numpydoc, qtconsole, sphinx-rtd-theme, snowballstemmer, six, docutils, pytz, babel, alabaster, Sphinx, funcsigs, pbr, mock, ipython
Running setup.py install for pickleshare
Running setup.py install for simplegeneric
Running setup.py install for pexpect
Running setup.py install for backports.ssl-match-hostname
Running setup.py install for tornado
Running setup.py install for functools32
Running setup.py install for MarkupSafe
Running setup.py install for ptyprocess
Running setup.py install for terminado
Running setup.py install for pyreadline
Running setup.py install for numpydoc
Running setup.py install for snowballstemmer
Running setup.py install for docutils
Found existing installation: pytz 2012d
Uninstalling pytz-2012d:
Successfully uninstalled pytz-2012d
Successfully installed MarkupSafe-0.23 Sphinx-1.3.1 alabaster-0.7.6 appnope-0.1.0 babel-2.1.1 backports.ssl-match-hostname-3.4.0.2 certifi-2015.9.6.2 decorator-4.0.4 docutils-0.12 funcsigs-0.4 functools32-3.2.3-2 gnureadline-6.3.3 ipykernel-4.0.3 ipyparallel-4.0.2 ipython-4.0.0 ipython-genutils-0.1.0 jinja2-2.8 jsonschema-2.5.1 jupyter-client-4.0.0 jupyter-core-4.0.6 mistune-0.7.1 mock-1.3.0 nbconvert-4.0.0 nbformat-4.0.0 nose-1.3.7 notebook-4.0.5 numpydoc-0.5 path.py-8.1.1 pbr-1.8.0 pexpect-3.3 pickleshare-0.5 ptyprocess-0.5 pygments-2.0.2 pyreadline-2.1 pytz-2015.6 pyzmq-14.7.0 qtconsole-4.0.1 requests-2.7.0 simplegeneric-0.8.1 six-1.9.0 snowballstemmer-1.2.0 sphinx-rtd-theme-0.1.9 terminado-0.5 testpath-0.2 tornado-4.2.1 traitlets-4.0.0
/Library/Python/2.7/site-packages/pip-7.1.2-py2.7.egg/pip/_vendor/requests/packages/urllib3/util/ssl_.py:90: InsecurePlatformWarning: A true SSLContext object is not available. This prevents urllib3 from configuring SSL appropriately and may cause certain SSL connections to fail. For more information, see https://urllib3.readthedocs.org/en/latest/security.html#insecureplatformwarning.
InsecurePlatformWarning
```
 
###6. To resolve the "InsecurePlatformWarning" from previous command, upgrade urllib3
```
(soupy)~/Documents/NYCDA/Projects/pythonWork/soupy:master$ sudo -H pip install urllib3 --upgrade
Collecting urllib3
/Users/praneshabunsee/Documents/NYCDA/Projects/pythonWork/soupy/lib/python2.7/site-packages/pip/_vendor/requests/packages/urllib3/util/ssl_.py:90: InsecurePlatformWarning: A true SSLContext object is not available. This prevents urllib3 from configuring SSL appropriately and may cause certain SSL connections to fail. For more information, see https://urllib3.readthedocs.org/en/latest/security.html#insecureplatformwarning.
  InsecurePlatformWarning
  Downloading urllib3-1.12-py2.py3-none-any.whl (85kB)
    100% |████████████████████████████████| 86kB 3.3MB/s 
Installing collected packages: urllib3
Successfully installed urllib3-1.12
```
	
###7. Take care of making SSL requests over HTTP work
>Since I am using the default Python version provided on MAC OS X - i.e. Python version 2.7.5, I took heed of the info provided about SSL requests over HTTP in [urllib3 dev documentation](https://urllib3.readthedocs.org/en/latest/security.html#insecureplatformwarning)
>and ran the following command:  

```
(soupy)~/Documents/NYCDA/Projects/pythonWork/soupy:master$ sudo -H pip install pyopenssl ndg-httpsclient pyasn1
Collecting pyopenssl
/Users/praneshabunsee/Documents/NYCDA/Projects/pythonWork/soupy/lib/python2.7/site-packages/pip/_vendor/requests/packages/urllib3/util/ssl_.py:90: InsecurePlatformWarning: A true SSLContext object is not available. This prevents urllib3 from configuring SSL appropriately and may cause certain SSL connections to fail. For more information, see https://urllib3.readthedocs.org/en/latest/security.html#insecureplatformwarning.
  InsecurePlatformWarning
  Downloading pyOpenSSL-0.15.1-py2.py3-none-any.whl (102kB)
    100% |████████████████████████████████| 106kB 1.1MB/s 
Collecting ndg-httpsclient
  Downloading ndg_httpsclient-0.4.0.tar.gz
Collecting pyasn1
  Downloading pyasn1-0.1.9-py2.py3-none-any.whl
Collecting six>=1.5.2 (from pyopenssl)
  Downloading six-1.9.0-py2.py3-none-any.whl
Collecting cryptography>=0.7 (from pyopenssl)
  Downloading cryptography-1.0.2.tar.gz (332kB)
    100% |████████████████████████████████| 335kB 1.2MB/s 
Collecting idna>=2.0 (from cryptography>=0.7->pyopenssl)
  Downloading idna-2.0-py2.py3-none-any.whl (61kB)
    100% |████████████████████████████████| 61kB 4.3MB/s 
Requirement already satisfied (use --upgrade to upgrade): setuptools in ./lib/python2.7/site-packages (from cryptography>=0.7->pyopenssl)
Collecting enum34 (from cryptography>=0.7->pyopenssl)
  Downloading enum34-1.0.4.tar.gz
Collecting ipaddress (from cryptography>=0.7->pyopenssl)
  Downloading ipaddress-1.0.14-py27-none-any.whl
Collecting cffi>=1.1.0 (from cryptography>=0.7->pyopenssl)
  Downloading cffi-1.2.1.tar.gz (335kB)
    100% |████████████████████████████████| 335kB 861kB/s 
Collecting pycparser (from cffi>=1.1.0->cryptography>=0.7->pyopenssl)
  Downloading pycparser-2.14.tar.gz (223kB)
    100% |████████████████████████████████| 225kB 1.1MB/s 
Building wheels for collected packages: ndg-httpsclient, cryptography, enum34, cffi, pycparser
  Running setup.py bdist_wheel for ndg-httpsclient
  Stored in directory: /var/root/Library/Caches/pip/wheels/30/85/40/a29750f9287fe119a10708580a73cfb16f51e5f9a820430a2d
  Running setup.py bdist_wheel for cryptography
  Stored in directory: /var/root/Library/Caches/pip/wheels/a6/26/db/a0fe3e48fccc54c031bd4c43705e6abf6ac7e7b85df95373ee
  Running setup.py bdist_wheel for enum34
  Stored in directory: /var/root/Library/Caches/pip/wheels/d1/b2/2c/b51348698bd1921a226cf48d790b282d86fb4bcf9728afd6b3
  Running setup.py bdist_wheel for cffi
  Stored in directory: /var/root/Library/Caches/pip/wheels/fa/ad/ab/28df6da3b6cf3c510c6dc64f336ef17ef37cd1b0d4d5eff3bc
  Running setup.py bdist_wheel for pycparser
  Stored in directory: /var/root/Library/Caches/pip/wheels/c7/28/31/bac6d0b118c0bdcbf57f9219afdf2e624379c07efa6c769dbc
Successfully built ndg-httpsclient cryptography enum34 cffi pycparser
Installing collected packages: six, idna, pyasn1, enum34, ipaddress, pycparser, cffi, cryptography, pyopenssl, ndg-httpsclient
Successfully installed cffi-1.2.1 cryptography-1.0.2 enum34-1.0.4 idna-2.0 ipaddress-1.0.14 ndg-httpsclient-0.4.0 pyasn1-0.1.9 pycparser-2.14 pyopenssl-0.15.1 six-1.9.0
(soupy)~/Documents/NYCDA/Projects/pythonWork/soupy:master$ 
```

###8. Install beautifulsoup4
>Use sudo -H to install beautifulsoup4 (have to use --upgrade flag since it is already installed)  
```
sudo -H pip install beautifulsoup4
Password:
Collecting beautifulsoup4
/Users/praneshabunsee/Documents/NYCDA/Projects/pythonWork/soupy/lib/python2.7/site-packages/pip/_vendor/requests/packages/urllib3/util/ssl_.py:90: InsecurePlatformWarning: A true SSLContext object is not available. This prevents urllib3 from configuring SSL appropriately and may cause certain SSL connections to fail. For more information, see https://urllib3.readthedocs.org/en/latest/security.html#insecureplatformwarning.
  InsecurePlatformWarning
  Downloading beautifulsoup4-4.4.1-py2-none-any.whl (81kB)
    100% |████████████████████████████████| 81kB 1.8MB/s 
Installing collected packages: beautifulsoup4
Successfully installed beautifulsoup4-4.4.1
(soupy)~/Documents/NYCDA/Projects/pythonWork/soupy:master$ 
```

###9. Review the products installed by issuing the following command:
```
pip freeze
wheel==0.24.0
```


