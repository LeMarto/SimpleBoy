from . import ld_ops
from . import misc_ops
from . import add_ops
from . import sub_ops
from . import inc_ops

inst = []
inst_cb = []

for code in range(0xFF):
    inst.append(None)
    inst_cb.append(None)

ld_ops.fill(inst)
misc_ops.fill(inst)
add_ops.fill(inst)
sub_ops.fill(inst)
inc_ops.fill(inst)