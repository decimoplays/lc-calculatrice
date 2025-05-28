# Generated from hexcalc.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .hexcalcParser import hexcalcParser
else:
    from hexcalcParser import hexcalcParser

# This class defines a complete listener for a parse tree produced by hexcalcParser.
class hexcalcListener(ParseTreeListener):

    # Enter a parse tree produced by hexcalcParser#prog.
    def enterProg(self, ctx:hexcalcParser.ProgContext):
        pass

    # Exit a parse tree produced by hexcalcParser#prog.
    def exitProg(self, ctx:hexcalcParser.ProgContext):
        pass


    # Enter a parse tree produced by hexcalcParser#Assign.
    def enterAssign(self, ctx:hexcalcParser.AssignContext):
        pass

    # Exit a parse tree produced by hexcalcParser#Assign.
    def exitAssign(self, ctx:hexcalcParser.AssignContext):
        pass


    # Enter a parse tree produced by hexcalcParser#Expr.
    def enterExpr(self, ctx:hexcalcParser.ExprContext):
        pass

    # Exit a parse tree produced by hexcalcParser#Expr.
    def exitExpr(self, ctx:hexcalcParser.ExprContext):
        pass


    # Enter a parse tree produced by hexcalcParser#FuncCall.
    def enterFuncCall(self, ctx:hexcalcParser.FuncCallContext):
        pass

    # Exit a parse tree produced by hexcalcParser#FuncCall.
    def exitFuncCall(self, ctx:hexcalcParser.FuncCallContext):
        pass


    # Enter a parse tree produced by hexcalcParser#HexFloatNumber.
    def enterHexFloatNumber(self, ctx:hexcalcParser.HexFloatNumberContext):
        pass

    # Exit a parse tree produced by hexcalcParser#HexFloatNumber.
    def exitHexFloatNumber(self, ctx:hexcalcParser.HexFloatNumberContext):
        pass


    # Enter a parse tree produced by hexcalcParser#Variable.
    def enterVariable(self, ctx:hexcalcParser.VariableContext):
        pass

    # Exit a parse tree produced by hexcalcParser#Variable.
    def exitVariable(self, ctx:hexcalcParser.VariableContext):
        pass


    # Enter a parse tree produced by hexcalcParser#Mod.
    def enterMod(self, ctx:hexcalcParser.ModContext):
        pass

    # Exit a parse tree produced by hexcalcParser#Mod.
    def exitMod(self, ctx:hexcalcParser.ModContext):
        pass


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


    # Enter a parse tree produced by hexcalcParser#UnaryMinus.
    def enterUnaryMinus(self, ctx:hexcalcParser.UnaryMinusContext):
        pass

    # Exit a parse tree produced by hexcalcParser#UnaryMinus.
    def exitUnaryMinus(self, ctx:hexcalcParser.UnaryMinusContext):
        pass


    # Enter a parse tree produced by hexcalcParser#HexNumber.
    def enterHexNumber(self, ctx:hexcalcParser.HexNumberContext):
        pass

    # Exit a parse tree produced by hexcalcParser#HexNumber.
    def exitHexNumber(self, ctx:hexcalcParser.HexNumberContext):
        pass


    # Enter a parse tree produced by hexcalcParser#Power.
    def enterPower(self, ctx:hexcalcParser.PowerContext):
        pass

    # Exit a parse tree produced by hexcalcParser#Power.
    def exitPower(self, ctx:hexcalcParser.PowerContext):
        pass


    # Enter a parse tree produced by hexcalcParser#functionCall.
    def enterFunctionCall(self, ctx:hexcalcParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by hexcalcParser#functionCall.
    def exitFunctionCall(self, ctx:hexcalcParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by hexcalcParser#argList.
    def enterArgList(self, ctx:hexcalcParser.ArgListContext):
        pass

    # Exit a parse tree produced by hexcalcParser#argList.
    def exitArgList(self, ctx:hexcalcParser.ArgListContext):
        pass



del hexcalcParser