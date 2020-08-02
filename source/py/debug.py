import llvmlite.binding
import os
import platform

print("Platform Architecture: "+str(platform.architecture()))
print("Machine Type: "+str(platform.machine()))
print("Network Node: "+str(platform.node()))
print("Platform Identifier: "+str(platform.platform()))
print("Platform CPU: "+str(platform.processor()))
print("Python Implementation: "+str(platform.python_implementation()))
print("Python Compiler: "+str(platform.python_compiler()))
print("Python Version: "+str(platform.python_version_tuple()))
print("Python Build: "+str(platform.python_build()))
print("Platform Release: "+str(platform.release()))
print("System Name: "+str(platform.system()))
print("System Details: "+str(platform.system_alias(platform.system(), platform.release(), platform.version())))
print("OS Name: "+str(os.name))
print("Username: "+str(os.getlogin()))
print("")
print("LLVM Version: "+str(llvmlite.binding.llvm_version_info))
print("Default Triple: "+llvmlite.binding.get_default_triple())
print("Process Triple: "+llvmlite.binding.get_process_triple())
print("Object Format: "+llvmlite.binding.get_object_format())
print("Host CPU Name: "+llvmlite.binding.get_host_cpu_name())

if llvmlite.binding.check_jit_execution() == None:
    print("JIT can be executed: Yes")
else:
    raise RuntimeError

#print("Host CPU Features: \n"+str(llvmlite.binding.get_host_cpu_features()))
print("Global Context: "+str(llvmlite.binding.get_global_context()))
