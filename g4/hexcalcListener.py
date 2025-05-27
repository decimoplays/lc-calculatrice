# Generated from hexcalc.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .hexcalcParser import hexcalcParser
else:
    from hexcalcParser import hexcalcParser

# This class defines a complete listener for a parse tree produced by hexcalcParser.
class hexcalcListener(ParseTreeListener):

    # Enter a parse tree produced by hexcalcParser#MulDiv.
    def enterMulDiv(self, ctx:hexcalcParser.MulDivContext):
        pass

    # Exit a parse tree produced by hexcalcParser#MulDiv.
    def exitMulDiv(self, ctx:hexcalcParser.MulDivContext):
        pass


    # Enter a parse tree produced by hexcalcParser#AddSub.
    def enterAddSub(self, ctx:hexcalcParser.AddSubContext):
        pass

    # Exit a parse tree produced by hexcalcParser#AddSub.
    def exitAddSub(self, ctx:hexcalcParser.AddSubContext):
        pass


    # Enter a parse tree produced by hexcalcParser#Parens.
    def enterParens(self, ctx:hexcalcParser.ParensContext):
        pass

    # Exit a parse tree produced by hexcalcParser#Parens.
    def exitParens(self, ctx:hexcalcParser.ParensContext):
        pass


    # Enter a parse tree produced by hexcalcParser#HexNumber.
    def enterHexNumber(self, ctx:hexcalcParser.HexNumberContext):
        pass

    # Exit a parse tree produced by hexcalcParser#HexNumber.
    def exitHexNumber(self, ctx:hexcalcParser.HexNumberContext):
        pass



del hexcalcParser