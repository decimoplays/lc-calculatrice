# Generated from hexcalc.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,14,66,2,0,7,0,2,1,7,1,2,2,7,2,1,0,4,0,8,8,0,11,0,12,0,9,1,0,
        1,0,1,1,1,1,1,1,1,1,3,1,18,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,
        2,1,2,1,2,5,2,31,8,2,10,2,12,2,34,9,2,1,2,1,2,1,2,1,2,1,2,1,2,1,
        2,1,2,1,2,1,2,1,2,3,2,47,8,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,5,2,61,8,2,10,2,12,2,64,9,2,1,2,0,1,4,3,0,2,4,0,2,1,
        0,7,8,2,0,5,5,10,10,75,0,7,1,0,0,0,2,17,1,0,0,0,4,46,1,0,0,0,6,8,
        3,2,1,0,7,6,1,0,0,0,8,9,1,0,0,0,9,7,1,0,0,0,9,10,1,0,0,0,10,11,1,
        0,0,0,11,12,5,0,0,1,12,1,1,0,0,0,13,14,5,11,0,0,14,15,5,1,0,0,15,
        18,3,4,2,0,16,18,3,4,2,0,17,13,1,0,0,0,17,16,1,0,0,0,18,3,1,0,0,
        0,19,20,6,2,-1,0,20,21,5,11,0,0,21,22,5,2,0,0,22,23,3,4,2,0,23,24,
        5,3,0,0,24,47,1,0,0,0,25,26,5,11,0,0,26,27,5,2,0,0,27,32,3,4,2,0,
        28,29,5,4,0,0,29,31,3,4,2,0,30,28,1,0,0,0,31,34,1,0,0,0,32,30,1,
        0,0,0,32,33,1,0,0,0,33,35,1,0,0,0,34,32,1,0,0,0,35,36,5,3,0,0,36,
        47,1,0,0,0,37,38,5,5,0,0,38,47,3,4,2,9,39,40,5,2,0,0,40,41,3,4,2,
        0,41,42,5,3,0,0,42,47,1,0,0,0,43,47,5,12,0,0,44,47,5,11,0,0,45,47,
        5,13,0,0,46,19,1,0,0,0,46,25,1,0,0,0,46,37,1,0,0,0,46,39,1,0,0,0,
        46,43,1,0,0,0,46,44,1,0,0,0,46,45,1,0,0,0,47,62,1,0,0,0,48,49,10,
        8,0,0,49,50,5,6,0,0,50,61,3,4,2,9,51,52,10,7,0,0,52,53,7,0,0,0,53,
        61,3,4,2,8,54,55,10,6,0,0,55,56,5,9,0,0,56,61,3,4,2,7,57,58,10,5,
        0,0,58,59,7,1,0,0,59,61,3,4,2,6,60,48,1,0,0,0,60,51,1,0,0,0,60,54,
        1,0,0,0,60,57,1,0,0,0,61,64,1,0,0,0,62,60,1,0,0,0,62,63,1,0,0,0,
        63,5,1,0,0,0,64,62,1,0,0,0,6,9,17,32,46,60,62
    ]

class hexcalcParser ( Parser ):

    grammarFileName = "hexcalc.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'('", "')'", "','", "'-'", "'^'", 
                     "'*'", "'/'", "'%'", "'+'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "ID", "HEXFLOAT", 
                      "HEX", "WS" ]

    RULE_prog = 0
    RULE_statement = 1
    RULE_expression = 2

    ruleNames =  [ "prog", "statement", "expression" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    ID=11
    HEXFLOAT=12
    HEX=13
    WS=14

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(hexcalcParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(hexcalcParser.StatementContext)
            else:
                return self.getTypedRuleContext(hexcalcParser.StatementContext,i)


        def getRuleIndex(self):
            return hexcalcParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = hexcalcParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 7 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 6
                self.statement()
                self.state = 9 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 14372) != 0)):
                    break

            self.state = 11
            self.match(hexcalcParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return hexcalcParser.RULE_statement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ExprContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a hexcalcParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(hexcalcParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)


    class AssignContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a hexcalcParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(hexcalcParser.ID, 0)
        def expression(self):
            return self.getTypedRuleContext(hexcalcParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign" ):
                listener.enterAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign" ):
                listener.exitAssign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign" ):
                return visitor.visitAssign(self)
            else:
                return visitor.visitChildren(self)



    def statement(self):

        localctx = hexcalcParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 17
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                localctx = hexcalcParser.AssignContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 13
                self.match(hexcalcParser.ID)
                self.state = 14
                self.match(hexcalcParser.T__0)
                self.state = 15
                self.expression(0)
                pass

            elif la_ == 2:
                localctx = hexcalcParser.ExprContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 16
                self.expression(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return hexcalcParser.RULE_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class HexFloatNumberContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a hexcalcParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def HEXFLOAT(self):
            return self.getToken(hexcalcParser.HEXFLOAT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHexFloatNumber" ):
                listener.enterHexFloatNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHexFloatNumber" ):
                listener.exitHexFloatNumber(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHexFloatNumber" ):
                return visitor.visitHexFloatNumber(self)
            else:
                return visitor.visitChildren(self)


    class VariableContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a hexcalcParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(hexcalcParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable" ):
                listener.enterVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable" ):
                listener.exitVariable(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable" ):
                return visitor.visitVariable(self)
            else:
                return visitor.visitChildren(self)


    class ModContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a hexcalcParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(hexcalcParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(hexcalcParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMod" ):
                listener.enterMod(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMod" ):
                listener.exitMod(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMod" ):
                return visitor.visitMod(self)
            else:
                return visitor.visitChildren(self)


    class MulDivContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a hexcalcParser.ExpressionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(hexcalcParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(hexcalcParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulDiv" ):
                listener.enterMulDiv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulDiv" ):
                listener.exitMulDiv(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulDiv" ):
                return visitor.visitMulDiv(self)
            else:
                return visitor.visitChildren(self)


    class AddSubContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a hexcalcParser.ExpressionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(hexcalcParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(hexcalcParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddSub" ):
                listener.enterAddSub(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddSub" ):
                listener.exitAddSub(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddSub" ):
                return visitor.visitAddSub(self)
            else:
                return visitor.visitChildren(self)


    class ParensContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a hexcalcParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(hexcalcParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParens" ):
                listener.enterParens(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParens" ):
                listener.exitParens(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParens" ):
                return visitor.visitParens(self)
            else:
                return visitor.visitChildren(self)


    class UnaryMinusContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a hexcalcParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(hexcalcParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryMinus" ):
                listener.enterUnaryMinus(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryMinus" ):
                listener.exitUnaryMinus(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryMinus" ):
                return visitor.visitUnaryMinus(self)
            else:
                return visitor.visitChildren(self)


    class ExpLnContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a hexcalcParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(hexcalcParser.ID, 0)
        def expression(self):
            return self.getTypedRuleContext(hexcalcParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpLn" ):
                listener.enterExpLn(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpLn" ):
                listener.exitExpLn(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpLn" ):
                return visitor.visitExpLn(self)
            else:
                return visitor.visitChildren(self)


    class HexNumberContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a hexcalcParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def HEX(self):
            return self.getToken(hexcalcParser.HEX, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHexNumber" ):
                listener.enterHexNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHexNumber" ):
                listener.exitHexNumber(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHexNumber" ):
                return visitor.visitHexNumber(self)
            else:
                return visitor.visitChildren(self)


    class MinMaxContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a hexcalcParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(hexcalcParser.ID, 0)
        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(hexcalcParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(hexcalcParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMinMax" ):
                listener.enterMinMax(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMinMax" ):
                listener.exitMinMax(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMinMax" ):
                return visitor.visitMinMax(self)
            else:
                return visitor.visitChildren(self)


    class PowerContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a hexcalcParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(hexcalcParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(hexcalcParser.ExpressionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPower" ):
                listener.enterPower(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPower" ):
                listener.exitPower(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPower" ):
                return visitor.visitPower(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = hexcalcParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                localctx = hexcalcParser.ExpLnContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 20
                self.match(hexcalcParser.ID)
                self.state = 21
                self.match(hexcalcParser.T__1)
                self.state = 22
                self.expression(0)
                self.state = 23
                self.match(hexcalcParser.T__2)
                pass

            elif la_ == 2:
                localctx = hexcalcParser.MinMaxContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 25
                self.match(hexcalcParser.ID)
                self.state = 26
                self.match(hexcalcParser.T__1)
                self.state = 27
                self.expression(0)
                self.state = 32
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==4:
                    self.state = 28
                    self.match(hexcalcParser.T__3)
                    self.state = 29
                    self.expression(0)
                    self.state = 34
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 35
                self.match(hexcalcParser.T__2)
                pass

            elif la_ == 3:
                localctx = hexcalcParser.UnaryMinusContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 37
                self.match(hexcalcParser.T__4)
                self.state = 38
                self.expression(9)
                pass

            elif la_ == 4:
                localctx = hexcalcParser.ParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 39
                self.match(hexcalcParser.T__1)
                self.state = 40
                self.expression(0)
                self.state = 41
                self.match(hexcalcParser.T__2)
                pass

            elif la_ == 5:
                localctx = hexcalcParser.HexFloatNumberContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 43
                self.match(hexcalcParser.HEXFLOAT)
                pass

            elif la_ == 6:
                localctx = hexcalcParser.VariableContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 44
                self.match(hexcalcParser.ID)
                pass

            elif la_ == 7:
                localctx = hexcalcParser.HexNumberContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 45
                self.match(hexcalcParser.HEX)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 62
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 60
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        localctx = hexcalcParser.PowerContext(self, hexcalcParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 48
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 49
                        self.match(hexcalcParser.T__5)
                        self.state = 50
                        self.expression(9)
                        pass

                    elif la_ == 2:
                        localctx = hexcalcParser.MulDivContext(self, hexcalcParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 51
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 52
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==7 or _la==8):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 53
                        self.expression(8)
                        pass

                    elif la_ == 3:
                        localctx = hexcalcParser.ModContext(self, hexcalcParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 54
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 55
                        self.match(hexcalcParser.T__8)
                        self.state = 56
                        self.expression(7)
                        pass

                    elif la_ == 4:
                        localctx = hexcalcParser.AddSubContext(self, hexcalcParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 57
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 58
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==5 or _la==10):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 59
                        self.expression(6)
                        pass

             
                self.state = 64
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 5)
         




