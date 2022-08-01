# Simple tests for an adder module
import cocotb
from cocotb.triggers import Timer
import random

@cocotb.test()
async def my_design_tb(dut):

    X = 5
    Y = 10

    # input driving
    dut.x.value = X
    dut.y.value = Y

    await Timer(2, units='ns')
    
    assert dut.out.value == X*Y, "Multiplier result is incorrect: {X} * {Y} != {OUT}, expected value={E}".format( X=int(dut.x.value), Y=int(dut.y.value), OUT=int(dut.out.value), E=X*Y)
