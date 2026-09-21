# Numerical Computations Course Materials

Archived materials for the [Numerical Computations](https://docs.ce.sharif.ir/course/40215) course at [Sharif University of Technology](https://en.sharif.ir).

The repository collects past exam papers, homework sets and their official solutions, quizzes, lecture slides, cheat sheets, class practice problems, a few Jupyter notebooks and the reference texts the course draws on. Material is filed by content type first and then by Persian academic semester, so `Homework/1402-1/` holds the homework for the first semester of 1402.

Most documents are in Persian. The LaTeX sources are written for XeLaTeX with the `xepersian` package and the XB Niloofar font family, which is bundled alongside the documents that need it. Compiled PDFs are tracked deliberately: for most items the PDF is the thing you actually want.

## Layout

| Directory | What is in it | Semesters available |
| --- | --- | --- |
| `Exam/` | Midterm and final papers, some with LaTeX sources and official solutions | 1399-2, 1400-1, 1400-2, 1401-1, 1401-2, 1402-1 |
| `Homework/` | Problem sets, most accompanied by an official solution | 1399-2 through 1402-2 |
| `Quiz/` | Short in-class quizzes | 1399-2, 1400-1, 1400-2 |
| `Slides/` | Lecture slides, including the GPU and CUDA sessions | 1400-2, 1401-1, 1401-2, 1402-2 |
| `Class Practice/` | Exercises worked through during class | 1402-1 |
| `Cheat Sheet/` | Student-prepared reference sheets for the midterm and final | 1402-2 |
| `Jupyter Notebooks/` | Interpolation, Taylor series and linear system solvers | not split by semester |
| `Source/` | Reference books used by the course | not split by semester |

## Coverage

Coverage is uneven, and a few directories exist only as placeholders for material that has not been collected yet:

- `Cheat Sheet/` has content for 1402-2 only; the `1401-1`, `1401-2` and `1402-1` folders hold no material yet.
- `Class Practice/1402-2` and `Exam/1402-2` hold no material yet.
- `Slides/` has nothing for 1402-1.
- `Quiz/` stops after 1400-2.
- Where a homework or exam folder has no `official solution` counterpart, no solution has been published for it.
- The original question sheets corresponding to `Homework/1399-2/HW1 - official solution.pdf` and `Homework/1401-1/HW4 - official solution.pdf` are not present in this repository, its Git history, or the related archived repositories. The solution files are retained as historical material rather than reconstructing question wording speculatively.
- No HW5 artifact for 1401-1 was found in the repository, its Git history, or the related archived repositories.

If you have material from a semester that is missing here, a pull request adding it is welcome.

## Contributing

Corrections and additions from students are welcome through the usual pull request process. When adding LaTeX sources, please commit the compiled PDF as well, and leave build artifacts such as `.aux` and `.log` files out; the `.gitignore` already covers them.

## Contact

For questions about the course or this repository, contact [Dr. Hossein Ghorban](mailto:s.hosseinghorban@ipm.ir).
