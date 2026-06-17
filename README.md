# Pi Phase-Sector Model

Russian README: [README_RU.md](README_RU.md).

This repository contains the public v7 manuscript package for the phase-sector model of digit-expansion addressing, using the decimal expansion of pi as the main worked example.

The package includes the Russian manuscript, the experimental supplement, figures, CSV summaries, extracted experiment artifacts, minimal demonstration code, and a small Python module for exact proportional sector arithmetic.

## Scope

The work documents a finite, reproducible locate pipeline:

```text
target -> proportion -> finite phase index -> certificate -> address
```

The v7 wording makes the main distinction explicit: this is a constructive decoder and proof-object architecture, not a statistical predictor. A known tail plus an algebraically computable external sector certificate plus exact proportional arithmetic gives certified decoding of a continuation. Without an external certificate, there remain `10^k` candidates for the next `k` digits.

The external sector certificate may be computed from an independent representation of the number, for example Machin's formula:

```text
pi = 16 atan(1/5) - 4 atan(1/239)
```

The repository does not claim normality of pi, does not prove existence of a 1000-zero block, and does not claim autonomous prediction of new pi digits from the known decimal tail alone. The formalism is stated for arbitrary real carriers `alpha`; pi is the main experimental example.

## Repository Layout

- `main_ru_v7.pdf` / `main_ru_v7.tex` - main Russian manuscript.
- `supplement_experiments_ru.pdf` / `supplement_experiments_ru.tex` - experimental supplement for experiments 001-018.
- `cover_letter_ru.pdf` / `cover_letter_ru.tex` - Russian cover letter from the submission package.
- `figures/` - root figures used by the manuscript.
- `tables/` - key CSV summary tables from the submission package.
- `code/boundary_continue.py` - recover a decimal suffix from a known tail and an external sector certificate.
- `code/make_certificate.py` - demonstration generator for a Machin-formula external certificate.
- `experiments/pi_fs_experiment_001/` ... `experiments/pi_fs_experiment_018/` - extracted experiment reports and artifacts.
- `modules/pifs_proportion_module/` - exact proportional sector arithmetic module, docs, and tests.
- `docs/roadmap.md` - current repository roadmap and completed work.

The original nested experiment archives from the submission package were unpacked into regular directories so GitHub can show the actual files.

## Build PDFs

The TeX sources are intended for LuaLaTeX. The submitted PDFs are already included.

```bash
lualatex main_ru_v7.tex
lualatex main_ru_v7.tex
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

## Demo Scripts

The continuation script uses only the Python standard library:

```bash
python3 code/boundary_continue.py --help
```

The Machin certificate demo additionally imports `mpmath`. It is intentionally kept as an optional script dependency instead of a repository-wide runtime dependency.

```bash
python3 code/make_certificate.py --help
```

## License

No license has been selected yet. Until a license is added, default copyright rules apply.
