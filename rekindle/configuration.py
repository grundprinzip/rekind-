import decimal

class Configuration:

    def __init__(self):

        self.page_width = 0
        self.page_height = 0
        
        self.margin_left = 0
        self.margin_right = 0
        self.margin_top = 0
        self.margin_bottom = 0

        self.subs = 0

        self.columns = 0
        self.column_width = 0
        self.col_spacing = 0



# Create configurations for different kind of papers
ACM = Configuration()
ACM.margin_left = decimal.Decimal('1.7')
ACM.margin_right = decimal.Decimal('1.7')
ACM.margin_top = decimal.Decimal('2.1')
ACM.margin_bottom = decimal.Decimal('2.3')
ACM.page_height = decimal.Decimal('27.94')
ACM.page_width = decimal.Decimal('21.59')
ACM.columns = 2
ACM.column_width = decimal.Decimal('8.8')
ACM.col_spacing = decimal.Decimal('0.84')
ACM.subs = 2


IEEE = Configuration()
IEEE.margin_left = decimal.Decimal('1.65')
IEEE.margin_right = decimal.Decimal('1.65')
IEEE.margin_top = decimal.Decimal('1.78')
IEEE.margin_bottom = decimal.Decimal('1.78')
IEEE.page_height = decimal.Decimal('27.94')
IEEE.page_width = decimal.Decimal('21.59')
IEEE.columns = 2
IEEE.column_width = decimal.Decimal('8.89')
IEEE.col_spacing = decimal.Decimal('0.51')
IEEE.subs = 2


LNCS = Configuration()
LNCS.margin_left = decimal.Decimal('3.2')
LNCS.margin_right = decimal.Decimal('3.2')
LNCS.margin_top = decimal.Decimal('2')
LNCS.margin_bottom = decimal.Decimal('4')
LNCS.page_height = decimal.Decimal('23.5')
LNCS.page_width = decimal.Decimal('15.2')
LNCS.columns = 1
LNCS.subs = 2

LNCS2 = Configuration()
LNCS2.margin_left = decimal.Decimal('3.2')
LNCS2.margin_right = decimal.Decimal('3.2')
LNCS2.margin_top = decimal.Decimal('2')
LNCS2.margin_bottom = decimal.Decimal('4')
LNCS2.page_height = decimal.Decimal('23.5')
LNCS2.page_width = decimal.Decimal('15.2')
LNCS2.columns = 1
LNCS2.subs = 1
