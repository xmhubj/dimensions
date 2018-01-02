#### Check the CPU info:
- Any CPU with the same physical ID are threads or cores in the same physical socket.
- Any CPU with the same core ID are hyper-threads in the same core.
```
> cat /proc/cpuinfo |grep "physical id" |sore |uniq |wc -l
```

#### Check the mem info:
- Available Memory = free + buffers + cached
```
> free -m
```

#### Check the disk info:

```
> fdisk -l
> df -h

# check disk I/O performance
# iostat [ options ] [ <interval> [ <count> ] ]
# %util ~= 100%, %idle < 70%
# vmstat, 
# r(displays the total number of processes waiting for access to the processor), 
# b(displays the total number of processes in a “sleep” state),
# wa(the amount of time that the processor spends waiting for IO operations to complete)
> iostat -x 1 10
```

#### Check load average:
```
# system load averages for the past 1, 5, and 15 minutes
# vmstat, r > 3/4, id < 50%, busy
> uptime
> w
> top
```

#### Show the status of modules in the Linux Kernel
```
# formats the contents of the /proc/modules
> lsmod
```

#### List all PCI devices:
```
> lspci
```

#### 

