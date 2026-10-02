# firewall_handler.py

import subprocess
import re
import os
from constants import FIREWALL_CMD, PDF_FILE
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER

def get_all_rules():
    """Run netsh command and return raw output."""
    try:
        result = subprocess.run(FIREWALL_CMD, capture_output=True, text=True, shell=True)
        if result.returncode != 0:
            return None
        return result.stdout
    except Exception:
        return None

def parse_rules(raw_output):
    """
    Parse netsh output into list of rule dicts.
    Returns list of dict with keys: Name, Enable, Direction, Action, Protocol, LocalPort, RemotePort, etc.
    """
    rules = []
    blocks = re.split(r'Rule Name:\s*', raw_output)
    for block in blocks:
        if not block.strip():
            continue
        rule = {}
        lines = block.strip().splitlines()
        if lines:
            rule['Name'] = lines[0].strip()
        for line in lines[1:]:
            if ':' in line:
                key, value = line.split(':', 1)
                rule[key.strip()] = value.strip()
        # Only keep enabled rules
        if rule.get('Enable') == 'Yes':
            rules.append(rule)
    return rules

def separate_rules(rules):
    """Return two lists: blocking rules and allow rules."""
    block_rules = [r for r in rules if r.get('Action') == 'Block']
    allow_rules = [r for r in rules if r.get('Action') == 'Allow']
    return block_rules, allow_rules

def export_to_pdf(all_rules, block_rules, allow_rules):
    """Export ALL rules to PDF on desktop (one table with Action column)."""
    doc = SimpleDocTemplate(PDF_FILE, pagesize=letter)
    styles = getSampleStyleSheet()
    story = []

    # Title
    title_style = ParagraphStyle(
        'Title',
        parent=styles['Title'],
        fontSize=18,
        textColor=colors.HexColor('#1a237e'),
        alignment=TA_CENTER,
        spaceAfter=20
    )
    story.append(Paragraph("Windows Firewall Rules Report (All Rules)", title_style))
    story.append(Spacer(1, 12))

    # Summary counts
    story.append(Paragraph(f"<b>Total Rules:</b> {len(all_rules)}", styles['Normal']))
    story.append(Paragraph(f"<b>Blocking:</b> {len(block_rules)} &nbsp;&nbsp; <b>Allowed:</b> {len(allow_rules)}", styles['Normal']))
    story.append(Spacer(1, 12))

    # All Rules Table (with Action)
    story.append(Paragraph("<b>All Rules (Enabled)</b>", styles['Heading2']))
    if all_rules:
        data = [["#", "Rule Name", "Direction", "Action", "Protocol", "Local Port", "Remote Port"]]
        for idx, r in enumerate(all_rules, 1):
            data.append([
                str(idx),
                r.get('Name', 'N/A')[:30],  # truncate long names
                r.get('Direction', 'N/A'),
                r.get('Action', 'N/A'),
                r.get('Protocol', 'N/A'),
                r.get('LocalPort', 'N/A'),
                r.get('RemotePort', 'N/A'),
            ])
        table = Table(data, colWidths=[30, 120, 60, 60, 60, 60, 60])
        table.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1565C0')),
            ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
            ('ALIGN', (0,0), (-1,-1), 'CENTER'),
            ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
            ('FONTSIZE', (0,0), (-1,-1), 8),
            ('BOTTOMPADDING', (0,0), (-1,0), 6),
            ('BACKGROUND', (0,1), (-1,-1), colors.beige),
            ('GRID', (0,0), (-1,-1), 1, colors.grey),
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ]))
        story.append(table)
    else:
        story.append(Paragraph("No rules found.", styles['Normal']))

    doc.build(story)
    return PDF_FILE