import markdown
import os

markdown_files = [
    '/Users/fitrianovitasari/.gemini/antigravity/brain/fbe5c532-c3ac-4452-90cf-019d3091c1d1/PORTFOLIO_PART1.md',
    '/Users/fitrianovitasari/.gemini/antigravity/brain/fbe5c532-c3ac-4452-90cf-019d3091c1d1/PORTFOLIO_PART2.md',
    '/Users/fitrianovitasari/.gemini/antigravity/brain/fbe5c532-c3ac-4452-90cf-019d3091c1d1/PORTFOLIO_PART3.md'
]

content = ""
for file in markdown_files:
    if os.path.exists(file):
        with open(file, 'r', encoding='utf-8') as f:
            content += f.read() + "\n\n"

# Cleanup artifacts markdown headers
content = content.replace("# GAV SmartProcure: Business Analysis Portfolio (Part 1)", "")
content = content.replace("# GAV SmartProcure: Business Analysis Portfolio (Part 2)", "")
content = content.replace("# GAV SmartProcure: Business Analysis Portfolio (Part 3)", "")
content = content.replace("> [!NOTE]", "> **NOTE:**")

# Convert markdown to html
html_body = markdown.markdown(content, extensions=['tables'])

# Read the base template from sa-wellbe.html
with open('/Users/fitrianovitasari/.gemini/antigravity/scratch/portfolio/sa-wellbe.html', 'r', encoding='utf-8') as f:
    template_lines = f.readlines()

# Extract everything up to <body>
head_html = ""
for line in template_lines:
    head_html += line
    if "<body>" in line:
        break

nav_html = """
  <nav class="nav">
    <div style="max-width: 900px; margin: 0 auto; display: flex; justify-content: space-between;">
      <a href="index.html" class="nav-link">← Back to Portfolio</a>
      <span style="font-size: 0.9rem; font-weight: 600;">GAV SmartProcure</span>
    </div>
  </nav>
  <div class="container">
"""

cover_html = """
    <div class="cover">
      <h1>GAV SMARTPROCURE<br>ENTERPRISE SYSTEM ANALYSIS</h1>
      <p style="text-align: center; font-size: 1.2rem; color: var(--text-secondary); max-width: 650px; margin: 0 auto;">
        A comprehensive business analysis case study detailing the digital transformation of an SAP-integrated procurement and inventory management system.
      </p>
    </div>
"""

footer_html = """
  </div>
</body>
</html>
"""

final_html = head_html + nav_html + cover_html + html_body + footer_html

with open('/Users/fitrianovitasari/.gemini/antigravity/scratch/portfolio/gav-smartprocure.html', 'w', encoding='utf-8') as f:
    f.write(final_html)

print("Generated gav-smartprocure.html successfully.")
