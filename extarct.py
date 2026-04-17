import nbformat

with open('minproject.ipynb') as f:
    nb = nbformat.read(f, as_version=4)

# Filter for code cells only
code_cells = [cell.source for cell in nb.cells if cell.cell_type == 'code']
full_code = "\n\n".join(code_cells)

with open('miniproject.py', 'w') as f:
    f.write(full_code)
