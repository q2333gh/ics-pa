TODO
build commands for nemu in vscode to correctly hint in code editor.

TODO 
make gdb into vscode to show DDD of debuggerr ?
maybe STFW

使用工具也是编程的一部分:
1. git
2. build systems
3. shell
基本原则:任何感到不爽的时候,一定有一个工具能帮你.
如果真没有,自己造一个的机会就来了.
    不太可能是真的.
    但可能是一份非常好的研究工作



# build process explain:
不论多么复杂的makefile: 本质是从下至上构建一个程序
![Alt text](./pictures/image.png)
即把.c -> .o  然后层次 link 他们为一个程序.


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
-D :define a macro **during the compilation process.** So sometimes in vscode cant see some macro.
-lreadline :  linker flag that instructs the linker to link the readline library with the program. 
-ldl : ink the dl (dynamic loading)

-wall  :if int a= 0; but never use . give warning. why warning: because other .c file may clash .
-werror :force above give error compile err.  


## phylosophy: Doc as code :现代的文档方式,使用Doxygen自动生成Makefile的文档.
goto AM home and `make html`
like python doc . llvm doc.** doc gen by source code .**


# CONFIDENCE SKILL :如何阅读一个可能1000个文件的中型项目? very useful and important
##  如果是一个程序:
start from main:
    如何找到main?
        用IDE的搜索功能.
            alt+3 main
如何在大量代码中找到关键逻辑? 其余的函数只是辅助构造.            
## 如果是一个库:




