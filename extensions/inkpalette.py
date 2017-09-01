import sys
sys.path.append('/usr/share/inkscape/extensions')
import inkex
from simplestyle import *
from inkpallete_db import *

class InkpaletteEffect(inkex.Effect):
    def __init__(self):
        inkex.Effect.__init__(self)

        self.OptionParser.add_option('-c', '--colors', action = 'store',
          type = 'string', dest = 'colors', default = 'Airbnb',
          help = 'Select the brand color:')

        

    def effect(self):
        colors = self.options.colors
        brand_name = palettes[colors]
        svg = self.document.getroot()

        # Create a new layer.
        layer = inkex.etree.SubElement(svg, 'g')
        layer.set(inkex.addNS('label', 'inkscape'), 'Palette %s' % (colors))
        layer.set(inkex.addNS('groupmode', 'inkscape'), 'layer')

        rect_height = 12
        rect_width = 35
        rect_x= -50
        rect_y = 0

        for color in brand_name:
            
            style = {   'stroke'        : 'none',
                        'stroke-width'  : '1px',
                        'fill'          : '%s' %(color[0]),
            }

            text_style = {'font-size' : '3px', 'color' : '#ffffff'}

                
            attribs = {
                'style'     : formatStyle(style),
                'height'    : str(rect_height),
                'width'     : str(rect_width),
                'x'         : str(rect_x),
                'y'         : str(rect_y)
                    }

            text_attribs = {
                'x'         : str(rect_x + 3),
                'y'         : str(rect_y + 7),
                'color'     : str('white')
                    }

            text = inkex.etree.Element(inkex.addNS('text','svg'), text_attribs)
            text.text = str(color[0])

            text.set('style', formatStyle(text_style))
            
            rectangle = inkex.etree.Element(inkex.addNS('rect','svg'), attribs )

            layer.append(rectangle)
            layer.append(text)
            
            rect_y += (rect_height)


effect = InkpaletteEffect()
effect.affect()