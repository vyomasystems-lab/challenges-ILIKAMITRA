# See LICENSE.vyoma for details

# SPDX-License-Identifier: CC0-1.0

import os
import random
from pathlib import Path

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge
def seq_detected(input_1):
    exp=[]
    det = [i for i in range(len(input_1)) if input_1.startswith('1011', i)]
    detected_places=[i+len('1011')-1 for i in det]
    exp=[0 for i in range(len(input_1))]
    #print(detected_places)
    for i in detected_places:
            exp[i]=1
    return exp
@cocotb.test()
async def test_seq_bug1(dut):
    """Test for seq detection """

    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock

    # reset
    dut.reset.value = 1
    await FallingEdge(dut.clk)  
    dut.reset.value = 0
    await FallingEdge(dut.clk)

    cocotb.log.info('#### CTB: Develop your test here! ######')
    input_1='101011'
    ex=seq_detected(input_1)
    inp_arr= [int(i) for i in list(input_1)]
    output =[]
    for i in range(len(inp_arr)):
        dut.inp_bit.value= inp_arr[i]
        await FallingEdge(dut.clk)
        output.append(dut.seq_seen.value)
    print("Dut ", output)
    print("exp ", ex)
    assert output== ex, "ERROR IN DETECTING expected {e} but got output as {d}".format(e=ex, d=output)