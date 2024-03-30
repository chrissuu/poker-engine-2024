"""
Simple example pokerbot, written in Python.
"""

import random
from typing import Optional

from skeleton.actions import Action, CallAction, CheckAction, FoldAction, RaiseAction
from skeleton.states import GameState, TerminalState, RoundState
from skeleton.states import NUM_ROUNDS, STARTING_STACK, BIG_BLIND, SMALL_BLIND
from skeleton.bot import Bot
from skeleton.runner import parse_args, run_bot


x_1 = random.randrange(1,100) /100
x_2 = random.randrange(1,100) /100
x_3 = random.randrange(1,100) /100
x_4 = random.randrange(1,100) /100
x_5 = random.randrange(1,100) /100
x_6 = random.randrange(1,100) /100

def PREFLOP(PREFLOP_EQUITY_SCALE = 0.5, PREFLOP_RAISE_STANDARD = 0.3, PREFLOP_RAISE_SCALE = 1.5, PREFLOP_CALL_STANDARD = 0.3, PREFLOP_RAISED_AGAINST_SCALE = 1.4):
    return (
           PREFLOP_EQUITY_SCALE,
           PREFLOP_RAISE_STANDARD,
           PREFLOP_RAISE_SCALE,
           PREFLOP_CALL_STANDARD,
           PREFLOP_RAISED_AGAINST_SCALE

           )
    

rankings ={('1S', '2S'): 274572, ('1S', '3S'): 286452, ('1S', '4S'): 247184, ('1S', '5S'): 259990, ('1S', '6S'): 263334, ('1S', '7S'): 271906, ('1S', '8S'): 283796, ('1S', '9S'): 308424, ('1S', '1D'): 362120, ('1S', '2D'): 252386, ('1S', '3D'): 265958, ('1S', '4D'): 222122, ('1S', '5D'): 236252, ('1S', '6D'): 239648, ('1S', '7D'): 248600, ('1S', '8D'): 260870, ('1S', '9D'): 286850, ('1S', '1H'): 362120, ('1S', '2H'): 252386, ('1S', '3H'): 265958, ('1S', '4H'): 222122, ('1S', '5H'): 236252, ('1S', '6H'): 239648, ('1S', '7H'): 248600, ('1S', '8H'): 260870, ('1S', '9H'): 286850, ('2S', '1S'): 276528, ('2S', '3S'): 317244, ('2S', '4S'): 287258, ('2S', '5S'): 256718, ('2S', '6S'): 270744, ('2S', '7S'): 279036, ('2S', '8S'): 290366, ('2S', '9S'): 314154, ('2S', '1D'): 254464, ('2S', '2D'): 365300, ('2S', '3D'): 299654, ('2S', '4D'): 266816, ('2S', '5D'): 232604, ('2S', '6D'): 247910, ('2S', '7D'): 256550, ('2S', '8D'): 268196, ('2S', '9D'): 293240, ('2S', '1H'): 254464, ('2S', '2H'): 365300, ('2S', '3H'): 299654, ('2S', '4H'): 266816, ('2S', '5H'): 232604, ('2S', '6H'): 247910, ('2S', '7H'): 256550, ('2S', '8H'): 268196, ('2S', '9H'): 293240, ('3S', '1S'): 286472, ('3S', '2S'): 319192, ('3S', '4S'): 317406, ('3S', '5S'): 296524, ('3S', '6S'): 267746, ('3S', '7S'): 286160, ('3S', '8S'): 296930, ('3S', '9S'): 319878, ('3S', '1D'): 265978, ('3S', '2D'): 301732, ('3S', '3D'): 375443, ('3S', '4D'): 299843, ('3S', '5D'): 276986, ('3S', '6D'): 244556, ('3S', '7D'): 264482, ('3S', '8D'): 275504, ('3S', '9D'): 299612, ('3S', '1H'): 265978, ('3S', '2H'): 301732, ('3S', '3H'): 375443, ('3S', '4H'): 299843, ('3S', '5H'): 276986, ('3S', '6H'): 244556, ('3S', '7H'): 264482, ('3S', '8H'): 275504, ('3S', '9H'): 299612, ('4S', '1S'): 247204, ('4S', '2S'): 287278, ('4S', '3S'): 319345, ('4S', '5S'): 321770, ('4S', '6S'): 300796, ('4S', '7S'): 277438, ('4S', '8S'): 298330, ('4S', '9S'): 321558, ('4S', '1D'): 222142, ('4S', '2D'): 266836, ('4S', '3D'): 301921, ('4S', '4D'): 375158, ('4S', '5D'): 304631, ('4S', '6D'): 281414, ('4S', '7D'): 254756, ('4S', '8D'): 277064, ('4S', '9D'): 301484, ('4S', '1H'): 222142, ('4S', '2H'): 266836, ('4S', '3H'): 301921, ('4S', '4H'): 375158, ('4S', '5H'): 304631, ('4S', '6H'): 281414, ('4S', '7H'): 254756, ('4S', '8H'): 277064, ('4S', '9H'): 301484, ('5S', '1S'): 260010, ('5S', '2S'): 256738, ('5S', '3S'): 296544, ('5S', '4S'): 323697, ('5S', '6S'): 323880, ('5S', '7S'): 308546, ('5S', '8S'): 289258, ('5S', '9S'): 321488, ('5S', '1D'): 236272, ('5S', '2D'): 232624, ('5S', '3D'): 277006, ('5S', '4D'): 306709, ('5S', '5D'): 375218, ('5S', '6D'): 306761, ('5S', '7D'): 289448, ('5S', '8D'): 266948, ('5S', '9D'): 301406, ('5S', '1H'): 236272, ('5S', '2H'): 232624, ('5S', '3H'): 277006, ('5S', '4H'): 306709, ('5S', '5H'): 375218, ('5S', '6H'): 306761, ('5S', '7H'): 289448, ('5S', '8H'): 266948, ('5S', '9H'): 301406, ('6S', '1S'): 263354, ('6S', '2S'): 270764, ('6S', '3S'): 267766, ('6S', '4S'): 300816, ('6S', '5S'): 325793, ('6S', '7S'): 330620, ('6S', '8S'): 317724, ('6S', '9S'): 313606, ('6S', '1D'): 239668, ('6S', '2D'): 247930, ('6S', '3D'): 244576, ('6S', '4D'): 281434, ('6S', '5D'): 308839, ('6S', '6D'): 377552, ('6S', '7D'): 313793, ('6S', '8D'): 298694, ('6S', '9D'): 292616, ('6S', '1H'): 239668, ('6S', '2H'): 247930, ('6S', '3H'): 244576, ('6S', '4H'): 281434, ('6S', '5H'): 308839, ('6S', '6H'): 377552, ('6S', '7H'): 313793, ('6S', '8H'): 298694, ('6S', '9H'): 292616, ('7S', '1S'): 271926, ('7S', '2S'): 279056, ('7S', '3S'): 286180, ('7S', '4S'): 277458, ('7S', '5S'): 308566, ('7S', '6S'): 331629, ('7S', '8S'): 341402, ('7S', '9S'): 344608, ('7S', '1D'): 248620, ('7S', '2D'): 256570, ('7S', '3D'): 264502, ('7S', '4D'): 254776, ('7S', '5D'): 289468, ('7S', '6D'): 314881, ('7S', '7D'): 384170, ('7S', '8D'): 324995, ('7S', '9D'): 327194, ('7S', '1H'): 248620, ('7S', '2H'): 256570, ('7S', '3H'): 264502, ('7S', '4H'): 254776, ('7S', '5H'): 289468, ('7S', '6H'): 314881, ('7S', '7H'): 384170, ('7S', '8H'): 324995, ('7S', '9H'): 327194, ('8S', '1S'): 283816, ('8S', '2S'): 290386, ('8S', '3S'): 296950, ('8S', '4S'): 298350, ('8S', '5S'): 289278, ('8S', '6S'): 317744, ('8S', '7S'): 341423, ('8S', '9S'): 337182, ('8S', '1D'): 260890, ('8S', '2D'): 268216, ('8S', '3D'): 275524, ('8S', '4D'): 277084, ('8S', '5D'): 266968, ('8S', '6D'): 298714, ('8S', '7D'): 325015, ('8S', '8D'): 387242, ('8S', '9D'): 318899, ('8S', '1H'): 260890, ('8S', '2H'): 268216, ('8S', '3H'): 275524, ('8S', '4H'): 277084, ('8S', '5H'): 266968, ('8S', '6H'): 298714, ('8S', '7H'): 325015, ('8S', '8H'): 387242, ('8S', '9H'): 318899, ('9S', '1S'): 308444, ('9S', '2S'): 314174, ('9S', '3S'): 319898, ('9S', '4S'): 321578, ('9S', '5S'): 321508, ('9S', '6S'): 313626, ('9S', '7S'): 344628, ('9S', '8S'): 337203, ('9S', '1D'): 286870, ('9S', '2D'): 293260, ('9S', '3D'): 299632, ('9S', '4D'): 301504, ('9S', '5D'): 301426, ('9S', '6D'): 292636, ('9S', '7D'): 327214, ('9S', '8D'): 318919, ('9S', '9D'): 397127, ('9S', '1H'): 286870, ('9S', '2H'): 293260, ('9S', '3H'): 299632, ('9S', '4H'): 301504, ('9S', '5H'): 301426, ('9S', '6H'): 292636, ('9S', '7H'): 327214, ('9S', '8H'): 318919, ('9S', '9H'): 397127, ('1D', '1S'): 362120, ('1D', '2S'): 252386, ('1D', '3S'): 265958, ('1D', '4S'): 222122, ('1D', '5S'): 236252, ('1D', '6S'): 239648, ('1D', '7S'): 248600, ('1D', '8S'): 260870, ('1D', '9S'): 286850, ('1D', '2D'): 274572, ('1D', '3D'): 286452, ('1D', '4D'): 247184, ('1D', '5D'): 259990, ('1D', '6D'): 263334, ('1D', '7D'): 271906, ('1D', '8D'): 283796, ('1D', '9D'): 308424, ('1D', '1H'): 362120, ('1D', '2H'): 252386, ('1D', '3H'): 265958, ('1D', '4H'): 222122, ('1D', '5H'): 236252, ('1D', '6H'): 239648, ('1D', '7H'): 248600, ('1D', '8H'): 260870, ('1D', '9H'): 286850, ('2D', '1S'): 254464, ('2D', '2S'): 365300, ('2D', '3S'): 299654, ('2D', '4S'): 266816, ('2D', '5S'): 232604, ('2D', '6S'): 247910, ('2D', '7S'): 256550, ('2D', '8S'): 268196, ('2D', '9S'): 293240, ('2D', '1D'): 276528, ('2D', '3D'): 317244, ('2D', '4D'): 287258, ('2D', '5D'): 256718, ('2D', '6D'): 270744, ('2D', '7D'): 279036, ('2D', '8D'): 290366, ('2D', '9D'): 314154, ('2D', '1H'): 254464, ('2D', '2H'): 365300, ('2D', '3H'): 299654, ('2D', '4H'): 266816, ('2D', '5H'): 232604, ('2D', '6H'): 247910, ('2D', '7H'): 256550, ('2D', '8H'): 268196, ('2D', '9H'): 293240, ('3D', '1S'): 265978, ('3D', '2S'): 301732, ('3D', '3S'): 375443, ('3D', '4S'): 299843, ('3D', '5S'): 276986, ('3D', '6S'): 244556, ('3D', '7S'): 264482, ('3D', '8S'): 275504, ('3D', '9S'): 299612, ('3D', '1D'): 286472, ('3D', '2D'): 319192, ('3D', '4D'): 317406, ('3D', '5D'): 296524, ('3D', '6D'): 267746, ('3D', '7D'): 286160, ('3D', '8D'): 296930, ('3D', '9D'): 319878, ('3D', '1H'): 265978, ('3D', '2H'): 301732, ('3D', '3H'): 375443, ('3D', '4H'): 299843, ('3D', '5H'): 276986, ('3D', '6H'): 244556, ('3D', '7H'): 264482, ('3D', '8H'): 275504, ('3D', '9H'): 299612, ('4D', '1S'): 222142, ('4D', '2S'): 266836, ('4D', '3S'): 301921, ('4D', '4S'): 375158, ('4D', '5S'): 304631, ('4D', '6S'): 281414, ('4D', '7S'): 254756, ('4D', '8S'): 277064, ('4D', '9S'): 301484, ('4D', '1D'): 247204, ('4D', '2D'): 287278, ('4D', '3D'): 319345, ('4D', '5D'): 321770, ('4D', '6D'): 300796, ('4D', '7D'): 277438, ('4D', '8D'): 298330, ('4D', '9D'): 321558, ('4D', '1H'): 222142, ('4D', '2H'): 266836, ('4D', '3H'): 301921, ('4D', '4H'): 375158, ('4D', '5H'): 304631, ('4D', '6H'): 281414, ('4D', '7H'): 254756, ('4D', '8H'): 277064, ('4D', '9H'): 301484, ('5D', '1S'): 236272, ('5D', '2S'): 232624, ('5D', '3S'): 277006, ('5D', '4S'): 306709, ('5D', '5S'): 375218, ('5D', '6S'): 306761, ('5D', '7S'): 289448, ('5D', '8S'): 266948, ('5D', '9S'): 301406, ('5D', '1D'): 260010, ('5D', '2D'): 256738, ('5D', '3D'): 296544, ('5D', '4D'): 323697, ('5D', '6D'): 323880, ('5D', '7D'): 308546, ('5D', '8D'): 289258, ('5D', '9D'): 321488, ('5D', '1H'): 236272, ('5D', '2H'): 232624, ('5D', '3H'): 277006, ('5D', '4H'): 306709, ('5D', '5H'): 375218, ('5D', '6H'): 306761, ('5D', '7H'): 289448, ('5D', '8H'): 266948, ('5D', '9H'): 301406, ('6D', '1S'): 239668, ('6D', '2S'): 247930, ('6D', '3S'): 244576, ('6D', '4S'): 281434, ('6D', '5S'): 308839, ('6D', '6S'): 377552, ('6D', '7S'): 313793, ('6D', '8S'): 298694, ('6D', '9S'): 292616, ('6D', '1D'): 263354, ('6D', '2D'): 270764, ('6D', '3D'): 267766, ('6D', '4D'): 300816, ('6D', '5D'): 325793, ('6D', '7D'): 330620, ('6D', '8D'): 317724, ('6D', '9D'): 313606, ('6D', '1H'): 239668, ('6D', '2H'): 247930, ('6D', '3H'): 244576, ('6D', '4H'): 281434, ('6D', '5H'): 308839, ('6D', '6H'): 377552, ('6D', '7H'): 313793, ('6D', '8H'): 298694, ('6D', '9H'): 292616, ('7D', '1S'): 248620, ('7D', '2S'): 256570, ('7D', '3S'): 264502, ('7D', '4S'): 254776, ('7D', '5S'): 289468, ('7D', '6S'): 314881, ('7D', '7S'): 384170, ('7D', '8S'): 324995, ('7D', '9S'): 327194, ('7D', '1D'): 271926, ('7D', '2D'): 279056, ('7D', '3D'): 286180, ('7D', '4D'): 277458, ('7D', '5D'): 308566, ('7D', '6D'): 331629, ('7D', '8D'): 341402, ('7D', '9D'): 344608, ('7D', '1H'): 248620, ('7D', '2H'): 256570, ('7D', '3H'): 264502, ('7D', '4H'): 254776, ('7D', '5H'): 289468, ('7D', '6H'): 314881, ('7D', '7H'): 384170, ('7D', '8H'): 324995, ('7D', '9H'): 327194, ('8D', '1S'): 260890, ('8D', '2S'): 268216, ('8D', '3S'): 275524, ('8D', '4S'): 277084, ('8D', '5S'): 266968, ('8D', '6S'): 298714, ('8D', '7S'): 325015, ('8D', '8S'): 387242, ('8D', '9S'): 318899, ('8D', '1D'): 283816, ('8D', '2D'): 290386, ('8D', '3D'): 296950, ('8D', '4D'): 298350, ('8D', '5D'): 289278, ('8D', '6D'): 317744, ('8D', '7D'): 341423, ('8D', '9D'): 337182, ('8D', '1H'): 260890, ('8D', '2H'): 268216, ('8D', '3H'): 275524, ('8D', '4H'): 277084, ('8D', '5H'): 266968, ('8D', '6H'): 298714, ('8D', '7H'): 325015, ('8D', '8H'): 387242, ('8D', '9H'): 318899, ('9D', '1S'): 286870, ('9D', '2S'): 293260, ('9D', '3S'): 299632, ('9D', '4S'): 301504, ('9D', '5S'): 301426, ('9D', '6S'): 292636, ('9D', '7S'): 327214, ('9D', '8S'): 318919, ('9D', '9S'): 397127, ('9D', '1D'): 308444, ('9D', '2D'): 314174, ('9D', '3D'): 319898, ('9D', '4D'): 321578, ('9D', '5D'): 321508, ('9D', '6D'): 313626, ('9D', '7D'): 344628, ('9D', '8D'): 337203, ('9D', '1H'): 286870, ('9D', '2H'): 293260, ('9D', '3H'): 299632, ('9D', '4H'): 301504, ('9D', '5H'): 301426, ('9D', '6H'): 292636, ('9D', '7H'): 327214, ('9D', '8H'): 318919, ('9D', '9H'): 397127, ('1H', '1S'): 362120, ('1H', '2S'): 252386, ('1H', '3S'): 265958, ('1H', '4S'): 222122, ('1H', '5S'): 236252, ('1H', '6S'): 239648, ('1H', '7S'): 248600, ('1H', '8S'): 260870, ('1H', '9S'): 286850, ('1H', '1D'): 362120, ('1H', '2D'): 252386, ('1H', '3D'): 265958, ('1H', '4D'): 222122, ('1H', '5D'): 236252, ('1H', '6D'): 239648, ('1H', '7D'): 248600, ('1H', '8D'): 260870, ('1H', '9D'): 286850, ('1H', '2H'): 274572, ('1H', '3H'): 286452, ('1H', '4H'): 247184, ('1H', '5H'): 259990, ('1H', '6H'): 263334, ('1H', '7H'): 271906, ('1H', '8H'): 283796, ('1H', '9H'): 308424, ('2H', '1S'): 254464, ('2H', '2S'): 365300, ('2H', '3S'): 299654, ('2H', '4S'): 266816, ('2H', '5S'): 232604, ('2H', '6S'): 247910, ('2H', '7S'): 256550, ('2H', '8S'): 268196, ('2H', '9S'): 293240, ('2H', '1D'): 254464, ('2H', '2D'): 365300, ('2H', '3D'): 299654, ('2H', '4D'): 266816, ('2H', '5D'): 232604, ('2H', '6D'): 247910, ('2H', '7D'): 256550, ('2H', '8D'): 268196, ('2H', '9D'): 293240, ('2H', '1H'): 276528, ('2H', '3H'): 317244, ('2H', '4H'): 287258, ('2H', '5H'): 256718, ('2H', '6H'): 270744, ('2H', '7H'): 279036, ('2H', '8H'): 290366, ('2H', '9H'): 314154, ('3H', '1S'): 265978, ('3H', '2S'): 301732, ('3H', '3S'): 375443, ('3H', '4S'): 299843, ('3H', '5S'): 276986, ('3H', '6S'): 244556, ('3H', '7S'): 264482, ('3H', '8S'): 275504, ('3H', '9S'): 299612, ('3H', '1D'): 265978, ('3H', '2D'): 301732, ('3H', '3D'): 375443, ('3H', '4D'): 299843, ('3H', '5D'): 276986, ('3H', '6D'): 244556, ('3H', '7D'): 264482, ('3H', '8D'): 275504, ('3H', '9D'): 299612, ('3H', '1H'): 286472, ('3H', '2H'): 319192, ('3H', '4H'): 317406, ('3H', '5H'): 296524, ('3H', '6H'): 267746, ('3H', '7H'): 286160, ('3H', '8H'): 296930, ('3H', '9H'): 319878, ('4H', '1S'): 222142, ('4H', '2S'): 266836, ('4H', '3S'): 301921, ('4H', '4S'): 375158, ('4H', '5S'): 304631, ('4H', '6S'): 281414, ('4H', '7S'): 254756, ('4H', '8S'): 277064, ('4H', '9S'): 301484, ('4H', '1D'): 222142, ('4H', '2D'): 266836, ('4H', '3D'): 301921, ('4H', '4D'): 375158, ('4H', '5D'): 304631, ('4H', '6D'): 281414, ('4H', '7D'): 254756, ('4H', '8D'): 277064, ('4H', '9D'): 301484, ('4H', '1H'): 247204, ('4H', '2H'): 287278, ('4H', '3H'): 319345, ('4H', '5H'): 321770, ('4H', '6H'): 300796, ('4H', '7H'): 277438, ('4H', '8H'): 298330, ('4H', '9H'): 321558, ('5H', '1S'): 236272, ('5H', '2S'): 232624, ('5H', '3S'): 277006, ('5H', '4S'): 306709, ('5H', '5S'): 375218, ('5H', '6S'): 306761, ('5H', '7S'): 289448, ('5H', '8S'): 266948, ('5H', '9S'): 301406, ('5H', '1D'): 236272, ('5H', '2D'): 232624, ('5H', '3D'): 277006, ('5H', '4D'): 306709, ('5H', '5D'): 375218, ('5H', '6D'): 306761, ('5H', '7D'): 289448, ('5H', '8D'): 266948, ('5H', '9D'): 301406, ('5H', '1H'): 260010, ('5H', '2H'): 256738, ('5H', '3H'): 296544, ('5H', '4H'): 323697, ('5H', '6H'): 323880, ('5H', '7H'): 308546, ('5H', '8H'): 289258, ('5H', '9H'): 321488, ('6H', '1S'): 239668, ('6H', '2S'): 247930, ('6H', '3S'): 244576, ('6H', '4S'): 281434, ('6H', '5S'): 308839, ('6H', '6S'): 377552, ('6H', '7S'): 313793, ('6H', '8S'): 298694, ('6H', '9S'): 292616, ('6H', '1D'): 239668, ('6H', '2D'): 247930, ('6H', '3D'): 244576, ('6H', '4D'): 281434, ('6H', '5D'): 308839, ('6H', '6D'): 377552, ('6H', '7D'): 313793, ('6H', '8D'): 298694, ('6H', '9D'): 292616, ('6H', '1H'): 263354, ('6H', '2H'): 270764, ('6H', '3H'): 267766, ('6H', '4H'): 300816, ('6H', '5H'): 325793, ('6H', '7H'): 330620, ('6H', '8H'): 317724, ('6H', '9H'): 313606, ('7H', '1S'): 248620, ('7H', '2S'): 256570, ('7H', '3S'): 264502, ('7H', '4S'): 254776, ('7H', '5S'): 289468, ('7H', '6S'): 314881, ('7H', '7S'): 384170, ('7H', '8S'): 324995, ('7H', '9S'): 327194, ('7H', '1D'): 248620, ('7H', '2D'): 256570, ('7H', '3D'): 264502, ('7H', '4D'): 254776, ('7H', '5D'): 289468, ('7H', '6D'): 314881, ('7H', '7D'): 384170, ('7H', '8D'): 324995, ('7H', '9D'): 327194, ('7H', '1H'): 271926, ('7H', '2H'): 279056, ('7H', '3H'): 286180, ('7H', '4H'): 277458, ('7H', '5H'): 308566, ('7H', '6H'): 331629, ('7H', '8H'): 341402, ('7H', '9H'): 344608, ('8H', '1S'): 260890, ('8H', '2S'): 268216, ('8H', '3S'): 275524, ('8H', '4S'): 277084, ('8H', '5S'): 266968, ('8H', '6S'): 298714, ('8H', '7S'): 325015, ('8H', '8S'): 387242, ('8H', '9S'): 318899, ('8H', '1D'): 260890, ('8H', '2D'): 268216, ('8H', '3D'): 275524, ('8H', '4D'): 277084, ('8H', '5D'): 266968, ('8H', '6D'): 298714, ('8H', '7D'): 325015, ('8H', '8D'): 387242, ('8H', '9D'): 318899, ('8H', '1H'): 283816, ('8H', '2H'): 290386, ('8H', '3H'): 296950, ('8H', '4H'): 298350, ('8H', '5H'): 289278, ('8H', '6H'): 317744, ('8H', '7H'): 341423, ('8H', '9H'): 337182, ('9H', '1S'): 286870, ('9H', '2S'): 293260, ('9H', '3S'): 299632, ('9H', '4S'): 301504, ('9H', '5S'): 301426, ('9H', '6S'): 292636, ('9H', '7S'): 327214, ('9H', '8S'): 318919, ('9H', '9S'): 397127, ('9H', '1D'): 286870, ('9H', '2D'): 293260, ('9H', '3D'): 299632, ('9H', '4D'): 301504, ('9H', '5D'): 301426, ('9H', '6D'): 292636, ('9H', '7D'): 327214, ('9H', '8D'): 318919, ('9H', '9D'): 397127, ('9H', '1H'): 308444, ('9H', '2H'): 314174, ('9H', '3H'): 319898, ('9H', '4H'): 321578, ('9H', '5H'): 321508, ('9H', '6H'): 313626, ('9H', '7H'): 344628, ('9H', '8H'): 337203}
deck = []
for suit in range(3):
    for num in range(1, 10):
        if suit == 0:
            card = str(num) + 's'
            deck.append(card)
        elif suit == 1:
            card = str(num) + 'd'
            deck.append(card)
        elif suit == 2:
            card = str(num) + 'h'
            deck.append(card)

possibleHands = []
for i in range(len(deck)):
    for j in range(len(deck) - i):
        possibleHands.append((deck[i], deck[j+i]))

def findPossibleHands(flopCard, hand):
    for hand in possibleHands:
        if flopCard in possibleHands or hand[0] in possibleHands or hand[1] in possibleHands:
            possibleHands.remove(hand)

            
def num_pairs(hand):
    values = set()
    for i in range(len(hand)):
        values.add(hand[i][0])
    if len(values) == 3:
        return 1
    if is_trips == False and len(values) == 2:
        return 2
    return 0

def high_card_value(hand):
    values = set()
    for i in range(len(hand)):
        values.add(hand[i][0])
    return int(max(values))

def is_straight_flush(hand):
    return is_4flush(hand) and is_4straight(hand)

def is_4flush(hand):
    value = True
    for i in range(len(hand)-1):
        x = hand[i]
        #print(hand)
        if x[1] != hand[i+1][1]:
            value = False
    return value

def is_4straight(hand):
    value = True
    for i in range(len(hand)-1):
        if int(hand[i][0]) != int(hand[i+1][0]) - 1:
            value = False
    return value

def is_3straight(hand):
    hand.sort()
    if int(hand[0][0]) == int(hand[1][0])-1 and int(hand[1][0]) == int(hand[2][0]) -1:
        return True
    elif int(hand[1][0]) == int(hand[2][0])-1 and int(hand[2][0]) == int(hand[3][0]) -1:
        return True
    else:
        return False

def find_straight(hand):
    hand.sort()
    if int(hand[0][0]) == int(hand[1][0])-1 and int(hand[1][0]) == int(hand[2][0]) -1:
        return[hand[0][0], hand[1][0], hand[2][0]]
    elif int(hand[1][0]) == int(hand[2][0])-1 and int(hand[2][0]) == int(hand[3][0]) -1:
        return[hand[1][0], hand[2][0], hand[3][0]]
    
def is_trips(hand):
    values = set()
    for i in range(len(hand)):
        values.add(hand[i][0])
    if len(values) == 2:
        return True
    else:
        return False

def frequent_card_value(hand):
    map = {}
    for i in hand:
        if i in map.keys():
            map[i] +=1
        else:
            map[i] = 1
    curr_max = 0
    max = 0
    for key in map.keys():
        if map[key] > curr_max:
            max = key
    return int(max[0])
    
    
def is_pair(hand):
    return num_pairs(hand) == 1

def is_two_pair(hand):
    return num_pairs(hand) == 2

def evaluate(hand, board):
    combined_hand = []
    #print('HAND', hand)
    combined_hand.extend(list(hand))
    combined_hand.extend(list(board))
    #print('COMBINED HAND', combined_hand)
    if is_straight_flush(combined_hand):
        return 80000 + high_card_value(combined_hand)
    elif is_trips(combined_hand):
        return 70000 + frequent_card_value(combined_hand)
    elif is_two_pair(combined_hand):
        return 60000 + high_card_value(combined_hand)
    elif is_4flush(combined_hand):
        return 50000 + high_card_value(combined_hand)
    elif is_4straight(combined_hand):
        return 40000 + high_card_value(combined_hand)
    elif is_3straight(combined_hand):
        return 30000 + high_card_value(find_straight(combined_hand))
    elif is_pair(combined_hand):
        return 20000 + frequent_card_value(combined_hand)
    else:
        return 10000 + high_card_value(combined_hand)

def playGame(hand, enemyHand, board):
    x = evaluate(hand, board)
    y = evaluate(enemyHand, board)
    if x >= y:
        return 1
    else:
        return 0

equity = {}
for key in rankings:
    equity[key] = (rankings[key]/(702*701)) 

def preFlopEquity(hand):
    return equity[(hand)]

# Returns our odds out of 1 of winning the hand 
def postFlopEquity(flopCard, player1Hand):
    player1Score = 0
    enemyScore = 0
    for hand in possibleHands:
        if notIn(flopCard, hand) and notIn(hand[0], player1Hand) and notIn(hand[1], player1Hand) and notIn(flopCard, player1Hand):
            for secondCard in deck:
                if secondCard != flopCard and secondCard != hand[0] and secondCard != hand[1]:
                    x = playGame(player1Hand, hand, (flopCard, secondCard))
                    if x == 1:
                        player1Score += 1
                    else:
                        enemyScore += 1
    
    return player1Score/(player1Score+enemyScore)

def notIn(card, hand):
    if card != hand[0] and card != hand[1]:
        return True
    else:
        return False

# Returns 1 if we win or tie and 0 if they're gonna win
def postRiverEquity(hand, board):
    enemyWins = 0
    count = 0
    for enemyHand in possibleHands:
        count += 1
        if notIn(hand[0], board) and notIn(hand[1], board):
            if playGame(hand, enemyHand, board) == 0:
                enemyWins += 1
    return 1- (enemyWins/count)

class Player(Bot):
    """
    A pokerbot. 
    """

    def __init__(self) -> None:
        """
        Called when a new game starts. Called exactly once.

        Arguments:
        Nothing.

        Returns:
        Nothing.
        """
        self.log = []
        pass

    def handle_new_round(self, game_state: GameState, round_state: RoundState, active: int) -> None:
        """
        Called when a new round starts. Called NUM_ROUNDS times.
        
        Args:
            game_state (GameState): The state of the game.
            round_state (RoundState): The state of the round.
            active (int): Your player's index.

        Returns:
            None
        """
        #my_bankroll = game_state.bankroll # the total number of chips you've gained or lost from the beginning of the game to the start of this round
        #game_clock = game_state.game_clock # the total number of seconds your bot has left to play this game
        #round_num = game_state.round_num # the round number from 1 to NUM_ROUNDS
        #my_cards = round_state.hands[0] # your cards
        #big_blind = bool(active) # True if you are the big blind
        self.log = []
        self.log.append("================================")
        self.log.append("new round")
        pass

    def handle_round_over(self, game_state: GameState, terminal_state: TerminalState, active: int, is_match_over: bool) -> Optional[str]:
        """
        Called when a round ends. Called NUM_ROUNDS times.

        Args:
            game_state (GameState): The state of the game.
            terminal_state (TerminalState): The state of the round when it ended.
            active (int): Your player's index.

        Returns:
            Your logs.
        """
        #my_delta = terminal_state.deltas[active] # your bankroll change from this round
        #previous_state = terminal_state.previous_state # RoundState before payoffs
        #street = previous_state.street # 0, 3, 4, or 5 representing when this round ended
        #my_cards = previous_state.hands[0] # your cards
        #opp_cards = previous_state.hands[1] # opponent's cards or [] if not revealed
        self.log.append("game over")
        self.log.append("================================\n")

        return self.log
    





    def equity_needed_against_bet(self, betsize, potsize):
        #so far pre-flop
        if (betsize / potsize) <= 0.25:
            return 0.16
        elif 0.25 < (betsize / potsize) <= 0.33:
            return 0.2
        elif 0.33 < (betsize / potsize) <= 0.5:
            return 0.25
        elif 0.5 < (betsize / potsize) <= 0.66:
            return 0.28
        elif 0.66 < (betsize / potsize) <= 0.75:
            return 0.3
        elif 0.75 < (betsize / potsize) <= 1:
            return 0.33
        elif 1 < (betsize / potsize) <= 2:
            return 0.4
        elif 2 < (betsize / potsize):
            return 0.45
    # def bet_size(int equity_difference):
    #     if equity_difference < 0.5:
        
    
    def bet_or_nah(self, observation: dict):
        my_hand = observation["my_cards"]
        my_cards = (my_hand[0], my_hand[1])
        potsize = 400 - (observation["my_stack"] + observation["op_stack"])
        button = False
        
        # PREFLOP_EQUITY_SCALE,PREFLOP_RAISE_STANDARD,PREFLOP_RAISE_SCALE,PREFLOP_CALL_STANDARD,PREFLOP_RAISE_STANDARD,PREFLOP_RAISED_AGAINST_SCALE = PREFLOP(x_1,x_2,x_3,x_4,x_5,x_6)
        PREFLOP_EQUITY_SCALE,PREFLOP_RAISE_STANDARD,PREFLOP_RAISE_SCALE,PREFLOP_CALL_STANDARD,PREFLOP_RAISE_STANDARD,PREFLOP_RAISED_AGAINST_SCALE = PREFLOP()

        if observation["street"] == 0:
            equity = preFlopEquity(my_cards) * PREFLOP_EQUITY_SCALE #0.5
            if observation["opp_pip"] - observation["my_pip"] > 0: #There is a bet against you
                bet_size = observation["opp_pip"] - observation["my_pip"]
                if bet_size == 1: #you are small blind first action
                    button = True
                    #you can either call or raise
                    if equity > PREFLOP_RAISE_STANDARD: #0.3, given some equity is it high enough to raise?
                        if potsize * PREFLOP_RAISE_SCALE > observation["max_raise"]:
                            return (observation["max_raise"], False)
                        else: return (int(potsize * PREFLOP_RAISE_SCALE), False) #how much do you scale potsize by?
                    else: #call as small blind
                        return (bet_size, True)
                else: # enemy raised as small blind (you are big blind)
                    #you can either call/re-raise/fold
                    if equity - self.equity_needed_against_bet(bet_size, potsize-bet_size) < 0: #we have less equity than the price (the price to pay is more than our equity)
                        difference = abs(equity - self.equity_needed_against_bet(bet_size, potsize-bet_size))
                        if difference < 0.08: #PREFLOP_BLUFFING_STANDARD if the margin we are down equity by is less than 8%
                            x = random.randrage(1, 101)
                            if x > 10: #90 percent of the times we will opt to fold
                                return (-1, False)
                            else: #10 percent of the times we will raise bluff
                                if (observation["min_raise"] * PREFLOP_RAISED_AGAINST_SCALE > observation["max_raise"]):
                                    return ((observation["max_raise"]), False)
                                return ((observation["min_raise"] * PREFLOP_RAISED_AGAINST_SCALE), False) #3 betting nearly 3x the raise, 1.4
                        return (-1, False) #we are now folding the hands when our equity deficit is less than 8%
                    else: #we do not have less equity (can either call or re-raise)
                        difference = equity - self.equity_needed_against_bet(bet_size, potsize-bet_size)
                        if difference < PREFLOP_CALL_STANDARD: #WE OPT TO CALL, how much risk are you willing to take relative to your opp equity, 0.3
                            return (bet_size, True) #this can be exploitable ***TENTATIVE*** (we are calling if our equity is only like 0.05 higher needed to proceed)
                        else: # WE OPT TO RE-RAISE
                            if difference > PREFLOP_RAISE_STANDARD: #equity difference is high 10%, how much are you confident relative to opp equity, 0.1
                                if (observation["min_raise"] * PREFLOP_RAISED_AGAINST_SCALE > observation["max_raise"]):
                                    return ((observation["max_raise"]), False)
                                return ((observation["min_raise"] * PREFLOP_RAISED_AGAINST_SCALE), False) #3 betting nearly 3x the raise, 1.4
                            else:
                                return ((observation["min_raise"] * 1), False)
                        

                    pot_odds
                    #calculate your equity. 
            elif observation["opp_pip"] - observation["my_pip"] == 0: #you can either check or raise:
                if equity > 0.3:
                    return (int(potsize*PREFLOP_RAISE_SCALE), False)
                else:
                    return (0, False)
            else: # There is no bet against you. you can either check  #YOU ARE BIG BLIND
                if equity > 0.3: #if you have at least 30% equity
                    return (int(potsize*0.7), False)
                else: #checking
                    return (0, False);

            ###### you only have the option to check on preflop if you are big blind on first action
            # if observation["opp_pip"] - observation["my_pip"] == 0: #little blind called over to you on first action
            #     if equity > 0.3: #if you have at least 30% equity
            #         return (potsize*2, false) #raise 2* the pot
            #     else: #if have less than 20% equity
            #         return (0, true) #check
            # 
        if observation["street"] == 1: #FLOP
            
            equity = postFlopEquity(my_cards) * 0.5
            if observation["opp_pip"] - observation["my_pip"] > 0: #enemy raised you
                bet_size = observation["opp_pip"] - observation["my_pip"]
                if equity - self.equity_needed_against_bet(bet_size, potsize-bet_size) < 0: #we have less equity than the price (the price to pay is more than our equity)
                        difference = abs(equity - self.equity_needed_against_bet(bet_size, potsize-bet_size))
                        if difference < 0.05: #PREFLOP_BLUFFING_STANDARD if the margin we are down equity by is less than 5%
                            x = random.randrage(1, 101)
                            if x > 15: #90 percent of the times we will opt to fold
                                return (-1, False)
                            else: #85 percent of the times we will raise bluff
                                if (observation["min_raise"] * PREFLOP_RAISED_AGAINST_SCALE > observation["max_raise"]):
                                    return ((observation["max_raise"]), False)
                                return ((observation["min_raise"] * PREFLOP_RAISED_AGAINST_SCALE), False) #3 betting nearly 3x the raise, 1.4
                        return (-1, False) #we are now folding the hands when our equity deficit is less than 8%
                        # return (-1, False) #this can be exploitable ***TENTATIVE*** (WE FOLD TOO MUCH)
                else: #we do not have less equity (can either call or re-raise)
                    difference = equity - self.equity_needed_against_bet(bet_size, potsize-bet_size)
                    if difference < 0.05: #WE OPT TO CALL
                        return (bet_size, True) #this can be exploitable ***TENTATIVE*** (we are calling if our equity is only like 0.05 higher needed to proceed)
                    else: # WE OPT TO RE-RAISE
                        if difference > PREFLOP_RAISE_STANDARD: #equity difference is high 10%, how much are you confident relative to opp equity, 0.1
                            if (observation["min_raise"] * PREFLOP_RAISED_AGAINST_SCALE > observation["max_raise"]):
                                return ((observation["max_raise"]), False)
                            return ((observation["min_raise"] * PREFLOP_RAISED_AGAINST_SCALE), False) #equity difference is high 10% 3x bet
                        else:
                            return ((observation["min_raise"] * 1), False)
            else: #no bet against you you can either check or raise.
                if equity > 0.3: #if you have at least 30% equity
                    if not button:
                        x = random.randrange(1, 101)
                        if x < 30: #30 percent of hands when we are out of position and we have high equity, we will raise on first action
                            if (observation["min_raise"] * PREFLOP_RAISED_AGAINST_SCALE > observation["max_raise"]):
                                return ((observation["max_raise"]), False)
                            return (int(potsize * 0.7), False)
                        else:
                            return(0, False)
                    else: # if we have position and equity advantage
                        x = random.randrange(1, 101)
                        if equity > 0.42: #AFTER FLOP WE HAVE VERY HIGH EQUITY AND WE HAVE POSITION
                            if 1 < x < 20: #20 percent of the time we check to trap
                                return(0, False)
                            elif 20 <= x < 50: # 70 percent of the time we make a value bet
                                if (observation["min_raise"] * PREFLOP_RAISED_AGAINST_SCALE > observation["max_raise"]):
                                    return ((observation["max_raise"]), False)
                                return (int(potsize * 0.5), False)
                            else: #50 percent of the time in position, we all in with the best hand
                                return (observation["max_raise"], False)
                        else: #our equity is between 30% and 42 
                            if 1 < x < 15: #20 percent of the time we check to trap
                                return(0, False)
                            elif 15 <= x < 85: # 70 percent of the time we make a value bet
                                if (observation["min_raise"] * PREFLOP_RAISED_AGAINST_SCALE > observation["max_raise"]):
                                    return ((observation["max_raise"]), False)
                                return (int(potsize * 0.7), False)
                            else: #15 percent of the time in position, we all in with the best hand
                                return (observation["max_raise"], False)
                            
                else:
                    x = random.randrange(1, 101)
                    if equity > 0.2:
                        if 1 < x < 60: #20 percent of the time we check
                            return(0, False)
                        elif 60 <= x < 97: # 37 percent of the time we make a stab
                            if (observation["min_raise"] * PREFLOP_RAISED_AGAINST_SCALE > observation["max_raise"]):
                                return ((observation["max_raise"]), False)
                            return (int(potsize * 0.5), False)
                        else: #<4 percent of the time in position, we all in with a meh ass hand
                            return (observation["max_raise"], False)
                    else:
                        return(0, False)


        #RIVER
        if observation["street"] == 2:
            equity = postRiverEquity(my_cards) * 0.5
            if observation["opp_pip"] - observation["my_pip"] > 0: #enemy raised you
                bet_size = observation["opp_pip"] - observation["my_pip"]
                if equity - self.equity_needed_against_bet(bet_size, potsize-bet_size) < 0: #we have less equity than the price (the price to pay is more than our equity)
                        difference = abs(equity - self.equity_needed_against_bet(bet_size, potsize-bet_size))
                        if difference < 0.05: #PREFLOP_BLUFFING_STANDARD if the margin we are down equity by is less than 5%
                            x = random.randrage(1, 101)
                            if x > 15: #90 percent of the times we will opt to fold
                                return (-1, False)
                            else: #85 percent of the times we will raise bluff
                                if (observation["min_raise"] * PREFLOP_RAISED_AGAINST_SCALE > observation["max_raise"]):
                                    return ((observation["max_raise"]), False)
                                return ((observation["min_raise"] * PREFLOP_RAISED_AGAINST_SCALE), False) #3 betting nearly 3x the raise, 1.4
                        return (-1, False) #we are now folding the hands when our equity deficit is less than 8%
                        # return (-1, False) #this can be exploitable ***TENTATIVE*** (WE FOLD TOO MUCH)
                else: #we do not have less equity (can either call or re-raise)
                    difference = equity - self.equity_needed_against_bet(bet_size, potsize-bet_size)
                    if difference < 0.05: #WE OPT TO CALL
                        return (bet_size, True) #this can be exploitable ***TENTATIVE*** (we are calling if our equity is only like 0.05 higher needed to proceed)
                    else: # WE OPT TO RE-RAISE
                        if difference > PREFLOP_RAISE_STANDARD: #equity difference is high 10%, how much are you confident relative to opp equity, 0.1
                            if (observation["min_raise"] * PREFLOP_RAISED_AGAINST_SCALE > observation["max_raise"]):
                                return ((observation["max_raise"]), False)
                            return ((observation["min_raise"] * PREFLOP_RAISED_AGAINST_SCALE), False) #equity difference is high 10% 3x bet
                        else:
                            return ((observation["min_raise"] * 1), False)
            else: #no bet against you you can either check or raise.
                if equity > 0.3: #if you have at least 30% equity
                    if not button:
                        x = random.randrange(1, 101)
                        if x < 30: #30 percent of hands when we are out of position and we have high equity, we will raise on first action
                            if (observation["min_raise"] * PREFLOP_RAISED_AGAINST_SCALE > observation["max_raise"]):
                                return ((observation["max_raise"]), False)
                            return (int(potsize * 0.7), False)
                        else:
                            return(0, False)
                    else: # if we have position and equity advantage
                        x = random.randrange(1, 101)
                        if equity > 0.42: #AFTER FLOP WE HAVE VERY HIGH EQUITY AND WE HAVE POSITION
                            if 1 < x < 20: #20 percent of the time we check to trap
                                return(0, False)
                            elif 20 <= x < 50: # 70 percent of the time we make a value bet
                                if (observation["min_raise"] * PREFLOP_RAISED_AGAINST_SCALE > observation["max_raise"]):
                                    return ((observation["max_raise"]), False)
                                return (int(potsize * 0.5), False)
                            else: #50 percent of the time in position, we all in with the best hand
                                return (observation["max_raise"], False)
                        else: #our equity is between 30% and 42 
                            if 1 < x < 15: #20 percent of the time we check to trap
                                return(0, False)
                            elif 15 <= x < 85: # 70 percent of the time we make a value bet
                                if (observation["min_raise"] * PREFLOP_RAISED_AGAINST_SCALE > observation["max_raise"]):
                                    return ((observation["max_raise"]), False)
                                return (int(potsize * 0.7), False)
                            else: #15 percent of the time in position, we all in with the best hand
                                return (observation["max_raise"], False)
                            
                else:
                    x = random.randrange(1, 101)
                    if equity > 0.2:
                        if 1 < x < 60: #20 percent of the time we check
                            return(0, False)
                        elif 60 <= x < 97: # 37 percent of the time we make a stab
                            if (observation["min_raise"] * PREFLOP_RAISED_AGAINST_SCALE > observation["max_raise"]):
                                return ((observation["max_raise"]), False)
                            return (int(potsize * 0.5), False)
                        else: #<4 percent of the time in position, we all in with a meh ass hand
                            return (observation["max_raise"], False)
                    else:
                        return(0, False)

    def get_action(self, observation: dict) -> Action:
        
        """
        Where the magic happens - your code should implement this function.
        Called any time the engine needs an action from your bot.

        Args:
            observation (dict): The observation of the current state.
            {
                "legal_actions": List of the Actions that are legal to take.
                "street": 0, 1, or 2 representing pre-flop, flop, or river respectively
                "my_cards": List[str] of your cards, e.g. ["1s", "2h"]
                "board_cards": List[str] of the cards on the board
                "my_pip": int, the number of chips you have contributed to the pot this round of betting
                "opp_pip": int, the number of chips your opponent has contributed to the pot this round of betting
                "my_stack": int, the number of chips you have remaining
                "opp_stack": int, the number of chips your opponent has remaining
                "my_bankroll": int, the number of chips you have won or lost from the beginning of the game to the start of this round
                "min_raise": int, the smallest number of chips for a legal bet/raise
                "max_raise": int, the largest number of chips for a legal bet/raise
            }

        Returns:
            Action: The action you want to take.
        """
        my_contribution = STARTING_STACK - observation["my_stack"] # the number of chips you have contributed to the pot
        opp_contribution = STARTING_STACK - observation["opp_stack"] # the number of chips your opponent has contributed to the pot
        continue_cost = observation["opp_pip"] - observation["my_pip"] # the number of chips needed to stay in the pot

        self.log.append("My cards: " + str(observation["my_cards"]))
        self.log.append("Board cards: " + str(observation["board_cards"]))
        self.log.append("My stack: " + str(observation["my_stack"]))
        self.log.append("My contribution: " + str(my_contribution))
        self.log.append("My bankroll: " + str(observation["my_bankroll"]))
        

        bool_bet, call = self.bet_or_nah(observation)
        
        if bool_bet > 0 and not call:
            return RaiseAction(bool_bet)
        
        if bool_bet > 0 and call:
            return CallAction()
        
        if bool_bet == 0 and not call:
            return CheckAction() 
       
        return FoldAction()

if __name__ == '__main__':
    run_bot(Player(), parse_args())




def call_check_bot(obs):
    # Call if possible, otherwise check
    if obs["legal_actions"][1] == 1:
        return (1,0)
    elif obs["legal_actions"][2] == 1:
        return (2,0)
    else:
        return (0,0)

def raise_bot(obs):
    # Raise if possible, otherwise call or check
    if obs["legal_actions"][3] == 1:
        min_raise = int(obs["min_raise"][0])
        max_raise = int(obs["max_raise"][0])
        return (3,max_raise)
    else:
        return call_check_bot(obs)
    
def random_bot(obs):
    # Randomly choose a legal action
    action_probs = np.random.rand(4)
    action_probs = action_probs * obs["legal_actions"]
    action = np.argmax(action_probs)
    if action == 3:
        min_raise = obs["min_raise"][0]
        max_raise = obs["max_raise"][0]
        raise_amount = np.random.randint(min_raise, max_raise+1)
        return (action, raise_amount)
    else:
        return (action, 0)
    
def fold_bot(obs):
    if obs["legal_actions"][0] == 1:
        return (0,0)
    else:
        return call_check_bot(obs)

num_to_action = {0: "Fold", 1: "Call", 2: "Check", 3: "Raise"}

def player_bot(obs):
    Player.get_action(obs)

# # Two player mode
# env = PokerEnv(1000)
# (obs1, obs2), info = env.reset()
# bot1, bot2 = random_bot, random_bot
# print("\n"+"*"*50 + " Two player " + "*"*50)
# print(obs1)
# print(obs2)

# done = False
# while not done:
#     if obs1["is_my_turn"]:
#         action = bot1(obs1)
#         print(f"Bot1: {num_to_action[action[0]]} {action[1]}")
#     else:
#         action = bot2(obs2)
#         print(f"Bot2: {num_to_action[action[0]]} {action[1]}")
    
#     print("\n")
#     (obs1, obs2), (reward1, reward2), done, trunc, info = env.step(action)
#     if reward1 != 0:
#         print("New Round")
#     print(obs1, reward1, done)
#     print(obs2, reward2, done)


# Single player mode