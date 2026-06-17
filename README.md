# Pi Phase-Sector Model

Russian README: [README_RU.md](README_RU.md).

This repository contains the public manuscript package for the phase-sector model of digit-expansion addressing, using the decimal expansion of pi as the main worked example.

The package includes the Russian manuscript, the experimental supplement, figures, CSV summaries, extracted experiment artifacts, and a small Python module for exact proportional sector arithmetic.

## Scope

The work documents a finite, reproducible locate pipeline:

```text
target -> proportion -> finite phase index -> certificate -> address
```

The positive result is the finite certifying locate contour and the external sector certificate lemma. The repository does not claim normality of pi, does not prove existence of a 1000-zero block, and does not claim autonomous prediction of new pi digits beyond a public computed horizon without an external certificate.

## Repository Layout

- `main_ru_v3.pdf` / `main_ru_v3.tex` - main Russian manuscript.
- `supplement_experiments_ru.pdf` / `supplement_experiments_ru.tex` - experimental supplement for experiments 001-018.
- `cover_letter_ru.pdf` / `cover_letter_ru.tex` - Russian cover letter from the submission package.
- `figures/` - figures used by the manuscript and supplement.
- `tables/` - key CSV summary tables.
- `experiments/pi_fs_experiment_001/` ... `experiments/pi_fs_experiment_018/` - extracted experiment reports and artifacts.
- `modules/pifs_proportion_module/` - exact proportional sector arithmetic module, docs, and tests.
- `docs/roadmap.md` - current repository roadmap and completed work.

The original nested experiment archives from the submission package were unpacked into regular directories so GitHub can show the actual files.

## Build PDFs

The TeX sources are intended for LuaLaTeX. The submitted PDFs are already included.

```bash
lualatex main_ru_v3.tex
lualatex main_ru_v3.tex
lualatex supplement_experiments_ru.tex
lualatex cover_letter_ru.tex
```

The sources use the `Tinos` and `DejaVu Sans Mono` fonts.

## Run Module Tests

```bash
cd modules/pifs_proportion_module
python3 -m unittest discover
```

Current local verification: 6 tests pass.

## License

No license has been selected yet. Until a license is added, default copyright rules apply.
