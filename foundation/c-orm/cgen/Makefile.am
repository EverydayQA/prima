if HAVE_DOXYGEN
SUBDIRS = docs
endif

env: env/bin/activate

env/bin/activate: requirements.txt
	test -d env || pyvenv-3.4 env
	env/bin/pip install -Ur requirements.txt
	touch env/bin/activate

all: env
build: env
check: env
