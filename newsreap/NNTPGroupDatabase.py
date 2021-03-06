# -*- coding: utf-8 -*-
#
# A common Group Database management class used by SQLAlchemy
#
# Copyright (C) 2015-2017 Chris Caron <lead2gold@gmail.com>
#
# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.

import gevent.monkey
gevent.monkey.patch_all()

# Importing these libraries forces them associate themselves
# with the ObjectBase
from .objects.group.Article import Article

# The ObjectBase which contains all of the data required to
# access our table.
from .objects.group.ObjectBase import ObjectBase
from .objects.group.Vsp import Vsp

from .Database import Database

# The catch wit SQLite when referencing paths is:
# sqlite:///relative/path/to/where we are now
# sqlite:////absolute/path/


class NNTPGroupDatabase(Database):
    """
    A managment class to handle Group/Article Databases
    """

    def __init__(self, engine=None, reset=None):
        """
        Initialize NNTP Group/Article Database
        """
        super(NNTPGroupDatabase, self).__init__(
            base=ObjectBase,
            vsp=Vsp,
            engine=engine,
            reset=reset,
        )
