# -*- coding: utf-8 -*-

"""
/***************************************************************************
Name		     : tetris
Date                 : 2019-10-19
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""



def classFactory(iface):    
    from .tetris_plugin import TetrisPlugin
    return TetrisPlugin(iface)
