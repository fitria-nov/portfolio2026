import os

def main():
    portfolio_dir = "/Users/fitrianovitasari/.gemini/antigravity/scratch/portfolio"
    portal_path = os.path.join(portfolio_dir, "lppm-portal.html")
    build_script_path = os.path.join(portfolio_dir, "build_portfolio.py")
    
    with open(portal_path, "r", encoding="utf-8") as f:
        portal_content = f.read()
        
    # Extract sidebar_nav_html
    sidebar_start_marker = '<div class="doc-sidebar-nav">'
    sidebar_start_idx = portal_content.find(sidebar_start_marker)
    if sidebar_start_idx == -1:
        print("Error: Could not find sidebar start marker")
        return
    sidebar_start_idx += len(sidebar_start_marker)
    
    workspace_marker = '<div class="main-workspace">'
    workspace_idx = portal_content.find(workspace_marker)
    if workspace_idx == -1:
        print("Error: Could not find main-workspace marker")
        return
        
    sidebar_nav_html = portal_content[sidebar_start_idx:workspace_idx].strip()
    
    # Strip the trailing closing </div> of doc-sidebar-nav and doc-sidebar
    if sidebar_nav_html.endswith('</div>'):
        sidebar_nav_html = sidebar_nav_html[:-len('</div>')].strip()
    if sidebar_nav_html.endswith('</div>'):
        sidebar_nav_html = sidebar_nav_html[:-len('</div>')].strip()
    
    # Extract main_content_html
    main_start_marker = '<!-- PHASE 1: CASE STUDY -->'
    main_start_idx = portal_content.find(main_start_marker)
    if main_start_idx == -1:
        print("Error: Could not find main content start marker")
        return
        
    main_end_marker = '<div class="workspace-footer">'
    main_end_idx = portal_content.find(main_end_marker, main_start_idx)
    if main_end_idx == -1:
        print("Error: Could not find main content end marker")
        return
        
    main_content_html = portal_content[main_start_idx:main_end_idx].strip()
    
    # Read build_portfolio.py
    with open(build_script_path, "r", encoding="utf-8") as f:
        build_content = f.read()
        
    # Find the range of def generate_lppm():
    gen_lppm_def = "def generate_lppm():"
    gen_lppm_start = build_content.find(gen_lppm_def)
    if gen_lppm_start == -1:
        print("Error: Could not find generate_lppm function in build script")
        return
        
    # Let's find the next function def or the end of generate_lppm
    next_def = "def "
    next_def_idx = build_content.find(next_def, gen_lppm_start + len(gen_lppm_def))
    if next_def_idx == -1:
        next_def_idx = build_content.find("if __name__", gen_lppm_start)
        
    if next_def_idx == -1:
        print("Error: Could not find end of generate_lppm function")
        return
        
    # Let's reconstruct generate_lppm() with the new strings (using standard raw-like triple quotes, no f-string)
    # Note: we use regular triple quotes inside generate_lppm, so no curly brace escaping is needed in build_portfolio.py!
    new_gen_lppm = f"""def generate_lppm():
    project_name = "SIMPPM LPMB Portal"
    title = "SIMPPM Portal: Sistem Manajemen Pengisian Pengabdian Masyarakat (PENGMAS) LPMB"
    role = "Senior Business & System Analyst"
    meta_units = "LPMB (Lembaga Pengabdian Masyarakat dan Bisnis)"
    meta_platform = "LPMB Pengmas Workflow Portal, REST API Integration & WUADC Database"
    meta_author = "Fitria Indah Novitasari"
    accent_class = "accent-amber"
    
    color_theme_style = \"\"\"
    .nav-item:hover {{
      background: #f1f5f9;
      color: var(--accent-amber);
    }}
    .nav-item.active {{
      background: var(--accent-amber-soft);
      color: var(--accent-amber);
      font-weight: 600;
    }}
    .timeline-dot {{
      border: 2px solid var(--accent-amber);
      color: var(--accent-amber);
    }}
    .section-card {{
      border-left: 5px solid var(--accent-amber);
    }}
    \"\"\"
    
    sidebar_nav_html = \"\"\"
{sidebar_nav_html}
    \"\"\"
    
    main_content_html = \"\"\"
{main_content_html}
    \"\"\"
    
    return build_html(title, project_name, role, meta_units, meta_platform, meta_author, sidebar_nav_html, main_content_html, accent_class, color_theme_style)

"""
    
    # Replace in build_portfolio.py
    updated_build_content = build_content[:gen_lppm_start] + new_gen_lppm + build_content[next_def_idx:]
    
    with open(build_script_path, "w", encoding="utf-8") as f:
        f.write(updated_build_content)
        
    print("Success: build_portfolio.py has been synchronized with lppm-portal.html changes!")

if __name__ == "__main__":
    main()
