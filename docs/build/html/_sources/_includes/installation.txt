Installation
============

The easiest way to install panstamps is to use ``pip``:

.. code:: bash

    pip install panstamps

Or you can clone the `github repo <https://github.com/thespacedoctor/panstamps>`__ and install from a local version of the code:

.. code:: bash

    git clone git@github.com:thespacedoctor/panstamps.git
    cd panstamps
    python setup.py install

To upgrade to the latest version of panstamps use the command:

.. code:: bash

    pip install panstamps --upgrade

Troubleshooting on Mac OSX
---------------------------

panstamps uses pillow (a fork of the Python Imaging Library) which requires some `external libraries <https://pillow.readthedocs.org/en/3.1.x/installation.html#external-libraries>`_. 

If you have issues running panstamps on OSX, try installing `Homebrew <http://brew.sh/>`_ and running:

.. code:: bash

    brew install libtiff libjpeg webp little-cms2

