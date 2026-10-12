"""Verify that MetPy #4095 changes docstrings only and moves equations into Notes."""

import ast
import subprocess
import sys
from pathlib import Path

from numpydoc.docscrape import NumpyDocString


class WithoutDocstrings(ast.NodeTransformer):
    def visit_FunctionDef(self, node):
        self.generic_visit(node)
        if ast.get_docstring(node) is not None:
            node.body.pop(0)
        return node

    visit_AsyncFunctionDef = visit_FunctionDef
    visit_ClassDef = visit_FunctionDef
    visit_Module = visit_FunctionDef


repo = Path(sys.argv[1])
path = "src/metpy/calc/kinematics.py"
base = subprocess.check_output(
    ["git", "show", f"upstream/main:{path}"], cwd=repo, text=True
)
changed = (repo / path).read_text()
assert ast.dump(WithoutDocstrings().visit(ast.parse(base))) == ast.dump(
    WithoutDocstrings().visit(ast.parse(changed))
), "Runtime AST differs from upstream/main"

names = {
    "frontogenesis",
    "storm_relative_helicity",
    "potential_vorticity_baroclinic",
    "potential_vorticity_barotropic",
    "inertial_advective_wind",
    "q_vector",
}
checked = set()
for node in ast.parse(changed).body:
    if isinstance(node, ast.FunctionDef) and node.name in names:
        doc = NumpyDocString(ast.get_docstring(node))
        assert doc["Notes"], f"Missing Notes in {node.name}"
        assert any(".. math::" in line for line in doc["Notes"]), node.name
        assert not any(".. math::" in line for line in doc["Extended Summary"]), node.name
        checked.add(node.name)
assert checked == names
print("Runtime AST unchanged; equations in Notes for all six functions.")
