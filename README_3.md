 # challenges-ILIKAMITRA
challenges-ILIKAMITRA created by GitHub Classroom
![image](https://user-images.githubusercontent.com/53615130/182180356-c1844483-78b0-4ae4-b00c-85d6687c4781.png)
# challenge_2 level1_design2:

The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives inputs to the Design Under Test which takes in 3 32 bit input signals for a operation namely *mav_putvalue_src1*, *mav_putvalue_src2*, *mav_putvalue_src3*, and there is another input of 32 bit, namely *mav_putvalue_instr*, which corrosponds to which operation is to be perdormed with the given inputs
## Test Scenario_1**(Important)**
- Test Inputs: mav_putvalue_src1 = 0, mav_putvalue_src2 = 0, mav_putvalue_src3 = 1, mav_putvalue_instr = 0x101010B3
- Expected Output: output= 0x0
- Observed Output in the DUT = 0x2

The values are assigned to the input port using
```
    for i in range (2**8):
        for j in range (2**8):
            for k in range (2**8):
                mav_putvalue_src1 = i
                mav_putvalue_src2 = j
                mav_putvalue_src3 = k
                mav_putvalue_instr = 0x101010B3
```
The assert statement is used for comparing the mux output to the expected value.
![image](https://user-images.githubusercontent.com/53615130/182183131-4d849568-3010-448d-9ea7-e5c602424160.png)
The following error is seen:
```
                          assert dut_output == expected_mav_putvalue, error_message
                     AssertionError: Value mismatch DUT = 0x2 does not match MODEL = 0x0 
```

Output mismatches for the above inputs proving that there is a design bug


### Design Bug
### Design Fix
