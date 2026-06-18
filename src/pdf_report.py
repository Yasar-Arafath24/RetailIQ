from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet


def generate_pdf_report(
    forecast_results,
    risk_report
):

    pdf = SimpleDocTemplate(
        "reports/RetailIQ_Report.pdf"
    )

    styles = getSampleStyleSheet()

    elements = []

    elements.append(
        Paragraph(
            "RetailIQ Business Report",
            styles["Title"]
        )
    )

    elements.append(
        Spacer(1, 12)
    )

    elements.append(
        Paragraph(
            "Forecast Summary",
            styles["Heading2"]
        )
    )

    for product, demand in (
        forecast_results.items()
    ):

        elements.append(

            Paragraph(
                f"{product}: {demand} units",
                styles["BodyText"]
            )

        )

    elements.append(
        Spacer(1, 12)
    )

    elements.append(
        Paragraph(
            "Risk Analysis",
            styles["Heading2"]
        )
    )

    for product, data in (
        risk_report.items()
    ):

        elements.append(

            Paragraph(
                f"{product}: {data['Status']}",
                styles["BodyText"]
            )

        )

    pdf.build(elements)

    print(
        "PDF Report Generated!"
    )