#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import os.path
class FileRemove(object):
    def rm(self, filename):
        if os.path.isfile(filename):
            os.remove(filename)