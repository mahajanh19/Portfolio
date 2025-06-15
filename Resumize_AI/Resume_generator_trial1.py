from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.colors import blue, black
from reportlab.lib.enums import TA_CENTER, TA_LEFT
import ast
import requests
import re

summary =  "A result-oriented Quantitative Researcher with a strong foundation in data analysis, machine learning, and engineering. " \
"I hold a Ph.D. in Structural Health Monitoring and have expertise in predictive analytics. I have worked on data extraction, cleaning, " \
"and feature generation, developed machine learning models, and led projects from research to production, driving business insights and strategy."

detail_job_2 = [
            "Built SQL queries to extract data from various sources, including bureau data, customer details, loan details etc.",
            "Curated pipeline for data preparation resulting in data cleaning and feature generation.",
            "Developed an optimised machine learning classification model for customer loan approval, bounce status and foreclosure possibility aims to replace existing third-party ML services aimed to save Rs 5Million per annum.",
            "Designed Risk based scoring framework using ML model for housing loan.",
            "Engineered API endpoint for model deployment using Altair Rapid Miner and Fast API for real-time prediction.",
            "Participated in data visualisation and EDA process for different aspects of business using SQL queries and Power BI.",
            "Coached two interns for ML model development."
        ]

detail_job_1 =[
            "Evaluated alternate data to conduct predictive analysis of US stocks, enhancing investment strategies.",
            "Conducted comprehensive sector-level performance attribution, significantly contributing to assessments framework and the development of strategic investment initiatives.",
            "Executed projects from research inception to production through production ready code.",
            "Collaborated with data and portfolio teams to seamlessly integrate findings into portfolio construction.",
            "Modelled Machine learning algorithms for factor generation based on alternative dataset.",
            "Explored the relation between fundamentals and news dataset using regression framework."
        ]

skills = [
    "Python", "SQL", "Machine Learning", "Statistical Analysis", "PowerBI", "PCA",
    "Quantitative Finance", "Data Analysis", "Prompt Engineering", "Credit risk modelling",
    "TensorFlow", "GitHub", "Agentic AI", "RAG", "LLM"
]

about_job =  """

We’ll look to you for:

• 7-10 years of experience in machine learning, deep learning.
• Experience End-to-end architecture design for machine learning solutions
• Deployment of AI models into scalable services
• Staying at the forefront of generative AI advancements
• Optimizing models for performance and scalability
• Collaborating with cross-functional teams for successful project delivery

All About You

We value passion and attitude over experience. That’s why we don’t expect you to have every single skill. Instead, we’ve listed some that we think will help you succeed and grow in this role:

• Degree in Computer Science, Information Technology, Electrical Engineering, or related field
• Experience or understanding of machine learning, deep learning, generative AI and MLOps
• Knowledge of deep learning techniques and frameworks (TensorFlow, PyTorch)
• Familiarity with cloud platforms, preferably Microsoft Azure
• A certification in AI or machine learning is advantageous
• Strong analytical and problem-solving skills
• Excellent communication and team collaboration abilities
"""

url = "http://127.0.0.1:1234/v1/chat/completions"
headers = {"Content-Type": "application/json"}
prompt = f"""
You are a resume optimization assistant. I will provide you with my resume content and a job description.
Update each section to make it more ATS-friendly and aligned with the job. keep this in mind i have stritly 2.5 year experience.

Please output ONLY in the following Python dictionary format:

summary = "<updated summary text>"
detail_job_1 = [<updated list of bullet points>]
detail_job_2 = [<updated list of bullet points>]
skills = [<updated skill list>]
about_job = "<rephrased job summary if needed>"

Here is the input data:

summary = "{summary}"

detail_job_1 = {detail_job_1}

detail_job_2 = {detail_job_2}

skills = {skills}

about_job = \"\"\"{about_job}\"\"\"

Please update the content accordingly. Do not change the format.
"""
payload = {
    "model": "google/gemma-3-4b",
    "messages": [
        {"role": "system", "content": "You are an expert resume writer."},
        {"role": "user", "content": prompt}
    ],
    "temperature": 0.7
}

response = requests.post(url, headers=headers, json=payload)
raw_output = response.json()["choices"][0]["message"]["content"]


clean_output = raw_output.strip().removeprefix("```python").removesuffix("```").strip()
try:
    updated_resume_data = ast.literal_eval(clean_output)
except Exception as e:
    print("Error parsing output:", e)
    updated_resume_data = None




# --- Resume Data (Copied from previous turn) ---
profile_data = {
    "name": "Harsh Mahajan",
    "contact": "+91-9753351408",
    "email": "mahajanharsh1909@gmail.com",
    "github": "github.com/mahajanh19/Portfolio",
    "linkedin": "linkedin.com/in/harshmahajan1909",
    "summary": updated_resume_data['summary']
}

experience_data = [
    {
        "title": "Quantitative Researcher",
        "company": "QR System LLP",
        "location": "Mumbai, India",
        "dates": "January 2024 - Present",
        "details":  updated_resume_data['detail_job_1']
    },
    {
        "title": "Data Analyst",
        "company": "Vastu Housing Finance Pvt. Ltd.",
        "location": "Mumbai, India",
        "dates": "February 2024 - December 2024",
        "details": updated_resume_data['detail_job_2']
    }
]

education_data = [
    {
        "degree": "Master of Science in Financial Engineering",
        "institution": "World Quant University",
        "location": "Remote (USA)",
        "dates": "Pursuing"
    },
    {
        "degree": "Doctor of Philosophy in Structural Engineering",
        "institution": "Indian Institute of Technology Bombay",
        "location": "Mumbai, India",
        "dates": "July 2016 - August 2024",
        "gpa": "8.41",
        "thesis": "Machine Learning Enabled Active and Passive Health Monitoring of Railway Tracks"
    },
    {
        "degree": "Master of Science in Financial Engineering",
        "institution": "Shri G.S. Institute of Technology and Science",
        "location": "Indore, India",
        "dates": "July 2013 - November 2015",
        "gpa": "7.82",
        "thesis": "Decision model for Repair Prioritization of Reinforced Concrete Structure"
    }
]

skills_data = updated_resume_data['skills']

certifications_data = [
    {
        "name": "Foundations of Financial Engineering",
        "issuer": "World Quant University"
    },
    {
        "name": "ChatGPT Prompt Engineering for Developers",
        "issuer": "DeepLearning.ai"
    },
    {
        "name": "Agile Project management",
        "issuer": "Google"
    },
    {
        "name": "Advanced Certificate Programme in Machine learning and Deep learning",
        "issuer": "IIIT Bangalore"
    },
    {
        "name": "Data Science Professional Certificate",
        "issuer": "IBM"
    }
]

publications_data = [
    {
        "title": "Acoustic emission source localisation for structural health monitoring of rail section based on deep learning approach",
        "authors": "H. Mahajan, S. Banerjee",
        "type": "Research Article",
        "journal": "Measurement Science and Technology (IOP)",
        "volume": "34",
        "number": "4",
        "doi": "https://doi.org/10.1088/1361-6501/acb002"
    },
    {
        "title": "Quantitative Investigation of Acoustic Emission Waveform Parameters from Crack Opening in a Rail Section Using Clustering Algorithms and Advanced Signal Processing",
        "authors": "H. Mahajan, S. Banerjee",
        "type": "Research Article",
        "journal": "Sensors (MDPI)",
        "volume": "22(22)",
        "number": "8643",
        "doi": "https://doi.org/10.3390/s22228643"
    },
    {
        "title": "A machine learning framework for guided wave based damage detection of rail head using surface bonded piezo-electric wafer transducers",
        "authors": "H. Mahajan, S. Banerjee",
        "type": "Research Article",
        "journal": "Machine Learning with Applications (Elsevier)",
        "volume": "7",
        "doi": "https://doi.org/10.1016/j.mlwa.2021.100216"
    }
]




class ResumeGeneratorReportLab:
    """
    Generates a resume PDF using ReportLab.
    """
    def __init__(self, filename='harsh_mahajan_resume.pdf', pagesize=A4, margin=15*mm):
        self.c = canvas.Canvas(filename, pagesize=pagesize)
        self.width, self.height = pagesize
        self.margin = margin
        self.x_start = self.margin
        self.y_cursor = self.height - self.margin # Start from top
        self.line_height = 12 # Default line height for text

    def add_line_break(self, height=None):
        """Adds vertical space."""
        self.y_cursor -= (height if height is not None else self.line_height / 2)
        # Check for page break
        if self.y_cursor < self.margin + self.line_height * 2: # Keep some space at bottom
            self.c.showPage()
            self.y_cursor = self.height - self.margin

    def section_title(self, title):
        """Adds a section title with an underline."""
        self.add_line_break(self.line_height * 1.5) # Space before title
        self.c.setFont('Helvetica-Bold', 16)
        self.c.drawString(self.x_start, self.y_cursor, title)
        self.y_cursor -= 2 # Small adjustment for line placement
        self.c.line(self.x_start, self.y_cursor, self.x_start + self.width - 2 * self.margin, self.y_cursor)
        self.add_line_break(self.line_height) # Space after line

    def draw_wrapped_text(self, text, font_name, font_size, x, y, max_width, align=TA_LEFT):
        """Draws text that wraps within a given width."""
        self.c.setFont(font_name, font_size)
        textobject = self.c.beginText(x, y)
        textobject.setTextOrigin(x, y)
        textobject.setFont(font_name, font_size)
        textobject.setFillColor(black)

        lines = []
        words = text.split(' ')
        current_line = []
        for word in words:
            # Estimate width of current line + new word + space
            test_line = ' '.join(current_line + [word])
            if self.c.stringWidth(test_line, font_name, font_size) < max_width:
                current_line.append(word)
            else:
                lines.append(' '.join(current_line))
                current_line = [word]
        lines.append(' '.join(current_line))

        for line in lines:
            textobject.textLine(line)
            self.y_cursor -= (font_size + 2) # Adjust for line height in ReportLab
        
        self.c.drawText(textobject)
        self.add_line_break(2) # Small break after wrapped text


    def add_profile(self, profile):
        """Adds the profile section."""
        # Name
        self.c.setFont('Helvetica-Bold', 24)
        self.y_cursor -= 12 # Adjust for font size
        self.c.drawCentredString(self.width / 2, self.y_cursor, profile['name'])
        self.y_cursor -= 10 # Space after name

        # Contact Info (centered with links)
        self.c.setFont('Helvetica', 10)
        contact_items = [
            profile['contact'],
            profile['email'],
            f"GitHub: {profile['github'].split('/')[-1]}",
            f"LinkedIn: {profile['linkedin'].split('/')[-1]}"
        ]
        contact_line_text = " | ".join(contact_items)
        
        # Calculate width of the contact line to center it
        contact_line_width = self.c.stringWidth(contact_line_text, 'Helvetica', 10)
        x_center_contact = (self.width - contact_line_width) / 2

        # Draw contact info with clickable links
        current_x = x_center_contact
        self.y_cursor -= 6 # Move down for contact info
        for i, item in enumerate(contact_items):
            self.c.setFillColor(black)
            if "GitHub:" in item:
                self.c.setFillColor(blue)
                self.c.linkURL(f"https://{profile['github']}", (current_x, self.y_cursor, current_x + self.c.stringWidth(item, 'Helvetica', 10), self.y_cursor + 10), thickness=0)
            elif "LinkedIn:" in item:
                self.c.setFillColor(blue)
                self.c.linkURL(f"https://{profile['linkedin']}", (current_x, self.y_cursor, current_x + self.c.stringWidth(item, 'Helvetica', 10), self.y_cursor + 10), thickness=0)
            elif "@" in item: # Simple check for email
                self.c.setFillColor(blue)
                self.c.linkURL(f"mailto:{profile['email']}", (current_x, self.y_cursor, current_x + self.c.stringWidth(item, 'Helvetica', 10), self.y_cursor + 10), thickness=0)
            
            self.c.drawString(current_x, self.y_cursor, item)
            current_x += self.c.stringWidth(item + " | ", 'Helvetica', 10) # Advance x for next item
            if i < len(contact_items) - 1:
                self.c.setFillColor(black)
                self.c.drawString(current_x - self.c.stringWidth(" | ", 'Helvetica', 10), self.y_cursor, " | ") # Draw separator
            
        self.add_line_break(self.line_height) # Space after contact info

        self.section_title("PROFILE")
        self.draw_wrapped_text(profile['summary'], 'Helvetica', 10, self.x_start, self.y_cursor, self.width - 2 * self.margin)
        self.add_line_break(5)


    def add_experience(self, experience):
        """Adds the experience section."""
        self.section_title("EXPERIENCE")
        for job in experience:
            # Job Title and Company
            self.c.setFont('Helvetica-Bold', 12)
            self.y_cursor -= self.line_height
            self.c.drawString(self.x_start, self.y_cursor, f"{job['title']} - {job['company']}")

            # Location and Dates
            self.c.setFont('Helvetica-Oblique', 10) # Italic for location/dates
            self.y_cursor -= self.line_height # Move down for next line
            self.c.drawString(self.x_start, self.y_cursor, job['location'])
            self.c.drawRightString(self.width - self.margin, self.y_cursor, job['dates']) # Right align dates
            self.add_line_break(4) # Small break

            # Details
            self.c.setFont('Helvetica', 10)
            self.y_cursor -= self.line_height
            for detail in job['details']:
                self.y_cursor -= self.line_height/2 # Move down for bullet point
                # Manually handle bullet and wrap text
                bullet_x = self.x_start + 5 # Indent for bullet
                text_x = bullet_x + 5
                text_width = self.width - 2 * self.margin - (text_x - self.x_start)
                
                self.c.drawString(bullet_x, self.y_cursor, "*") # Use asterisk for bullet
                self.draw_wrapped_text(detail, 'Helvetica', 10, text_x, self.y_cursor, text_width, align=TA_LEFT)
            self.add_line_break(3)

    def add_education(self, education):
        """Adds the education section."""
        self.section_title("EDUCATION")
        for edu in education:
            # Degree and Institution
            self.c.setFont('Helvetica-Bold', 12)
            self.y_cursor -= self.line_height
            self.c.drawString(self.x_start, self.y_cursor, f"{edu['degree']} - {edu['institution']}")

            # Location and Dates
            self.c.setFont('Helvetica-Oblique', 10)
            self.y_cursor -= self.line_height
            self.c.drawString(self.x_start, self.y_cursor, edu['location'])
            self.c.drawRightString(self.width - self.margin, self.y_cursor, edu['dates'])
            self.add_line_break(2)

            # GPA and Thesis (if present)
            self.c.setFont('Helvetica', 10)
            if 'gpa' in edu:
                self.add_line_break(2)
                self.y_cursor -= self.line_height
                self.c.drawString(self.x_start, self.y_cursor, f"GPA: {edu['gpa']}")
            if 'thesis' in edu:
                self.add_line_break(12)
                self.draw_wrapped_text(f"Thesis: {edu['thesis']}", 'Helvetica', 10, self.x_start, self.y_cursor, self.width - 2 * self.margin)
            self.add_line_break(5)

    def add_skills(self, skills):
        """Adds the skills section."""
        self.section_title("SKILLS")
        self.draw_wrapped_text(", ".join(skills), 'Helvetica', 11, self.x_start, self.y_cursor, self.width - 2 * self.margin)
        self.add_line_break(5)

    def add_certifications(self, certifications):
        """Adds the certifications section."""
        self.section_title("CERTIFICATIONS")
        self.c.setFont('Helvetica', 11)
        for cert in certifications:
            self.y_cursor -= self.line_height
            # Use asterisk for bullet
            self.c.drawString(self.x_start + 5, self.y_cursor, "*") 
            self.draw_wrapped_text(f"{cert['name']}", 'Helvetica', 11, self.x_start + 10, self.y_cursor, self.width - 2 * self.margin - 10)
            
            self.c.setFont('Helvetica-Oblique', 10)
            # self.y_cursor -= self.line_height
            self.c.drawString(self.x_start + 10, self.y_cursor, f"  {cert['issuer']}") # Indent issuer
            self.add_line_break(2)

    def add_publications(self, publications):
        """Adds the publications section."""
        self.section_title("PUBLICATIONS")
        
        for pub in publications:
            self.y_cursor -= self.line_height
            self.add_line_break(2)
            # Title
            self.c.setFont('Helvetica', 11)
            self.c.drawString(self.x_start + 5, self.y_cursor, "*") # Bullet
            self.draw_wrapped_text(pub['title'], 'Helvetica', 11, self.x_start + 10, self.y_cursor, self.width - 2 * self.margin - 10)

            # Authors, Type, Journal
            self.c.setFont('Helvetica-Oblique', 10)
            # self.y_cursor -= self.line_height
            journal_info = f"{pub['authors']} | {pub['type']} | {pub['journal']}"
            if 'volume' in pub and 'number' in pub:
                journal_info += f" | Volume {pub['volume']}, Number {pub['number']}"
            self.draw_wrapped_text(journal_info, 'Helvetica-Oblique', 10, self.x_start, self.y_cursor, self.width - 2 * self.margin)

            # DOI (with link)
            if 'doi' in pub:
                # self.y_cursor -= self.line_height
                self.c.setFont('Helvetica', 10)
                doi_text = "DOI: "
                doi_link_text = pub['doi']
                
                self.c.drawString(self.x_start, self.y_cursor, doi_text)
                link_x = self.x_start + self.c.stringWidth(doi_text, 'Helvetica', 10)
                self.c.setFillColor(blue)
                self.c.linkURL(doi_link_text, (link_x, self.y_cursor, link_x + self.c.stringWidth(doi_link_text, 'Helvetica', 10), self.y_cursor + 10), thickness=0)
                self.c.drawString(link_x, self.y_cursor, doi_link_text)
                self.c.setFillColor(black) # Reset color
                self.add_line_break(5) # Space after DOI

            self.add_line_break(5) # Space after publication

    def save_pdf(self):
        """Saves the generated PDF."""
        self.c.save()


# --- Main execution ---
if __name__ == '__main__':
    generator = ResumeGeneratorReportLab()

    # Add all sections
    generator.add_profile(profile_data)
    generator.add_experience(experience_data)
    generator.add_education(education_data)
    generator.add_skills(skills_data)
    generator.add_certifications(certifications_data)
    generator.add_publications(publications_data)

    # Output the PDF file
    generator.save_pdf()
    print("Resume PDF 'harsh_mahajan_resume.pdf' has been generated successfully using ReportLab!")