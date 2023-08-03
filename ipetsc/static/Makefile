# https://stackoverflow.com/questions/22925380/how-to-display-the-value-of-all-the-variables-in-makefile
include ${PETSC_PREFIX}/lib/petsc/conf/rules
include ${PETSC_PREFIX}/lib/petsc/conf/variables

$(foreach var, $(.VARIABLES), $(info $(var)=$($(var))))
