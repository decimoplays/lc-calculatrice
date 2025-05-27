# Generated from hexcalc.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .hexcalcParser import hexcalcParser
else:
    from hexcalcParser import hexcalcParser

# This class defines a complete generic visitor for a parse tree produced by hexcalcParser.

class hexcalcVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by hexcalcParser#MulDiv.
    def visitMulDiv(self, ctx:hexcalcParser.MulDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hexcalcParser#AddSub.
    def visitAddSub(self, ctx:hexcalcParser.AddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hexcalcParser#Parens.
    def visitParens(self, ctx:hexcalcParser.ParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hexcalcParser#HexNumber.
    def visitHexNumber(self, ctx:hexcalcParser.HexNumberContext):
        return self.visitChildren(ctx)



del hexcalcParser