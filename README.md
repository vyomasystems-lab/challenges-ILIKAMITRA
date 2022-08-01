# challenges-ILIKAMITRA
challenges-ILIKAMITRA created by GitHub Classroom
# challenge_1 level1_design1:

The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives inputs to the Design Under Test (adder module here) which takes in inputs *sel* of 5-bit  and 30 *inp* lines of 2-bit and gives 2-bit output based on the value of the select line

## Test Scenario_1**(Important)**
- Test Inputs: sel = 12, inp12 = 01
- Expected Output: output=01
- Observed Output in the DUT dut.output.value=00

The values are assigned to the input port using 
```
dut.sel.value = 12
dut.inp12.value= 1 
```

The assert statement is used for comparing the mux output to the expected value.
![image](https://user-images.githubusercontent.com/53615130/182140177-ed9533fd-a070-49e1-b50e-e0abd6077404.png)
The following error is seen:
```
assert dut.out.value ==  i , "mux result is incorrect: {sl} should select {exp} not {W}".format(sl=int(dut.sel.value), exp=i, W=str(dut.out.value))
                     AssertionError: mux result is incorrect : inp12 should select 01 not 00 
```

Output mismatches for the above inputs proving that there is a design bug


### Design Bug
Based on the above test input and analysing the design, we see the following
![image](https://user-images.githubusercontent.com/53615130/182140327-7bdbb22d-3fef-47b6-b092-3f61a50cf894.png)


For the mux design, the logic should be for a 5 bit input of sel ``5'b01100: out = inp12; `` instead of ``5'b01101: out = inp12;`` as in the design code.

### Design Fix
Updating the design and re-running the test makes the test pass.

![image](https://user-images.githubusercontent.com/53615130/182145389-1fe6e949-3eee-4493-bafb-bfe1d86f02b6.png)



## Test Scenario_2**(Important)**
- Test Inputs: sel = 30, inp30 = 01
- Expected Output: output=01
- Observed Output in the DUT dut.output.value=00

The values are assigned to the input port using 
```
dut.sel.value = 30
dut.inp30.value= 01 
```

The assert statement is used for comparing the mux output to the expected value.
![image](https://user-images.githubusercontent.com/53615130/182146396-b74369fc-47fc-4312-b793-a2d7925ea9b6.png)

The following error is seen:
```
assert dut.out.value ==  i , "mux result is incorrect: {sl} should select {exp} not {W}".format(sl=int(dut.sel.value), exp=i, W=str(dut.out.value))
                     AssertionError: mux result is incorrect : inp30 should select 01 not 00 
```

Output mismatches for the above inputs proving that there is a design bug


### Design Bug
Based on the above test input and analysing the design, we see the following
![image](https://user-images.githubusercontent.com/53615130/182146468-65fecc75-6c75-49a6-8cbb-be6abe305836.png)


For the mux design, the logic should be for a 5 bit input of sel ``5'b01100: out = inp12; `` instead of ``5'b01101: out = inp12;`` as in the design code.

### Design Fix
Updating the design and re-running the test makes the test pass.
![image](https://user-images.githubusercontent.com/53615130/182146526-67aa4679-e239-4cef-8368-e68a63b13217.png)


The updated design is updated in the file mux.v










