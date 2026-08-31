# Configuración latexmk para compilación automática con SumatraPDF
# Compilador: pdflatex con codificación UTF-8
$pdflatex = 'pdflatex -synctex=1 -interaction=nonstopmode -file-line-error %O %S';

# Modo PDF
$pdf_mode = 1;

# Visor PDF: SumatraPDF (se actualiza automáticamente al recompilar)
$pdf_previewer = 'start "C:\Users\Juan\AppData\Local\SumatraPDF\SumatraPDF.exe" %O %S';

# Actualizar el visor sin cerrarlo
$preview_continuous_mode = 1;

# Extensiones a limpiar
@generated_exts = ('aux', 'bbl', 'bcf', 'blg', 'fdb_latexmk', 'fls', 'idx',
                   'ilg', 'ind', 'lof', 'log', 'lot', 'nav', 'out', 'run.xml',
                   'snm', 'synctex.gz', 'toc', 'vrb');
