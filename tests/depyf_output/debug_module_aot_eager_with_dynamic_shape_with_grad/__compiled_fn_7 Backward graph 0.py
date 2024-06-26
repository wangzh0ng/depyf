from __future__ import annotations



def forward(self, primals_1: "Sym(s0)", primals_2: "f32[s0]", div: "f32[s0]", tangents_1: "f32[s0]"):
    # File: /Users/youkaichao/data/DeepLearning/depyf/tests/test_pytorch/test_pytorch.py:14 in forward, code: x = a / (torch.abs(a) + 1)
    neg: "f32[s0]" = torch.ops.aten.neg.default(tangents_1)
    abs_1: "f32[s0]" = torch.ops.aten.abs.default(primals_2)
    add: "f32[s0]" = torch.ops.aten.add.Tensor(abs_1, 1);  abs_1 = None
    div_2: "f32[s0]" = torch.ops.aten.div.Tensor(div, add);  div = None
    mul: "f32[s0]" = torch.ops.aten.mul.Tensor(neg, div_2);  neg = div_2 = None
    div_3: "f32[s0]" = torch.ops.aten.div.Tensor(tangents_1, add);  tangents_1 = add = None
    sgn: "f32[s0]" = torch.ops.aten.sgn.default(primals_2);  primals_2 = None
    mul_1: "f32[s0]" = torch.ops.aten.mul.Tensor(mul, sgn);  mul = sgn = None
    
    # File: /Users/youkaichao/data/DeepLearning/depyf/tests/test_pytorch/test_pytorch.py:14 in forward, code: x = a / (torch.abs(a) + 1)
    add_1: "f32[s0]" = torch.ops.aten.add.Tensor(div_3, mul_1);  div_3 = mul_1 = None
    return [None, add_1, None, None]
    