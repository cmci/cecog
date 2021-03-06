"""
                           The CellCognition Project
                     Copyright (c) 2006 - 2010 Michael Held
                      Gerlich Lab, ETH Zurich, Switzerland
                              www.cellcognition.org

              CellCognition is distributed under the LGPL License.
                        See trunk/LICENSE.txt for details.
                 See trunk/AUTHORS.txt for author contributions.
"""

__author__ = 'Michael Held'
__date__ = '$Date$'
__revision__ = '$Rev$'
__source__ = '$URL$'

__all__ = []

#-------------------------------------------------------------------------------
# standard library imports:
#
import os

#-------------------------------------------------------------------------------
# extension module imports:
#

#-------------------------------------------------------------------------------
# cecog imports:
#
from cecog.util.util import resolve_os_name

#-------------------------------------------------------------------------------
# constants:
#

#-------------------------------------------------------------------------------
# functions:
#
def map_path_to_os(path, path_mappings, target_os=None):
    path = os.path.normpath(path)
    path_mapped = None
    if target_os is None:
        target_os = resolve_os_name()
    found = False
    for mapping in path_mappings:
        for path_prefix in mapping.values():
            if path.find(path_prefix) == 0:
                path_mapped = mapping[target_os] + os.sep + \
                              path[len(path_prefix):]
                path_mapped = os.path.normpath(path_mapped)
                found = True
                break
        if found:
            break
    return path_mapped

#-------------------------------------------------------------------------------
# classes:
#


#-------------------------------------------------------------------------------
# main:
#

