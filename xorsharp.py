#! /usr/bin/python3
import sys

def xorvba():
    key=sys.argv[2]
    array=sys.argv[1]
    array=array.replace("\n","");
    array=array.replace("(","");
    array=array.replace(")","");
    array=array.replace(" ","");
    array=array.replace("_","_,");

    output="buf =  Array("
    count=0;
    for i in array.split(",")[3:]:
        if i !="_":
            value=int(i,10) ^ int("bd",16);
            output=output+str(value)+", "
        else:
            output=output+"_\n"

        count=count+1;


    print("Counter: ",count)
    print("Key: ",key)

    print("Key: ",int(key,16))
    output=output[:-2]
    output+=" )"

    print(output)

def xorcsharp():

    key=sys.argv[2]
    array=sys.argv[1]
    array=array.replace("\n","");
    array=array.replace("{","");
    array=array.replace("}","");
    array=array.replace(" ",",");

    output="{ "
    count=0;
    for i in array.split(",")[5:]:
        if "0x" in i:
            i=i.replace("0x","")
            value=int(i,16) ^ int("bd",16);
            output=output+hex(value)+", "
            count=count+1;

    print("Counter: ",count)
    print("Key: ",key)
    output=output[:-2]
    output+=" }"

    print(output)



if len(sys.argv)!=3:
    print("[*] Execute: python3 xorchap.py array[] 0xkey ")
    sys.exit(-1);


key=sys.argv[2]
array=sys.argv[1]

if 'byte[]' in array:
    xorcsharp();

if 'Array(' in array:
    xorvba();
