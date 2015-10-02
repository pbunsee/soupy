#Using BeautifulSoup to scrape data from websites


##Pre-requisites:
###1. INSTALL pip


	```sudo easy_install pip
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

	which pip
	/usr/local/bin/pip

	pip --version
	pip 7.1.2 from /Library/Python/2.7/site-packages/pip-7.1.2-py2.7.egg (python 2.7)
```


###2. INSTALL iPython
iPython provides a better IDE for developers than the default python IDE. 
It provides helpful features like auto-complete and context-sensitive help.

	```sudo pip install ipython[all]
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
 
###3. TO RESOLVE THE "InsecurePlatformWarning" from previous command, upgrade urllib3
	```/Library/Python/2.7/site-packages:$ sudo pip install urllib3 --upgrade
	Password:
	The directory '/Users/praneshabunsee/Library/Caches/pip/http' or its parent directory is not owned by the current user and the cache has been disabled. Please check the permissions and owner of that directory. If executing pip with sudo, you may want sudo's -H flag.
	The directory '/Users/praneshabunsee/Library/Caches/pip' or its parent directory is not owned by the current user and caching wheels has been disabled. check the permissions and owner of that directory. If executing pip with sudo, you may want sudo's -H flag.
	Collecting urllib3
	/Library/Python/2.7/site-packages/pip-7.1.2-py2.7.egg/pip/_vendor/requests/packages/urllib3/util/ssl_.py:90: InsecurePlatformWarning: A true SSLContext object is not available. This prevents urllib3 from configuring SSL appropriately and may cause certain SSL connections to fail. For more information, see https://urllib3.readthedocs.org/en/latest/security.html#insecureplatformwarning.
  	InsecurePlatformWarning
  	Downloading urllib3-1.12-py2.py3-none-any.whl (85kB)
    	100% |████████████████████████████████| 86kB 3.6MB/s 
	Installing collected packages: urllib3
	Successfully installed urllib3-1.12
	/Library/Python/2.7/site-packages:$ 
    ```
	
	
###4. NOT SURE IF openssl COMPONENT NEEDS TO BE INSTALLED SEPARATELY AFTER RUNNING PREVIOUS COMMAND BUT RAN THE INSTALL FOR IT ANYWAY AND FOUND THAT THE INSTALL WAS ALREADY TAKEN CARE OF
	```~/Documents/NYCDA/Projects/pythonWork/soupy:$ sudo pip install pyopenssl ndg-httpsclient pyasn1
	The directory '/Users/praneshabunsee/Library/Caches/pip/http' or its parent directory is not owned by the current user and the cache has been disabled. Please check the permissions and owner of that directory. If executing pip with sudo, you may want sudo's -H flag.
	The directory '/Users/praneshabunsee/Library/Caches/pip' or its parent directory is not owned by the current user and caching wheels has been disabled. check the permissions and owner of that directory. If executing pip with sudo, you may want sudo's -H flag.
	Requirement already satisfied (use --upgrade to upgrade): pyopenssl in /System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python
	Collecting ndg-httpsclient
	/Library/Python/2.7/site-packages/pip-7.1.2-py2.7.egg/pip/_vendor/requests/packages/urllib3/util/ssl_.py:90: InsecurePlatformWarning: A true SSLContext object is not available. This prevents urllib3 from configuring SSL appropriately and may cause certain SSL connections to fail. For more information, see https://urllib3.readthedocs.org/en/latest/security.html#insecureplatformwarning.
  	InsecurePlatformWarning
  	Downloading ndg_httpsclient-0.4.0.tar.gz
	Collecting pyasn1
  	Downloading pyasn1-0.1.9-py2.py3-none-any.whl
	Installing collected packages: ndg-httpsclient, pyasn1
  	Running setup.py install for ndg-httpsclient
	Successfully installed ndg-httpsclient-0.4.0 pyasn1-0.1.9
	
    ```

###5. INSTALL BEAUTIFULSOUP 4

```~/Documents/NYCDA/Projects/pythonWork/soupy:$ sudo pip install BeautifulSoup
Password:
The directory '/Users/praneshabunsee/Library/Caches/pip/http' or its parent directory is not owned by the current user and the cache has been disabled. Please check the permissions and owner of that directory. If executing pip with sudo, you may want sudo's -H flag.
The directory '/Users/praneshabunsee/Library/Caches/pip' or its parent directory is not owned by the current user and caching wheels has been disabled. check the permissions and owner of that directory. If executing pip with sudo, you may want sudo's -H flag.
Collecting BeautifulSoup
  Downloading BeautifulSoup-3.2.1.tar.gz
Installing collected packages: BeautifulSoup
  Running setup.py install for BeautifulSoup
Successfully installed BeautifulSoup-3.2.1
~/Documents/NYCDA/Projects/pythonWork/soupy:$ 
```


OR Use the following command:
```
~/Documents/NYCDA/Projects/pythonWork/soupy:$ sudo pip install beautifulsoup4
The directory '/Users/praneshabunsee/Library/Caches/pip/http' or its parent directory is not owned by the current user and the cache has been disabled. Please check the permissions and owner of that directory. If executing pip with sudo, you may want sudo's -H flag.
The directory '/Users/praneshabunsee/Library/Caches/pip' or its parent directory is not owned by the current user and caching wheels has been disabled. check the permissions and owner of that directory. If executing pip with sudo, you may want sudo's -H flag.
Collecting beautifulsoup4
  Downloading beautifulsoup4-4.4.1-py2-none-any.whl (81kB)
    100% |████████████████████████████████| 81kB 4.5MB/s 
Installing collected packages: beautifulsoup4
Successfully installed beautifulsoup4-4.4.1
~/Documents/NYCDA/Projects/pythonWork/soupy:$ 
```


