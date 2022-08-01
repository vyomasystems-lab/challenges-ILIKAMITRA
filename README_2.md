# challenges-ILIKAMITRA
challenges-ILIKAMITRA created by GitHub Classroom
# challenge_2 level1_design2:

The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives inputs to the Design Under Test (adder module here) which takes in inputs as the *reset* pin, *clk* pin and the input sequence from *inp_bit*

## Test Scenario_1**(Important)**
- Test Inputs: inp_bit= '1011011'
- Expected Output: output=[0,0,0,1,0,0,1]
- Observed Output in the DUT =[0,0,0,1,0,0,0]

The values are assigned to the input port using 
```
    input_1='1011011'
    inp_arr= [int(i) for i in list(input_1)]
    output =[0]
    for i in range(len(inp_arr)):
        dut.inp_bit.value= inp_arr[i]
        await FallingEdge(dut.clk)
        output.append(dut.seq_seen.value)
```


The assert statement is used for comparing the mux output to the expected value.
![image](https://user-images.githubusercontent.com/53615130/182167442-b2b8e9c6-03f5-48b4-bd53-00ce94cd522f.png)
The following error is seen:
```
        assert output== ex, "ERROR IN DETECTING expected {e} but got output as {d}".format(e=ex, d=output)

                     AssertionError: ERROR IN DETECTING expected [0, 0, 0, 1, 0, 0, 1] but got output as [0, 0, 0, 0, 1, 0, 0, 0] 
```

Output mismatches for the above inputs proving that there is a design bug


### Design Bug
Based on the above test input and analysing the design, we see the following
![image](https://user-images.githubusercontent.com/53615130/182168305-81dad8b5-ffac-44de-b22e-e88f6c99325e.png)

For the SEQUENCE DETECTOR design, the logic should be for that after detecting a sequence, ``SEQ_1011`` if it detects a 0 , it should move itself to `` SEQ_10``

### Design Fix
Updating the design and re-running the test makes the test pass.
![image](https://user-images.githubusercontent.com/53615130/182169740-543f088d-79f1-4432-a1e3-0e3fce97d026.png)
![image](https://user-images.githubusercontent.com/53615130/182171517-58be0176-6645-42a5-a790-be648e287942.png)

## Test Scenario_2**(Important)**
- Test Inputs: inp_bit= '10111011'
- Expected Output: output=[0,0,0,1,0,0,0,1]
- Observed Output in the DUT =[0,0,0,1,0,0,0,0]

The values are assigned to the input port using 
```
    input_1='10111011'
    inp_arr= [int(i) for i in list(input_1)]
    output =[]
    for i in range(len(inp_arr)):
        dut.inp_bit.value= inp_arr[i]
        await FallingEdge(dut.clk)
        output.append(dut.seq_seen.value)
```


The assert statement is used for comparing the mux output to the expected value.
![image](https://user-images.githubusercontent.com/53615130/182167442-b2b8e9c6-03f5-48b4-bd53-00ce94cd522f.png)
The following error is seen:
```
        assert output== ex, "ERROR IN DETECTING expected {e} but got output as {d}".format(e=ex, d=output)

                     AssertionError: ERROR IN DETECTING expected [0, 0, 0, 1, 0, 0, 0, 1] but got output as [0, 0, 0, 0, 1, 0, 0, 0,0] 
```

Output mismatches for the above inputs proving that there is a design bug


### Design Bug
Based on the above test input and analysing the design, we see the following
![image](https://user-images.githubusercontent.com/53615130/182169740-543f088d-79f1-4432-a1e3-0e3fce97d026.png)

For the SEQUENCE DETECTOR design, the logic should be for that after detecting a sequence, ``SEQ_1011`` if it detects a 1 , it should move itself to `` SEQ_1``

### Design Fix
![image](https://user-images.githubusercontent.com/53615130/182173985-6d54ce34-bfe6-4c18-bf90-ef29fdbc0924.png)

Updating the design and re-running the test makes the test pass.
![image](https://user-images.githubusercontent.com/53615130/182173911-d5cb3a6d-bedc-451b-809f-ccf8b2d80f9e.png)

## Test Scenario_3**(Important)**
- Test Inputs: inp_bit= '11011'
- Expected Output: output=[0,0,0,0,1]
- Observed Output in the DUT =[0,0,0,0,0]

The values are assigned to the input port using 
```
    input_1='11011'
    inp_arr= [int(i) for i in list(input_1)]
    output =[]
    for i in range(len(inp_arr)):
        dut.inp_bit.value= inp_arr[i]
        await FallingEdge(dut.clk)
        output.append(dut.seq_seen.value)
```


The assert statement is used for comparing the mux output to the expected value.
![image](https://user-images.githubusercontent.com/53615130/182175081-7e5777e2-094b-4032-bda8-e3498249cb50.png)

The following error is seen:
```
        assert output== ex, "ERROR IN DETECTING expected {e} but got output as {d}".format(e=ex, d=output)

                     AssertionError: ERROR IN DETECTING expected [0, 0, 0, 0, 1] but got output as [0, 0, 0, 0, 0] 
```

Output mismatches for the above inputs proving that there is a design bug


### Design Bug
Based on the above test input and analysing the design, we see the following
![image](https://user-images.githubusercontent.com/53615130/182175306-1a8c8cca-4afe-449e-ad59-708138f17cde.png)


For the SEQUENCE DETECTOR design, the logic should be for that after detecting a sequence, ``SEQ_1`` if it detects a 1 , it should move itself to `` SEQ_1`` not ``IDLE``

### Design Fix
![image](https://user-images.githubusercontent.com/53615130/182175609-7ee2e0b5-8d87-4dc9-b58e-7788ecffa045.png)


Updating the design and re-running the test makes the test pass.
![image](https://user-images.githubusercontent.com/53615130/182175672-9bd11145-ac65-4e6f-bf1b-2ceb3007f29b.png)

## Test Scenario_4**(Important)**
- Test Inputs: inp_bit= '101011'
- Expected Output: output=[0,0,0,0,0,1]
- Observed Output in the DUT =[0,0,0,0,0,0]

The values are assigned to the input port using 
```
    input_1='101011'
    inp_arr= [int(i) for i in list(input_1)]
    output =[]
    for i in range(len(inp_arr)):
        dut.inp_bit.value= inp_arr[i]
        await FallingEdge(dut.clk)
        output.append(dut.seq_seen.value)
```


The assert statement is used for comparing the mux output to the expected value.
![image](https://user-images.githubusercontent.com/53615130/182176618-6ab591a7-6f61-414d-973c-cf93da377f47.png)


The following error is seen:
```
        assert output== ex, "ERROR IN DETECTING expected {e} but got output as {d}".format(e=ex, d=output)

                     AssertionError: ERROR IN DETECTING expected [0, 0, 0, 0, 0, 1] but got output as [0, 0, 0, 0, 0, 0] 
```

Output mismatches for the above inputs proving that there is a design bug


### Design Bug
Based on the above test input and analysing the design, we see the following
![image](https://user-images.githubusercontent.com/53615130/182177007-1fb8abfc-2040-4f53-b96e-278289f9fa64.png)


For the SEQUENCE DETECTOR design, the logic should be for that after detecting a sequence, ``SEQ_101`` if it detects a 0 , it should move itself to `` SEQ_10`` not ``IDLE``

### Design Fix
![image](https://user-images.githubusercontent.com/53615130/182177213-fdaf563e-feab-4285-a0bd-ae67ada3041d.png)



Updating the design and re-running the test makes the test pass.
![image](https://user-images.githubusercontent.com/53615130/182177333-03c233a2-3c07-46de-882d-bcab079c966f.png)


