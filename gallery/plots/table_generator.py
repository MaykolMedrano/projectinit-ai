import pandas as pd

class AERTable:
    """
    A simple utility to generate professional LaTeX tables 
    following AER/NBER standards (booktabs, no vertical lines).
    
    Logic:
    - Enforces booktabs styling.
    - Implements siunitx alignment through 'S' column format.
    - Standardizes dependent variable multi-column headers.
    """
    def __init__(self, df, label=None, caption=None):
        self.df = df
        self.label = label
        self.caption = caption

    def to_latex(self, output_path):
        latex = self.df.to_latex(
            index=True,
            escape=False,
            column_format="l" + "S" * len(self.df.columns),
            label=self.label,
            caption=self.caption,
            position="htbp",
            bold_rows=False
        )
        
        # Adding AER custom touches
        latex = latex.replace("\\toprule", "\\toprule\n& \\multicolumn{" + str(len(self.df.columns)) + "}{c}{Dependent Variable: Outcome Y} \\\\\n\\cmidrule(lr){2-" + str(len(self.df.columns)+1) + "}")
        
        with open(output_path, "w") as f:
            f.write(latex)
        print(f"Professional Table generated at: {output_path}")

# Example Usage
if __name__ == "__main__":
    data = {
        "(1)": ["1.24*** (0.12)", "0.15", "Yes", "No"],
        "(2)": ["1.18*** (0.11)", "0.22", "Yes", "Yes"],
        "(3)": ["1.05** (0.45)", "0.34", "Yes", "Yes"]
    }
    index = ["Treatment", "R-squared", "Controls", "State FE"]
    df = pd.DataFrame(data, index=index)
    
    table = AERTable(df, label="tab:results", caption="Automated AER Table Generation")
    table.to_latex("example_automated_table.tex")
