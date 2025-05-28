# Generated from hexcalc.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .hexcalcParser import hexcalcParser
else:
    from hexcalcParser import hexcalcParser

# This class defines a complete generic visitor for a parse tree produced by hexcalcParser.

class hexcalcVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by hexcalcParser#prog.
    def visitProg(self, ctx:hexcalcParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hexcalcParser#Assign.
    def visitAssign(self, ctx:hexcalcParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hexcalcParser#Expr.
    def visitExpr(self, ctx:hexcalcParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hexcalcParser#HexFloatNumber.
    def visitHexFloatNumber(self, ctx:hexcalcParser.HexFloatNumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hexcalcParser#Variable.
    def visitVariable(self, ctx:hexcalcParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hexcalcParser#Mod.
    def visitMod(self, ctx:hexcalcParser.ModContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hexcalcParser#MulDiv.
    def visitMulDiv(self, ctx:hexcalcParser.MulDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hexcalcParser#AddSub.
    def visitAddSub(self, ctx:hexcalcParser.AddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hexcalcParser#Parens.
    def visitParens(self, ctx:hexcalcParser.ParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hexcalcParser#UnaryMinus.
    def visitUnaryMinus(self, ctx:hexcalcParser.UnaryMinusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hexcalcParser#ExpLn.
    def visitExpLn(self, ctx:hexcalcParser.ExpLnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hexcalcParser#HexNumber.
    def visitHexNumber(self, ctx:hexcalcParser.HexNumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hexcalcParser#MinMax.
    def visitMinMax(self, ctx:hexcalcParser.MinMaxContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by hexcalcParser#Power.
    def visitPower(self, ctx:hexcalcParser.PowerContext):
        return self.visitChildren(ctx)



del hexcalcParser