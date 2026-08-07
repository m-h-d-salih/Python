# make_linkedin_pdf.py
# Generates two PDFs:
# 1) LinkedIn_Profile_Update.pdf (full version)
# 2) LinkedIn_Profile_OnePager.pdf (condensed)

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

FULL_FILENAME = "LinkedIn_Profile_Update.pdf"
ONEPAGER_FILENAME = "LinkedIn_Profile_OnePager.pdf"

def build_styles():
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name="Tight", parent=styles["Normal"], leading=14, spaceAfter=8))
    styles.add(ParagraphStyle(name="Small", parent=styles["Normal"], fontSize=9, leading=12, spaceAfter=6))
    styles.add(ParagraphStyle(name="H2", parent=styles["Heading2"], spaceAfter=6))
    styles.add(ParagraphStyle(name="H1", parent=styles["Title"], spaceAfter=12))
    return styles

def make_doc(filename, title="LinkedIn Profile Update"):
    return SimpleDocTemplate(
        filename,
        pagesize=A4,
        leftMargin=2*cm, rightMargin=2*cm, topMargin=2*cm, bottomMargin=2*cm
    )

def build_full_pdf():
    styles = build_styles()
    doc = make_doc(FULL_FILENAME)
    story = []

    # Title
    story.append(Paragraph("LinkedIn Profile Update", styles["H1"]))
    story.append(Spacer(1, 6))

    # Headline
    story.append(Paragraph("Suggested Headline", styles["H2"]))
    story.append(Paragraph(
        "Software Engineer @ Ergon Technologies | Full Stack & Generative AI Developer | "
        "Building RAG-powered Enterprise Chatbots on Vertex AI",
        styles["Tight"]
    ))
    story.append(Spacer(1, 12))

    # About
    story.append(Paragraph("Suggested About Section", styles["H2"]))
    about_html = (
        "I am a Software Engineer with expertise in full-stack development and applied AI. "
        "At Ergon Technologies, I design and build scalable enterprise systems that combine robust web platforms with modern AI.<br/><br/>"
        "Recently, I have been leading the development of an <b>internal Retrieval-Augmented Generation (RAG) chatbot</b> "
        "using <b>Google Vertex AI</b>, designed to support enterprise applications (HRMS, LMS, and internal operations) in the "
        "<b>oil &amp; gas services</b> domain (e.g., rig spares trading).<br/><br/>"
        "<b>My core focus areas:</b><br/>"
        "&bull; Full-stack web applications (front-end &amp; back-end)<br/>"
        "&bull; Generative AI integration (LLMs, RAG, embeddings, vector search)<br/>"
        "&bull; Cloud-native deployment (Google Cloud, Vertex AI)<br/>"
        "&bull; Intelligent systems for enterprise workflows<br/><br/>"
        "Passionate about building intelligent, user-centric solutions that drive efficiency and digital transformation."
    )
    story.append(Paragraph(about_html, styles["Tight"]))
    story.append(Spacer(1, 12))

    # Experience
    story.append(Paragraph("Suggested Experience (Ergon Technologies)", styles["H2"]))
    exp_html = (
        "&bull; Developed an internal enterprise chatbot using Retrieval-Augmented Generation (RAG) on Vertex AI, "
        "enabling employees to query company systems (HRMS, LMS, operations) and access knowledge efficiently within "
        "the oil &amp; gas services domain."
    )
    story.append(Paragraph(exp_html, styles["Tight"]))
    story.append(Spacer(1, 12))

    # Skills
    story.append(Paragraph("Suggested Skills to Add", styles["H2"]))
    skills_html = (
        "&bull; Generative AI<br/>"
        "&bull; Retrieval-Augmented Generation (RAG)<br/>"
        "&bull; Large Language Models (LLMs)<br/>"
        "&bull; Vertex AI<br/>"
        "&bull; Google Cloud Platform (GCP)<br/>"
        "&bull; Enterprise Software Development"
    )
    story.append(Paragraph(skills_html, styles["Tight"]))

    doc.build(story)

def build_onepager_pdf():
    styles = build_styles()
    doc = make_doc(ONEPAGER_FILENAME)
    story = []

    # Title
    story.append(Paragraph("LinkedIn Profile — One Pager", styles["H1"]))
    story.append(Spacer(1, 6))

    # Headline
    story.append(Paragraph("Headline", styles["H2"]))
    story.append(Paragraph(
        "Software Engineer @ Ergon Technologies | Full Stack & Generative AI Developer | "
        "Building RAG-powered Enterprise Chatbots on Vertex AI",
        styles["Tight"]
    ))
    story.append(Spacer(1, 8))

    # Short About
    story.append(Paragraph("About (Condensed)", styles["H2"]))
    short_about = (
        "Full-stack Software Engineer applying Generative AI to enterprise workflows. "
        "Currently building an internal <b>RAG-powered chatbot</b> on <b>Vertex AI</b> "
        "supporting HRMS, LMS, and operations in the oil &amp; gas services domain."
    )
    story.append(Paragraph(short_about, styles["Tight"]))
    story.append(Spacer(1, 8))

    # Skills
    story.append(Paragraph("Key Skills", styles["H2"]))
    skills_inline = (
        "Generative AI • RAG • LLMs • Embeddings • Vector Search • Vertex AI • "
        "GCP • Full-Stack Development"
    )
    story.append(Paragraph(skills_inline, styles["Tight"]))

    doc.build(story)

if __name__ == "__main__":
    build_full_pdf()
    build_onepager_pdf()
    print(f"Created: {FULL_FILENAME}")
    print(f"Created: {ONEPAGER_FILENAME}")
