# This is the main file
import configuration
import pyPdf
import os
from copy import copy

MARGIN = 0

class Rekind:

    def __init__(self, fn, config, output=None):

        self.doc = pyPdf.PdfFileReader(file(fn, "rb"))
        self.conf = config

        dir(self.doc)

        if output:
            self.output = output
        else:
            b,f = os.path.split(fn)
            self.output = os.path.join(b, "rekind_" + f)

    def calculate(self):
        """This method creates media boxes for the page type"""
        result = []
        
        boxes = self.conf.columns * self.conf.subs

        p = self.doc.getPage(2)
        yval = p.mediaBox.getUpperRight_y() / self.conf.page_height
        xval = p.mediaBox.getUpperRight_x() / self.conf.page_width


        if boxes == 4:

            # This is the base copy to work with
            mb = copy(p.mediaBox)

            import decimal
            halfp = self.conf.page_height / decimal.Decimal(2)
            landp = self.conf.page_width / decimal.Decimal(2)

            # for 4 boxes we generate 4 different yvalues and 4 x values
            yyy = (mb.getUpperLeft_y() - self.conf.margin_top * yval,
                   mb.getUpperLeft_y() - halfp  * yval,
                   mb.getLowerLeft_y() + halfp  * yval,
                   mb.getLowerLeft_y() + self.conf.margin_bottom * yval)
            
            xxx = (mb.getUpperLeft_x() + self.conf.margin_left * xval,
                   mb.getUpperLeft_x() + landp * xval,
                   mb.getUpperRight_x() - landp * xval,
                   mb.getUpperRight_x() - self.conf.margin_right * xval)

            tmp = copy(mb)
            tmp.upperLeft = (xxx[0] - MARGIN, yyy[0] + MARGIN)
            tmp.upperRight = (xxx[1] + MARGIN, yyy[0] + MARGIN)
            tmp.lowerLeft = (xxx[0] - MARGIN, yyy[1] - MARGIN)
            tmp.lowerRight = (xxx[1] + MARGIN, yyy[1] - MARGIN)
            result.append(tmp)

            tmp = copy(mb)
            tmp.upperLeft = (xxx[0] - MARGIN, yyy[2] + MARGIN)
            tmp.upperRight = (xxx[1] + MARGIN, yyy[2] + MARGIN)
            tmp.lowerLeft = (xxx[0] - MARGIN, yyy[3] - MARGIN)
            tmp.lowerRight = (xxx[1] + MARGIN, yyy[3] - MARGIN)
            result.append(tmp)

            tmp = copy(mb)
            tmp.upperLeft = (xxx[2] - MARGIN, yyy[0] + MARGIN)
            tmp.upperRight = (xxx[3] + MARGIN, yyy[0] + MARGIN)
            tmp.lowerLeft = (xxx[2] - MARGIN, yyy[1] - MARGIN)
            tmp.lowerRight = (xxx[3] + MARGIN, yyy[1] - MARGIN)
            result.append(tmp)

            tmp = copy(mb)
            tmp.upperLeft = (xxx[2] - MARGIN, yyy[2] + MARGIN)
            tmp.upperRight = (xxx[3] + MARGIN, yyy[2] + MARGIN)
            tmp.lowerLeft = (xxx[2] - MARGIN, yyy[3] - MARGIN)
            tmp.lowerRight = (xxx[3] + MARGIN, yyy[3] - MARGIN)
            result.append(tmp)

        else:

            if self.conf.subs == 2:

                # This is the base copy to work with
                mb = copy(p.mediaBox)

                import decimal
                halfp = self.conf.page_height / decimal.Decimal(2)

                yyy = (mb.getUpperLeft_y() - self.conf.margin_top * yval,
                       mb.getUpperLeft_y() - halfp  * yval,
                       mb.getLowerLeft_y() + halfp  * yval,
                       mb.getLowerLeft_y() + self.conf.margin_bottom * yval)
                
                xxx = (mb.getUpperLeft_x() + self.conf.margin_left * xval,
                       mb.getUpperRight_x() - self.conf.margin_right * xval)

                tmp = copy(mb)
                tmp.upperLeft = (xxx[0] - MARGIN, yyy[0] + MARGIN)
                tmp.upperRight = (xxx[1] + MARGIN, yyy[0] + MARGIN)
                tmp.lowerLeft = (xxx[0] - MARGIN, yyy[1] - MARGIN)
                tmp.lowerRight = (xxx[1] + MARGIN, yyy[1] - MARGIN)
                result.append(tmp)
                
                tmp = copy(mb)
                tmp.upperLeft = (xxx[0] - MARGIN, yyy[2] + MARGIN)
                tmp.upperRight = (xxx[1] + MARGIN, yyy[2] + MARGIN)
                tmp.lowerLeft = (xxx[0] - MARGIN, yyy[3] - MARGIN)
                tmp.lowerRight = (xxx[1] + MARGIN, yyy[3] - MARGIN)
                result.append(tmp)
                
            else:

                # This is the base copy to work with
                mb = copy(p.mediaBox)

                import decimal
                halfp = self.conf.page_height

                yyy = (mb.getUpperLeft_y() - self.conf.margin_top * yval,
                       mb.getLowerLeft_y() + self.conf.margin_bottom * yval)
                
                xxx = (mb.getUpperLeft_x() + self.conf.margin_left * xval,
                       mb.getUpperRight_x() - self.conf.margin_right * xval)

                tmp = copy(mb)
                tmp.upperLeft = (xxx[0] - MARGIN, yyy[0] + MARGIN)
                tmp.upperRight = (xxx[1] + MARGIN, yyy[0] + MARGIN)
                tmp.lowerLeft = (xxx[0] - MARGIN, yyy[1] - MARGIN)
                tmp.lowerRight = (xxx[1] + MARGIN, yyy[1] - MARGIN)
                result.append(tmp)

        return result


    def start(self):
        """ Start the process """

        boxes = self.calculate()
        
        writer = pyPdf.PdfFileWriter()

        for i in range(self.doc.getNumPages()):
            # For all calculated boxes apply
            for b in boxes:
                page = copy(self.doc.getPage(i))
                page.mediaBox = b
                writer.addPage(page)


        fid = file(self.output, "wb")
        writer.write(fid)
        fid.close()
    
        

if __name__ == "__main__":

    import sys

    if len(sys.argv) == 4:
        MARGIN = int(sys.argv[3])

    r = Rekind(sys.argv[1], configuration.__dict__[sys.argv[2]])
    r.start()
