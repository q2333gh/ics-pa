TODO
build commands for nemu in vscode to correctly hint in code editor.

TODO 
make gdb into vscode to show DDD of debuggerr ?
maybe STFW



# build process explain:
不论多么复杂的makefile: 本质是从下至上构建一个程序
![Alt text](./pictures/image.png)

cmd to check build histroy in detail : 
approach :  

man make :essence here in this proj: 
-B  强制无条件构建所有.
-n  不执行脚本,只是打印
make -nB

**格式化处理和过滤整个make日志**
make clean && make -nB  &> make_verbose.log
![Alt text](./pictures/image2.png)
`vim -`  - 表示从stdout读入 ( - unix shell一般语法)
```bash
 make clean && make -nB \
     | grep -ve '^\(\#\|echo\|mkdir\|mv\)' \
     &> make_gcc.log
```
过滤掉带有echo和 mkdir 的输出行


man gcc essence:
-D 

