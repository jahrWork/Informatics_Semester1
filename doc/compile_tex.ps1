# compile_tex.ps1 - Compila un fichero .tex y lo abre en SumatraPDF
# Uso: .\compile_tex.ps1 [nombre_fichero_sin_extension]
# Ejemplo: .\compile_tex.ps1 Hitos_semanales

param(
    [string]$TexFile = "Hitos_semanales"
)

$SumatraPDF = "C:\Users\Juan\AppData\Local\SumatraPDF\SumatraPDF.exe"
$DocDir = Split-Path -Parent $MyInvocation.MyCommand.Path

Write-Host "Compilando $TexFile.tex ..." -ForegroundColor Cyan

# Primera pasada
pdflatex -synctex=1 -interaction=nonstopmode "$TexFile.tex"

# Segunda pasada (para referencias cruzadas y tabla de contenidos)
pdflatex -synctex=1 -interaction=nonstopmode "$TexFile.tex" | Out-Null

if (Test-Path "$TexFile.pdf") {
    Write-Host "PDF generado: $TexFile.pdf" -ForegroundColor Green
    # Abrir/actualizar en SumatraPDF
    $running = Get-Process "SumatraPDF" -ErrorAction SilentlyContinue
    if ($running) {
        Write-Host "SumatraPDF ya abierto, recargando..." -ForegroundColor Yellow
    } else {
        Start-Process $SumatraPDF -ArgumentList "$TexFile.pdf"
        Write-Host "PDF abierto en SumatraPDF." -ForegroundColor Green
    }
} else {
    Write-Host "Error: No se generó el PDF. Revisa el log: $TexFile.log" -ForegroundColor Red
}
