from . import memory_ops
from . import misc_ops
from . import add_ops

inst = []
inst_cb = []

for code in range(0xFF):
    inst.append(None)
    inst_cb.append(None)

memory_ops.fill(inst)
misc_ops.fill(inst)
add_ops.fill(inst)