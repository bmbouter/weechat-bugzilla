Bugzilla
========

Weechat script that links to bugzilla bugs::

    17:51:59 Wraithan | We should really look into bz 800000 some more.
    17:51:59          | [https://bugzilla.redhat.com/show_bug.cgi?id=800000]

I plan to add the ability for the script to look up bugs and get summary/status
like firebot, since firebot isn't always around, but that is in the future,
right now linking is better than nothing.

Installation
------------

You can install it using the ``/script`` command like so::

    /script install bugzilla.py

As of time of writing the script is pending approval, you'll need to use the
manual installation below if the above command fails.

Manual Installation
-------------------

Copy ``bugzilla.py`` into ``~/.weechat/python`` then in weechat run::

    /python load bugzilla.py

If you want the script to load every time you start weechat, symlink into the
autoload directory like this::

    ln -s ~/.weechat/python/{,autoload/}bugzilla.py

Syntax
------

Any line containing bz (case insensitive) that is followed by a number would 
match.  The 'bz' and number may be separated by an optional space and/or #.  
All of the following lines would match:

    bz 1234
    BZ 1234
    bz1234
    bz#1234

