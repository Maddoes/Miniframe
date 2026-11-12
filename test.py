# Here’s one that should be properly hard: MiniFrame, a tiny pandas built from scratch, with a small ML pipeline on top.
# It builds on the classes, generators and JSON work you’ve done and adds what pandas and ML lean on: hashing, complexity, operator overloading, numerics and testing.
#
# Rules: Standard library only, so no numpy, pandas or scikit-learn. Use one package with several modules, type hints and tests.
# Use a real, messy CSV with numeric columns and a numeric target, such as a housing or car-prices dataset. Daily stock prices also work well as a second dataset for the join stage.
#
# Loading. Read the CSV into column-oriented storage and infer each column’s type. Handle missing values, and raise a custom error that names the row and column when parsing fails.
# Support length, a readable repr, indexing by column name, row slicing, boolean masks and a lazy row iterator.
# Querying. Build select, filter with a user-supplied function, multi-key sort (stable, missing values last), derived columns, drop and rename. Every operation returns a new table so calls can be chained. Think hard about what gets copied and what gets shared.
# Aggregation and joins. Write describe yourself (count, mean, std, min, quartiles, max). Add group-by with several aggregations, including a custom one. Build inner and left joins using a hash index, then compare against a naive nested-loop join as the row count doubles.
# Linear algebra. Write vector and matrix classes with operator overloading and shape checks that give helpful errors. Time a 200×200 matrix multiply. You’ll see exactly what numpy fixes.
# ML from scratch. Do a seeded train/test split and standardize using only the training data. Derive the gradient of the loss by hand, then implement gradient descent for linear regression and track the loss per epoch. Evaluate with RMSE and R², and beat a baseline that always predicts the mean. For a stretch, add k-nearest neighbors using a heap, or logistic regression with a confusion matrix.
# Polish. Write 30+ tests, including edge cases like an empty table, an all-missing column, duplicate join keys and a single row. Profile and speed up your slowest operation, add a command-line entry point, and write a short README on design choices and complexity.
#
# You’re ready to move on if:
#
# You did stages 1 to 3 unaided. That makes you pandas-ready, because read_csv, filtering, groupby and merge will all feel like things you’ve built.
# You did stages 4 and 5 and can explain the loss curve, why too high a learning rate diverges, and why fitting the scaler on test data leaks information. This makes you ML-ready.
# You can say why pandas stores data by column and why hash-based joins are fast.
# You fixed bugs by reading tracebacks and reasoning, not by trial and error.
#
# Whichever stage you can’t get through is the gap to close first. If the gradient derivation in stage 5 feels shaky, revisit partial derivatives before starting ML.
#
# Write every line yourself. Before you code stage 1, send me your design for column storage and type inference, and I’ll push back with questions instead of answers.

