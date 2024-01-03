import os
import glob
import fnmatch

# Sanity check
NEMU_HOME = os.getenv('NEMU_HOME')
if not os.path.isfile(os.path.join(NEMU_HOME, 'src', 'nemu-main.c')):
    raise ValueError(f'NEMU_HOME={NEMU_HOME} is not a NEMU repo')

# Extract variables from menuconfig
# Assuming CONFIG_ISA and CONFIG_ENGINE are environment variables
GUEST_ISA = os.getenv('CONFIG_ISA', '').replace('"', '')
ENGINE = os.getenv('CONFIG_ENGINE', '').replace('"', '')
NAME = f'{GUEST_ISA}-nemu-{ENGINE}'

# Include all filelist.mk to merge file lists
# Python doesn't have a direct equivalent for Makefile's include directive

# Filter out directories and files in blacklist to obtain the final set of source files
DIRS_BLACKLIST = []  # Define your blacklist directories here
SRCS_BLACKLIST = []  # Define your blacklist source files here
SRCS_BLACKLIST += [os.path.join(root, name)
                   for dir in DIRS_BLACKLIST
                   for root, dirs, files in os.walk(dir)
                   for name in files
                   if name.endswith((".c"))]
SRCS = [os.path.join(root, name)
        for root, dirs, files in os.walk('./src')
        for name in files
        if name.endswith((".c")) and os.path.join(root, name) not in SRCS_BLACKLIST]

# Extract compiler and options from menuconfig
# Assuming CONFIG_CC, CONFIG_CC_OPT, CONFIG_CC_LTO, CONFIG_CC_DEBUG, CONFIG_CC_ASAN, CONFIG_ITRACE_COND are environment variables
CC = os.getenv('CONFIG_CC', '').replace('"', '')
CFLAGS_BUILD = os.getenv('CONFIG_CC_OPT', '').replace('"', '')
CFLAGS_BUILD += ' -flto' if os.getenv('CONFIG_CC_LTO') else ''
CFLAGS_BUILD += ' -Og -ggdb3' if os.getenv('CONFIG_CC_DEBUG') else ''
CFLAGS_BUILD += ' -fsanitize=address' if os.getenv('CONFIG_CC_ASAN') else ''
CFLAGS_TRACE = f'-DITRACE_COND={os.getenv("CONFIG_ITRACE_COND", "true").replace(\'"\', \'\')}'
CFLAGS = f'{CFLAGS_BUILD} {CFLAGS_TRACE} -D__GUEST_ISA__={GUEST_ISA}'
LDFLAGS = CFLAGS_BUILD

# Include rules for menuconfig
# Python doesn't have a direct equivalent for Makefile's include directive

# Conditional inclusion
if os.getenv('CONFIG_TARGET_AM'):
    # Include Makefile from AM_HOME
    # Python doesn't have a direct equivalent for Makefile's include directive
    LINKAGE = []  # Define your ARCHIVES here
else:
    # Include rules to build NEMU
    # Python doesn't have a direct equivalent for Makefile's include directive
    pass