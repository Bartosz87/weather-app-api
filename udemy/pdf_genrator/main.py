from fpdf import FPDF
import glob
import pandas as pd
from pathlib import Path

excel_files = glob.glob("invoices/*.xlsx")

for file in excel_files:
    df = pd.read_excel(f"{file}")
    columns_list = list(df.columns)

    invoice_number = Path(file).stem.split("-")

    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    pdf.set_font("Arial", style="B", size=12)
    pdf.cell(200, 10, txt=f"Invoice: {invoice_number[0]}", ln=1,  align="L")
    pdf.cell(200, 10, txt=f"Date: {invoice_number[1]}", ln=1, align="L")

    for c in columns_list:
        pdf.set_font("Arial", style="B", size=8)
        pdf.cell(38, 10, txt=f"{c}", ln=0, border=1, align="L")

    pdf.cell(0, 10, txt="", ln=1, align="L")

    for index, row in df.iterrows():

        for c in columns_list:
            pdf.cell(38, 10, txt=f"{row[c]}", ln=0, border=1, align="L")


        pdf.cell(0, 10, txt="", ln=1, align="L")


    pdf.output(f"{file}.pdf")
