import json
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import pandas as pd

def summarize_sentiment_data(df):
    avg_compound_score = df['compound'].mean()
    positive_count = (df['compound'] > 0.05).sum()
    negative_count = (df['compound'] < -0.05).sum()
    neutral_count = len(df) - positive_count - negative_count

    return {
        'average_score': avg_compound_score,
        'positive_count': positive_count,
        'negative_count': negative_count,
        'neutral_count': neutral_count,
        'total_count': len(df)
    }

def generate_report_text(summary):
    text = []
    text.append(f"Over a total of {summary['total_count']} analyzed tweets, ")
    text.append(f"the average compound sentiment score was {summary['average_score']:.2f}. ")
    text.append(f"This includes {summary['positive_count']} positive tweets, ")
    text.append(f"{summary['negative_count']} negative tweets, ")
    text.append(f"and {summary['neutral_count']} neutral tweets.")
    return ' '.join(text)

def generate_detailed_pdf_report(df, visualizations, output_file):
    summary = summarize_sentiment_data(df)
    report_text = generate_report_text(summary)

    c = canvas.Canvas(output_file, pagesize=letter)
    width, height = letter

    text_object = c.beginText(72, height - 72)
    text_object.setFont("Helvetica", 12)
    text_object.textLines(report_text)
    c.drawText(text_object)

    y_position = height - 250
    for viz in visualizations:
        c.drawImage(viz, 72, y_position, width=400, preserveAspectRatio=True, anchor='c')
        y_position -= 450

    c.save()