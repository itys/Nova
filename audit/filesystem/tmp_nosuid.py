# -*- coding: utf-8 -*-
'''
Since the /tmp filesystem is only intended for temporary file storage, set this
option to ensure that users cannot create set userid files in /tmp.
'''
from __future__ import absolute_import
from audit import *
import logging


def __virtual__():
    if 'Linux' in __salt__['grains.get']('kernel'):
        return __virtualname__
    return False


def audit(): ret = _grep('"/tmp"', '/etc/fstab')
    if 'nosuid' in ret:
        return True
    else:
        return False
