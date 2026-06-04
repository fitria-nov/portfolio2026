import os

# Helper to create HTML template
def build_html(title, project_name, role, meta_units, meta_platform, meta_author, sidebar_nav_html, main_content_html, accent_class="accent-indigo", color_theme_style=""):
    return f"""<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width,initial-scale=1.0"/>
  <title>{title}</title>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet"/>
  <!-- Mermaid JS for diagrams -->
  <script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
  <script>
    mermaid.initialize({{ 
      startOnLoad: true, 
      theme: 'neutral',
      themeVariables: {{
        fontFamily: 'Plus Jakarta Sans',
        fontSize: '13px'
      }}
    }});
  </script>
  <style>
    :root {{
      --bg-workspace: #f8fafc;
      --bg-card: #ffffff;
      --border-color: #e2e8f0;
      
      --accent-indigo: #4f46e5;
      --accent-indigo-soft: #e0e7ff;
      --accent-teal: #0d9488;
      --accent-teal-soft: #ccfbf1;
      --accent-rose: #e11d48;
      --accent-rose-soft: #ffe4e6;
      --accent-amber: #d97706;
      --accent-amber-soft: #fef3c7;
      --accent-emerald: #10b981;
      --accent-emerald-soft: #d1fae5;
      
      --text-dark: #0f172a;
      --text-muted: #64748b;
      --sidebar-width: 320px;
    }}
    
    * {{ margin: 0; padding: 0; box-sizing: border-box; }}
    html {{ scroll-behavior: smooth; }}
    body {{ 
      font-family: 'Plus Jakarta Sans', sans-serif; 
      background: var(--bg-workspace); 
      color: var(--text-dark); 
      line-height: 1.6;
      display: flex;
      background-image: radial-gradient(#e2e8f0 1.5px, transparent 1.5px);
      background-size: 24px 24px;
    }}
    
    /* Document Sidebar / Index Table of Contents */
    .doc-sidebar {{
      position: fixed;
      top: 0;
      left: 0;
      bottom: 0;
      width: var(--sidebar-width);
      background: #ffffff;
      border-right: 1px solid var(--border-color);
      display: flex;
      flex-direction: column;
      z-index: 50;
      box-shadow: 2px 0 20px rgba(0,0,0,0.02);
    }}
    .doc-sidebar-header {{
      padding: 30px 24px;
      border-bottom: 1px solid var(--border-color);
    }}
    .doc-sidebar-header h2 {{
      font-size: 1.15rem;
      font-weight: 800;
      letter-spacing: -0.02em;
      margin-bottom: 4px;
    }}
    .doc-sidebar-header span {{
      font-size: 0.75rem;
      color: var(--text-muted);
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }}
    .doc-sidebar-nav {{
      flex: 1;
      overflow-y: auto;
      padding: 20px 16px;
    }}
    .nav-group-title {{
      font-size: 0.72rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: var(--text-muted);
      margin: 20px 0 8px 8px;
    }}
    .nav-item {{
      display: flex;
      align-items: center;
      gap: 10px;
      padding: 8px 12px;
      border-radius: 8px;
      font-size: 0.82rem;
      font-weight: 500;
      color: #475569;
      text-decoration: none;
      transition: all 0.2s ease;
      cursor: pointer;
    }}
    
    /* Theme color specific styling */
    {color_theme_style}
    
    .nav-num {{
      font-weight: 700;
      font-size: 0.75rem;
      opacity: 0.7;
    }}
    
    /* Main Content Area */
    .main-workspace {{
      margin-left: var(--sidebar-width);
      flex: 1;
      min-width: 0;
      padding: 60px 80px 100px;
    }}
    
    .workspace-header {{
      max-width: 1100px;
      margin-bottom: 60px;
      border-bottom: 2px solid var(--border-color);
      padding-bottom: 40px;
      position: relative;
    }}
    .workspace-header h1 {{
      font-size: 2.8rem;
      font-weight: 800;
      letter-spacing: -0.04em;
      line-height: 1.15;
      margin-bottom: 16px;
      color: #0f172a;
    }}
    .workspace-header p {{
      font-size: 1.15rem;
      color: var(--text-muted);
      max-width: 750px;
    }}
    .workspace-header-meta {{
      display: flex;
      gap: 20px;
      margin-top: 24px;
      font-size: 0.85rem;
      color: var(--text-muted);
    }}
    .workspace-header-meta span strong {{
      color: var(--text-dark);
    }}
    
    /* Phase Blocks & Section Styles */
    .phase-block {{
      margin-bottom: 80px;
    }}
    .phase-badge {{
      display: inline-block;
      padding: 6px 16px;
      border-radius: 99px;
      font-size: 0.75rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      margin-bottom: 20px;
    }}
    .pb-purple {{ background: var(--accent-indigo-soft); color: var(--accent-indigo); }}
    .pb-blue {{ background: #dbeafe; color: #1e40af; }}
    .pb-green {{ background: var(--accent-teal-soft); color: var(--accent-teal); }}
    .pb-amber {{ background: var(--accent-amber-soft); color: var(--accent-amber); }}
    .pb-rose {{ background: var(--accent-rose-soft); color: var(--accent-rose); }}
    .pb-emerald {{ background: var(--accent-emerald-soft); color: var(--accent-emerald); }}
    
    /* Layout Cards & Grids */
    .section-card {{
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: 16px;
      padding: 40px;
      margin-bottom: 40px;
      box-shadow: 0 4px 30px rgba(0,0,0,0.015);
      scroll-margin-top: 100px;
    }}
    .section-card h3 {{
      font-size: 1.5rem;
      font-weight: 800;
      letter-spacing: -0.02em;
      margin-bottom: 10px;
      color: var(--text-dark);
      display: flex;
      align-items: center;
      gap: 12px;
    }}
    .section-card-num {{
      color: var(--text-muted);
      font-size: 1rem;
      font-weight: 500;
    }}
    .section-card-desc {{
      font-size: 0.95rem;
      color: var(--text-muted);
      margin-bottom: 24px;
      max-width: 800px;
    }}
    
    /* Bento Grid */
    .bento-grid {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 20px;
    }}
    .bento-cell {{
      border: 1px solid var(--border-color);
      background: #fafafb;
      padding: 24px;
      border-radius: 12px;
    }}
    .bento-wide {{ grid-column: span 2; }}
    .bento-cell h4 {{ font-size: 1rem; margin-bottom: 8px; color: var(--text-dark); }}
    .bento-cell p {{ font-size: 0.88rem; color: #475569; }}
    
    /* RACI & Data Tables */
    .table-wrapper {{
      overflow-x: auto;
      border: 1px solid var(--border-color);
      border-radius: 12px;
      margin-bottom: 20px;
    }}
    table {{
      width: 100%;
      border-collapse: collapse;
      text-align: left;
      font-size: 0.88rem;
    }}
    th, td {{
      padding: 14px 20px;
      border-bottom: 1px solid var(--border-color);
    }}
    th {{
      background: #f8fafc;
      font-weight: 600;
      color: var(--text-muted);
      text-transform: uppercase;
      font-size: 0.75rem;
      letter-spacing: 0.05em;
    }}
    tr:last-child td {{ border-bottom: none; }}
    
    /* Workflow Timeline */
    .workflow-timeline {{
      display: flex;
      flex-direction: column;
      gap: 20px;
      position: relative;
      padding-left: 32px;
    }}
    .workflow-timeline::before {{
      content: '';
      position: absolute;
      left: 11px;
      top: 10px;
      bottom: 10px;
      width: 2px;
      background: var(--border-color);
    }}
    .timeline-item {{
      position: relative;
    }}
    .timeline-dot {{
      position: absolute;
      left: -32px;
      top: 6px;
      width: 24px;
      height: 24px;
      border-radius: 50%;
      background: #ffffff;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 0.7rem;
      font-weight: 800;
    }}
    .timeline-content {{
      background: #fafafb;
      padding: 16px 20px;
      border-radius: 10px;
      border: 1px solid var(--border-color);
    }}
    .timeline-content h4 {{ font-size: 0.95rem; margin-bottom: 4px; }}
    .timeline-content p {{ font-size: 0.85rem; color: var(--text-muted); }}
    
    /* Sticky Notes (UX Style) */
    .sticky-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
      gap: 20px;
      margin-top: 10px;
    }}
    .sticky-note {{
      padding: 24px;
      border-radius: 8px;
      box-shadow: 0 4px 15px rgba(0,0,0,0.03);
      position: relative;
      transform: rotate(-1deg);
      transition: all 0.2s ease;
    }}
    .sticky-note:nth-child(even) {{
      transform: rotate(1.5deg);
    }}
    .sticky-note:hover {{
      transform: scale(1.03) rotate(0deg);
      box-shadow: 0 8px 25px rgba(0,0,0,0.06);
    }}
    .sticky-note h4 {{
      font-size: 1rem;
      font-weight: 700;
      margin-bottom: 10px;
      color: #1e293b;
      border-bottom: 1px dashed rgba(0,0,0,0.1);
      padding-bottom: 6px;
    }}
    .sticky-note p {{
      font-size: 0.85rem;
      color: #334155;
    }}
    .sticky-yellow {{ background: #fef08a; border-left: 5px solid #ca8a04; }}
    .sticky-blue {{ background: #bfdbfe; border-left: 5px solid #2563eb; }}
    .sticky-green {{ background: #a7f3d0; border-left: 5px solid #059669; }}
    .sticky-rose {{ background: #fecdd3; border-left: 5px solid #e11d48; }}
    .sticky-purple {{ background: #e9d5ff; border-left: 5px solid #7c3aed; }}
    
    /* Image containers */
    .img-container {{
      background: #fafafb;
      border: 1px solid var(--border-color);
      border-radius: 12px;
      padding: 30px;
      text-align: center;
      margin-top: 20px;
    }}
    .img-container img {{
      max-width: 100%;
      height: auto;
      border-radius: 8px;
      box-shadow: 0 4px 12px rgba(0,0,0,0.05);
    }}
    .img-caption {{
      margin-top: 12px;
      font-size: 0.85rem;
      color: var(--text-muted);
      font-weight: 600;
    }}
    
    .grid-2 {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 20px;
    }}
    @media (max-width: 1024px) {{
      .grid-2 {{
        grid-template-columns: 1fr;
      }}
    }}
    
    /* Mermaid Box Styling */
    .diagram-container {{
      background: #fafafb;
      border: 1px solid var(--border-color);
      border-radius: 12px;
      padding: 30px;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      margin-top: 20px;
      overflow-x: auto;
    }}
    
    /* Tag & Badges */
    .badge {{
      display: inline-block;
      padding: 4px 10px;
      border-radius: 6px;
      font-size: 0.75rem;
      font-weight: 600;
      text-transform: uppercase;
    }}
    .badge-primary {{ background: var(--accent-indigo-soft); color: var(--accent-indigo); }}
    .badge-success {{ background: var(--accent-teal-soft); color: var(--accent-teal); }}
    .badge-danger {{ background: var(--accent-rose-soft); color: var(--accent-rose); }}
    .badge-warning {{ background: var(--accent-amber-soft); color: var(--accent-amber); }}
    
    /* Code block */
    pre {{
      background: #0f172a;
      color: #cbd5e1;
      padding: 20px;
      border-radius: 12px;
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.85rem;
      overflow-x: auto;
      margin-top: 15px;
    }}
    
    /* Footer */
    .workspace-footer {{
      text-align: center;
      padding-top: 40px;
      border-top: 1px solid var(--border-color);
      color: var(--text-muted);
      font-size: 0.85rem;
    }}
    
    /* Return Button */
    .return-btn {{
      position: absolute;
      right: 0;
      top: 10px;
      background: #ffffff;
      border: 1px solid var(--border-color);
      color: var(--text-dark);
      padding: 8px 16px;
      border-radius: 8px;
      font-size: 0.85rem;
      font-weight: 600;
      text-decoration: none;
      display: flex;
      align-items: center;
      gap: 6px;
      transition: all 0.2s;
    }}
    .return-btn:hover {{
      background: #f8fafc;
      border-color: #cbd5e1;
    }}
  </style>
</head>
<body>

<div class="doc-sidebar">
  <div class="doc-sidebar-header">
    <h2>{project_name}</h2>
    <span>{role}</span>
  </div>
  
  <div class="doc-sidebar-nav">
    {sidebar_nav_html}
  </div>
</div>

<div class="main-workspace">

  <div class="workspace-header">
    <a href="index.html" class="return-btn">← Kembali ke Portfolio</a>
    <h1>{title}</h1>
    <p>Dokumentasi portfolio profesional dan detail analisis sistem.</p>
    <div class="workspace-header-meta">
      <span>Unit Bisnis: <strong>{meta_units}</strong></span>
      <span>Platform: <strong>{meta_platform}</strong></span>
      <span>Arsitek Sistem: <strong>{meta_author}</strong></span>
    </div>
  </div>

  {main_content_html}

  <div class="workspace-footer">
    <p>&copy; 2026 {meta_author}. All Rights Reserved. Portfolio Canvas Workspace.</p>
  </div>

</div>

<script>
  // Active nav highlighting on scroll
  const sections = document.querySelectorAll('.section-card');
  const navItems = document.querySelectorAll('.nav-item');
  
  window.addEventListener('scroll', () => {{
    let current = '';
    sections.forEach(section => {{
      const sectionTop = section.offsetTop;
      const sectionHeight = section.clientHeight;
      if (pageYOffset >= (sectionTop - 150)) {{
        current = section.getAttribute('id');
      }}
    }});
    
    navItems.forEach(item => {{
      item.classList.remove('active');
      if (item.getAttribute('href') === `#${{current}}`) {{
        item.classList.add('active');
      }}
    }});
  }});
</script>

</body>
</html>
"""

def generate_gav():
    project_name = "GAV SmartProcure"
    title = "GAV SmartProcure: Enterprise Procurement & Inventory Blueprint"
    role = "Lead Enterprise System Analyst"
    meta_units = "MRO Logistics & Aircraft Engineering"
    meta_platform = "SAP ECC 6.0 EHP8 / SAP S/4HANA & OData Integrator"
    meta_author = "Fitria Indah Novitasari"
    accent_class = "accent-indigo"
    
    color_theme_style = """
    .nav-item:hover {
      background: #f1f5f9;
      color: var(--accent-indigo);
    }
    .nav-item.active {
      background: var(--accent-indigo-soft);
      color: var(--accent-indigo);
      font-weight: 600;
    }
    .timeline-dot {
      border: 2px solid var(--accent-indigo);
      color: var(--accent-indigo);
    }
    .section-card {
      border-left: 5px solid var(--accent-indigo);
    }
    """
    
    sidebar_nav_html = """
    <div class="nav-group-title">Fase 1: Discovery</div>
    <a href="#ex-summary" class="nav-item active"><span class="nav-num">01</span> Executive Summary</a>
    <a href="#biz-problem" class="nav-item"><span class="nav-num">02</span> Business Problem</a>
    <a href="#stakeholder" class="nav-item"><span class="nav-num">03</span> Stakeholder Analysis</a>
    
    <div class="nav-group-title">Fase 2: Proses Bisnis</div>
    <a href="#asis-proc" class="nav-item"><span class="nav-num">04</span> AS-IS Process</a>
    <a href="#tobe-proc" class="nav-item"><span class="nav-num">05</span> TO-BE Process</a>
    
    <div class="nav-group-title">Fase 3: Kebutuhan Sistem</div>
    <a href="#brd" class="nav-item"><span class="nav-num">06</span> BRD Overview</a>
    <a href="#func-req" class="nav-item"><span class="nav-num">07</span> Functional Specs</a>
    <a href="#nonfunc-req" class="nav-item"><span class="nav-num">08</span> Non-Functional Specs</a>
    <a href="#accept-crit" class="nav-item"><span class="nav-num">09</span> Acceptance Criteria</a>
    
    <div class="nav-group-title">Fase 4: Pemodelan UML</div>
    <a href="#usecase" class="nav-item"><span class="nav-num">10</span> Use Case Diagram</a>
    <a href="#activity" class="nav-item"><span class="nav-num">11</span> Activity Diagram</a>
    <a href="#sequence" class="nav-item"><span class="nav-num">12</span> Sequence Diagram</a>
    <a href="#dfd" class="nav-item"><span class="nav-num">13</span> DFD (Level 0 & 1)</a>
    <a href="#erd" class="nav-item"><span class="nav-num">14</span> ERD Database</a>
    <a href="#architecture" class="nav-item"><span class="nav-num">15</span> System Architecture</a>
    
    <div class="nav-group-title">Fase 5: Teknis & Integrasi</div>
    <a href="#api-doc" class="nav-item"><span class="nav-num">16</span> API Documentation</a>
    <a href="#val-rules" class="nav-item"><span class="nav-num">17</span> Validation Rules</a>
    <a href="#role-matrix" class="nav-item"><span class="nav-num">18</span> Role & RACI Matrix</a>
    <a href="#integration" class="nav-item"><span class="nav-num">19</span> Integration Flow</a>
    <a href="#exception" class="nav-item"><span class="nav-num">20</span> Exception Flow</a>
    
    <div class="nav-group-title">Fase 6: Pengujian & Risiko</div>
    <a href="#uat" class="nav-item"><span class="nav-num">21</span> UAT Test Plan</a>
    <a href="#rtm" class="nav-item"><span class="nav-num">22</span> RTM Document</a>
    <a href="#risk-reg" class="nav-item"><span class="nav-num">23</span> Risk Register</a>
    <a href="#change-req" class="nav-item"><span class="nav-num">24</span> Change Request</a>
    
    <div class="nav-group-title">Fase 7: Dampak Bisnis</div>
    <a href="#biz-impact" class="nav-item"><span class="nav-num">25</span> Business Impact</a>
    """
    
    main_content_html = """
  <!-- PHASE 1 -->
  <div class="phase-block">
    <div class="phase-badge pb-purple">Fase 1: Discovery & Initiation</div>
    
    <!-- 1. Executive Summary -->
    <div class="section-card" id="ex-summary">
      <h3><span class="section-card-num">01.</span> Executive Summary</h3>
      <p class="section-card-desc">Latar belakang bisnis penerbangan MRO dan kebutuhan kritis integrasi SAP ERP.</p>
      <div class="bento-grid">
        <div class="bento-cell bento-wide">
          <h4>Urgensi Operasional Maskapai</h4>
          <p>Dalam industri Maintenance, Repair, and Overhaul (MRO) pesawat, keterlambatan pengadaan suku cadang kritis langsung berdampak pada kondisi <strong>Aircraft On Ground (AOG)</strong>. Kerugian satu jam armada grounded mencapai <strong>$15,000 USD</strong> akibat biaya pembatalan penerbangan dan biaya parkir bandara. SmartProcure hadir sebagai jembatan web portal modern untuk mendigitalisasi proses pengadaan tanpa memaksa pengguna umum membuka SAP GUI yang rumit.</p>
        </div>
        <div class="bento-cell">
          <h4>Target KPI Bisnis</h4>
          <p style="font-size: 2.2rem; font-weight: 800; color: var(--accent-indigo); line-height: 1;">1.8 Hari</p>
          <p style="font-weight: 600; margin-top: 10px;">Rata-rata Siklus PR ke PO</p>
          <p>Memangkas birokrasi manual dari rata-rata 7.2 hari menjadi di bawah 48 jam secara otomatis.</p>
        </div>
      </div>
    </div>
    
    <!-- 2. Business Problem Analysis -->
    <div class="section-card" id="biz-problem">
      <h3><span class="section-card-num">02.</span> Business Problem Analysis (Fishbone Roots)</h3>
      <p class="section-card-desc">Analisis akar masalah pengadaan logistik hangar menggunakan diagram tulang ikan.</p>
      
      <div class="table-wrapper">
        <table>
          <thead>
            <tr>
              <th>Faktor Penyebab</th>
              <th>Detail Kendala Operasional</th>
              <th>Dampak Finansial & Teknis</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><span class="badge badge-danger">Sistem & Akses</span></td>
              <td>Mekanik di Hangar harus menulis PR manual pada logbook fisik, lalu admin logistik mengetik ulang di SAP GUI menggunakan T-Code <strong>ME51N</strong> (Create Purchase Requisition).</td>
              <td>Kesalahan input kode material (Part Number) mencapai <strong>12%</strong>, memicu salah kirim barang dari supplier.</td>
            </tr>
            <tr>
              <td><span class="badge badge-danger">Prosedur & SLA</span></td>
              <td>Proses approval memerlukan persetujuan berjenjang fisik. Jika Manager sedang bertugas di luar kota, berkas PR menumpuk di meja kerja.</td>
              <td>Waktu rilis Purchase Requisition terhambat, memaksa pembelian darurat (Spot Buy) dengan harga 20% lebih mahal.</td>
            </tr>
            <tr>
              <td><span class="badge badge-danger">Kontrol Anggaran</span></td>
              <td>Verifikasi budget cost center dilakukan secara manual oleh tim Finance melalui SAP FMBB (Budget Control System) mingguan.</td>
              <td>Over-budget pada Cost Center divisi teknik akibat komitmen pembelian yang tidak tercatat secara real-time.</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    
    <!-- 3. Stakeholder Analysis -->
    <div class="section-card" id="stakeholder">
      <h3><span class="section-card-num">03.</span> Stakeholder Analysis & RACI Matrix</h3>
      <p class="section-card-desc">Pemetaan akuntabilitas peran dalam siklus hidup dokumen transaksi PR/PO.</p>
      <div class="table-wrapper">
        <table>
          <thead>
            <tr>
              <th>Stakeholder</th>
              <th>Tanggung Jawab Teknis</th>
              <th>Kebutuhan Antarmuka Kunci</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Mekanik Hangar</strong></td>
              <td>Identifikasi kerusakan suku cadang dan input Part SKU sesuai IPC (Illustrated Parts Catalog).</td>
              <td>Katalog web dinamis, pencarian SKU cerdas, validasi otomatis Form FAA 8130-3 / EASA Form One.</td>
            </tr>
            <tr>
              <td><strong>Engineering Lead</strong></td>
              <td>Verifikasi kelayakan teknis suku cadang pengganti yang diajukan.</td>
              <td>Dashboard komparasi spesifikasi teknik material alternatif jika part utama kosong di pasaran.</td>
            </tr>
            <tr>
              <td><strong>Finance Controller</strong></td>
              <td>Audit kecukupan pagu anggaran Cost Center dan WBS (Work Breakdown Structure) proyek.</td>
              <td>Hard-block system terintegrasi modul SAP FI-FM (Funds Management) secara langsung.</td>
            </tr>
            <tr>
              <td><strong>Warehouse Officer</strong></td>
              <td>Penerimaan fisik barang (GR) dan verifikasi dokumen pengiriman dari vendor.</td>
              <td>Scan barcode nirkabel terhubung ke REST API SAP RFC untuk update kuantitas logistik.</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>

  <!-- PHASE 2 -->
  <div class="phase-block">
    <div class="phase-badge pb-blue">Fase 2: Pemetaan Proses Bisnis</div>
    
    <!-- 4. AS-IS Process -->
    <div class="section-card" id="asis-proc">
      <h3><span class="section-card-num">04.</span> AS-IS Process (Alur Manual Berjalan)</h3>
      <p class="section-card-desc">Proses birokrasi manual yang menyebabkan kemacetan logistik suku cadang pesawat.</p>
      
      <div class="workflow-timeline">
        <div class="timeline-item">
          <div class="timeline-dot">1</div>
          <div class="timeline-content">
            <h4>Pencatatan Fisik IPC Boeing/Airbus</h4>
            <p>Mekanik menyalin kode part number dari buku panduan pesawat (katalog manual) ke lembar kertas Excel PR.</p>
          </div>
        </div>
        <div class="timeline-item">
          <div class="timeline-dot">2</div>
          <div class="timeline-content">
            <h4>Persetujuan Fisik Berjenjang</h4>
            <p>Formulir dikirimkan lewat kurir internal kantor untuk meminta tanda tangan basah tim Engineering dan Finance.</p>
          </div>
        </div>
        <div class="timeline-item">
          <div class="timeline-dot">3</div>
          <div class="timeline-content">
            <h4>Rekap Manual & SAP Input</h4>
            <p>Admin logistik mengetik ulang data dari kertas ke dalam program SAP GUI via T-code <strong>ME51N</strong>.</p>
          </div>
        </div>
      </div>
    </div>
    
    <!-- 5. TO-BE Process -->
    <div class="section-card" id="tobe-proc">
      <h3><span class="section-card-num">05.</span> TO-BE Process (Alur Otomatis Integrasi SAP)</h3>
      <p class="section-card-desc">Alur transaksi digital tanpa kertas dengan validasi instan terintegrasi SAP ERP.</p>
      
      <div class="workflow-timeline">
        <div class="timeline-item">
          <div class="timeline-dot">1</div>
          <div class="timeline-content">
            <h4>E-Catalog & OCI Punchout</h4>
            <p>Mekanik memilih material secara langsung via web. Sistem mengambil data master material dari modul SAP MM.</p>
          </div>
        </div>
        <div class="timeline-item">
          <div class="timeline-dot">2</div>
          <div class="timeline-content">
            <h4>Validasi Dana Real-time</h4>
            <p>API Gateway mengirim query pengecekan ke SAP FI-FM. Transaksi otomatis ditolak jika pagu dana Cost Center habis.</p>
          </div>
        </div>
        <div class="timeline-item">
          <div class="timeline-dot">3</div>
          <div class="timeline-content">
            <h4>Rilis BAPI Otomatis</h4>
            <p>Setelah disetujui via mobile app, sistem langsung mengeksekusi BAPI pembuat PO (<strong>BAPI_PO_CREATE1</strong>) ke sistem SAP ERP.</p>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- PHASE 3 -->
  <div class="phase-block">
    <div class="phase-badge pb-green">Fase 3: Kebutuhan Sistem (BRD & Specs)</div>
    
    <!-- 6. BRD -->
    <div class="section-card" id="brd">
      <h3><span class="section-card-num">06.</span> Business Requirements (BRD Overview)</h3>
      <p class="section-card-desc">Kebutuhan level bisnis strategis untuk efisiensi rantai logistik maskapai.</p>
      <div style="background: #fafafb; padding: 24px; border-radius: 12px; border: 1px solid var(--border-color);">
        <p><strong>BR-01:</strong> Sistem harus mampu menghemat total pengeluaran operasional akibat AOG minimum <strong>15%</strong> pada tahun pertama perilisan.</p>
        <p style="margin-top: 8px;"><strong>BR-02:</strong> Validasi anggaran belanja wajib dilakukan secara real-time pada modul SAP FI-FM menggunakan RFC <strong>RFC_READ_FM_BUDGET</strong> sebelum Purchase Requisition (PR) memperoleh nomor dokumen resmi.</p>
      </div>
    </div>
    
    <!-- 7. Functional Requirements -->
    <div class="section-card" id="func-req">
      <h3><span class="section-card-num">07.</span> Functional Requirements</h3>
      <p class="section-card-desc">Spesifikasi fungsional sistem pengadaan SmartProcure.</p>
      <div class="table-wrapper">
        <table>
          <thead>
            <tr>
              <th>ID Kebutuhan</th>
              <th>Deskripsi Spesifikasi Kebutuhan</th>
              <th>Ketergantungan SAP</th>
              <th>Prioritas</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>FR-01</strong></td>
              <td>Sistem wajib mengeksekusi fungsi pemeriksaan anggaran secara real-time sebelum rilis transaksi PR.</td>
              <td>Modul SAP FI-FM (Funds Management)</td>
              <td><span class="badge badge-danger">Critical</span></td>
            </tr>
            <tr>
              <td><strong>FR-02</strong></td>
              <td>Sistem wajib mengirimkan notifikasi mobile push notification ke perangkat ponsel pintar manager.</td>
              <td>Firebase Cloud Messaging (FCM)</td>
              <td><span class="badge badge-primary">High</span></td>
            </tr>
            <tr>
              <td><strong>FR-03</strong></td>
              <td>Sistem wajib mengeksekusi update persediaan logistik di SAP MM setelah gudang memindai QR barang.</td>
              <td>BAPI_GOODSMVT_CREATE (MIGO)</td>
              <td><span class="badge badge-success">Medium</span></td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    
    <!-- 8. Non-Functional Requirements -->
    <div class="section-card" id="nonfunc-req">
      <h3><span class="section-card-num">08.</span> Non-Functional Requirements</h3>
      <p class="section-card-desc">Parameter performa, keandalan, dan keamanan sistem pengadaan.</p>
      <div class="bento-grid">
        <div class="bento-cell">
          <h4>Waktu Respon (SLA)</h4>
          <p>Waktu respon API Gateway dari web portal ke SAP PI/PO integrasi hub tidak boleh melebihi <strong>2.2 detik</strong>.</p>
        </div>
        <div class="bento-cell">
          <h4>Enkripsi Data</h4>
          <p>Seluruh pertukaran payload data JSON/XML wajib dienkripsi dengan standar <strong>AES-256-GCM</strong>.</p>
        </div>
        <div class="bento-cell">
          <h4>Skalabilitas</h4>
          <p>Sistem harus stabil menangani hingga <strong>12,000 request PR</strong> secara simultan selama periode puncak liburan.</p>
        </div>
      </div>
    </div>
    
    <!-- 9. Acceptance Criteria -->
    <div class="section-card" id="accept-crit">
      <h3><span class="section-card-num">09.</span> Acceptance Criteria (Gherkin Scenario)</h3>
      <p class="section-card-desc">Kriteria pengujian fitur pengecekan anggaran menggunakan struktur Given-When-Then.</p>
      <pre>Scenario: Percobaan Transaksi PR Melebihi Anggaran Cost Center
  Given Mekanik mengajukan PR untuk part "MAIN GEAR WHEEL" seharga IDR 750,000,000
  And Sisa pagu anggaran Cost Center "CC_MRO_ENG" di SAP FM adalah IDR 500,000,000
  When Mekanik mengklik tombol "Kirim Pengajuan"
  Then Sistem memunculkan pesan error "Transaksi Dihentikan: Anggaran Kurang Sebesar IDR 250,000,000"
  And Status dokumen PR dibatalkan secara otomatis</pre>
    </div>
  </div>

  <!-- PHASE 4 -->
  <div class="phase-block">
    <div class="phase-badge pb-amber">Fase 4: Pemodelan UML & Arsitektur</div>
    
    <!-- 10. Use Case Diagram -->
    <div class="section-card" id="usecase">
      <h3><span class="section-card-num">10.</span> Use Case Diagram</h3>
      <p class="section-card-desc">Pemetaan interaksi pengguna terhadap fitur inti SmartProcure.</p>
      <div class="diagram-container">
        <div class="mermaid">
          graph LR
            Mekanik((Mekanik Hangar)) --> UC1(Buat Pengajuan PR)
            Mekanik --> UC2(Cek Katalog OCI)
            Manager((Manager Approval)) --> UC3(Persetujuan Mobile)
            Warehouse((Warehouse Staff)) --> UC4(Konfirmasi GR MIGO)
            UC1 -.->|include| UC5(Validasi Budget SAP FI-FM)
            UC3 -.->|include| UC6(Trigger BAPI PO Create)
        </div>
      </div>
    </div>
    
    <!-- 11. Activity Diagram -->
    <div class="section-card" id="activity">
      <h3><span class="section-card-num">11.</span> Activity Diagram</h3>
      <p class="section-card-desc">Alur logis aktivitas verifikasi transaksi PR.</p>
      <div class="diagram-container">
        <div class="mermaid">
          stateDiagram-v2
            [*] --> InputFormPR
            InputFormPR --> KirimValidasi
            state KirimValidasi <<choice>>
            KirimValidasi --> TampilkanPeringatan : jika Budget SAP Kurang
            KirimValidasi --> CariApprovalManager : jika Budget Cukup
            TampilkanPeringatan --> [*]
            CariApprovalManager --> KeputusanManager
            state KeputusanManager <<choice>>
            KeputusanManager --> CancelPR : jika Ditolak
            KeputusanManager --> GenerateSAP_PO : jika Disetujui
            CancelPR --> [*]
            GenerateSAP_PO --> [*]
        </div>
      </div>
    </div>
    
    <!-- 12. Sequence Diagram -->
    <div class="section-card" id="sequence">
      <h3><span class="section-card-num">12.</span> Sequence Diagram</h3>
      <p class="section-card-desc">Sekuen panggilan API real-time dari portal ke modul SAP ERP.</p>
      <div class="diagram-container">
        <div class="mermaid">
          sequenceDiagram
            actor Mekanik as Mekanik Hangar
            participant Web as Portal Web
            participant Gate as API Gateway (Kong)
            participant SAP as SAP ERP Core (HANA)
            
            Mekanik->>Web: Submit PR Form
            Web->>Gate: POST /api/v1/pr
            Gate->>SAP: Call RFC_READ_FM_BUDGET
            SAP-->>Gate: Return Budget State (IDR 50M)
            alt Anggaran Kurang
                Gate-->>Web: 400 Bad Request (Overbudget)
                Web-->>Mekanik: Tampilkan Peringatan Anggaran Habis
            else Anggaran Cukup
                Gate->>SAP: Call BAPI_PR_CREATE
                SAP-->>Gate: Return PR Number (10002931)
                Gate-->>Web: 201 Created
                Web-->>Mekanik: Tampilkan Status Sukses
            end
        </div>
      </div>
    </div>
    
    <!-- 13. DFD -->
    <div class="section-card" id="dfd">
      <h3><span class="section-card-num">13.</span> Data Flow Diagram (DFD Level 0)</h3>
      <p class="section-card-desc">Aliran data antar entitas eksternal dengan sistem SmartProcure.</p>
      <div class="diagram-container">
        <div class="mermaid">
          graph LR
            Mekanik[Mekanik Hangar] -->|Kirim Formulir PR| Sys((SmartProcure))
            Sys -->|Kirim Informasi PR| Manager[Manager Engineering]
            Manager -->|Kirim Keputusan Persetujuan| Sys
            Sys <-->|Call RFC Check & BAPI| SAP[SAP Core ERP]
            Sys -->|Kirim PO Resmi| Vendor[Vendor Eksternal]
        </div>
      </div>
    </div>
    
    <!-- 14. ERD -->
    <div class="section-card" id="erd">
      <h3><span class="section-card-num">14.</span> Entity Relationship Diagram (ERD Schema)</h3>
      <p class="section-card-desc">Relasi tabel database lokal untuk buffer data transaksi sebelum didorong ke SAP.</p>
      <div class="diagram-container">
        <div class="mermaid">
          erDiagram
            PEGAWAI ||--o{ PR_HEADER : submits
            PR_HEADER ||--|{ PR_ITEM : contains
            MATERIAL_MASTER ||--o{ PR_ITEM : references
            PR_HEADER ||--o| PO_HEADER : generates
            
            PEGAWAI {
              int id PK
              string nama
              string cost_center
            }
            PR_HEADER {
              int pr_id PK
              int pegawai_id FK
              string sap_pr_number
              float total_amount
              string status
            }
            PR_ITEM {
              int item_id PK
              int pr_id FK
              string sku_part_number FK
              int qty
            }
            MATERIAL_MASTER {
              string sku_part_number PK
              string deskripsi
              string unit_measure
            }
        </div>
      </div>
    </div>
    
    <!-- 15. High-Level Architecture -->
    <div class="section-card" id="architecture">
      <h3><span class="section-card-num">15.</span> High-Level Architecture Blueprint</h3>
      <p class="section-card-desc">Arsitektur integrasi sistem, middleware, dan modul ERP SAP.</p>
      <div class="diagram-container">
        <div class="mermaid">
          graph TD
            App[Web & Mobile Client] -->|HTTPS REST| GW[API Gateway Kong]
            GW -->|JSON Payload| NodeApp[Express Node.js Cluster]
            NodeApp -->|Session Buffer| PG[(PostgreSQL AppDB)]
            NodeApp -->|SOAP XML / RFC| SAP_PI{SAP PI/PO Integration Hub}
            SAP_PI <-->|SAP BAPI Connection| SAP_ERP[(SAP ECC 6.0 EHP8 ERP Core)]
        </div>
      </div>
    </div>
  </div>

  <!-- PHASE 5 -->
  <div class="phase-block">
    <div class="phase-badge pb-rose">Fase 5: Spesifikasi Teknis & Integrasi</div>
    
    <!-- 16. API Documentation -->
    <div class="section-card" id="api-doc">
      <h3><span class="section-card-num">16.</span> API Documentation (Integration Endpoint)</h3>
      <p class="section-card-desc">Payload input untuk interaksi data transaksi PR dari API Gateway ke middleware.</p>
      
      <strong>REST Endpoint:</strong> <code style="background:#e2e8f0; padding:2px 6px; border-radius:4px; font-family:'JetBrains Mono';">POST /api/v1/purchase-requisition</code>
      <pre>{
  "employee_id": 44920,
  "cost_center": "CC_MRO_ENG",
  "wbs_element": "WBS-737-LANDINGGEAR",
  "items": [
    {
      "part_number": "411W5101-1",
      "qty": 1,
      "unit": "PC",
      "estimated_price_idr": 450000000.00
    }
  ]
}</pre>
    </div>
    
    <!-- 17. Validation Rules -->
    <div class="section-card" id="val-rules">
      <h3><span class="section-card-num">17.</span> Validation Rules</h3>
      <p class="section-card-desc">Aturan validasi input guna menjamin konsistensi data sebelum masuk ke SAP database.</p>
      <div class="table-wrapper">
        <table>
          <thead>
            <tr>
              <th>Aturan Validasi</th>
              <th>Kriteria Sistem</th>
              <th>Pesan Kesalahan (Error Message)</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Cost Center Lock</td>
              <td>Cost Center wajib terdaftar aktif di modul SAP FI/CO master data.</td>
              <td>CC_BLOCKED: Cost Center Diblokir/Tidak Terdaftar</td>
            </tr>
            <tr>
              <td>Part SKU Match</td>
              <td>Kode part number harus sesuai dengan master data SAP MM.</td>
              <td>SKU_INVALID: Part Number Tidak Dikenali di SAP MM</td>
            </tr>
            <tr>
              <td>Regulatory Document</td>
              <td>Dokumen PR bernilai > $10k wajib melampirkan Form EASA/FAA.</td>
              <td>DOC_MISSING: Form Sertifikasi Kelayakan Diperlukan</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    
    <!-- 18. Role Matrix -->
    <div class="section-card" id="role-matrix">
      <h3><span class="section-card-num">18.</span> Role & RACI Matrix</h3>
      <p class="section-card-desc">Pengaturan kontrol akses berbasis peran (RBAC) pada sistem pengadaan.</p>
      <div class="table-wrapper">
        <table>
          <thead>
            <tr>
              <th>Fitur / Aksi</th>
              <th>Mekanik Hangar</th>
              <th>Engineering Lead</th>
              <th>VP Finance</th>
              <th>SAP Admin</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Akses Katalog OCI</td>
              <td><span class="badge badge-success">Full Access</span></td>
              <td><span class="badge badge-primary">Read</span></td>
              <td>-</td>
              <td><span class="badge badge-warning">Maintain</span></td>
            </tr>
            <tr>
              <td>Rilis PR &lt; IDR 50jt</td>
              <td>-</td>
              <td><span class="badge badge-success">Approve</span></td>
              <td>-</td>
              <td>-</td>
            </tr>
            <tr>
              <td>Rilis PR &gt; IDR 500jt</td>
              <td>-</td>
              <td>-</td>
              <td><span class="badge badge-danger">Approve</span></td>
              <td>-</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    
    <!-- 19. Integration Flow -->
    <div class="section-card" id="integration">
      <h3><span class="section-card-num">19.</span> Integration Flow Detail</h3>
      <p class="section-card-desc">Aliran pertukaran data sinkronisasi API dari server logistik ke SAP gateway.</p>
      <div class="diagram-container">
        <div class="mermaid">
          flowchart TD
            Client[Aplikasi SmartProcure] -->|REST JSON| GW[API Gateway Kong]
            GW -->|SOAP XML Mapping| PI[SAP PI/PO Integration Hub]
            PI -->|Call RFC| ERP[(SAP ECC HANA Core)]
            ERP -->|Konfirmasi Sukses PR/PO| PI
            PI -->|Kembalikan Response JSON| GW
            GW -->|Tampilkan Nomor PR/PO| Client
        </div>
      </div>
    </div>
    
    <!-- 20. Exception Flow -->
    <div class="section-card" id="exception">
      <h3><span class="section-card-num">20.</span> Exception Flow (Mitigasi Downtime)</h3>
      <p class="section-card-desc">Sistem cadangan ketika integrasi API SAP mengalami gangguan.</p>
      <div style="background: #fff5f5; border: 1px solid #fecaca; border-radius: 12px; padding: 24px;">
        <p style="color: #991b1b; font-weight: 700; margin-bottom: 8px;">Kebijakan API Offline (SAP ERP Down Mitigation):</p>
        <p style="color: #7f1d1d; font-size: 0.9rem;">Apabila server integrasi SAP tidak merespon dalam waktu 5 detik (Timeout), sistem akan otomatis mengaktifkan antrean cadangan (Message Queue) berbasis Apache Kafka. Dokumen PR disimpan secara lokal berstatus "Offline Queue", dan tim IT akan menerima peringatan otomatis via Discord Webhook untuk audit manual.</p>
      </div>
    </div>
  </div>

  <!-- PHASE 6 -->
  <div class="phase-block">
    <div class="phase-badge pb-purple">Fase 6: Pengujian & Manajemen Perubahan</div>
    
    <!-- 21. UAT -->
    <div class="section-card" id="uat">
      <h3><span class="section-card-num">21.</span> UAT Test Plan</h3>
      <p class="section-card-desc">Daftar kasus uji penerimaan pengguna sebelum rilis ke server produksi.</p>
      <div class="table-wrapper">
        <table>
          <thead>
            <tr>
              <th>ID Uji</th>
              <th>Target Pengujian</th>
              <th>Langkah Eksperimen</th>
              <th>Ekspektasi Hasil</th>
              <th>Status</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>UAT-001</td>
              <td>Pengecekan Anggaran SAP FI-FM</td>
              <td>Kirim PR dengan nilai melebihi limit Cost Center.</td>
              <td>Sistem memblokir pengajuan dan menampilkan pesan anggaran kurang.</td>
              <td><span class="badge badge-success">Passed</span></td>
            </tr>
            <tr>
              <td>UAT-002</td>
              <td>Bypass Emergency AOG</td>
              <td>Kirim PR berstatus kritis tanpa lampiran Form Sertifikasi.</td>
              <td>Sistem menolak dokumen dan meminta upload file pendukung.</td>
              <td><span class="badge badge-success">Passed</span></td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    
    <!-- 22. RTM -->
    <div class="section-card" id="rtm">
      <h3><span class="section-card-num">22.</span> Requirements Traceability Matrix (RTM)</h3>
      <p class="section-card-desc">Matriks penelusuran dari dokumen bisnis kebutuhan (BR) hingga kasus uji UAT.</p>
      <div class="table-wrapper">
        <table>
          <thead>
            <tr>
              <th>ID Kebutuhan Bisnis</th>
              <th>ID Fungsional (FR)</th>
              <th>Modul Integrasi</th>
              <th>Kode Test Case UAT</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>BR-01 (AOG Prevention)</td>
              <td>FR-02 (Mobile Approval Routing)</td>
              <td>Workflow Engine Gateway</td>
              <td>UAT-003 (Mobile Push & Sign)</td>
            </tr>
            <tr>
              <td>BR-02 (Financial Audit)</td>
              <td>FR-01 (Real-time Budget Check)</td>
              <td>SAP RFC FI-FM Interface</td>
              <td>UAT-001 (Pengecekan Anggaran)</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    
    <!-- 23. Risk Register -->
    <div class="section-card" id="risk-reg">
      <h3><span class="section-card-num">23.</span> Risk Register</h3>
      <p class="section-card-desc">Analisis mitigasi terhadap potensi kendala proyek selama migrasi sistem.</p>
      <div class="table-wrapper">
        <table>
          <thead>
            <tr>
              <th>Deskripsi Risiko</th>
              <th>Level Dampak</th>
              <th>Skenario Dampak</th>
              <th>Rencana Mitigasi</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Gagal Koneksi OData SAP Gateway</td>
              <td><span class="badge badge-danger">Tinggi</span></td>
              <td>Logistik material hangar lumpuh, PO tidak terbit.</td>
              <td>Sediakan offline-buffer queue di internal database portal.</td>
            </tr>
            <tr>
              <td>Penolakan Adaptasi Mekanik Senior</td>
              <td><span class="badge badge-warning">Sedang</span></td>
              <td>Mekanik kembali menggunakan formulir Excel manual.</td>
              <td>Sediakan pendampingan onsite di hangar selama 30 hari pertama.</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    
    <!-- 24. Change Request -->
    <div class="section-card" id="change-req">
      <h3><span class="section-card-num">24.</span> Change Request Document</h3>
      <p class="section-card-desc">Formulir permohonan perubahan lingkup fitur paska fase 1 rilis.</p>
      <div style="background: #fafafb; border: 1px solid var(--border-color); border-radius: 12px; padding: 24px;">
        <p><strong>CR Nomor:</strong> CR-MRO-2026-009</p>
        <p><strong>Deskripsi Perubahan:</strong> Penambahan modul konversi kurs mata uang asing otomatis (USD ke IDR) terintegrasi SAP Bank Master Data untuk transaksi pembelian suku cadang luar negeri.</p>
        <p style="margin-top: 10px;"><strong>Status Analisis Dampak:</strong> <span class="badge badge-warning">Under Review</span> (Dampak terhadap performa endpoint RFC SAP FI).</p>
      </div>
    </div>
  </div>

  <!-- PHASE 7 -->
  <div class="phase-block">
    <div class="phase-badge pb-emerald">Fase 7: Dampak Bisnis (ROI)</div>
    
    <!-- 25. Business Impact Analysis -->
    <div class="section-card" id="biz-impact">
      <h3><span class="section-card-num">25.</span> Business Impact Analysis</h3>
      <p class="section-card-desc">Dampak riil transformasi sistem terhadap KPI operasional maskapai.</p>
      
      <div class="bento-grid">
        <div class="bento-cell">
          <h4>SLA Efisiensi Logistik</h4>
          <p style="font-size: 2.2rem; font-weight: 800; color: var(--accent-teal); line-height: 1;">-75%</p>
          <p style="font-weight: 600; margin-top: 10px;">Siklus PR ke PO</p>
          <p>Pemangkasan alur rilis material dari rata-rata 7.2 hari menjadi kurang dari 40 jam kerja.</p>
        </div>
        <div class="bento-cell">
          <h4>Audit Keuangan</h4>
          <p style="font-size: 2.2rem; font-weight: 800; color: var(--accent-teal); line-height: 1;">100%</p>
          <p style="font-weight: 600; margin-top: 10px;">Akurasi Anggaran</p>
          <p>Zero instances of over-budget spending di Cost Center hangar berkat modul FM hard-block.</p>
        </div>
        <div class="bento-cell">
          <h4>Akurasi Fisik Stok</h4>
          <p style="font-size: 2.2rem; font-weight: 800; color: var(--accent-teal); line-height: 1;">99.85%</p>
          <p style="font-weight: 600; margin-top: 10px;">Kesesuaian SAP MM</p>
          <p>Mengeliminasi selisih stok gudang melalui entri real-time GR pemindaian barcode mobile.</p>
        </div>
      </div>
    </div>
  </div>
    """
    
    return build_html(title, project_name, role, meta_units, meta_platform, meta_author, sidebar_nav_html, main_content_html, accent_class, color_theme_style)

def generate_srs():
    project_name = "Well-Be Care App"
    title = "SRS Well-Be Care App: Alzheimer Patient Monitoring Specification"
    role = "UI/UX & Requirements Engineer"
    meta_units = "Healthcare Technology Research & Development"
    meta_platform = "WearOS Smartwatch, Android & iOS Mobile Client with Firebase Cloud Backend"
    meta_author = "Fitria Indah Novitasari"
    accent_class = "accent-teal"
    
    color_theme_style = """
    .nav-item:hover {
      background: #f1f5f9;
      color: var(--accent-teal);
    }
    .nav-item.active {
      background: var(--accent-teal-soft);
      color: var(--accent-teal);
      font-weight: 600;
    }
    .timeline-dot {
      border: 2px solid var(--accent-teal);
      color: var(--accent-teal);
    }
    .section-card {
      border-left: 5px solid var(--accent-teal);
    }
    """
    
    sidebar_nav_html = """
    <div class="nav-group-title">Fase 1: Introduction</div>
    <a href="#purpose" class="nav-item active"><span class="nav-num">1.1</span> Purpose & Tujuan</a>
    <a href="#scope" class="nav-item"><span class="nav-num">1.2</span> Scope & Deskripsi</a>
    <a href="#definitions" class="nav-item"><span class="nav-num">1.3</span> Definitions & Acronyms</a>
    
    <div class="nav-group-title">Fase 2: Product Perspective</div>
    <a href="#architecture" class="nav-item"><span class="nav-num">2.1</span> Architecture Diagram</a>
    <a href="#usecase" class="nav-item"><span class="nav-num">2.2</span> Use Case Specification</a>
    
    <div class="nav-group-title">Fase 3: Requirements</div>
    <a href="#nonfunctional" class="nav-item"><span class="nav-num">2.3</span> Non-Functional Req</a>
    <a href="#user-classes" class="nav-item"><span class="nav-num">2.4</span> User Classes</a>
    <a href="#constraints" class="nav-item"><span class="nav-num">2.5</span> Design Constraints</a>
    <a href="#assumptions" class="nav-item"><span class="nav-num">2.6</span> Assumptions & Deps</a>
    
    <div class="nav-group-title">Fase 4: Appendix & UML</div>
    <a href="#dfd-appendix" class="nav-item"><span class="nav-num">2.7</span> DFD level 0, 1, 2</a>
    <a href="#cdm-pdm" class="nav-item"><span class="nav-num">2.8</span> CDM & PDM Diagram</a>
    <a href="#sequence-diagrams" class="nav-item"><span class="nav-num">2.9</span> Sequence Diagrams</a>
    <a href="#user-stories" class="nav-item"><span class="nav-num">2.10</span> User Story & Scenarios</a>
    """
    
    main_content_html = """
  <!-- FASE 1: INTRODUCTION -->
  <div class="phase-block">
    <div class="phase-badge pb-purple">Fase 1: Introduction & Scope</div>
    
    <!-- 1.1 Purpose -->
    <div class="section-card" id="purpose">
      <h3><span class="section-card-num">1.1.</span> Purpose & Tujuan Penulisan</h3>
      <p class="section-card-desc">Tujuan utama penyusunan dokumen SRS Well-Be Application untuk perawatan Alzheimer.</p>
      <div class="bento-grid">
        <div class="bento-cell bento-wide">
          <h4>Ringkasan Keseluruhan Aplikasi</h4>
          <p>Aplikasi <strong>Well-Be</strong> adalah inovasi teknologi yang proaktif untuk memantau lansia penderita demensia, Alzheimer, dan penurunan daya ingat. Aplikasi ini memiliki fitur penunjang kualitas hidup pasien dan mengurangi beban kerja perawat/keluarga, seperti fitur Linimasa momen hangat lansia dan monitoring pelacak GPS secara real-time.</p>
        </div>
        <div class="bento-cell">
          <h4>Audiens Utama</h4>
          <p>Dokumen ini ditujukan bagi <strong>Product Manager, Developers, Insinyur QA, Ahli Hukum Kesehatan</strong>, serta tim perancang perangkat medis untuk memastikan kepatuhan regulasi dan standar kualitas.</p>
        </div>
      </div>
    </div>
    
    <!-- 1.2 Scope -->
    <div class="section-card" id="scope">
      <h3><span class="section-card-num">1.2.</span> Product Scope & Operating Environment</h3>
      <p class="section-card-desc">Definisi cakupan produk, batas operasional, serta batasan umum pengembangan.</p>
      <div class="bento-grid">
        <div class="bento-cell">
          <h4>Cakupan Sistem</h4>
          <p>Pelacakan lokasi real-time dengan GPS, sinkronisasi jam pintar, perekaman data kesehatan dasar, dan manajemen kenangan/moments terpadu.</p>
        </div>
        <div class="bento-cell">
          <h4>Lingkungan Operasional</h4>
          <p>Aplikasi mobile berjalan pada <strong>Android 8.0 (Oreo)+</strong> dan <strong>iOS 12.0+</strong> dengan koneksi internet konstan dan integrasi GPS internal.</p>
        </div>
        <div class="bento-cell">
          <h4>Evaluasi Kualitas Hidup</h4>
          <p>Pengumpulan data aktivitas fisik harian, pola tidur, dan perilaku kognitif subjektif guna mengurangi stres perawat (Caregiver Burden).</p>
        </div>
      </div>
    </div>
    
    <!-- 1.3 Definitions -->
    <div class="section-card" id="definitions">
      <h3><span class="section-card-num">1.3.</span> Definitions, Acronyms, and Abbreviations</h3>
      <p class="section-card-desc">Glosarium istilah teknis yang digunakan di dalam dokumen.</p>
      <div class="table-wrapper">
        <table>
          <thead>
            <tr>
              <th>Istilah/Akronim</th>
              <th>Definisi Lengkap</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>SRS</strong></td>
              <td>Software Requirements Specifications: Dokumen spesifikasi kebutuhan sistem.</td>
            </tr>
            <tr>
              <td><strong>GPS</strong></td>
              <td>Global Positioning System: Sistem berbasis satelit untuk penentuan koordinat lokasi geografis.</td>
            </tr>
            <tr>
              <td><strong>Caregiver</strong></td>
              <td>Pengasuh atau wali yang bertanggung jawab penuh merawat pasien demensia sehari-hari.</td>
            </tr>
            <tr>
              <td><strong>Geofencing</strong></td>
              <td>Batas perimeter geografis virtual yang jika dilanggar akan mengirimkan alarm ke perawat.</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>

  <!-- FASE 2: PRODUCT PERSPECTIVE -->
  <div class="phase-block">
    <div class="phase-badge pb-blue">Fase 2: Product Perspective & Function</div>
    
    <!-- 2.1 Architecture Diagram -->
    <div class="section-card" id="architecture">
      <h3><span class="section-card-num">2.1.</span> Product Perspective (Arsitektur Sistem)</h3>
      <p class="section-card-desc">Diagram visual perspektif produk yang menunjukkan arsitektur dari aplikasi Well-Be.</p>
      <div class="img-container">
        <img src="img/srs_diagrams/page4_img1.png" alt="Architecture Diagram"/>
        <div class="img-caption">Gambar 2.1: Perspektif Arsitektur Sistem Well-Be Application</div>
      </div>
    </div>
    
    <!-- 2.2 Use Case Specification -->
    <div class="section-card" id="usecase">
      <h3><span class="section-card-num">2.2.</span> Use Case Specifications</h3>
      <p class="section-card-desc">Diagram fungsional sistem dan penjelasan rinci interaksi aktor.</p>
      
      <div class="img-container">
        <img src="img/srs_diagrams/page5_img1.png" alt="Use Case Diagram"/>
        <div class="img-caption">Gambar 2.2: Use Case Diagram Well-Be App</div>
      </div>
      
      <h4 style="margin: 30px 0 15px; font-size:1.1rem; color:var(--text-dark);">Detail Spesifikasi Use Case Kunci:</h4>
      
      <div class="table-wrapper">
        <table>
          <thead>
            <tr>
              <th>Fitur / Use Case</th>
              <th>Aktor Utama</th>
              <th>Prasyarat (Precondition)</th>
              <th>Alur Utama (Basic Path)</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Melacak Lokasi dengan GPS</strong></td>
              <td>Keluarga, Pengasuh, Smartwatch</td>
              <td>Smartwatch terpasang di pergelangan tangan pasien dan terhubung ke GPS aktif.</td>
              <td>1. Smartwatch mengirim koordinat ke server.<br>2. Aplikasi perawat mengambil data real-time.<br>3. Peta menampilkan penanda lokasi pasien.</td>
            </tr>
            <tr>
              <td><strong>Mengelola Memories (Linimasa)</strong></td>
              <td>Pasien, Keluarga, Pengasuh</td>
              <td>Pengguna telah login dan memiliki hak akses ke modul kenangan pasien.</td>
              <td>1. Aktor mengunggah foto/catatan momen bahagia.<br>2. Sistem memberi stempel waktu otomatis.<br>3. Momen ditampilkan berurutan di linimasa.</td>
            </tr>
            <tr>
              <td><strong>Pencatatan Catatan Kesehatan</strong></td>
              <td>Pengasuh, Keluarga, Admin</td>
              <td>Akses modul kesehatan diaktifkan untuk akun perawat.</td>
              <td>1. Perawat mencatat asupan obat, waktu tidur, atau insiden.<br>2. Data disimpan ke server Cloud secara aman.</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>

  <!-- FASE 3: REQUIREMENTS & CONSTRAINTS -->
  <div class="phase-block">
    <div class="phase-badge pb-green">Fase 3: Kebutuhan Sistem & Batasan</div>
    
    <!-- 2.3 Non-Functional Requirements -->
    <div class="section-card" id="nonfunctional">
      <h3><span class="section-card-num">2.3.</span> Non-Functional Requirements</h3>
      <p class="section-card-desc">Persyaratan kualitas non-fungsional berdasarkan standar kualitas ISO/IEC 25010.</p>
      <div class="table-wrapper">
        <table>
          <thead>
            <tr>
              <th>Dimensi Kualitas</th>
              <th>Deskripsi Spesifikasi Kebutuhan</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Functional Suitability</strong></td>
              <td>Keakuratan lokasi koordinat GPS berada di bawah toleransi selisih 5 meter. Kelengkapan fitur pelacakan, linimasa, dan alarm darurat wajib terpenuhi 100%.</td>
            </tr>
            <tr>
              <td><strong>Performance Efficiency</strong></td>
              <td>SLA waktu respon pengambilan data lokasi ke peta maksimal 5 detik pada koneksi internet seluler selambat 4G/LTE.</td>
            </tr>
            <tr>
              <td><strong>Compatibility</strong></td>
              <td>Mampu diinstal pada Android 8.0+ dan iOS 12.0+ serta kompatibel dengan Apple Watch dan WearOS Smartwatches.</td>
            </tr>
            <tr>
              <td><strong>Security & Privacy</strong></td>
              <td>Enkripsi data pribadi pasien (PII) saat diam (at rest) dan berpindah (in transit) menggunakan cipher enkripsi AES-256 dan protokol SSL/TLS.</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    
    <!-- 2.4 User Classes -->
    <div class="section-card" id="user-classes">
      <h3><span class="section-card-num">2.4.</span> User Classes and Characteristics</h3>
      <p class="section-card-desc">Segmentasi karakteristik pengguna akhir aplikasi Well-Be.</p>
      <div class="bento-grid">
        <div class="bento-cell">
          <h4>1. Administrator</h4>
          <p>Memiliki literasi IT tinggi, bertugas memantau server, mengelola database pengguna, mengekspor laporan bulanan, dan audit log keamanan.</p>
        </div>
        <div class="bento-cell">
          <h4>2. Pengasuh (Caregiver)</h4>
          <p>Mempunyai pemahaman dasar aplikasi mobile, memantau pergerakan lansia secara harian, dan menerima alarm geofencing.</p>
        </div>
        <div class="bento-cell">
          <h4>3. Pasien & Keluarga</h4>
          <p>Keluarga mengakses info medis, mengelola dokumen memori pasien. Lansia (pasien) berinteraksi dengan visual sederhana (satu-klik) pada smartwatch.</p>
        </div>
      </div>
    </div>
    
    <!-- 2.5 Constraints -->
    <div class="section-card" id="constraints">
      <h3><span class="section-card-num">2.5.</span> Design and Implementation Constraints</h3>
      <p class="section-card-desc">Aturan dan batasan teknis yang mengikat arsitektur desain perangkat lunak.</p>
      <div class="bento-grid">
        <div class="bento-cell bento-wide">
          <h4>Regulatory & Security Compliance</h4>
          <p>Aplikasi wajib mematuhi standar kerahasiaan data rekam medis pasien sesuai <strong>UU Pelindungan Data Pribadi (UU PDP)</strong> serta regulasi internasional medis seperti <strong>GDPR / HIPAA</strong> untuk ekspor data medis eksternal.</p>
        </div>
        <div class="bento-cell">
          <h4>Hardware Constraints</h4>
          <p>Aplikasi Smartwatch harus hemat daya agar tidak menghabiskan baterai pelacak dalam waktu kurang dari 24 jam pengoperasian aktif.</p>
        </div>
      </div>
    </div>
    
    <!-- 2.6 Assumptions -->
    <div class="section-card" id="assumptions">
      <h3><span class="section-card-num">2.6.</span> Assumptions and Dependencies</h3>
      <p class="section-card-desc">Faktor asumsi eksternal dan ketergantungan sistem.</p>
      <div class="table-wrapper">
        <table>
          <thead>
            <tr>
              <th>Asumsi Pengembangan</th>
              <th>Ketergantungan Sistem (Dependencies)</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Pengguna perawat memiliki smartphone pribadi yang terhubung dengan paket data internet aktif.</td>
              <td>Sistem bergantung pada API Google Maps / Apple Maps untuk me-render peta geofencing secara visual.</td>
            </tr>
            <tr>
              <td>Literasi teknologi keluarga cukup untuk melakukan setup integrasi bluetooth smartwatch mandiri.</td>
              <td>Kompatibilitas dipengaruhi oleh pembaharuan patch keamanan OS Android/iOS pihak ketiga.</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>

  <!-- FASE 4: APPENDIX & UML -->
  <div class="phase-block">
    <div class="phase-badge pb-rose">Fase 4: Appendix & Pemodelan Teknis</div>
    
    <!-- 2.7 DFD Appendix -->
    <div class="section-card" id="dfd-appendix">
      <h3><span class="section-card-num">2.7.</span> Data Flow Diagram (DFD)</h3>
      <p class="section-card-desc">Detail aliran data transaksi sistem Well-Be untuk Level 0, Level 1, dan Level 2.</p>
      
      <div class="img-container">
        <img src="img/srs_diagrams/page18_img1.png" alt="DFD Level 0"/>
        <div class="img-caption">Gambar 2.7.1: DFD Level 0 (Context Diagram)</div>
      </div>
      
      <div class="img-container" style="margin-top:40px;">
        <img src="img/srs_diagrams/page19_img1.png" alt="DFD Level 1"/>
        <div class="img-caption">Gambar 2.7.2: DFD Level 1 (Overview Sistem)</div>
      </div>
      
      <div class="grid-2" style="margin-top:40px;">
        <div class="img-container">
          <img src="img/srs_diagrams/page20_img1.png" alt="DFD Level 2 Mengelola Pengguna"/>
          <div class="img-caption">Gambar 2.7.3: DFD Level 2 (Mengelola Pengguna)</div>
        </div>
        <div class="img-container">
          <img src="img/srs_diagrams/page20_img2.png" alt="DFD Level 2 Notification"/>
          <div class="img-caption">Gambar 2.7.4: DFD Level 2 (Notification Service)</div>
        </div>
      </div>
    </div>
    
    <!-- 2.8 CDM & PDM -->
    <div class="section-card" id="cdm-pdm">
      <h3><span class="section-card-num">2.8.</span> CDM & PDM Schema</h3>
      <p class="section-card-desc">Skema konseptual (CDM) dan fisikal (PDM) relasi database sistem.</p>
      
      <div class="img-container">
        <img src="img/srs_diagrams/page21_img1.png" alt="Conceptual Data Model (CDM)"/>
        <div class="img-caption">Gambar 2.8.1: Conceptual Data Model (CDM) Schema</div>
      </div>
      
      <div class="img-container" style="margin-top:40px;">
        <img src="img/srs_diagrams/page21_img2.png" alt="Physical Data Model (PDM)"/>
        <div class="img-caption">Gambar 2.8.2: Physical Data Model (PDM) Schema</div>
      </div>
    </div>
    
    <!-- 2.9 Sequence Diagrams -->
    <div class="section-card" id="sequence-diagrams">
      <h3><span class="section-card-num">2.9.</span> Sequence Diagrams</h3>
      <p class="section-card-desc">Urunan diagram sekuensial interaksi aktor dan sistem dalam runtime.</p>
      
      <h4 style="margin:20px 0 10px; font-size:1rem; color:var(--text-dark);">Sekuens Admin:</h4>
      <div class="grid-2">
        <div class="img-container">
          <img src="img/srs_diagrams/page22_img1.png" alt="Sequence Admin a"/>
          <div class="img-caption">a. Mengelola Memories Pasien</div>
        </div>
        <div class="img-container">
          <img src="img/srs_diagrams/page23_img1.png" alt="Sequence Admin b"/>
          <div class="img-caption">b. Mengelola Data Pasien</div>
        </div>
      </div>
      <div class="grid-2" style="margin-top:20px;">
        <div class="img-container">
          <img src="img/srs_diagrams/page24_img1.png" alt="Sequence Admin c"/>
          <div class="img-caption">c. Mengelola Progress Kesehatan</div>
        </div>
        <div class="img-container">
          <img src="img/srs_diagrams/page25_img1.png" alt="Sequence Admin d"/>
          <div class="img-caption">d. Mengelola Log Lokasi Real-time</div>
        </div>
      </div>
      
      <h4 style="margin:40px 0 10px; font-size:1rem; color:var(--text-dark);">Sekuens Keluarga:</h4>
      <div class="grid-2">
        <div class="img-container">
          <img src="img/srs_diagrams/page26_img1.png" alt="Sequence Keluarga a"/>
          <div class="img-caption">a. Integrasi Smartwatch (Input)</div>
        </div>
        <div class="img-container">
          <img src="img/srs_diagrams/page27_img1.png" alt="Sequence Keluarga b"/>
          <div class="img-caption">b. Integrasi Smartwatch (GPS)</div>
        </div>
      </div>
      <div class="grid-2" style="margin-top:20px;">
        <div class="img-container">
          <img src="img/srs_diagrams/page28_img1.png" alt="Sequence Keluarga c"/>
          <div class="img-caption">c. Mengelola Memories</div>
        </div>
        <div class="img-container">
          <img src="img/srs_diagrams/page29_img1.png" alt="Sequence Keluarga d"/>
          <div class="img-caption">d. Mengelola Catatan Kesehatan</div>
        </div>
      </div>
      
      <h4 style="margin:40px 0 10px; font-size:1rem; color:var(--text-dark);">Sekuens Pengasuh, Pasien, & Smartwatch:</h4>
      <div class="grid-2">
        <div class="img-container">
          <img src="img/srs_diagrams/page31_img1.png" alt="Sequence Pengasuh a"/>
          <div class="img-caption">Pengasuh: Menerima Notifikasi</div>
        </div>
        <div class="img-container">
          <img src="img/srs_diagrams/page32_img2.png" alt="Sequence Smartwatch a"/>
          <div class="img-caption">Smartwatch: Tampil Biodata Singkat</div>
        </div>
      </div>
    </div>
    
    <!-- 2.10 User Stories -->
    <div class="section-card" id="user-stories">
      <h3><span class="section-card-num">2.10.</span> User Stories & Scenarios</h3>
      <p class="section-card-desc">Skenario penggunaan sistem oleh berbagai peran pengguna.</p>
      <div class="table-wrapper">
        <table>
          <thead>
            <tr>
              <th>Peran Pengguna</th>
              <th>Kebutuhan User Story</th>
              <th>Skenario Kasus Uji</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Pengasuh (Caregiver)</strong></td>
              <td>"Saya ingin memantau keberadaan pasien saya dengan real-time agar bisa merespon cepat jika berada di area berbahaya."</td>
              <td>1. Pengguna login.<br>2. Buka modul pelacakan.<br>3. Sistem memperbarui titik koordinat pasien otomatis.</td>
            </tr>
            <tr>
              <td><strong>Keluarga</strong></td>
              <td>"Saya ingin mengunggah dan melihat momen indah pasien pada linimasa untuk membantunya mengingat memori penting."</td>
              <td>1. Buka menu linimasa.<br>2. Klik unggah gambar kenangan.<br>3. Gambar masuk ke katalog memories.</td>
            </tr>
          </tbody>
        </table>
      </div>
      
      <div style="background: #fafafb; border: 1px solid var(--border-color); border-radius: 12px; padding: 24px; margin-top:20px; text-align:center;">
        <p><strong>Akses Figma Desain Antarmuka:</strong></p>
        <a href="https://www.figma.com/design/Aa6INxCDc2vmNrIezTfcsO/GUI-Will-be?node-id=0-1&t=ZgsoWkNLg5SAI5e6-1" target="_blank" style="display:inline-block; margin-top:10px; background: var(--accent-teal); color:white; padding:12px 24px; border-radius:8px; font-weight:700;">Buka Link Desain Figma GUI &rarr;</a>
      </div>
    </div>
  </div>
    """
    
    return build_html(title, project_name, role, meta_units, meta_platform, meta_author, sidebar_nav_html, main_content_html, accent_class, color_theme_style)

def generate_psdp():
    project_name = "Ketan Bersaudara ERP"
    title = "Ketan Bersaudara: ERP Odoo Implementation Blueprint"
    role = "Enterprise System Analyst"
    meta_units = "Food & Beverage Retail Operations"
    meta_platform = "Odoo ERP (Manufacturing, Inventory, Quality, Marketing, CRM & POS Modules)"
    meta_author = "Fitria Indah Novitasari"
    accent_class = "accent-emerald"
    
    color_theme_style = """
    .nav-item:hover {
      background: #f1f5f9;
      color: var(--accent-emerald);
    }
    .nav-item.active {
      background: var(--accent-emerald-soft);
      color: var(--accent-emerald);
      font-weight: 600;
    }
    .timeline-dot {
      border: 2px solid var(--accent-emerald);
      color: var(--accent-emerald);
    }
    .section-card {
      border-left: 5px solid var(--accent-emerald);
    }
    """
    
    sidebar_nav_html = """
    <div class="nav-group-title">Fase 1: Case Study</div>
    <a href="#general-overview" class="nav-item active"><span class="nav-num">1.1</span> Gambaran Perusahaan</a>
    <a href="#org-structure" class="nav-item"><span class="nav-num">1.2</span> Struktur Organisasi</a>
    <a href="#current-system" class="nav-item"><span class="nav-num">1.3</span> Sistem Saat Ini</a>
    
    <div class="nav-group-title">Fase 2: Tantangan & Strategi</div>
    <a href="#challenges" class="nav-item"><span class="nav-num">2.1</span> Tantangan Operasional</a>
    <a href="#marketing-strat" class="nav-item"><span class="nav-num">2.2</span> Strategi Pemasaran</a>
    <a href="#recommendations" class="nav-item"><span class="nav-num">2.3</span> Rekomendasi Sistem</a>
    
    <div class="nav-group-title">Fase 3: Modul Production</div>
    <a href="#production-func" class="nav-item"><span class="nav-num">3.1</span> Fungsi Produksi</a>
    <a href="#products-list" class="nav-item"><span class="nav-num">3.2</span> Daftar Produk & Bahan</a>
    <a href="#bom-spec" class="nav-item"><span class="nav-num">3.3</span> Bill of Materials (BoM)</a>
    
    <div class="nav-group-title">Fase 4: Logistik & Quality</div>
    <a href="#inventory-func" class="nav-item"><span class="nav-num">4.1</span> Fungsi Inventaris</a>
    <a href="#mo-process" class="nav-item"><span class="nav-num">4.2</span> Manufacturing Order</a>
    <a href="#quality-control" class="nav-item"><span class="nav-num">4.3</span> Quality Control Specs</a>
    <a href="#stock-reporting" class="nav-item"><span class="nav-num">4.4</span> Laporan Stok</a>
    
    <div class="nav-group-title">Fase 5: Marketing & Sales</div>
    <a href="#marketing-sales-exploration" class="nav-item"><span class="nav-num">5.1</span> Overview Odoo CRM</a>
    <a href="#email-events" class="nav-item"><span class="nav-num">5.2</span> Email Marketing & Events</a>
    <a href="#survey-sms" class="nav-item"><span class="nav-num">5.3</span> Feedback Survey & SMS</a>
    <a href="#sales-pos" class="nav-item"><span class="nav-num">5.4</span> Sales Workflow & POS</a>
    <a href="#crm-dashboard" class="nav-item"><span class="nav-num">5.5</span> CRM Pipeline & Dashboard</a>
    
    <div class="nav-group-title">Fase 6: Pemodelan BPMN</div>
    <a href="#bpmn-sales-asis" class="nav-item"><span class="nav-num">6.1</span> BPMN Sales As-Is</a>
    <a href="#bpmn-sales-tobe" class="nav-item"><span class="nav-num">6.2</span> BPMN Sales To-Be</a>
    <a href="#bpmn-prod-asis" class="nav-item"><span class="nav-num">6.3</span> BPMN Production As-Is</a>
    <a href="#bpmn-prod-tobe" class="nav-item"><span class="nav-num">6.4</span> BPMN Production To-Be</a>
    <a href="#system-comparison" class="nav-item"><span class="nav-num">6.5</span> Perbandingan As-Is vs To-Be</a>
    
    <div class="nav-group-title">Fase 7: Kesimpulan & Saran</div>
    <a href="#kesimpulan" class="nav-item"><span class="nav-num">7.1</span> Kesimpulan Hasil</a>
    <a href="#saran" class="nav-item"><span class="nav-num">7.2</span> Saran Pengembangan</a>
    """
    
    main_content_html = """
  <!-- PHASE 1: CASE STUDY -->
  <div class="phase-block">
    <div class="phase-badge pb-purple">Fase 1: Case Study & Context</div>
    
    <!-- 1.1 Gambaran Umum -->
    <div class="section-card" id="general-overview">
      <h3><span class="section-card-num">1.1.</span> Gambaran Umum Perusahaan</h3>
      <p class="section-card-desc">Konteks bisnis F&B tradisional-modern Ketan Bersaudara.</p>
      <div class="bento-grid">
        <div class="bento-cell bento-wide">
          <h4>Ketan Bersaudara di Pasar Tunjungan</h4>
          <p><strong>Ketan Bersaudara</strong> adalah usaha kuliner di sektor F&B (Food & Beverage) yang berfokus pada makanan penutup tradisional (dessert). Berlokasi di Pasar Tunjungan, Surabaya, usaha ini dimiliki oleh Koko Nico dengan mitra operasional Cece Olivia. Konsep yang diusung memadukan ketan tradisional dengan aneka topping modern untuk menghadirkan pengalaman kuliner yang kekinian dan unik bagi konsumen lokal.</p>
        </div>
        <div class="bento-cell">
          <h4>Lokasi & Target Pasar</h4>
          <p>Pasar Tunjungan, Surabaya. Menargetkan generasi muda, pecinta kuliner tradisional-modern, dan turis lokal yang mencari citra rasa khas setempat dengan penyajian estetik.</p>
        </div>
      </div>
    </div>
    
    <!-- 1.2 Struktur Organisasi -->
    <div class="section-card" id="org-structure">
      <h3><span class="section-card-num">1.2.</span> Struktur Organisasi</h3>
      <p class="section-card-desc">Pemetaan peran operasional yang masih bersifat informal.</p>
      <p>Struktur organisasi Ketan Bersaudara bersifat informal dan sederhana. Pengawasan operasional harian dilakukan langsung oleh Pemilik (Koko Nico) dan Mitra Operasional (Cece Olivia). Staf di toko menjalankan peran ganda (kasir, juru masak, pelayan, petugas kebersihan) tanpa adanya divisi formal. Kondisi ini memicu ketergantungan pada satu titik (single point of failure) untuk tugas-tugas kritis di gerai.</p>
    </div>
    
    <!-- 1.3 Sistem Saat Ini -->
    <div class="section-card" id="current-system">
      <h3><span class="section-card-num">1.3.</span> Sistem Operasional yang Digunakan Saat Ini (Sebelum ERP)</h3>
      <p class="section-card-desc">Tiga sistem utama yang berjalan secara terpisah tanpa sinkronisasi terpusat.</p>
      <div class="sticky-grid">
        <div class="sticky-note sticky-yellow">
          <h4>1. POS Mandiri</h4>
          <p>Sistem Point of Sale berbasis langganan bulanan digunakan untuk mencatat transaksi dan pengelolaan kasir cabang.</p>
        </div>
        <div class="sticky-note sticky-blue">
          <h4>2. Pelaporan Manual</h4>
          <p>Laporan penjualan diekspor ke Microsoft Excel secara harian. Pemantauan toko didukung oleh sistem CCTV harian.</p>
        </div>
        <div class="sticky-note sticky-green">
          <h4>3. Absensi Terbatas</h4>
          <p>Kehadiran staf dicatat melalui login manual sistem POS dengan memasukkan ID, kata sandi, dan foto.</p>
        </div>
      </div>
    </div>
  </div>

  <!-- PHASE 2: TANTANGAN & STRATEGI -->
  <div class="phase-block">
    <div class="phase-badge pb-blue">Fase 2: Tantangan Operasional & Rekomendasi</div>
    
    <!-- 2.1 Tantangan -->
    <div class="section-card" id="challenges">
      <h3><span class="section-card-num">2.1.</span> Tantangan Operasional Bisnis</h3>
      <p class="section-card-desc">Daftar kendala utama yang menghambat efisiensi operasional Ketan Bersaudara.</p>
      <div class="table-wrapper">
        <table>
          <thead>
            <tr>
              <th>Area Kendala</th>
              <th>Deskripsi Masalah</th>
              <th>Dampak Operasional</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Pengelolaan Stok</strong></td>
              <td>Pemeriksaan sediaan stok tidak teratur dan sangat bergantung pada kehadiran fisik owner.</td>
              <td>Sering terjadi kehabisan bahan baku secara mendadak.</td>
            </tr>
            <tr>
              <td><strong>Pengadaan Reaktif</strong></td>
              <td>Pembelian bahan baku (seperti gula dan susu) dilakukan ad-hoc setelah stok benar-benar habis.</td>
              <td>Siklus operasional terhenti dan terpaksa membeli eceran dengan harga mahal.</td>
            </tr>
            <tr>
              <td><strong>Ketidakjelasan Peran</strong></td>
              <td>Tanggung jawab pendelegasian tugas antar staf dapur, kasir, dan pelayan belum terdefinisi formal.</td>
              <td>Akuntabilitas kerja staf rendah dan efisiensi kerja menurun.</td>
            </tr>
            <tr>
              <td><strong>Absensi SDM</strong></td>
              <td>Sistem login POS tidak memiliki fitur pembagian shift kerja, penugasan harian, dan pencatatan telat.</td>
              <td>Kesulitan mengelola kehadiran dan jam kerja karyawan secara transparan.</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    
    <!-- 2.2 Strategi Pemasaran -->
    <div class="section-card" id="marketing-strat">
      <h3><span class="section-card-num">2.2.</span> Strategi Pemasaran</h3>
      <p class="section-card-desc">Promosi digital untuk membangun brand awareness.</p>
      <div class="bento-grid">
        <div class="bento-cell">
          <h4>Instagram Marketing</h4>
          <p>Fokus pada estetika foto produk ketan kekinian untuk menarik perhatian audiens muda lokal di Surabaya.</p>
        </div>
        <div class="bento-cell">
          <h4>TikTok Tren Video</h4>
          <p>Memanfaatkan video pendek bertema kuliner estetik untuk menjangkau viralitas organik secara luas.</p>
        </div>
        <div class="bento-cell">
          <h4>Kemitraan Influencer</h4>
          <p>Bekerja sama dengan mikro-influencer kuliner Surabaya untuk memicu ulasan jujur dan kunjungan langsung ke gerai.</p>
        </div>
      </div>
    </div>
    
    <!-- 2.3 Rekomendasi -->
    <div class="section-card" id="recommendations">
      <h3><span class="section-card-num">2.3.</span> Rekomendasi Pengembangan Sistem (Odoo ERP)</h3>
      <p class="section-card-desc">Solusi integrasi bisnis menggunakan Odoo ERP.</p>
      <div class="sticky-grid">
        <div class="sticky-note sticky-rose">
          <h4>ERP Terintegrasi</h4>
          <p>Menghubungkan POS kasir, manajemen stok gudang, pengadaan barang, dan logistik produksi dalam satu platform Odoo.</p>
        </div>
        <div class="sticky-note sticky-purple">
          <h4>Standarisasi Peran</h4>
          <p>Mendefinisikan alur tanggung jawab formal untuk pengecekan persediaan minimum bahan baku.</p>
        </div>
        <div class="sticky-note sticky-yellow">
          <h4>Sistem Penjadwalan</h4>
          <p>Menerapkan modul absensi digital terintegrasi kalender shift kerja dan modul pelaporan KPI di Odoo.</p>
        </div>
      </div>
    </div>
  </div>

  <!-- PHASE 3: MODUL PRODUCTION -->
  <div class="phase-block">
    <div class="phase-badge pb-green">Fase 3: Modul Production (Odoo Manufacturing)</div>
    
    <!-- 3.1 Fungsi Produksi -->
    <div class="section-card" id="production-func">
      <h3><span class="section-card-num">3.1.</span> Fungsi Produksi (Manufacturing Module)</h3>
      <p class="section-card-desc">Bagaimana Odoo mengelola siklus pembuatan ketan dari pesanan masuk.</p>
      <p>Modul Manufacturing Odoo memproses pesanan penjualan dari Point of Sale untuk diterjemahkan menjadi Manufacturing Order secara otomatis. Sistem akan langsung mencocokkan ketersediaan bahan baku di gudang dengan resep standar (Bill of Materials), lalu memotong jumlah persediaan secara real-time saat produksi selesai.</p>
    </div>
    
    <!-- 3.2 Daftar Produk -->
    <div class="section-card" id="products-list">
      <h3><span class="section-card-num">3.2.</span> Daftar Produk Jadi & Bahan Baku</h3>
      <p class="section-card-desc">Pendaftaran 47 item produk dan bahan pembantu di dalam database Odoo.</p>
      <p>Ketan Bersaudara mendaftarkan 47 jenis item produk jadi dan bahan baku di dalam sistem, meliputi produk siap saji seperti Ketan Bersaudara Signature, Ketan Bingsu, Ketan Bowl, Ketan Susu, Ketan Durian, Bingsu Strawberry, serta bahan mentah (Ketan Putih, Susu, Susu Kental Manis, Es Batu, Es Krim, Strawberry, Gula, Santan, Selasih, dll).</p>
      
      <div class="img-container">
        <img src="img/psdp_diagrams/page4_img1.jpeg" alt="Daftar Produk Odoo 1"/>
        <div class="img-caption">Gambar 2.1: Tampilan Daftar Produk Jadi & Bahan Baku di Odoo (Bagian 1)</div>
      </div>
      <div class="grid-2" style="margin-top: 20px;">
        <div class="img-container">
          <img src="img/psdp_diagrams/page5_img1.jpeg" alt="Daftar Produk Odoo 2"/>
          <div class="img-caption">Gambar 2.2: Tampilan Daftar Produk (Bagian 2)</div>
        </div>
        <div class="img-container">
          <img src="img/psdp_diagrams/page5_img2.jpeg" alt="Daftar Produk Odoo 3"/>
          <div class="img-caption">Gambar 2.3: Tampilan Daftar Produk (Bagian 3)</div>
        </div>
      </div>
    </div>
    
    <!-- 3.3 BoM Spec -->
    <div class="section-card" id="bom-spec">
      <h3><span class="section-card-num">3.3.</span> Bill of Materials (BoM / Resep Baku)</h3>
      <p class="section-card-desc">Komposisi bahan baku untuk memproduksi 1 unit menu jadi.</p>
      <p>Terdapat 10 BoM aktif di dalam sistem. Contoh detail komposisi resep untuk <strong>1 unit Ketan Susu</strong>: Ketan Putih (1.00 unit) + Susu (1.00 unit) + Susu Kental Manis (1.00 unit). Apabila pesanan Ketan Susu tervalidasi, sistem otomatis mengurangi ketiga bahan tersebut.</p>
      
      <div class="img-container">
        <img src="img/psdp_diagrams/page5_img3.jpeg" alt="Bill of Materials Odoo"/>
        <div class="img-caption">Gambar 2.4: Daftar Konfigurasi Bill of Materials (BoM) di Odoo</div>
      </div>
    </div>
  </div>

  <!-- PHASE 4: LOGISTIK & QUALITY -->
  <div class="phase-block">
    <div class="phase-badge pb-amber">Fase 4: Logistik, Inventaris, & Quality Control</div>
    
    <!-- 4.1 Inventaris -->
    <div class="section-card" id="inventory-func">
      <h3><span class="section-card-num">4.1.</span> Fungsi Inventaris (Inventory Module)</h3>
      <p class="section-card-desc">Pencatatan persediaan bahan baku secara real-time di gudang.</p>
      <p>Modul Inventory Odoo memelihara database stok bahan baku di gerai Pasar Tunjungan secara akurat. Input stok awal dilakukan menggunakan fitur physical inventory untuk 36 bahan baku utama. Integrasi penuh dengan modul produksi memastikan setiap bahan baku yang dikonsumsi untuk Manufacturing Order langsung tercatat keluar dari kartu stok digital.</p>
      
      <div class="img-container">
        <img src="img/psdp_diagrams/page6_img1.jpeg" alt="Stok On Hand Gudang"/>
        <div class="img-caption">Gambar 2.6: Tampilan Saldo Persediaan Bahan Baku (Stock On Hand) di Odoo</div>
      </div>
    </div>
    
    <!-- 4.2 MO Process -->
    <div class="section-card" id="mo-process">
      <h3><span class="section-card-num">4.2.</span> Proses Manufacturing Order (MO)</h3>
      <p class="section-card-desc">Alur pembuatan dan konfirmasi perintah produksi.</p>
      <p>Ketika transaksi POS tervalidasi, MO berkode <strong>WH/MO/00001</strong> terbuat secara otomatis untuk melacak proses produksi menu seperti Bingsu Strawberry (2 unit). Status MO berpindah dari Draft -> Confirmed -> Done, memicu pemotongan bahan baku mentah (Ketan Putih, Susu, Strawberry, dll) secara instan.</p>
      
      <div class="grid-2">
        <div class="img-container">
          <img src="img/psdp_diagrams/page6_img2.jpeg" alt="Manufacturing Order Detail"/>
          <div class="img-caption">Gambar 2.7: Formulir Detail Perintah Produksi (MO) di Odoo</div>
        </div>
        <div class="img-container">
          <img src="img/psdp_diagrams/page6_img3.jpeg" alt="MO Completed"/>
          <div class="img-caption">Gambar 2.8: Status Penyelesaian Order Produksi (Done)</div>
        </div>
      </div>
    </div>
    
    <!-- 4.3 Quality Control -->
    <div class="section-card" id="quality-control">
      <h3><span class="section-card-num">4.3.</span> Spesifikasi Quality Control</h3>
      <p class="section-card-desc">Mekanisme pemeriksaan kualitas sajian sebelum diantar ke pelanggan.</p>
      <p>Modul Quality di Odoo mendukung standarisasi rasa dan kebersihan piring saji Ketan Bersaudara. Konfigurasi Quality Control Point (<strong>QCP00001</strong>) dipasang pada menu Bingsu Strawberry. Pemeriksaan kualitas menggunakan metode <strong>Pass/Fail</strong> oleh Main Quality Team guna menjamin estetika topping dan kesegaran es krim sebelum divalidasi ke pelanggan.</p>
      
      <div class="grid-2">
        <div class="img-container">
          <img src="img/psdp_diagrams/page7_img1.jpeg" alt="Quality Check Form"/>
          <div class="img-caption">Gambar 2.9: Antarmuka Verifikasi Kualitas (Quality Check) di Odoo</div>
        </div>
        <div class="img-container">
          <img src="img/psdp_diagrams/page7_img2.jpeg" alt="QCP Config"/>
          <div class="img-caption">Gambar 2.10: Konfigurasi Titik Kontrol Kualitas (QCP00001)</div>
        </div>
      </div>
    </div>
    
    <!-- 4.4 Laporan Stok -->
    <div class="section-card" id="stock-reporting">
      <h3><span class="section-card-num">4.4.</span> Laporan Stok & Replenishment</h3>
      <p class="section-card-desc">Sistem monitoring stok kritis bagi owner.</p>
      <p>Melalui fitur Reporting -> Inventory at Date, owner dapat melihat daftar On Hand, Free to Use, dan Incoming stock. Terdapat tombol replenishment cepat di samping barang kritis (seperti Air Mineral atau Es Krim) agar tim gudang dapat langsung membuat purchase request bahan tanpa harus menunggu owner datang ke toko.</p>
      
      <div class="img-container">
        <img src="img/psdp_diagrams/page8_img1.jpeg" alt="Laporan Stok Inventory"/>
        <div class="img-caption">Gambar 2.11: Tampilan Laporan Stok Real-Time & Riwayat Mutasi di Odoo</div>
      </div>
    </div>
  </div>

  <!-- PHASE 5: MARKETING & SALES -->
  <div class="phase-block">
    <div class="phase-badge pb-rose">Fase 5: Eksplorasi Modul Marketing & Sales</div>
    
    <!-- 5.1 Overview -->
    <div class="section-card" id="marketing-sales-exploration">
      <h3><span class="section-card-num">5.1.</span> Overview Odoo Marketing & CRM</h3>
      <p class="section-card-desc">Digitalisasi promosi dan penjualan untuk mendorong loyalitas konsumen.</p>
      <p>Ketan Bersaudara memanfaatkan modul Odoo CRM (ketan-bersaudara.odoo.com) untuk mengelola prospek pelanggan dari saluran digital, meluncurkan blast promosi teratur, membuat event spesial, mengelola database transaksi kasir POS, dan memantau KPI omset harian melalui dashboard visual terintegrasi.</p>
    </div>
    
    <!-- 5.2 Email & Events -->
    <div class="section-card" id="email-events">
      <h3><span class="section-card-num">5.2.</span> Email Marketing & Modul Events</h3>
      <p class="section-card-desc">Manajemen kampanye email massal dan koordinasi acara luring.</p>
      <p>Modul Email Marketing digunakan untuk mengirim welcome email berisi kode diskon 10% (<strong>KETANBARU10</strong>). Modul Events mengoordinasikan acara "Grand Opening & Free Tasting" di Pasar Tunjungan (25 April 2026, kapasitas 200 peserta). Integrasi kedua modul memastikan pendaftar acara luring langsung masuk ke dalam kontak langganan email promosi.</p>
      
      <div class="grid-2">
        <div class="img-container">
          <img src="img/psdp_diagrams/page16_img1.jpeg" alt="Email Marketing Blast"/>
          <div class="img-caption">Gambar 5.1: Kampanye Email Massal di Odoo</div>
        </div>
        <div class="img-container">
          <img src="img/psdp_diagrams/page17_img1.jpeg" alt="Email Editor"/>
          <div class="img-caption">Gambar 5.2: Desain Drag-and-Drop Email Editor</div>
        </div>
      </div>
      <div class="grid-2" style="margin-top: 20px;">
        <div class="img-container">
          <img src="img/psdp_diagrams/page18_img1.jpeg" alt="Events Management"/>
          <div class="img-caption">Gambar 5.3: Manajemen Penjadwalan Acara (Events)</div>
        </div>
        <div class="img-container">
          <img src="img/psdp_diagrams/page18_img2.jpeg" alt="Events Registration"/>
          <div class="img-caption">Gambar 5.4: Form Detail Tiket & Registrasi Acara</div>
        </div>
      </div>
    </div>
    
    <!-- 5.3 Survey & SMS -->
    <div class="section-card" id="survey-sms">
      <h3><span class="section-card-num">5.3.</span> Feedback Survey & SMS Marketing</h3>
      <p class="section-card-desc">Pengukuran NPS kepuasan pelanggan dan blast SMS terarah.</p>
      <p>Modul Survey mengumpulkan masukan konsumen secara berkala menggunakan pertanyaan terstruktur berbasis NPS (Net Promoter Score). Modul SMS Marketing dimanfaatkan untuk blast promosi instan (misal: "Beli 2 porsi, GRATIS 1 topping tambahan, berlaku s/d Rabu") langsung ke ponsel pelanggan yang terdaftar.</p>
      
      <div class="grid-2">
        <div class="img-container">
          <img src="img/psdp_diagrams/page18_img3.jpeg" alt="Survey Form"/>
          <div class="img-caption">Gambar 5.8: Pembuatan Kuesioner Kepuasan Konsumen</div>
        </div>
        <div class="img-container">
          <img src="img/psdp_diagrams/page19_img1.jpeg" alt="Survey Share"/>
          <div class="img-caption">Gambar 5.9: Tombol Distribusi Tautan Survei</div>
        </div>
      </div>
      <div class="grid-2" style="margin-top: 20px;">
        <div class="img-container">
          <img src="img/psdp_diagrams/page19_img2.jpeg" alt="Survey Preview"/>
          <div class="img-caption">Gambar 5.10: Tampilan Kuesioner di Layar Konsumen</div>
        </div>
        <div class="img-container">
          <img src="img/psdp_diagrams/page20_img1.jpeg" alt="Survey Results"/>
          <div class="img-caption">Gambar 5.12: Dashboard Ringkasan Hasil Analisis Survei</div>
        </div>
      </div>
    </div>
    
    <!-- 5.4 Sales & POS -->
    <div class="section-card" id="sales-pos">
      <h3><span class="section-card-num">5.4.</span> Modul Sales & Point of Sale (POS)</h3>
      <p class="section-card-desc">Dokumentasi transaksi penjualan luring di meja kasir Pasar Tunjungan.</p>
      <p>Alur modul Sales mengelola pesanan formal (Quotation -> Sales Order -> Invoice -> PAID). Sementara modul POS berjalan sebagai mesin kasir layar sentuh di gerai, mendukung pencatatan identitas konsumen setia, penambahan detail pesanan, metode bayar nontunai (QRIS/Debit), dan cetak struk instan.</p>
      
      <div class="grid-2">
        <div class="img-container">
          <img src="img/psdp_diagrams/page21_img1.jpeg" alt="Sales Quotation"/>
          <div class="img-caption">Gambar 5.14: Formulir Pembuatan Quotation (Penawaran)</div>
        </div>
        <div class="img-container">
          <img src="img/psdp_diagrams/page21_img2.jpeg" alt="Invoice Generate"/>
          <div class="img-caption">Gambar 5.15: Dialog Pembuatan Faktur (Invoice)</div>
        </div>
      </div>
      <div class="grid-2" style="margin-top: 20px;">
        <div class="img-container">
          <img src="img/psdp_diagrams/page21_img3.jpeg" alt="Invoice Proforma"/>
          <div class="img-caption">Gambar 5.16: Tampilan Faktur Proforma</div>
        </div>
        <div class="img-container">
          <img src="img/psdp_diagrams/page22_img1.jpeg" alt="Invoice Paid"/>
          <div class="img-caption">Gambar 5.17: Status Faktur Lunas (PAID) dengan Stempel Sistem</div>
        </div>
      </div>
      <div class="grid-2" style="margin-top: 20px;">
        <div class="img-container">
          <img src="img/psdp_diagrams/page22_img2.jpeg" alt="POS Dashboard"/>
          <div class="img-caption">Gambar 5.18: Dashboard Utama Point of Sale (POS)</div>
        </div>
        <div class="img-container">
          <img src="img/psdp_diagrams/page23_img1.jpeg" alt="POS Product Add"/>
          <div class="img-caption">Gambar 5.19: Form Pendaftaran Produk Baru di POS</div>
        </div>
      </div>
    </div>
    
    <!-- 5.5 CRM & Dashboard -->
    <div class="section-card" id="crm-dashboard">
      <h3><span class="section-card-num">5.5.</span> CRM Pipeline & Pelaporan Dashboard</h3>
      <p class="section-card-desc">Visualisasi grafik kinerja bisnis dan prospek hubungan pelanggan.</p>
      <p>Modul CRM melacak prospek calon kemitraan atau pelanggan loyal melalui tahapan pipeline (New -> Qualified -> Proposition -> Won). Modul Dashboard merangkum metrik finansial, produk terlaris (Best Category / SKU), total omset harian, dan metrik gudang secara grafis.</p>
      
      <div class="grid-2">
        <div class="img-container">
          <img src="img/psdp_diagrams/page24_img1.jpeg" alt="Dashboard Sales Charts"/>
          <div class="img-caption">Gambar 5.23: Visualisasi Grafik Pendapatan & Kinerja Gudang</div>
        </div>
        <div class="img-container">
          <img src="img/psdp_diagrams/page24_img2.jpeg" alt="CRM Pipeline stage"/>
          <div class="img-caption">Gambar 5.24: Tampilan Papan Kanban Tahapan Prospek CRM</div>
        </div>
      </div>
    </div>
  </div>

  <!-- PHASE 6: PEMODELAN BPMN -->
  <div class="phase-block">
    <div class="phase-badge pb-amber">Fase 6: Pemodelan Alur Kerja Bisnis (BPMN)</div>
    
    <!-- 6.1 BPMN Sales As-Is -->
    <div class="section-card" id="bpmn-sales-asis">
      <h3><span class="section-card-num">6.1.</span> BPMN As-Is Marketing & Sales (Sebelum ERP)</h3>
      <p class="section-card-desc">Alur penjualan lama yang lambat dan didominasi pencatatan manual harian.</p>
      <p>Sebelum implementasi ERP Odoo, alur pemesanan dan pemasaran berjalan terfragmentasi. Kasir mencatat pesanan, memeriksa bahan secara fisik ke dapur, memasak secara manual, dan owner melakukan rekap penjualan harian dari kertas struk kasir.</p>
      
      <div class="img-container">
        <img src="img/psdp_diagrams/page9_img1.jpeg" alt="BPMN Sales As-Is"/>
        <div class="img-caption">Gambar 3.1: Diagram Alur Proses Bisnis Penjualan Manual (As-Is)</div>
      </div>
    </div>
    
    <!-- 6.2 BPMN Sales To-Be -->
    <div class="section-card" id="bpmn-sales-tobe">
      <h3><span class="section-card-num">6.2.</span> BPMN To-Be Marketing & Sales (Setelah ERP)</h3>
      <p class="section-card-desc">Otomatisasi pengiriman promosi, input POS, dan sinkronisasi laporan.</p>
      <p>Sistem baru mengintegrasikan modul pemasaran digital (Email/SMS) untuk menarik calon pembeli. Transaksi POS kasir langsung memicu pembuatan nota digital, pengurangan stok bahan baku, dan pengkinian dashboard penjualan owner secara real-time.</p>
      
      <div class="img-container">
        <img src="img/psdp_diagrams/page11_img1.jpeg" alt="BPMN Sales To-Be"/>
        <div class="img-caption">Gambar 3.2: Diagram Alur Proses Bisnis Penjualan Terintegrasi Odoo (To-Be)</div>
      </div>
    </div>
    
    <!-- 6.3 BPMN Production As-Is -->
    <div class="section-card" id="bpmn-prod-asis">
      <h3><span class="section-card-num">6.3.</span> BPMN As-Is Production (Sebelum ERP)</h3>
      <p class="section-card-desc">Proses dapur yang tidak terdokumentasi dan pemeriksaan stok manual.</p>
      <p>Alur produksi as-is sangat bergantung pada ingatan dan pemeriksaan manual oleh staf dapur. Kendali mutu dilakukan subjektif dan laporan pemakaian bahan baku tidak terintegrasi ke sistem keuangan.</p>
      
      <div class="img-container">
        <img src="img/psdp_diagrams/page13_img1.jpeg" alt="BPMN Production As-Is"/>
        <div class="img-caption">Gambar 4.1: Diagram Alur Proses Bisnis Produksi Manual (As-Is)</div>
      </div>
    </div>
    
    <!-- 6.4 BPMN Production To-Be -->
    <div class="section-card" id="bpmn-prod-tobe">
      <h3><span class="section-card-num">6.4.</span> BPMN To-Be Production (Setelah ERP)</h3>
      <p class="section-card-desc">Siklus produksi terotomatisasi Bill of Materials (BoM) dan pos pengecekan mutu.</p>
      <p>Begitu penjualan terkonfirmasi di kasir, Odoo otomatis menerbitkan Manufacturing Order (MO), merujuk resep BoM untuk mengurangi stok di gudang, mewajibkan staf dapur melewati quality check titik Pass/Fail, dan merilis status selesai ke dashboard monitoring.</p>
      
      <div class="img-container">
        <img src="img/psdp_diagrams/page14_img1.jpeg" alt="BPMN Production To-Be"/>
        <div class="img-caption">Gambar 4.2: Diagram Alur Proses Bisnis Produksi Terintegrasi Odoo (To-Be)</div>
      </div>
    </div>
    
    <!-- 6.5 Perbandingan -->
    <div class="section-card" id="system-comparison">
      <h3><span class="section-card-num">6.5.</span> Perbandingan Proses Bisnis As-Is vs To-Be</h3>
      <p class="section-card-desc">Tabel matriks transformasi operasional Ketan Bersaudara paska implementasi Odoo.</p>
      <div class="table-wrapper">
        <table>
          <thead>
            <tr>
              <th>Dimensi Operasional</th>
              <th>Kondisi As-Is (Sistem Manual)</th>
              <th>Kondisi To-Be (Sistem ERP Odoo)</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Pencatatan Transaksi</strong></td>
              <td>Pencatatan manual / POS terpisah tanpa update data pusat.</td>
              <td>Otomatis tercatat terintegrasi dengan modul inventory.</td>
            </tr>
            <tr>
              <td><strong>Manajemen Stok Gudang</strong></td>
              <td>Cek fisik manual berkala, reaktif saat stok habis.</td>
              <td>Pengecekan real-time berbasis kartu stok otomatis BoM.</td>
            </tr>
            <tr>
              <td><strong>Kendali Mutu (Quality Control)</strong></td>
              <td>Manual, subjektif, tidak ada bukti terdokumentasi.</td>
              <td>Terkonfigurasi melalui modul Quality Control Points (Pass/Fail).</td>
            </tr>
            <tr>
              <td><strong>Pelaporan Penjualan</strong></td>
              <td>Rekap Excel manual harian oleh owner di akhir shift.</td>
              <td>Dashboard KPI real-time merangkum penjualan per SKU.</td>
            </tr>
            <tr>
              <td><strong>Manajemen Promosi</strong></td>
              <td>Tidak terstruktur, posting sosial media seadanya.</td>
              <td>Terjadwal dan terpusat melalui modul Odoo Marketing.</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>

  <!-- PHASE 7: KESIMPULAN & SARAN -->
  <div class="phase-block">
    <div class="phase-badge pb-green">Fase 7: Kesimpulan & Saran Pengembangan</div>
    
    <!-- 7.1 Kesimpulan -->
    <div class="section-card" id="kesimpulan">
      <h3><span class="section-card-num">7.1.</span> Kesimpulan Hasil Implementasi</h3>
      <p class="section-card-desc">Ringkasan pencapaian integrasi sistem Ketan Bersaudara.</p>
      <p>Transformasi digital menggunakan platform Odoo ERP berhasil menyatukan seluruh fungsi operasional gerai Ketan Bersaudara Pasar Tunjungan dalam satu database terpadu. Kendala operasional kritis seperti kehabisan bahan baku mendadak, lambatnya pencatatan omset harian, dan ketidakjelasan tugas staf teratasi melalui modul Manufacturing, Inventory, Sales, dan CRM. Hal ini memangkas ketergantungan mutlak gerai pada kehadiran fisik owner di toko.</p>
    </div>
    
    <!-- 7.2 Saran -->
    <div class="section-card" id="saran">
      <h3><span class="section-card-num">7.2.</span> Saran Pengembangan Sistem Lebih Lanjut</h3>
      <p class="section-card-desc">Rekomendasi taktis untuk mengoptimalkan penggunaan sistem Odoo di masa depan.</p>
      <div class="sticky-grid">
        <div class="sticky-note sticky-yellow">
          <h4>1. Fitur Reorder Rules</h4>
          <p>Mengaktifkan pengaturan batas minimum stok di Odoo agar otomatis menerbitkan Purchase Requisition bahan baku saat kritis.</p>
        </div>
        <div class="sticky-note sticky-blue">
          <h4>2. Modul HR & Kalender Shift</h4>
          <p>Mengintegrasikan pencatatan jam kerja dan shift staf secara formal dalam modul SDM Odoo.</p>
        </div>
        <div class="sticky-note sticky-green">
          <h4>3. Optimasi CRM & Loyalitas</h4>
          <p>Memanfaatkan database kontak POS untuk merancang promosi personal berbasis riwayat belanja kesukaan konsumen.</p>
        </div>
        <div class="sticky-note sticky-rose">
          <h4>4. Modul Keuangan & Akuntansi</h4>
          <p>Mengeksplorasi modul Purchase & Accounting guna mengotomatiskan pembukuan laba rugi bulanan gerai.</p>
        </div>
      </div>
    </div>
    """
    return build_html(title, project_name, role, meta_units, meta_platform, meta_author, sidebar_nav_html, main_content_html, accent_class, color_theme_style)

def generate_lppm():
    project_name = "SIMPPM LPMB Portal"
    title = "SIMPPM Portal: Sistem Manajemen Pengisian Pengabdian Masyarakat (PENGMAS) LPMB"
    role = "Senior Business & System Analyst"
    meta_units = "LPMB (Lembaga Pengabdian Masyarakat dan Bisnis)"
    meta_platform = "LPMB Pengmas Workflow Portal, REST API Integration & WUADC Database"
    meta_author = "Fitria Indah Novitasari"
    accent_class = "accent-amber"
    
    color_theme_style = """
    .nav-item:hover {
      background: #f1f5f9;
      color: var(--accent-amber);
    }
    .nav-item.active {
      background: var(--accent-amber-soft);
      color: var(--accent-amber);
      font-weight: 600;
    }
    .timeline-dot {
      border: 2px solid var(--accent-amber);
      color: var(--accent-amber);
    }
    .section-card {
      border-left: 5px solid var(--accent-amber);
    }
    """
    
    sidebar_nav_html = """
<div class="nav-group-title">Fase 1: Case Study</div>
    <a href="#general-overview" class="nav-item active"><span class="nav-num">1.1</span> Gambaran Perusahaan</a>
    <a href="#org-structure" class="nav-item"><span class="nav-num">1.2</span> Peran Operasional</a>
    <a href="#current-system" class="nav-item"><span class="nav-num">1.3</span> Sistem Lama & Tantangan</a>
    
    <div class="nav-group-title">Fase 2: Proses Bisnis</div>
    <a href="#bpmn-swimlane" class="nav-item"><span class="nav-num">2.1</span> BPMN Swimlane Alur</a>
    <a href="#workflow-breakdown" class="nav-item"><span class="nav-num">2.2</span> Breakdown Alur Kerja</a>
    <a href="#status-code-map" class="nav-item"><span class="nav-num">2.3</span> Pemetaan Status Code</a>
    
    <div class="nav-group-title">Fase 3: Kebutuhan Sistem</div>
    <a href="#brd" class="nav-item"><span class="nav-num">3.1</span> BRD Overview</a>
    <a href="#func-req" class="nav-item"><span class="nav-num">3.2</span> Functional Specs</a>
    <a href="#nonfunc-req" class="nav-item"><span class="nav-num">3.3</span> Non-Functional Specs</a>
    <a href="#accept-crit" class="nav-item"><span class="nav-num">3.4</span> Acceptance Criteria</a>
    
    <div class="nav-group-title">Fase 4: Pemodelan Sistem</div>
    <a href="#activity" class="nav-item"><span class="nav-num">4.1</span> Activity Diagram</a>
    <a href="#sequence" class="nav-item"><span class="nav-num">4.2</span> Sequence Diagram</a>
    <a href="#erd" class="nav-item"><span class="nav-num">4.3</span> ERD Database</a>
    <a href="#data-dictionary" class="nav-item"><span class="nav-num">4.4</span> Data Dictionary</a>
    
    <div class="nav-group-title">Fase 5: Teknis & Integrasi</div>
    <a href="#api-doc" class="nav-item"><span class="nav-num">5.1</span> API Documentation</a>
    <a href="#val-rules" class="nav-item"><span class="nav-num">5.2</span> Validation Rules</a>
    <a href="#role-matrix" class="nav-item"><span class="nav-num">5.3</span> Role & RACI Matrix</a>
    <a href="#exception" class="nav-item"><span class="nav-num">5.4</span> Exception Flow</a>
    <a href="#sys-architecture" class="nav-item"><span class="nav-num">5.5</span> System Architecture</a>
    
    <div class="nav-group-title">Fase 6: Pengujian & Risiko</div>
    <a href="#uat" class="nav-item"><span class="nav-num">6.1</span> UAT Test Plan</a>
    <a href="#rtm" class="nav-item"><span class="nav-num">6.2</span> RTM Document</a>
    <a href="#risk-reg" class="nav-item"><span class="nav-num">6.3</span> Risk Register</a>
    <a href="#perf-benchmark" class="nav-item"><span class="nav-num">6.4</span> Performance Benchmark</a>
    
    <div class="nav-group-title">Fase 7: Dampak Bisnis</div>
    <a href="#biz-impact" class="nav-item"><span class="nav-num">7.1</span> Business Impact</a>
    <a href="#before-after" class="nav-item"><span class="nav-num">7.2</span> Before vs After</a>
    <a href="#lessons-roadmap" class="nav-item"><span class="nav-num">7.3</span> Lessons & Roadmap</a>
    """
    
    main_content_html = """
<!-- PHASE 1: CASE STUDY -->
  <div class="phase-block">
    <div class="phase-badge pb-purple">Fase 1: Case Study & Context</div>
    
    <!-- 1.1 Gambaran Umum -->
    <div class="section-card" id="general-overview">
      <h3><span class="section-card-num">1.1.</span> Gambaran Perusahaan</h3>
      <p class="section-card-desc">Latar belakang bisnis tata kelola administrasi Pengabdian Masyarakat (PENGMAS) tingkat universitas.</p>
      <div class="bento-grid">
        <div class="bento-cell bento-wide">
          <h4>LPMB Pengmas Workflow & Archiving Portal</h4>
          <p>Lembaga Pengabdian Masyarakat dan Bisnis (LPMB) memegang kendali penuh atas program pengabdian eksternal reguler, internal, dan mandiri. Portal SIMPPM dirancang untuk mendigitalisasi penanganan proposal, dokumen administrasi prasyarat (RAB, CV Ketua, SP, Pakta Integritas), koordinasi keanggotaan dosen-mahasiswa, hingga sistem pelaporan terarsip yang terintegrasi langsung dengan tabel basis data master <strong>WUADC</strong>.</p>
        </div>
        <div class="bento-cell">
          <h4>Target Efisiensi</h4>
          <p style="font-size: 2.2rem; font-weight: 800; color: var(--accent-amber); line-height: 1;">Under 5 Days</p>
          <p style="font-weight: 600; margin-top: 10px;">Siklus Verifikasi & Review</p>
          <p>Memotong rantai birokrasi peninjauan kelengkapan berkas fisik dari Akademik & Dekanat Fakultas menjadi sistem online real-time.</p>
        </div>
      </div>
    </div>
    
    <!-- 1.2 Struktur Organisasi -->
    <div class="section-card" id="org-structure">
      <h3><span class="section-card-num">1.2.</span> Peran Operasional Sistem</h3>
      <p class="section-card-desc">Tanggung jawab masing-masing aktor pengguna dalam alur kerja SIMPPM LPMB.</p>
      <div class="table-wrapper">
        <table>
          <thead>
            <tr>
              <th>Aktor Peran</th>
              <th>Tanggung Jawab Teknis</th>
              <th>Kebutuhan Antarmuka Sistem</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Admin LPMB</strong></td>
              <td>Mengelola skema pengmas, master dokumen prasyarat, melakukan verifikasi kesesuaian konten proposal, mengevaluasi laporan kemudahan/akhir, dan menyimpan data luaran ke tabel WUADC.</td>
              <td>Panel konfigurasi skema, antrean verifikasi konten, panel audit log, dan dashboard monitoring monev.</td>
            </tr>
            <tr>
              <td><strong>Dosen Ketua</strong></td>
              <td>Melakukan login (SSO Cyber/Gmail), memilih skema (reguler, internal, mandiri), mengisi form pengajuan berkas, mengunggah proposal/RAB/CV/SP/Pakta, menandatangani persetujuan administratif, melakukan kegiatan, dan mengunggah laporan kemajuan/akhir/luaran.</td>
              <td>Formulir pengajuan dinamis, modul upload file, status tracking proposal (Draft, Rejected, Approved), dan menu logbook pelaporan.</td>
            </tr>
            <tr>
              <td><strong>Dosen Anggota & Mahasiswa</strong></td>
              <td>Melihat riwayat usulan proyek pengmas di mana nama mereka didaftarkan, serta turut melaksanakan kegiatan pengmas secara paralel.</td>
              <td>Halaman riwayat usulan khusus anggota dan dasbor pelacakan status kegiatan.</td>
            </tr>
            <tr>
              <td><strong>Akademik Fakultas</strong></td>
              <td>Melakukan review kelengkapan berkas administratif awal pasca-submit, serta melakukan review akhir tingkat fakultas jika lolos administrasi LPMB.</td>
              <td>Daftar antrean verifikasi berkas fakultas, checklist kelengkapan berkas, dan modul penilaian akhir fakultas.</td>
            </tr>
            <tr>
              <td><strong>Dekanat Fakultas</strong></td>
              <td>Melakukan peninjauan proposal dan memberikan keputusan persetujuan rekomendasi, serta melakukan review akhir usulan tingkat dekanat.</td>
              <td>Halaman tinjauan proposal fakultas, tombol keputusan setuju/tolak rekomendasi, dan panel review akhir.</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    
    <!-- 1.3 Sistem Lama & Tantangan -->
    <div class="section-card" id="current-system">
      <h3><span class="section-card-num">1.3.</span> Analisis Sistem Lama & Tantangan Operasional</h3>
      <p class="section-card-desc">Kendala utama proses manual yang diselesaikan melalui implementasi portal SIMPPM.</p>
      <div class="sticky-grid">
        <div class="sticky-note sticky-yellow">
          <h4>Autentikasi Terpisah</h4>
          <p>Login dosen tidak terpusat, menyulitkan sinkronisasi profil pengusul antara cyber kampus dan server email gmail institusi.</p>
        </div>
        <div class="sticky-note sticky-blue">
          <h4>Berkas Persyaratan Fisik</h4>
          <p>Pengumpulan dokumen proposal, RAB, CV, SP, dan Pakta Integritas dilakukan manual berbentuk kertas cetak atau attachment email acak.</p>
        </div>
        <div class="sticky-note sticky-green">
          <h4>Review Fakultatif Lambat</h4>
          <p>Staf akademik dan dekanat kesulitan memantau antrean berkas pengajuan karena alur verifikasi berjalan menggunakan dokumen fisik.</p>
        </div>
        <div class="sticky-note sticky-rose">
          <h4>Arsip Laporan Terpencar</h4>
          <p>Logbook, laporan akhir, dan dokumen bukti luaran pengmas seringkali hilang karena tidak tersimpan otomatis ke database master WUADC.</p>
        </div>
      </div>
    </div>
  </div>

  <!-- PHASE 2: BUSINESS PROCESS -->
  <div class="phase-block">
    <div class="phase-badge pb-blue">Fase 2: Pemetaan Alur Kerja Bisnis</div>
    
    <!-- 2.1 BPMN Swimlane -->
    <div class="section-card" id="bpmn-swimlane">
      <h3><span class="section-card-num">2.1.</span> BPMN Swimlane Alur Pengajuan & Evaluasi Proposal</h3>
      <p class="section-card-desc">Visualisasi alur proses bisnis lintas peran dari pembukaan periode hingga penandatanganan kontrak riset. Diagram swimlane di bawah ini menggambarkan interaksi antara 6 aktor utama (Admin LPMB, Dosen Ketua, Dosen Anggota, Mahasiswa, Akademik Fakultas, dan Dekanat Fakultas) dalam satu siklus pengajuan pengmas lengkap — mulai dari konfigurasi skema oleh admin, autentikasi SSO, pengisian formulir, review berjenjang, pelaksanaan kegiatan, hingga pelaporan akhir dan pengarsipan ke WUADC.</p>
      
      <div class="img-container" style="margin-bottom: 30px;">
        <img src="img/lppm-swimlane.jpg" alt="Orisinal Swimlane Diagram LPMB SIMPPM"/>
        <div class="img-caption">Gambar 2.1: Diagram Swimlane Proses Bisnis Orisinal SIMPPM LPMB (File Input User)</div>
      </div>

      <div class="diagram-container">
        <h4 style="margin-bottom: 15px; color: var(--text-dark); font-weight: 700;">Model Digital Alur Kerja (Mermaid Flowchart)</h4>
        <div class="mermaid">
          graph TD
            subgraph Admin LPMB
              Start([Mulai]) --> ActSkema[Mengelola Skema Pengmas]
              ActSkema --> ActMasterDoc[Mengelola Master Dokumen Prasyarat]
              VerifyAdmin[Verifikasi Administrasi Kesesuaian Konten]
              LolosAdmin{Lolos Administrasi?}
              Monev[Monitoring dan Evaluasi]
              LaporanSesuai{Laporan Sesuai?}
              SaveWUADC[Save di Tabel WUADC] --> End([Selesai])
            end

            subgraph Dosen Ketua
              LoginCyber[Dosen Ketua Login Sistem via Cyber / Gmail]
              IsLoginSuccess{Sukses Login?}
              IsPeriodActive{Dalam Periode Pendaftaran Aktif?}
              QueryData[Sistem Query Data Dosen, Mhs, Unit Kerja & API Cyber]
              PilihSkema[Pilih Skema Pengmas: Reguler, Internal, Mandiri]
              FillForm[Mengisi Form Pengajuan Pengmas & Upload Berkas Dokumen, RAB, CV, SP, Pakta]
              SubmitDocs[Upload Berkas Sesuai Skema & Submit]
              RevisiDoc[Revisi & Lengkapi Dokumen]
              LengkapiTtd[Melengkapi Administrasi Ttd]
              MelakukanKegiatanKetua[Melakukan Kegiatan Pengmas]
              LaporKegiatan[Melakukan Pelaporan Kegiatan Logbook & Laporan]
              PerbaikanLaporan[Melakukan Perbaikan Laporan]
              HasilAkhir[Melakukan Hasil Akhir Usulan Dokumen Luaran Lengkap]
            end

            subgraph Dosen Anggota
              ViewUsulanDosen[Melihat Riwayat Usulan]
              MelakukanKegiatanDosen[Melakukan Kegiatan Pengmas]
            end

            subgraph Mahasiswa
              ViewUsulanMhs[Melihat Riwayat Usulan]
              MelakukanKegiatanMhs[Melakukan Kegiatan Pengmas]
            end

            subgraph Akademik Fakultas
              ReviewBerkas[Review Kelengkapan Berkas Usulan]
              IsBerkasSesuai{Berkas Lengkap & Sesuai?}
              ReviewAkhirAkad[Melakukan Review Akhir]
              IsUsulanDiterimaAkad{Usulan Diterima?}
            end

            subgraph Dekanat Fakultas
              ReviewDekan[Dekan Review Proposal Usulan]
              IsDekanSetuju{Dekan Menyetujui Usulan?}
              ReviewAkhirDekan[Melakukan Review Akhir]
              IsUsulanDiterimaDekan{Usulan Diterima?}
            end

            ActMasterDoc --> LoginCyber
            LoginCyber --> IsLoginSuccess
            IsLoginSuccess -- Tidak --> LoginCyber
            IsLoginSuccess -- Ya --> IsPeriodActive
            IsPeriodActive -- Tidak --> SelesaiNoPeriod([Selesai / Halaman Pengajuan Tidak Tersedia])
            IsPeriodActive -- Ya --> QueryData
            QueryData --> PilihSkema
            PilihSkema --> FillForm
            FillForm --> SubmitDocs
            SubmitDocs --> ViewUsulanDosen
            SubmitDocs --> ViewUsulanMhs
            ViewUsulanDosen --> ReviewBerkas
            ViewUsulanMhs --> ReviewBerkas
            ReviewBerkas --> IsBerkasSesuai
            IsBerkasSesuai -- Tidak: REJECTED AKADEMIK 3 --> RevisiDoc
            IsBerkasSesuai -- Ya: APPROVE AKADEMIK 2 --> ReviewDekan
            RevisiDoc --> SubmitDocs
            ReviewDekan --> IsDekanSetuju
            IsDekanSetuju -- Tidak: REJECTED DEKAN 5 --> RevisiDoc
            IsDekanSetuju -- Ya: APPROVE DEKAN 4 --> LengkapiTtd
            LengkapiTtd --> VerifyAdmin
            VerifyAdmin --> LolosAdmin
            LolosAdmin -- Tidak: REJECTED ADMINISTRASI 7 --> SelesaiDitolakAdmin([Selesai / Tahap Administrasi Ditolak])
            LolosAdmin -- Ya: APPROVE ADMINISTRASI 6 --> ReviewAkhirAkad
            ReviewAkhirAkad --> IsUsulanDiterimaAkad
            IsUsulanDiterimaAkad -- Tidak --> SelesaiDitolakAkad([Selesai / Usulan Ditolak])
            IsUsulanDiterimaAkad -- Ya --> ReviewAkhirDekan
            ReviewAkhirDekan --> IsUsulanDiterimaDekan
            IsUsulanDiterimaDekan -- Tidak --> SelesaiDitolakDekan([Selesai / Usulan Ditolak])
            IsUsulanDiterimaDekan -- Ya --> MelakukanKegiatanKetua
            IsUsulanDiterimaDekan -- Ya --> MelakukanKegiatanDosen
            IsUsulanDiterimaDekan -- Ya --> MelakukanKegiatanMhs
            MelakukanKegiatanKetua --> LaporKegiatan
            MelakukanKegiatanDosen --> LaporKegiatan
            MelakukanKegiatanMhs --> LaporKegiatan
            LaporKegiatan --> Monev
            Monev --> LaporanSesuai
            LaporanSesuai -- Tidak --> PerbaikanLaporan
            PerbaikanLaporan --> Monev
            LaporanSesuai -- Ya --> HasilAkhir
            HasilAkhir --> SaveWUADC
        </div>
      </div>
    </div>
    
    <!-- 2.2 Workflow Breakdown -->
    <div class="section-card" id="workflow-breakdown">
      <h3><span class="section-card-num">2.2.</span> Breakdown Detil Alur Kerja LPMB</h3>
      <p class="section-card-desc">Penjelasan langkah-langkah logis operasional lintas peran berdasarkan swimlane diagram. Setiap langkah mencakup deskripsi sub-proses, aktor penanggung jawab, perubahan status proposal, dan titik keputusan (decision gate) yang menentukan apakah proses berlanjut atau dikembalikan untuk perbaikan.</p>
      <div class="workflow-timeline">
        <div class="timeline-item">
          <div class="timeline-dot">1</div>
          <div class="timeline-content">
            <h4>Inisiasi & Konfigurasi Skema Pengmas (Admin LPMB)</h4>
            <p>Admin LPMB membuka menu konfigurasi skema pengabdian masyarakat dan menentukan parameter skema yang berlaku untuk periode berjalan. Terdapat tiga jenis skema: <strong>Reguler</strong> (pendanaan dari pihak eksternal, durasi 6-12 bulan), <strong>Internal</strong> (pendanaan dari universitas, durasi 4-6 bulan), dan <strong>Mandiri</strong> (tanpa pendanaan institusional, fleksibel). Untuk setiap skema, admin mengatur: daftar dokumen prasyarat wajib, batas maksimum anggota dosen dan mahasiswa, batas ukuran file upload (max 10MB per file), format file yang diperbolehkan (PDF/DOC/DOCX), serta template formulir pengisian proposal. Konfigurasi ini disimpan ke tabel <strong>SKEMA_PENGMAS</strong> dan menjadi referensi validasi saat dosen melakukan pengajuan.</p>
          </div>
        </div>
        <div class="timeline-item">
          <div class="timeline-dot">2</div>
          <div class="timeline-content">
            <h4>Pembukaan Periode Pendaftaran (Admin LPMB)</h4>
            <p>Admin LPMB mengaktifkan periode pendaftaran dengan menentukan <strong>tanggal_buka</strong> dan <strong>tanggal_tutup</strong> pada tabel <strong>PERIODE_PENGMAS</strong>. Hanya periode dengan flag <code>is_active = true</code> yang memperbolehkan dosen mengakses halaman formulir pengajuan. Sistem secara otomatis menonaktifkan periode ketika tanggal tutup terlewati, serta mengirimkan notifikasi pengingat H-7 dan H-1 sebelum periode berakhir kepada seluruh dosen yang belum menyelesaikan proses submit.</p>
          </div>
        </div>
        <div class="timeline-item">
          <div class="timeline-dot">3</div>
          <div class="timeline-content">
            <h4>Autentikasi SSO & Validasi Akun (Dosen Ketua)</h4>
            <p>Dosen Ketua melakukan login ke portal SIMPPM melalui dua metode Single Sign-On: <strong>SSO Cyber Kampus</strong> (autentikasi utama berbasis NIDN) atau <strong>Google OAuth (Gmail Institusi)</strong> (autentikasi alternatif). Sistem melakukan query real-time ke API Cyber Kampus untuk memvalidasi: (1) NIDN terdaftar dan status kepegawaian aktif, (2) data jabatan akademik, fakultas, dan program studi terisi lengkap, (3) tidak sedang dalam masa cuti atau non-aktif. Jika validasi gagal, sistem menampilkan pesan error spesifik dan memblokir akses ke halaman pengajuan. Status proposal pada tahap ini: belum ada record (pre-submission).</p>
          </div>
        </div>
        <div class="timeline-item">
          <div class="timeline-dot">4</div>
          <div class="timeline-content">
            <h4>Validasi Periode & Query Data Master (Sistem)</h4>
            <p>Setelah autentikasi berhasil, sistem memeriksa apakah saat ini berada dalam periode pendaftaran aktif (<code>is_active = true AND CURRENT_DATE BETWEEN tanggal_buka AND tanggal_tutup</code>). Jika periode tidak aktif, dosen diarahkan ke halaman informasi "Periode Pengajuan Belum Dibuka" dan tidak dapat mengakses formulir. Jika aktif, sistem melakukan batch query ke API Cyber Kampus dan PDDIKTI untuk mengambil data master: daftar dosen aktif per fakultas (untuk pemilihan anggota), daftar mahasiswa aktif per prodi, unit kerja, serta riwayat pengajuan sebelumnya. Data ini di-cache selama sesi untuk mempercepat proses pengisian formulir.</p>
          </div>
        </div>
        <div class="timeline-item">
          <div class="timeline-dot">5</div>
          <div class="timeline-content">
            <h4>Pemilihan Skema & Pengisian Formulir (Dosen Ketua)</h4>
            <p>Dosen Ketua memilih skema pengmas yang sesuai (Reguler/Internal/Mandiri). Formulir dinamis akan di-render sesuai konfigurasi skema terpilih, menampilkan field-field yang relevan: judul proposal, abstrak, tahun pelaksanaan, rencana anggaran biaya (dana_diajukan), lokasi kegiatan, dan daftar target capaian luaran. Dosen juga mendaftarkan anggota tim dengan memasukkan NIDN (untuk dosen anggota) dan NIM (untuk mahasiswa) — sistem langsung memvalidasi ketersediaan dan status aktif masing-masing calon anggota melalui API. Status proposal: <span class="badge badge-warning">DRAFT</span></p>
          </div>
        </div>
        <div class="timeline-item">
          <div class="timeline-dot">6</div>
          <div class="timeline-content">
            <h4>Upload Berkas Prasyarat & Submit (Dosen Ketua)</h4>
            <p>Dosen Ketua mengunggah seluruh dokumen prasyarat sesuai skema: (1) <strong>File Proposal</strong> — dokumen inti kegiatan pengmas, (2) <strong>RAB (Rencana Anggaran Biaya)</strong> — rincian penggunaan dana, (3) <strong>CV Ketua</strong> — curriculum vitae dosen ketua tim, (4) <strong>Surat Pernyataan (SP)</strong> — pernyataan keaslian dan kesanggupan, (5) <strong>Pakta Integritas</strong> — komitmen etik pelaksanaan. Sistem melakukan validasi real-time: tipe file (PDF/DOC/DOCX), ukuran maksimum 10MB per file, dan kelengkapan dokumen wajib per skema. Setelah semua berkas lengkap dan tervalidasi, Dosen Ketua menekan tombol "Upload Berkas dan Submit". Status proposal berubah: <span class="badge badge-warning">DRAFT</span> → <span class="badge badge-primary">SUBMITTED</span></p>
          </div>
        </div>
        <div class="timeline-item">
          <div class="timeline-dot">7</div>
          <div class="timeline-content">
            <h4>Notifikasi Paralel ke Anggota Tim (Dosen Anggota & Mahasiswa)</h4>
            <p>Saat proposal di-submit, sistem secara otomatis mengirimkan notifikasi (email + in-app notification) kepada seluruh Dosen Anggota dan Mahasiswa yang didaftarkan. Mereka dapat melihat detail proposal, riwayat usulan, dan status keterlibatan mereka melalui halaman "Riwayat Usulan Saya". Notifikasi ini mencakup: judul proposal, nama ketua tim, skema pengmas, dan tautan langsung ke detail proposal. Anggota tidak memiliki akses edit — hanya view dan konfirmasi partisipasi.</p>
          </div>
        </div>
        <div class="timeline-item">
          <div class="timeline-dot">8</div>
          <div class="timeline-content">
            <h4>Review Kelengkapan Berkas Administratif (Akademik Fakultas)</h4>
            <p>Staf Akademik Fakultas menerima notifikasi antrean review baru di dashboard mereka. Proses review meliputi pemeriksaan: (1) kelengkapan seluruh dokumen wajib sesuai skema, (2) kesesuaian format dan template dokumen, (3) validitas data identitas pengusul dan anggota, (4) konsistensi judul dan abstrak dengan isi proposal. Akademik menggunakan checklist digital terintegrasi untuk menandai setiap item yang telah diperiksa. <strong>Decision Gate:</strong> Jika berkas tidak lengkap/tidak sesuai → <span class="badge badge-danger">REJECTED_AKADEMIK</span> dengan catatan revisi spesifik yang dikirim ke Dosen Ketua. Jika berkas lengkap → <span class="badge badge-success">APPROVED_AKADEMIK</span>, proposal diteruskan ke Dekanat.</p>
          </div>
        </div>
        <div class="timeline-item">
          <div class="timeline-dot">9</div>
          <div class="timeline-content">
            <h4>Review Rekomendasi Substansi (Dekanat Fakultas)</h4>
            <p>Dekan atau Wakil Dekan melakukan peninjauan substansi proposal: kesesuaian tema dengan visi fakultas, kelayakan rencana anggaran, relevansi dengan kebutuhan masyarakat sasaran, dan kualifikasi tim pengusul. Dekanat dapat memberikan catatan evaluatif yang terekam di tabel <strong>REVIEW_LOG</strong>. <strong>Decision Gate:</strong> Jika dekan tidak menyetujui → <span class="badge badge-danger">REJECTED_DEKAN</span> dengan alasan penolakan yang dikirim ke Dosen Ketua untuk revisi. Jika disetujui → <span class="badge badge-success">APPROVED_DEKAN</span>, dan sistem mengirimkan notifikasi ke Dosen Ketua untuk melengkapi tanda tangan administrasi.</p>
          </div>
        </div>
        <div class="timeline-item">
          <div class="timeline-dot">10</div>
          <div class="timeline-content">
            <h4>Pelengkapan Tanda Tangan Administrasi (Dosen Ketua)</h4>
            <p>Dosen Ketua menerima notifikasi bahwa proposal telah disetujui oleh Dekanat dan perlu melengkapi tanda tangan digital pada dokumen administrasi final. Dokumen yang ditandatangani mencakup: Surat Pernyataan, Pakta Integritas, dan lembar persetujuan anggaran. Setelah seluruh tanda tangan terisi, Dosen Ketua mengkonfirmasi penyelesaian administrasi. Status proposal: <span class="badge badge-success">APPROVED_DEKAN</span> → <span class="badge badge-primary">TTD_ADMIN</span></p>
          </div>
        </div>
        <div class="timeline-item">
          <div class="timeline-dot">11</div>
          <div class="timeline-content">
            <h4>Verifikasi Kesesuaian Konten (Admin LPMB)</h4>
            <p>Admin LPMB melakukan verifikasi menyeluruh terhadap kesesuaian konten proposal: (1) substansi kegiatan sesuai dengan definisi pengabdian masyarakat, (2) RAB proporsional dengan ruang lingkup kegiatan, (3) tidak terdapat duplikasi dengan proposal aktif lainnya, (4) dokumen administrasi bertanda tangan lengkap dan sah. Admin LPMB menggunakan checklist konten internal dan dapat memberikan catatan verifikasi yang direkam dalam <strong>REVIEW_LOG</strong>. <strong>Decision Gate:</strong> Jika gagal verifikasi → <span class="badge badge-danger">REJECTED_ADMIN</span>, proposal dihentikan secara permanen (terminal state). Jika lolos → <span class="badge badge-success">VERIFIED</span>, dilanjutkan ke tahap review akhir berjenjang.</p>
          </div>
        </div>
        <div class="timeline-item">
          <div class="timeline-dot">12</div>
          <div class="timeline-content">
            <h4>Review Akhir Berjenjang (Akademik & Dekanat Fakultas)</h4>
            <p>Proposal yang telah lolos verifikasi LPMB memasuki tahap review akhir dua tingkat. <strong>Tingkat 1 — Akademik Fakultas:</strong> Melakukan penilaian akhir komprehensif mencakup kelayakan akademis dan kesiapan pelaksanaan. Jika ditolak → <span class="badge badge-danger">REJECTED_FINAL</span> (terminal). Jika diterima → status menjadi <span class="badge badge-primary">REVIEW_FINAL_AKAD</span>, diteruskan ke Dekanat. <strong>Tingkat 2 — Dekanat Fakultas:</strong> Memberikan keputusan penerimaan akhir. Jika ditolak → <span class="badge badge-danger">REJECTED_FINAL</span> (terminal). Jika diterima → <span class="badge badge-success">APPROVED</span>, proposal resmi diterima dan tim dapat memulai pelaksanaan kegiatan pengmas.</p>
          </div>
        </div>
        <div class="timeline-item">
          <div class="timeline-dot">13</div>
          <div class="timeline-content">
            <h4>Pelaksanaan Kegiatan Pengmas (Tim Pengmas)</h4>
            <p>Seluruh anggota tim (Dosen Ketua, Dosen Anggota, dan Mahasiswa) melaksanakan kegiatan pengabdian masyarakat secara paralel sesuai rencana yang tercantum dalam proposal. Status proposal berubah menjadi <span class="badge badge-primary">IN_PROGRESS</span>. Selama pelaksanaan, Dosen Ketua wajib mengisi <strong>Logbook Kegiatan</strong> secara berkala melalui portal, mencatat: tanggal kegiatan, uraian aktivitas, persentase kemajuan, dan mengunggah file lampiran dokumentasi (foto, video, notulensi). Logbook ini menjadi bukti pelaksanaan yang akan dievaluasi saat monitoring dan evaluasi (monev).</p>
          </div>
        </div>
        <div class="timeline-item">
          <div class="timeline-dot">14</div>
          <div class="timeline-content">
            <h4>Monitoring & Evaluasi / Monev (Admin LPMB)</h4>
            <p>Admin LPMB melakukan monitoring dan evaluasi (monev) berdasarkan data logbook yang telah diisi oleh Dosen Ketua. Evaluasi meliputi: kesesuaian kegiatan dengan rencana proposal, pencapaian target progres, kualitas dokumentasi, dan kepatuhan terhadap jadwal pelaksanaan. Status proposal: <span class="badge badge-primary">IN_PROGRESS</span> → <span class="badge badge-warning">MONEV</span>. <strong>Decision Gate:</strong> Jika laporan belum memenuhi standar → dikembalikan ke Dosen Ketua untuk perbaikan (status tetap MONEV, sub-status: REVISION_REQUIRED). Jika laporan memenuhi standar → Dosen Ketua diminta menyelesaikan laporan akhir dan dokumen luaran.</p>
          </div>
        </div>
        <div class="timeline-item">
          <div class="timeline-dot">15</div>
          <div class="timeline-content">
            <h4>Laporan Akhir, Luaran & Pengarsipan ke WUADC (Dosen Ketua & Admin LPMB)</h4>
            <p>Dosen Ketua menyelesaikan dan mengunggah: (1) <strong>Laporan Akhir</strong> — dokumen komprehensif hasil kegiatan pengmas, (2) <strong>Dokumen Luaran</strong> — bukti output kegiatan (publikasi, HKI, buku, produk, dsb.), (3) <strong>Bukti Pendukung</strong> — surat keterangan, sertifikat, foto kegiatan, dsb. Admin LPMB melakukan verifikasi final terhadap kelengkapan dan kualitas luaran. Setelah disetujui, status proposal berubah menjadi <span class="badge badge-success">COMPLETED</span> dan sistem secara otomatis melakukan sinkronisasi transaksional seluruh data (metadata proposal, logbook, luaran, file paths) ke tabel basis data master <strong>WUADC</strong>. Status akhir: <span class="badge badge-success">ARCHIVED</span>. Seluruh siklus selesai.</p>
          </div>
        </div>
      </div>
    </div>

    <!-- 2.3 Status Code Mapping -->
    <div class="section-card" id="status-code-map">
      <h3><span class="section-card-num">2.3.</span> Pemetaan Status Code Proposal</h3>
      <p class="section-card-desc">Daftar lengkap kode status proposal yang digunakan sistem SIMPPM beserta deskripsi, aktor pemicu transisi, dan alur perpindahan status dalam lifecycle pengajuan pengmas.</p>
      <div class="table-wrapper">
        <table>
          <thead>
            <tr>
              <th>Status Code</th>
              <th>Deskripsi Status</th>
              <th>Aktor Pemicu</th>
              <th>Transisi Berikutnya (Jika Berhasil)</th>
              <th>Transisi Gagal / Rollback</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><span class="badge badge-warning">DRAFT</span></td>
              <td>Proposal sedang disusun oleh Dosen Ketua, belum di-submit. Dapat diedit dan dihapus secara bebas.</td>
              <td>Dosen Ketua</td>
              <td>SUBMITTED</td>
              <td>— (dapat dihapus)</td>
            </tr>
            <tr>
              <td><span class="badge badge-primary">SUBMITTED</span></td>
              <td>Proposal telah di-submit dan menunggu review kelengkapan berkas oleh Akademik Fakultas. Tidak dapat diedit.</td>
              <td>Dosen Ketua</td>
              <td>REVIEW_AKADEMIK</td>
              <td>—</td>
            </tr>
            <tr>
              <td><span class="badge badge-primary">REVIEW_AKADEMIK</span></td>
              <td>Berkas sedang dalam proses review kelengkapan oleh staf Akademik Fakultas.</td>
              <td>Akademik Fakultas</td>
              <td>APPROVED_AKADEMIK</td>
              <td>REJECTED_AKADEMIK → DRAFT</td>
            </tr>
            <tr>
              <td><span class="badge badge-success">APPROVED_AKADEMIK</span></td>
              <td>Berkas dinyatakan lengkap dan sesuai oleh Akademik. Menunggu review substansi oleh Dekanat.</td>
              <td>Akademik Fakultas</td>
              <td>REVIEW_DEKAN</td>
              <td>—</td>
            </tr>
            <tr>
              <td><span class="badge badge-danger">REJECTED_AKADEMIK</span></td>
              <td>Berkas ditolak karena tidak lengkap atau tidak sesuai. Dosen Ketua harus merevisi dan submit ulang.</td>
              <td>Akademik Fakultas</td>
              <td>DRAFT (setelah revisi)</td>
              <td>— (terminal jika tidak direvisi)</td>
            </tr>
            <tr>
              <td><span class="badge badge-primary">REVIEW_DEKAN</span></td>
              <td>Proposal sedang dalam tinjauan substansi oleh Dekan / Wakil Dekan Fakultas.</td>
              <td>Dekanat Fakultas</td>
              <td>APPROVED_DEKAN</td>
              <td>REJECTED_DEKAN → DRAFT</td>
            </tr>
            <tr>
              <td><span class="badge badge-success">APPROVED_DEKAN</span></td>
              <td>Dekan menyetujui proposal. Dosen Ketua diminta melengkapi tanda tangan administrasi.</td>
              <td>Dekanat Fakultas</td>
              <td>TTD_ADMIN</td>
              <td>—</td>
            </tr>
            <tr>
              <td><span class="badge badge-danger">REJECTED_DEKAN</span></td>
              <td>Dekan menolak proposal. Catatan penolakan dikirim ke Dosen Ketua untuk perbaikan.</td>
              <td>Dekanat Fakultas</td>
              <td>DRAFT (setelah revisi)</td>
              <td>— (terminal jika tidak direvisi)</td>
            </tr>
            <tr>
              <td><span class="badge badge-primary">TTD_ADMIN</span></td>
              <td>Dosen Ketua sedang melengkapi tanda tangan digital pada dokumen administrasi final.</td>
              <td>Dosen Ketua</td>
              <td>VERIFIED</td>
              <td>—</td>
            </tr>
            <tr>
              <td><span class="badge badge-success">VERIFIED</span></td>
              <td>Admin LPMB telah memverifikasi kesesuaian konten proposal dan kelengkapan administrasi bertanda tangan.</td>
              <td>Admin LPMB</td>
              <td>REVIEW_FINAL_AKAD</td>
              <td>REJECTED_ADMIN (terminal)</td>
            </tr>
            <tr>
              <td><span class="badge badge-danger">REJECTED_ADMIN</span></td>
              <td>Proposal ditolak oleh Admin LPMB karena gagal verifikasi konten. Status terminal — tidak dapat direvisi.</td>
              <td>Admin LPMB</td>
              <td>— (terminal)</td>
              <td>—</td>
            </tr>
            <tr>
              <td><span class="badge badge-primary">REVIEW_FINAL_AKAD</span></td>
              <td>Proposal dalam review akhir tingkat Akademik Fakultas untuk penilaian kelayakan komprehensif.</td>
              <td>Akademik Fakultas</td>
              <td>REVIEW_FINAL_DEKAN</td>
              <td>REJECTED_FINAL (terminal)</td>
            </tr>
            <tr>
              <td><span class="badge badge-primary">REVIEW_FINAL_DEKAN</span></td>
              <td>Proposal dalam review akhir tingkat Dekanat untuk keputusan penerimaan final.</td>
              <td>Dekanat Fakultas</td>
              <td>APPROVED</td>
              <td>REJECTED_FINAL (terminal)</td>
            </tr>
            <tr>
              <td><span class="badge badge-success">APPROVED</span></td>
              <td>Proposal resmi diterima dan disetujui untuk pelaksanaan. Tim dapat memulai kegiatan pengmas.</td>
              <td>Dekanat Fakultas</td>
              <td>IN_PROGRESS</td>
              <td>—</td>
            </tr>
            <tr>
              <td><span class="badge badge-primary">IN_PROGRESS</span></td>
              <td>Kegiatan pengmas sedang berlangsung. Dosen Ketua wajib mengisi logbook secara berkala.</td>
              <td>Sistem (otomatis)</td>
              <td>MONEV</td>
              <td>—</td>
            </tr>
            <tr>
              <td><span class="badge badge-warning">MONEV</span></td>
              <td>Proposal dalam tahap monitoring dan evaluasi oleh Admin LPMB berdasarkan logbook.</td>
              <td>Admin LPMB</td>
              <td>COMPLETED</td>
              <td>IN_PROGRESS (perbaikan laporan)</td>
            </tr>
            <tr>
              <td><span class="badge badge-success">COMPLETED</span></td>
              <td>Kegiatan selesai, laporan akhir dan luaran disetujui. Menunggu sinkronisasi ke WUADC.</td>
              <td>Admin LPMB</td>
              <td>ARCHIVED</td>
              <td>—</td>
            </tr>
            <tr>
              <td><span class="badge badge-success">ARCHIVED</span></td>
              <td>Seluruh data proposal, logbook, dan luaran telah disinkronkan ke database master WUADC. Status akhir permanen.</td>
              <td>Sistem (otomatis)</td>
              <td>— (final state)</td>
              <td>—</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="diagram-container">
        <h4 style="margin-bottom: 15px; color: var(--text-dark); font-weight: 700;">State Machine — Lifecycle Status Proposal</h4>
        <div class="mermaid">
          stateDiagram-v2
            [*] --> DRAFT
            DRAFT --> SUBMITTED : Dosen klik Submit
            SUBMITTED --> REVIEW_AKADEMIK : Auto-assign ke Akademik
            REVIEW_AKADEMIK --> APPROVED_AKADEMIK : Berkas lengkap
            REVIEW_AKADEMIK --> REJECTED_AKADEMIK : Berkas tidak lengkap
            REJECTED_AKADEMIK --> DRAFT : Dosen revisi
            APPROVED_AKADEMIK --> REVIEW_DEKAN : Forward ke Dekan
            REVIEW_DEKAN --> APPROVED_DEKAN : Dekan setuju
            REVIEW_DEKAN --> REJECTED_DEKAN : Dekan tolak
            REJECTED_DEKAN --> DRAFT : Dosen revisi
            APPROVED_DEKAN --> TTD_ADMIN : Dosen lengkapi TTD
            TTD_ADMIN --> VERIFIED : Admin LPMB verifikasi
            TTD_ADMIN --> REJECTED_ADMIN : Gagal verifikasi
            REJECTED_ADMIN --> [*]
            VERIFIED --> REVIEW_FINAL_AKAD : Review akhir Akademik
            REVIEW_FINAL_AKAD --> REVIEW_FINAL_DEKAN : Akademik terima
            REVIEW_FINAL_AKAD --> REJECTED_FINAL : Akademik tolak
            REJECTED_FINAL --> [*]
            REVIEW_FINAL_DEKAN --> APPROVED : Dekan terima
            REVIEW_FINAL_DEKAN --> REJECTED_FINAL : Dekan tolak
            APPROVED --> IN_PROGRESS : Mulai kegiatan
            IN_PROGRESS --> MONEV : Submit logbook
            MONEV --> IN_PROGRESS : Perbaikan laporan
            MONEV --> COMPLETED : Laporan disetujui
            COMPLETED --> ARCHIVED : Sync ke WUADC
            ARCHIVED --> [*]
        </div>
      </div>
    </div>
  </div>

  <!-- PHASE 3: REQUIREMENTS -->
  <div class="phase-block">
    <div class="phase-badge pb-green">Fase 3: Kebutuhan Sistem (BRD & Specs)</div>
    
    <!-- 3.1 BRD -->
    <div class="section-card" id="brd">
      <h3><span class="section-card-num">3.1.</span> Business Requirements (BRD Overview)</h3>
      <p class="section-card-desc">Target bisnis utama dalam digitalisasi sistem manajemen pengabdian masyarakat LPMB. Setiap business requirement didefinisikan berdasarkan pain point operasional yang teridentifikasi pada analisis sistem lama (Fase 1.3) dan dipetakan ke kebutuhan fungsional teknis pada bagian 3.2.</p>
      <div style="background: #fafafb; padding: 24px; border-radius: 12px; border: 1px solid var(--border-color);">
        <p><strong>BR-01: Digitalisasi Alur Berkas Lampiran Prasyarat</strong></p>
        <p style="margin-bottom: 16px; color: #475569;">Sistem harus mendigitalisasi seluruh alur berkas lampiran prasyarat (proposal, RAB, CV, SP, pakta) dari proses cetak-fisik menjadi upload digital dengan validasi otomatis, serta mempercepat peninjauan kelengkapan berkas di tingkat fakultas dari rata-rata 2 minggu menjadi maksimal 3 hari kerja.</p>

        <p><strong>BR-02: Pengarsipan Otomatis ke WUADC</strong></p>
        <p style="margin-bottom: 16px; color: #475569;">Sistem wajib mengarsipkan secara otomatis seluruh logbook kegiatan, laporan akhir, dan bukti luaran terintegrasi ke dalam tabel data master <strong>WUADC</strong> secara transaksional, menghilangkan proses input ganda manual yang selama ini menjadi sumber inkonsistensi data pelaporan eksternal ke DIKTI.</p>

        <p><strong>BR-03: Integrasi SSO Terpusat</strong></p>
        <p style="margin-bottom: 16px; color: #475569;">Sistem harus menyediakan mekanisme autentikasi terpusat (Single Sign-On) yang terintegrasi dengan Cyber Kampus dan Google OAuth, sehingga dosen tidak perlu membuat akun terpisah dan data profil pengusul (NIDN, jabatan, fakultas, prodi) tersinkronisasi otomatis dari sumber data induk.</p>

        <p><strong>BR-04: Review Multi-Tier Berjenjang dengan Audit Trail</strong></p>
        <p style="margin-bottom: 16px; color: #475569;">Sistem harus mengimplementasikan alur review berjenjang (Akademik Fakultas → Dekanat → Admin LPMB → Review Akhir) dengan pencatatan audit trail otomatis untuk setiap keputusan review, mencakup: identitas reviewer, timestamp, aksi (approve/reject), dan catatan evaluasi — guna memenuhi kebutuhan akuntabilitas dan transparansi proses seleksi proposal.</p>

        <p><strong>BR-05: Monitoring & Evaluasi (Monev) Lifecycle</strong></p>
        <p style="margin-bottom: 16px; color: #475569;">Sistem harus menyediakan fitur monitoring dan evaluasi (monev) terintegrasi yang memungkinkan Admin LPMB memantau progres pelaksanaan kegiatan pengmas melalui logbook digital, melakukan evaluasi berkala, dan mendeteksi keterlambatan pelaksanaan secara proaktif melalui dashboard visual.</p>

        <p><strong>BR-06: Dashboard Pelaporan & Analitik</strong></p>
        <p style="color: #475569;">Sistem harus menyediakan dashboard analitik real-time yang menampilkan metrik kinerja operasional: jumlah proposal per status, distribusi per skema dan fakultas, rata-rata waktu review per tier, tingkat penolakan, dan statistik sinkronisasi WUADC — untuk mendukung pengambilan keputusan strategis oleh pimpinan LPMB.</p>
      </div>
    </div>
    
    <!-- 3.2 Functional Requirements -->
    <div class="section-card" id="func-req">
      <h3><span class="section-card-num">3.2.</span> Functional Requirements</h3>
      <p class="section-card-desc">Spesifikasi fungsional portal pengajuan proposal SIMPPM LPMB yang mencakup seluruh fitur inti dari autentikasi hingga pengarsipan, dipetakan ke business requirements (BR) dan diprioritaskan berdasarkan criticality terhadap keberlangsungan proses bisnis.</p>
      <div class="table-wrapper">
        <table>
          <thead>
            <tr>
              <th>ID</th>
              <th>Deskripsi Spesifikasi Kebutuhan</th>
              <th>Prasyarat Validasi (Trigger)</th>
              <th>BR Ref</th>
              <th>Prioritas</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>FR-01</strong></td>
              <td>Sistem harus memvalidasi data user dan status kepegawaian pengusul melalui query terpadu ke API Cyber Kampus dan PDDIKTI saat login, memastikan NIDN terdaftar aktif dan profil lengkap (jabatan, fakultas, prodi).</td>
              <td>SSO Login Request</td>
              <td>BR-03</td>
              <td><span class="badge badge-danger">Critical</span></td>
            </tr>
            <tr>
              <td><strong>FR-02</strong></td>
              <td>Sistem harus memvalidasi periode pendaftaran aktif sebelum menampilkan formulir pengajuan. Jika periode tidak aktif (<code>is_active = false</code> atau di luar rentang tanggal), halaman pengajuan tidak dapat diakses.</td>
              <td>Page Load / Navigation</td>
              <td>BR-01</td>
              <td><span class="badge badge-danger">Critical</span></td>
            </tr>
            <tr>
              <td><strong>FR-03</strong></td>
              <td>Sistem harus menyediakan pemilihan skema pengmas (Reguler, Internal, Mandiri) dan me-render formulir dinamis sesuai konfigurasi skema terpilih, termasuk daftar dokumen wajib, batas anggota, dan template yang relevan.</td>
              <td>Scheme Selection Event</td>
              <td>BR-01</td>
              <td><span class="badge badge-danger">Critical</span></td>
            </tr>
            <tr>
              <td><strong>FR-04</strong></td>
              <td>Sistem wajib memvalidasi kelengkapan berkas prasyarat sesuai jenis skema sebelum memperbolehkan submit, termasuk validasi tipe file (PDF/DOC/DOCX only), ukuran maksimum 10MB per file, dan jumlah dokumen minimum per skema.</td>
              <td>Submit Form Check</td>
              <td>BR-01</td>
              <td><span class="badge badge-danger">Critical</span></td>
            </tr>
            <tr>
              <td><strong>FR-05</strong></td>
              <td>Sistem harus menyediakan fitur pendaftaran anggota tim (dosen anggota via NIDN, mahasiswa via NIM) dengan validasi real-time status aktif dan pencegahan duplikasi anggota lintas proposal aktif dalam periode yang sama.</td>
              <td>Member Addition Event</td>
              <td>BR-01</td>
              <td><span class="badge badge-primary">High</span></td>
            </tr>
            <tr>
              <td><strong>FR-06</strong></td>
              <td>Sistem harus mengimplementasikan alur review berjenjang multi-tier: Akademik Fakultas (kelengkapan) → Dekanat (substansi) → Admin LPMB (verifikasi konten) → Review Akhir Akademik → Review Akhir Dekanat, dengan setiap transisi status tercatat otomatis.</td>
              <td>Workflow State Transitions</td>
              <td>BR-04</td>
              <td><span class="badge badge-danger">Critical</span></td>
            </tr>
            <tr>
              <td><strong>FR-07</strong></td>
              <td>Sistem otomatis merekam log audit (REVIEW_LOG) untuk setiap aksi keputusan review bertingkat, mencakup: reviewer_id, proposal_id, action (APPROVE/REJECT), catatan evaluasi, dan timestamp — bersifat immutable (tidak dapat diedit/dihapus).</td>
              <td>Workflow Review Triggers</td>
              <td>BR-04</td>
              <td><span class="badge badge-primary">High</span></td>
            </tr>
            <tr>
              <td><strong>FR-08</strong></td>
              <td>Sistem harus menyediakan fitur pengisian logbook kegiatan secara berkala oleh Dosen Ketua, mencakup: tanggal kegiatan, uraian aktivitas, persentase progres, dan file lampiran dokumentasi (foto/dokumen), sebagai basis evaluasi monev.</td>
              <td>Logbook Submission Event</td>
              <td>BR-05</td>
              <td><span class="badge badge-primary">High</span></td>
            </tr>
            <tr>
              <td><strong>FR-09</strong></td>
              <td>Sistem harus menyediakan dashboard monitoring dan evaluasi (monev) bagi Admin LPMB untuk menilai progres kegiatan, memberikan catatan evaluasi, dan mengembalikan laporan yang belum memenuhi standar untuk perbaikan.</td>
              <td>Monev Dashboard Access</td>
              <td>BR-05</td>
              <td><span class="badge badge-primary">High</span></td>
            </tr>
            <tr>
              <td><strong>FR-10</strong></td>
              <td>Sistem harus melakukan sinkronisasi transaksional otomatis seluruh data proposal (metadata, logbook, luaran, file paths) ke tabel master WUADC setelah status proposal mencapai COMPLETED, dengan mekanisme retry dan error logging jika sinkronisasi gagal.</td>
              <td>Status Change to COMPLETED</td>
              <td>BR-02</td>
              <td><span class="badge badge-danger">Critical</span></td>
            </tr>
            <tr>
              <td><strong>FR-11</strong></td>
              <td>Sistem harus mengirimkan notifikasi otomatis (email + in-app) kepada aktor terkait pada setiap perubahan status proposal: submit, approve, reject, revisi diperlukan, monev feedback, dan konfirmasi arsip WUADC.</td>
              <td>Status Change Events</td>
              <td>BR-04</td>
              <td><span class="badge badge-warning">Medium</span></td>
            </tr>
            <tr>
              <td><strong>FR-12</strong></td>
              <td>Sistem harus menyediakan dashboard analitik real-time dengan metrik: distribusi proposal per status/skema/fakultas, rata-rata waktu review per tier, SLA compliance rate, dan statistik sinkronisasi WUADC.</td>
              <td>Dashboard Page Load</td>
              <td>BR-06</td>
              <td><span class="badge badge-warning">Medium</span></td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    
    <!-- 3.3 Non-Functional -->
    <div class="section-card" id="nonfunc-req">
      <h3><span class="section-card-num">3.3.</span> Non-Functional Requirements</h3>
      <p class="section-card-desc">Persyaratan performa, keamanan, ketersediaan, skalabilitas, integritas data, dan auditabilitas sistem portal SIMPPM LPMB yang menjadi fondasi kualitas layanan (Quality of Service) untuk seluruh stakeholder.</p>
      <div class="bento-grid">
        <div class="bento-cell">
          <h4>🔄 Ketersediaan Sistem (Availability)</h4>
          <p>Portal wajib memiliki uptime minimal <strong>99.9%</strong> (SLA target) selama periode puncak pengiriman berkas. Downtime terencana hanya diperbolehkan di luar jam kerja (22:00-06:00 WIB) dengan notifikasi pemberitahuan minimal H-24. Mekanisme health check otomatis berjalan setiap 60 detik dengan auto-restart service jika terdeteksi kegagalan.</p>
        </div>
        <div class="bento-cell">
          <h4>🔒 Keamanan & Otorisasi (Security)</h4>
          <p>Implementasi Role-Based Access Control (RBAC) ketat untuk 6 peran pengguna. Seluruh komunikasi API menggunakan HTTPS/TLS 1.3. Dokumen sensitif (proposal, RAB, pakta) dienkripsi at-rest menggunakan AES-256. Session token menggunakan JWT dengan expiry 4 jam dan refresh token mechanism. Input sanitization diterapkan pada seluruh form field untuk mencegah XSS dan SQL injection.</p>
        </div>
        <div class="bento-cell">
          <h4>⚡ Performa & Responsivitas (Performance)</h4>
          <p>Waktu respons API harus <strong>kurang dari 2 detik</strong> untuk operasi standar (read/list) dan kurang dari 5 detik untuk operasi upload file. Portal harus mampu menangani minimal <strong>200 concurrent users</strong> saat periode puncak submission tanpa degradasi performa. File upload menggunakan chunked transfer untuk menghindari timeout pada koneksi lambat.</p>
        </div>
        <div class="bento-cell">
          <h4>📈 Skalabilitas (Scalability)</h4>
          <p>Arsitektur sistem harus mendukung horizontal scaling untuk mengakomodasi pertumbuhan jumlah proposal hingga <strong>5x</strong> dari volume saat ini tanpa perubahan arsitektur fundamental. Database menggunakan connection pooling dan read replicas untuk distribusi beban. File storage menggunakan cloud object storage (S3-compatible) yang auto-scalable.</p>
        </div>
        <div class="bento-cell">
          <h4>🗃️ Integritas Data (Data Integrity)</h4>
          <p>Sinkronisasi data ke tabel master WUADC wajib bersifat <strong>transaksional (ACID-compliant)</strong> dengan target kegagalan sinkronisasi <strong>0%</strong>. Mekanisme retry otomatis (max 3 attempts, exponential backoff) diterapkan jika koneksi ke WUADC terputus. Dead letter queue untuk menampung transaksi gagal yang memerlukan intervensi manual. Backup database otomatis setiap 6 jam dengan point-in-time recovery capability.</p>
        </div>
        <div class="bento-cell">
          <h4>📋 Auditabilitas (Auditability)</h4>
          <p>Seluruh aksi pengguna yang mengubah state sistem harus direkam dalam <strong>immutable audit log</strong> (REVIEW_LOG) yang tidak dapat diedit atau dihapus oleh siapapun termasuk admin. Log mencakup: user_id, action, timestamp, IP address, user agent, dan detail perubahan (before/after state). Retensi log minimal <strong>5 tahun</strong> sesuai kebijakan arsip perguruan tinggi.</p>
        </div>
      </div>
    </div>
    
    <!-- 3.4 Acceptance Criteria -->
    <div class="section-card" id="accept-crit">
      <h3><span class="section-card-num">3.4.</span> Acceptance Criteria (Gherkin Scenarios)</h3>
      <p class="section-card-desc">Kriteria pengujian penerimaan sistem dalam format Gherkin BDD yang mencakup skenario validasi berkas, alur persetujuan multi-tier, dan verifikasi sinkronisasi WUADC. Setiap skenario dipetakan ke Functional Requirement (FR) dan menjadi dasar UAT test plan pada Fase 6.</p>
      <pre>Scenario: Pengajuan Berkas Pengmas Tanpa Mengunggah RAB dan Pakta Integritas
  Given Dosen Ketua sedang mengisi formulir pengisian berkas pengmas skema "REGULER"
  And Dosen Ketua mengunggah berkas "t. proposal" dan "t. CV ketua"
  And Berkas "t. RAB" dan "pakta integritas" belum diunggah
  When Dosen Ketua melakukan klik tombol "Upload Berkas dan Submit"
  Then Sistem mengunci tombol submit dan memblokir pengiriman berkas
  And Menampilkan pesan kesalahan "Upload Berkas Gagal: Dokumen RAB dan Pakta Integritas wajib disertakan"
  And Status proposal tetap "DRAFT" tanpa perubahan
  # Mapped to: FR-04, UAT-L01</pre>

      <pre>Scenario: Alur Persetujuan Multi-Tier Berhasil Hingga Status APPROVED
  Given Dosen Ketua telah submit proposal dengan status "SUBMITTED"
  And Seluruh dokumen prasyarat (proposal, RAB, CV, SP, Pakta) telah diunggah lengkap
  When Akademik Fakultas melakukan review dan klik "Approve" dengan catatan "Berkas lengkap dan sesuai"
  Then Status proposal berubah menjadi "APPROVED_AKADEMIK"
  And Sistem mengirim notifikasi ke Dekanat Fakultas untuk review substansi
  When Dekanat Fakultas melakukan review dan klik "Approve" dengan catatan "Rekomendasi diterima"
  Then Status proposal berubah menjadi "APPROVED_DEKAN"
  And Sistem mengirim notifikasi ke Dosen Ketua untuk melengkapi tanda tangan
  When Dosen Ketua melengkapi tanda tangan administrasi dan klik "Konfirmasi TTD"
  Then Status proposal berubah menjadi "TTD_ADMIN"
  When Admin LPMB melakukan verifikasi konten dan klik "Verifikasi Lolos"
  Then Status proposal berubah menjadi "VERIFIED"
  When Akademik Fakultas melakukan review akhir dan klik "Terima Akhir"
  And Dekanat Fakultas melakukan review akhir dan klik "Terima Akhir"
  Then Status proposal berubah menjadi "APPROVED"
  And Sistem merekam 5 entri REVIEW_LOG secara kronologis dengan immutable timestamp
  # Mapped to: FR-06, FR-07, UAT-L03</pre>

      <pre>Scenario: Verifikasi Sinkronisasi Otomatis Data Arsip ke WUADC
  Given Proposal dengan ID "PMS-2026-0042" memiliki status "COMPLETED"
  And Laporan akhir, logbook (5 entri), dan dokumen luaran telah diunggah dan disetujui
  When Admin LPMB mengklik "Finalisasi dan Arsipkan"
  Then Sistem melakukan INSERT transaksional ke tabel WUADC_ARCHIVE dengan data:
    | Field               | Value                                         |
    | proposal_id         | PMS-2026-0042                                  |
    | tanggal_arsip       | 2026-06-04                                     |
    | doc_luaran_path     | /storage/wuadc/PMS-2026-0042/luaran_final.pdf  |
    | laporan_akhir_path  | /storage/wuadc/PMS-2026-0042/laporan_akhir.pdf |
    | status_arsip        | SYNCED                                         |
    | verified_by         | admin_lpmb_001                                 |
  And Status proposal berubah menjadi "ARCHIVED"
  And Sistem mengirim email konfirmasi arsip ke Dosen Ketua dan Admin LPMB
  And Jika sinkronisasi gagal, sistem melakukan retry max 3x dengan exponential backoff
  # Mapped to: FR-10, UAT-L06</pre>
    </div>
  </div>

  <!-- PHASE 4: SYSTEM DESIGN & MODELING -->
  <div class="phase-block">
    <div class="phase-badge pb-amber">Fase 4: Desain & Pemodelan Sistem (UML & Database)</div>
    
    <!-- 4.1 Activity Diagram -->
    <div class="section-card" id="activity">
      <h3><span class="section-card-num">4.1.</span> Activity Diagram (State Machine)</h3>
      <p class="section-card-desc">Alur logis aktivitas validasi dan seleksi proposal yang menggambarkan perpindahan state dari submission hingga keputusan akhir, termasuk jalur alternatif (reject/revisi) dan terminal state.</p>
      <div class="diagram-container">
        <div class="mermaid">
          stateDiagram-v2
            [*] --> SubmitProposal
            SubmitProposal --> CekFakultas
            state CekFakultas <<choice>>
            CekFakultas --> RevisiDraft : jika Dokumen Tidak Lengkap
            CekFakultas --> DeanApproval : jika Dokumen Lengkap
            RevisiDraft --> SubmitProposal
            DeanApproval --> FinalLPPMVerify
            state FinalLPPMVerify <<choice>>
            FinalLPPMVerify --> RejectAdmin : jika Gagal Verifikasi Administrasi
            FinalLPPMVerify --> AssignReviewers : jika Lolos Verifikasi Administrasi
            RejectAdmin --> [*]
            AssignReviewers --> ReviewProcess
            ReviewProcess --> PassingGradeCheck
            state PassingGradeCheck <<choice>>
            PassingGradeCheck --> ProposalRejected : jika Rata-rata Nilai < Passing Grade
            PassingGradeCheck --> ProposalApproved : jika Rata-rata Nilai >= Passing Grade
            ProposalRejected --> [*]
            ProposalApproved --> TandaTanganKontrak
            TandaTanganKontrak --> [*]
        </div>
      </div>

      <div style="background: #fafafb; padding: 24px; border-radius: 12px; border: 1px solid var(--border-color); margin-top: 20px;">
        <h4 style="margin-bottom: 12px; color: var(--text-dark);">Penjelasan State & Transisi</h4>
        <p style="font-size: 0.88rem; color: #475569; margin-bottom: 8px;"><strong>SubmitProposal →</strong> State awal ketika Dosen Ketua menyelesaikan pengisian formulir dan mengunggah seluruh berkas prasyarat. Proposal memasuki antrian review.</p>
        <p style="font-size: 0.88rem; color: #475569; margin-bottom: 8px;"><strong>CekFakultas (Decision) →</strong> Akademik Fakultas memeriksa kelengkapan berkas. Jika tidak lengkap, proposal dikembalikan ke Dosen Ketua untuk revisi (RevisiDraft). Jika lengkap, proposal diteruskan ke Dekanat (DeanApproval).</p>
        <p style="font-size: 0.88rem; color: #475569; margin-bottom: 8px;"><strong>RevisiDraft →</strong> State di mana Dosen Ketua memperbaiki dan melengkapi dokumen yang kurang. Setelah selesai, proposal dapat di-submit ulang kembali ke antrian CekFakultas.</p>
        <p style="font-size: 0.88rem; color: #475569; margin-bottom: 8px;"><strong>DeanApproval →</strong> Dekan melakukan review substansi dan memberikan rekomendasi persetujuan. Proposal yang disetujui diteruskan ke verifikasi Admin LPMB.</p>
        <p style="font-size: 0.88rem; color: #475569; margin-bottom: 8px;"><strong>FinalLPPMVerify (Decision) →</strong> Admin LPMB memverifikasi kesesuaian konten. Jika gagal, proposal ditolak secara permanen (RejectAdmin — terminal state). Jika lolos, proposal diteruskan ke tahap review akhir (AssignReviewers).</p>
        <p style="font-size: 0.88rem; color: #475569; margin-bottom: 8px;"><strong>AssignReviewers → ReviewProcess →</strong> Tahap review akhir berjenjang oleh Akademik dan Dekanat Fakultas dengan penilaian komprehensif berdasarkan passing grade yang telah ditetapkan.</p>
        <p style="font-size: 0.88rem; color: #475569; margin-bottom: 8px;"><strong>PassingGradeCheck (Decision) →</strong> Jika rata-rata nilai review di bawah passing grade, proposal ditolak (ProposalRejected — terminal). Jika memenuhi, proposal diterima (ProposalApproved) dan masuk tahap TandaTanganKontrak.</p>
        <p style="font-size: 0.88rem; color: #475569;"><strong>TandaTanganKontrak →</strong> State final di mana kontrak pelaksanaan kegiatan pengmas ditandatangani. Selanjutnya masuk ke fase pelaksanaan (IN_PROGRESS) yang dikelola di luar state machine validasi ini.</p>
      </div>
    </div>
    
    <!-- 4.2 Sequence Diagram -->
    <div class="section-card" id="sequence">
      <h3><span class="section-card-num">4.2.</span> Sequence Diagram — Full Approval Workflow</h3>
      <p class="section-card-desc">Aliran pesan lengkap dalam runtime untuk keseluruhan proses persetujuan proposal, dari submission oleh Dosen Ketua hingga sinkronisasi ke WUADC, melibatkan seluruh aktor dan komponen sistem.</p>
      <div class="diagram-container">
        <div class="mermaid">
          sequenceDiagram
            actor Ketua as Dosen Ketua
            participant Portal as Portal SIMPPM
            participant API as API Gateway
            participant DB as Database Server
            participant Cyber as API Cyber Kampus
            actor Akademik as Akademik Fakultas
            actor Dekan as Dekanat Fakultas
            actor Admin as Admin LPMB
            participant WUADC as WUADC Database

            Note over Ketua,Cyber: Fase Autentikasi & Pengajuan
            Ketua->>Portal: Login SSO (NIDN/Gmail)
            Portal->>Cyber: Validate credentials & status
            Cyber-->>Portal: User profile (NIDN, jabatan, fakultas)
            Portal->>DB: Create/Update user session
            Portal-->>Ketua: Dashboard + Active Period Check

            Ketua->>Portal: Pilih Skema & Isi Form Proposal
            Portal->>API: POST /api/v1/proposal (form + files)
            API->>DB: Validate period, scheme, member count
            API->>DB: INSERT proposal (status: SUBMITTED)
            API->>DB: INSERT member entries (status: PENDING)
            DB-->>API: proposal_id + confirmation
            API-->>Portal: 201 Created + proposal_id
            Portal-->>Ketua: Status UI: SUBMITTED

            Note over Akademik,Dekan: Fase Review Berjenjang
            Portal-->>Akademik: Notifikasi: Proposal baru menunggu review
            Akademik->>Portal: Buka detail proposal + checklist
            Akademik->>API: PUT /api/v1/proposal/{id}/review (action: APPROVE)
            API->>DB: UPDATE status = APPROVED_AKADEMIK
            API->>DB: INSERT review_log (reviewer, action, catatan)
            Portal-->>Dekan: Notifikasi: Proposal menunggu review Dekan

            Dekan->>Portal: Review substansi proposal
            Dekan->>API: PUT /api/v1/proposal/{id}/review (action: APPROVE)
            API->>DB: UPDATE status = APPROVED_DEKAN
            API->>DB: INSERT review_log
            Portal-->>Ketua: Notifikasi: Lengkapi TTD administrasi

            Ketua->>Portal: Upload TTD digital
            API->>DB: UPDATE status = TTD_ADMIN

            Note over Admin,WUADC: Fase Verifikasi & Finalisasi
            Portal-->>Admin: Notifikasi: Proposal menunggu verifikasi
            Admin->>Portal: Verifikasi konten proposal
            Admin->>API: PUT /api/v1/proposal/{id}/review (action: VERIFY)
            API->>DB: UPDATE status = VERIFIED
            API->>DB: INSERT review_log

            Portal-->>Akademik: Notifikasi: Review akhir
            Akademik->>API: PUT /api/v1/proposal/{id}/review (action: FINAL_APPROVE)
            Portal-->>Dekan: Notifikasi: Review akhir
            Dekan->>API: PUT /api/v1/proposal/{id}/review (action: FINAL_APPROVE)
            API->>DB: UPDATE status = APPROVED

            Note over Ketua,WUADC: Fase Pelaksanaan & Pengarsipan
            Ketua->>API: POST /api/v1/proposal/{id}/logbook (entries)
            API->>DB: INSERT logbook entries
            Admin->>API: Monev evaluation
            API->>DB: UPDATE status = COMPLETED

            Admin->>API: POST /api/v1/wuadc/sync (proposal_id)
            API->>WUADC: Transactional INSERT (metadata + files)
            WUADC-->>API: SYNC_SUCCESS
            API->>DB: UPDATE status = ARCHIVED
            Portal-->>Ketua: Email: Arsip WUADC berhasil
        </div>
      </div>
    </div>
    
    <!-- 4.3 ERD -->
    <div class="section-card" id="erd">
      <h3><span class="section-card-num">4.3.</span> Entity Relationship Diagram (ERD Schema)</h3>
      <p class="section-card-desc">Struktur relasi database portal yang diperluas untuk mengelola siklus lengkap pengabdian masyarakat, termasuk entitas pendukung: konfigurasi skema, pencatatan review audit trail, manajemen notifikasi, dan kontrol periode pendaftaran.</p>
      <div class="diagram-container">
        <div class="mermaid">
          erDiagram
            USER ||--o{ PROPOSAL : creates
            PROPOSAL ||--|{ MEMBER : contains
            USER ||--o{ MEMBER : joins
            PROPOSAL ||--o{ LOGBOOK_LPMB : tracks
            PROPOSAL ||--o| WUADC_ARCHIVE : archives
            PROPOSAL ||--o{ REVIEW_LOG : reviewed_by
            USER ||--o{ REVIEW_LOG : performs
            SKEMA_PENGMAS ||--o{ PROPOSAL : categorizes
            PERIODE_PENGMAS ||--o{ PROPOSAL : within
            USER ||--o{ NOTIFICATION : receives
            
            USER {
              int user_id PK
              string nama
              string email
              string nidn_nim
              string unit_kerja
              string role_type
              string jabatan_akademik
              string fakultas
              string prodi
              string phone
              string auth_provider
              datetime last_login
              boolean is_active
              datetime created_at
            }
            PROPOSAL {
              int proposal_id PK
              int ketua_id FK
              int skema_id FK
              int periode_id FK
              string judul
              string abstrak
              string tahun_pelaksanaan
              decimal dana_diajukan
              string status_approval
              string file_proposal_path
              string file_rab_path
              string file_cv_path
              string file_sp_path
              string file_pakta_path
              string file_laporan_akhir_path
              datetime tanggal_submit
              datetime tanggal_approve
              string catatan_reviewer
              datetime created_at
              datetime updated_at
            }
            MEMBER {
              int member_id PK
              int proposal_id FK
              int user_id FK
              string tipe_anggota
              string status_persetujuan
              string role_in_project
              datetime tanggal_join
              datetime created_at
            }
            LOGBOOK_LPMB {
              int logbook_id PK
              int proposal_id FK
              int submitted_by FK
              string tanggal_kegiatan
              string uraian_kegiatan
              float progress_percentage
              string file_lampiran_path
              string status_review
              string catatan_monev
              datetime created_at
            }
            WUADC_ARCHIVE {
              int wuadc_id PK
              int proposal_id FK
              string tanggal_arsip
              string doc_luaran_path
              string laporan_akhir_path
              string status_arsip
              string verified_by
              string sync_error_log
              datetime synced_at
            }
            REVIEW_LOG {
              int review_log_id PK
              int reviewer_id FK
              int proposal_id FK
              string action
              string review_tier
              string catatan
              string ip_address
              string user_agent
              datetime timestamp
            }
            SKEMA_PENGMAS {
              int skema_id PK
              string nama_skema
              string deskripsi
              int max_anggota_dosen
              int max_anggota_mhs
              string dokumen_wajib
              decimal max_dana
              boolean is_active
              datetime created_at
            }
            NOTIFICATION {
              int notification_id PK
              int user_id FK
              string tipe
              string pesan
              string link_url
              boolean is_read
              datetime created_at
            }
            PERIODE_PENGMAS {
              int periode_id PK
              string tahun_akademik
              date tanggal_buka
              date tanggal_tutup
              boolean is_active
              string deskripsi
              datetime created_at
            }
        </div>
      </div>
    </div>

    <!-- 4.4 Data Dictionary -->
    <div class="section-card" id="data-dictionary">
      <h3><span class="section-card-num">4.4.</span> Data Dictionary — Entitas PROPOSAL</h3>
      <p class="section-card-desc">Spesifikasi detail field-by-field untuk entitas inti PROPOSAL, mencakup tipe data, constraint, nilai default, dan deskripsi bisnis. Data dictionary ini menjadi referensi utama bagi tim development dan DBA dalam pembuatan migration script dan validasi input.</p>
      <div class="table-wrapper">
        <table>
          <thead>
            <tr>
              <th>Field Name</th>
              <th>Data Type</th>
              <th>Constraint</th>
              <th>Default</th>
              <th>Deskripsi Bisnis</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><code>proposal_id</code></td>
              <td>INT / SERIAL</td>
              <td>PRIMARY KEY, AUTO_INCREMENT</td>
              <td>-</td>
              <td>Identifier unik proposal yang di-generate otomatis oleh database. Format tampilan di UI: PMS-{YYYY}-{NNNN}.</td>
            </tr>
            <tr>
              <td><code>ketua_id</code></td>
              <td>INT</td>
              <td>FOREIGN KEY → USER.user_id, NOT NULL</td>
              <td>-</td>
              <td>Referensi ke user yang bertindak sebagai Dosen Ketua pengusul proposal. Satu user hanya boleh menjadi ketua 1 proposal aktif per periode.</td>
            </tr>
            <tr>
              <td><code>skema_id</code></td>
              <td>INT</td>
              <td>FOREIGN KEY → SKEMA_PENGMAS.skema_id, NOT NULL</td>
              <td>-</td>
              <td>Referensi ke skema pengmas yang dipilih (Reguler=1, Internal=2, Mandiri=3). Menentukan konfigurasi formulir dan dokumen wajib.</td>
            </tr>
            <tr>
              <td><code>periode_id</code></td>
              <td>INT</td>
              <td>FOREIGN KEY → PERIODE_PENGMAS.periode_id, NOT NULL</td>
              <td>-</td>
              <td>Referensi ke periode pendaftaran saat proposal di-submit. Digunakan untuk validasi bahwa submission hanya terjadi selama periode aktif.</td>
            </tr>
            <tr>
              <td><code>judul</code></td>
              <td>VARCHAR(500)</td>
              <td>NOT NULL</td>
              <td>-</td>
              <td>Judul lengkap proposal kegiatan pengabdian masyarakat. Maksimum 500 karakter, wajib diisi, di-index untuk full-text search.</td>
            </tr>
            <tr>
              <td><code>abstrak</code></td>
              <td>TEXT</td>
              <td>NOT NULL</td>
              <td>-</td>
              <td>Ringkasan isi proposal mencakup latar belakang, tujuan, metode, dan target luaran. Maksimum 2000 karakter.</td>
            </tr>
            <tr>
              <td><code>tahun_pelaksanaan</code></td>
              <td>VARCHAR(9)</td>
              <td>NOT NULL, FORMAT: YYYY/YYYY</td>
              <td>-</td>
              <td>Tahun akademik pelaksanaan kegiatan, misalnya "2026/2027". Digunakan untuk pelaporan per tahun akademik.</td>
            </tr>
            <tr>
              <td><code>dana_diajukan</code></td>
              <td>DECIMAL(15,2)</td>
              <td>NOT NULL, CHECK >= 0</td>
              <td>0.00</td>
              <td>Total anggaran biaya yang diajukan dalam Rupiah. Untuk skema Mandiri, nilai ini boleh 0. Untuk skema lain, harus > 0 dan <= max_dana pada SKEMA_PENGMAS.</td>
            </tr>
            <tr>
              <td><code>status_approval</code></td>
              <td>VARCHAR(30)</td>
              <td>NOT NULL, ENUM constraint</td>
              <td>'DRAFT'</td>
              <td>Status lifecycle proposal saat ini. Nilai yang diperbolehkan: DRAFT, SUBMITTED, REVIEW_AKADEMIK, APPROVED_AKADEMIK, REJECTED_AKADEMIK, REVIEW_DEKAN, APPROVED_DEKAN, REJECTED_DEKAN, TTD_ADMIN, VERIFIED, REJECTED_ADMIN, REVIEW_FINAL_AKAD, REVIEW_FINAL_DEKAN, REJECTED_FINAL, APPROVED, IN_PROGRESS, MONEV, COMPLETED, ARCHIVED.</td>
            </tr>
            <tr>
              <td><code>file_proposal_path</code></td>
              <td>VARCHAR(512)</td>
              <td>NULLABLE (wajib saat submit)</td>
              <td>NULL</td>
              <td>Path relatif ke file proposal yang diunggah di cloud storage. Format: /storage/proposals/{proposal_id}/proposal.pdf. Validasi: PDF/DOC/DOCX, max 10MB.</td>
            </tr>
            <tr>
              <td><code>file_rab_path</code></td>
              <td>VARCHAR(512)</td>
              <td>NULLABLE (wajib saat submit untuk skema non-Mandiri)</td>
              <td>NULL</td>
              <td>Path relatif ke file Rencana Anggaran Biaya. Validasi tipe dan ukuran file sama dengan file_proposal_path.</td>
            </tr>
            <tr>
              <td><code>file_cv_path</code></td>
              <td>VARCHAR(512)</td>
              <td>NULLABLE (wajib saat submit)</td>
              <td>NULL</td>
              <td>Path relatif ke file Curriculum Vitae Dosen Ketua. Wajib menyertakan riwayat pengabdian sebelumnya.</td>
            </tr>
            <tr>
              <td><code>file_sp_path</code></td>
              <td>VARCHAR(512)</td>
              <td>NULLABLE (wajib saat submit)</td>
              <td>NULL</td>
              <td>Path relatif ke file Surat Pernyataan keaslian dan kesanggupan pelaksanaan kegiatan.</td>
            </tr>
            <tr>
              <td><code>file_pakta_path</code></td>
              <td>VARCHAR(512)</td>
              <td>NULLABLE (wajib saat submit)</td>
              <td>NULL</td>
              <td>Path relatif ke file Pakta Integritas yang telah ditandatangani oleh Dosen Ketua.</td>
            </tr>
            <tr>
              <td><code>file_laporan_akhir_path</code></td>
              <td>VARCHAR(512)</td>
              <td>NULLABLE (wajib saat status COMPLETED)</td>
              <td>NULL</td>
              <td>Path relatif ke file Laporan Akhir kegiatan pengmas. Diisi setelah pelaksanaan kegiatan selesai.</td>
            </tr>
            <tr>
              <td><code>tanggal_submit</code></td>
              <td>DATETIME</td>
              <td>NULLABLE</td>
              <td>NULL</td>
              <td>Timestamp saat Dosen Ketua pertama kali menekan tombol Submit. Diisi otomatis oleh sistem dan tidak dapat diubah.</td>
            </tr>
            <tr>
              <td><code>tanggal_approve</code></td>
              <td>DATETIME</td>
              <td>NULLABLE</td>
              <td>NULL</td>
              <td>Timestamp saat proposal memperoleh status APPROVED (final approval). Digunakan untuk menghitung SLA review.</td>
            </tr>
            <tr>
              <td><code>catatan_reviewer</code></td>
              <td>TEXT</td>
              <td>NULLABLE</td>
              <td>NULL</td>
              <td>Catatan evaluasi terakhir dari reviewer. Untuk riwayat lengkap seluruh catatan review, lihat tabel REVIEW_LOG.</td>
            </tr>
            <tr>
              <td><code>created_at</code></td>
              <td>DATETIME</td>
              <td>NOT NULL, DEFAULT CURRENT_TIMESTAMP</td>
              <td>CURRENT_TIMESTAMP</td>
              <td>Timestamp pembuatan record proposal (saat pertama kali disimpan sebagai DRAFT).</td>
            </tr>
            <tr>
              <td><code>updated_at</code></td>
              <td>DATETIME</td>
              <td>NOT NULL, ON UPDATE CURRENT_TIMESTAMP</td>
              <td>CURRENT_TIMESTAMP</td>
              <td>Timestamp terakhir kali record proposal diubah (termasuk perubahan status, edit konten, dsb.).</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>

  <!-- PHASE 5: TECHNICAL SPECS -->
  <div class="phase-block">
    <div class="phase-badge pb-rose">Fase 5: Spesifikasi Teknis & Integrasi API</div>
    
    <!-- 5.1 API Doc -->
    <div class="section-card" id="api-doc">
      <h3><span class="section-card-num">5.1.</span> API Documentation (RESTful Endpoints)</h3>
      <p class="section-card-desc">Dokumentasi lengkap endpoint API portal SIMPPM LPMB yang mencakup seluruh operasi CRUD proposal, manajemen anggota, logbook submission, workflow review, sinkronisasi WUADC, dan dashboard analitik. Seluruh endpoint menggunakan base URL <code>/api/v1</code> dengan autentikasi JWT Bearer Token.</p>
      
      <strong>1. Endpoint:</strong> <code style="background:#e2e8f0; padding:2px 6px; border-radius:4px; font-family:'JetBrains Mono';">POST /api/v1/proposal</code>
      <p style="font-size: 0.88rem; color: #475569; margin: 4px 0 8px;">Membuat proposal pengmas baru dengan status awal DRAFT. Mendukung multipart/form-data untuk upload berkas bersamaan.</p>
      <pre>{
  "judul": "Sosialisasi Digital Marketing untuk UMKM Batik Tradisional",
  "abstrak": "Kegiatan pengabdian untuk meningkatkan kapabilitas pemasaran digital...",
  "skema_pengmas": "REGULER",
  "tahun_pelaksanaan": "2026/2027",
  "dana_diajukan": 15000000.00,
  "anggota_dosen": ["0423108821", "0415067702"],
  "anggota_mahasiswa": ["434231055", "434231078"],
  "file_proposal": "binary_content",
  "file_rab": "binary_content",
  "file_cv": "binary_content",
  "file_sp": "binary_content",
  "file_pakta": "binary_content"
}

// Response: 201 Created
{
  "status": "success",
  "data": {
    "proposal_id": "PMS-2026-0042",
    "status_approval": "SUBMITTED",
    "tanggal_submit": "2026-06-04T10:30:00Z",
    "message": "Proposal berhasil di-submit. Menunggu review Akademik Fakultas."
  }
}</pre>

      <strong style="display:block; margin-top:20px;">2. Endpoint:</strong> <code style="background:#e2e8f0; padding:2px 6px; border-radius:4px; font-family:'JetBrains Mono';">GET /api/v1/proposals?status={status}&skema={skema}&page={n}&limit={n}</code>
      <p style="font-size: 0.88rem; color: #475569; margin: 4px 0 8px;">Mengambil daftar proposal dengan filter status, skema, dan pagination. Digunakan oleh dashboard Admin LPMB dan halaman antrean reviewer.</p>
      <pre>// Response: 200 OK
{
  "status": "success",
  "data": {
    "proposals": [
      {
        "proposal_id": "PMS-2026-0042",
        "judul": "Sosialisasi Digital Marketing untuk UMKM Batik Tradisional",
        "ketua_nama": "Dr. Ahmad Fauzi, M.Kom.",
        "skema_pengmas": "REGULER",
        "status_approval": "REVIEW_AKADEMIK",
        "tanggal_submit": "2026-06-04T10:30:00Z",
        "fakultas": "Fakultas Ilmu Komputer"
      }
    ],
    "pagination": { "page": 1, "limit": 20, "total": 145, "total_pages": 8 }
  }
}</pre>

      <strong style="display:block; margin-top:20px;">3. Endpoint:</strong> <code style="background:#e2e8f0; padding:2px 6px; border-radius:4px; font-family:'JetBrains Mono';">GET /api/v1/proposal/{id}</code>
      <p style="font-size: 0.88rem; color: #475569; margin: 4px 0 8px;">Mengambil detail lengkap satu proposal beserta daftar anggota, file paths, dan riwayat review log.</p>
      <pre>// Response: 200 OK
{
  "status": "success",
  "data": {
    "proposal_id": "PMS-2026-0042",
    "judul": "Sosialisasi Digital Marketing untuk UMKM Batik Tradisional",
    "abstrak": "Kegiatan pengabdian untuk meningkatkan kapabilitas...",
    "skema_pengmas": "REGULER",
    "dana_diajukan": 15000000.00,
    "status_approval": "APPROVED_AKADEMIK",
    "members": [
      { "user_id": 102, "nama": "Dr. Siti Rahayu", "tipe": "DOSEN_ANGGOTA", "status": "APPROVED" },
      { "user_id": 305, "nama": "Budi Santoso", "tipe": "MAHASISWA", "status": "APPROVED" }
    ],
    "files": {
      "proposal": "/storage/proposals/PMS-2026-0042/proposal.pdf",
      "rab": "/storage/proposals/PMS-2026-0042/rab.pdf",
      "cv": "/storage/proposals/PMS-2026-0042/cv.pdf",
      "sp": "/storage/proposals/PMS-2026-0042/sp.pdf",
      "pakta": "/storage/proposals/PMS-2026-0042/pakta.pdf"
    },
    "review_logs": [
      { "reviewer": "Staf Akademik FIK", "action": "APPROVE", "catatan": "Berkas lengkap", "timestamp": "2026-06-05T09:15:00Z" }
    ]
  }
}

// Response: 404 Not Found
{ "status": "error", "message": "Proposal tidak ditemukan", "code": "PROPOSAL_NOT_FOUND" }</pre>

      <strong style="display:block; margin-top:20px;">4. Endpoint:</strong> <code style="background:#e2e8f0; padding:2px 6px; border-radius:4px; font-family:'JetBrains Mono';">PUT /api/v1/proposal/{id}/review</code>
      <p style="font-size: 0.88rem; color: #475569; margin: 4px 0 8px;">Mengubah status proposal melalui aksi review (approve/reject/verify). Digunakan oleh Akademik, Dekanat, dan Admin LPMB. Otomatis mencatat REVIEW_LOG.</p>
      <pre>{
  "action": "APPROVE",
  "review_tier": "AKADEMIK_AWAL",
  "catatan": "Berkas lengkap dan sesuai template. Diteruskan ke Dekanat untuk review substansi."
}

// Response: 200 OK
{
  "status": "success",
  "data": {
    "proposal_id": "PMS-2026-0042",
    "previous_status": "REVIEW_AKADEMIK",
    "new_status": "APPROVED_AKADEMIK",
    "review_log_id": 1847,
    "next_action": "Menunggu review Dekanat Fakultas"
  }
}

// Response: 403 Forbidden
{ "status": "error", "message": "Anda tidak memiliki hak akses untuk melakukan review pada proposal ini", "code": "UNAUTHORIZED_REVIEW" }</pre>

      <strong style="display:block; margin-top:20px;">5. Endpoint:</strong> <code style="background:#e2e8f0; padding:2px 6px; border-radius:4px; font-family:'JetBrains Mono';">POST /api/v1/proposal/{id}/member</code>
      <p style="font-size: 0.88rem; color: #475569; margin: 4px 0 8px;">Menambahkan anggota tim (dosen/mahasiswa) ke proposal. Validasi: NIDN/NIM harus aktif, belum menjadi anggota proposal lain dalam periode sama, dan tidak melebihi batas anggota per skema.</p>
      <pre>{
  "nidn_nim": "0423108821",
  "tipe_anggota": "DOSEN_ANGGOTA",
  "role_in_project": "Narasumber Pelatihan"
}

// Response: 201 Created
{
  "status": "success",
  "data": {
    "member_id": 256,
    "user_nama": "Dr. Siti Rahayu, M.T.",
    "status_persetujuan": "PENDING",
    "notification_sent": true
  }
}

// Response: 409 Conflict
{ "status": "error", "message": "Dosen sudah terdaftar sebagai anggota proposal aktif lain dalam periode ini", "code": "DUPLICATE_MEMBER" }</pre>

      <strong style="display:block; margin-top:20px;">6. Endpoint:</strong> <code style="background:#e2e8f0; padding:2px 6px; border-radius:4px; font-family:'JetBrains Mono';">POST /api/v1/proposal/{id}/logbook</code>
      <p style="font-size: 0.88rem; color: #475569; margin: 4px 0 8px;">Mengunggah entri logbook kegiatan untuk proposal yang berstatus IN_PROGRESS. Mendukung file lampiran dokumentasi.</p>
      <pre>{
  "tanggal_kegiatan": "2026-06-04",
  "uraian_kegiatan": "Pelaksanaan pelatihan pembuatan foto produk UMKM batik di Kelurahan Sukoharjo",
  "progress_percentage": 45.0,
  "file_lampiran": "binary_content"
}

// Response: 201 Created
{
  "status": "success",
  "data": {
    "logbook_id": 892,
    "proposal_id": "PMS-2026-0042",
    "progress_percentage": 45.0,
    "status_review": "PENDING_MONEV",
    "file_lampiran_path": "/storage/logbook/PMS-2026-0042/log_892.pdf"
  }
}</pre>

      <strong style="display:block; margin-top:20px;">7. Endpoint:</strong> <code style="background:#e2e8f0; padding:2px 6px; border-radius:4px; font-family:'JetBrains Mono';">POST /api/v1/wuadc/sync</code>
      <p style="font-size: 0.88rem; color: #475569; margin: 4px 0 8px;">Melakukan sinkronisasi transaksional data proposal yang telah COMPLETED ke database master WUADC. Mendukung retry mechanism dengan exponential backoff.</p>
      <pre>{
  "proposal_id": "PMS-2026-0042",
  "force_retry": false
}

// Response: 200 OK
{
  "status": "success",
  "data": {
    "wuadc_id": 1204,
    "proposal_id": "PMS-2026-0042",
    "status_arsip": "SYNCED",
    "synced_at": "2026-06-04T14:22:00Z",
    "records_inserted": {
      "metadata": 1, "logbook_entries": 5, "luaran_documents": 3
    }
  }
}

// Response: 500 Internal Server Error
{
  "status": "error",
  "message": "Sinkronisasi ke WUADC gagal setelah 3 percobaan. Transaksi masuk dead letter queue.",
  "code": "WUADC_SYNC_FAILED",
  "retry_count": 3,
  "dlq_id": "DLQ-2026-0891"
}</pre>

      <strong style="display:block; margin-top:20px;">8. Endpoint:</strong> <code style="background:#e2e8f0; padding:2px 6px; border-radius:4px; font-family:'JetBrains Mono';">GET /api/v1/dashboard/stats?periode_id={id}</code>
      <p style="font-size: 0.88rem; color: #475569; margin: 4px 0 8px;">Mengambil statistik dashboard untuk monitoring dan analitik. Tersedia bagi Admin LPMB dan pimpinan.</p>
      <pre>// Response: 200 OK
{
  "status": "success",
  "data": {
    "total_proposals": 245,
    "by_status": {
      "DRAFT": 12, "SUBMITTED": 28, "REVIEW_AKADEMIK": 15,
      "APPROVED_AKADEMIK": 8, "REVIEW_DEKAN": 6, "APPROVED_DEKAN": 4,
      "VERIFIED": 3, "APPROVED": 42, "IN_PROGRESS": 38,
      "MONEV": 11, "COMPLETED": 55, "ARCHIVED": 23
    },
    "by_skema": { "REGULER": 120, "INTERNAL": 85, "MANDIRI": 40 },
    "avg_review_time_hours": { "akademik": 18.5, "dekan": 24.2, "admin_lpmb": 12.8 },
    "sla_compliance_rate": 94.2,
    "wuadc_sync_success_rate": 100.0
  }
}</pre>
    </div>
    
    <!-- 5.2 Validation Rules -->
    <div class="section-card" id="val-rules">
      <h3><span class="section-card-num">5.2.</span> Validation Rules (Logika Bisnis)</h3>
      <p class="section-card-desc">Pengecekan integritas data yang diterapkan pada setiap titik input kritis dalam sistem, mencakup validasi akun, berkas, batasan proposal, ukuran file, tipe file, keanggotaan, periode, dan pencegahan duplikasi. Setiap aturan dilengkapi kode error standar untuk konsistensi pesan kesalahan di seluruh platform.</p>
      <div class="table-wrapper">
        <table>
          <thead>
            <tr>
              <th>ID</th>
              <th>Aturan Validasi</th>
              <th>Syarat Kriteria Sistem</th>
              <th>Pesan Kesalahan (Error Code)</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>VR-01</strong></td>
              <td>Cyber Kampus Account Check</td>
              <td>Nomor NIDN/NIM wajib terdaftar aktif di server database PDDIKTI dan API Cyber Kampus. Status kepegawaian/kemahasiswaan harus "AKTIF".</td>
              <td><code>USER_NOT_ACTIVE</code>: Pengguna Tidak Aktif / Tidak Terdaftar di Sistem Akademik</td>
            </tr>
            <tr>
              <td><strong>VR-02</strong></td>
              <td>Mandatory Files Check</td>
              <td>Dosen Ketua wajib menyertakan seluruh dokumen prasyarat sesuai skema saat submit: Proposal, RAB, CV, SP, dan Pakta Integritas. Untuk skema Mandiri, RAB bersifat opsional.</td>
              <td><code>MISSING_MANDATORY_DOCUMENTS</code>: Dokumen Prasyarat Wajib Tidak Lengkap — {nama_dokumen}</td>
            </tr>
            <tr>
              <td><strong>VR-03</strong></td>
              <td>Single Active Proposal</td>
              <td>Dosen Ketua hanya boleh mengusulkan maksimal 1 proposal aktif (status bukan ARCHIVED/REJECTED) dalam periode pendaftaran berjalan.</td>
              <td><code>LIMIT_EXCEEDED</code>: Batas Pengajuan Proposal Pengmas Terlampaui (Max: 1 per Periode)</td>
            </tr>
            <tr>
              <td><strong>VR-04</strong></td>
              <td>File Size Limit</td>
              <td>Setiap file yang diunggah tidak boleh melebihi ukuran <strong>10MB</strong>. Total ukuran seluruh file per proposal tidak boleh melebihi <strong>50MB</strong>.</td>
              <td><code>FILE_SIZE_EXCEEDED</code>: Ukuran File Melebihi Batas Maksimum (10MB per file, 50MB total)</td>
            </tr>
            <tr>
              <td><strong>VR-05</strong></td>
              <td>File Type Restriction</td>
              <td>Hanya file dengan ekstensi <strong>.pdf</strong>, <strong>.doc</strong>, dan <strong>.docx</strong> yang diperbolehkan untuk diunggah. File gambar, video, atau format lain akan ditolak.</td>
              <td><code>INVALID_FILE_TYPE</code>: Tipe File Tidak Diizinkan — Hanya PDF, DOC, DOCX</td>
            </tr>
            <tr>
              <td><strong>VR-06</strong></td>
              <td>Member Count Validation</td>
              <td>Jumlah anggota tim tidak boleh melebihi batas yang dikonfigurasi pada skema: Reguler (max 3 dosen, max 5 mahasiswa), Internal (max 2 dosen, max 3 mahasiswa), Mandiri (max 2 dosen, max 2 mahasiswa).</td>
              <td><code>MEMBER_LIMIT_EXCEEDED</code>: Jumlah Anggota Melebihi Batas Skema — {tipe}: {current}/{max}</td>
            </tr>
            <tr>
              <td><strong>VR-07</strong></td>
              <td>Period Submission Check</td>
              <td>Proposal hanya dapat di-submit selama periode pendaftaran aktif (<code>is_active = true AND CURRENT_DATE BETWEEN tanggal_buka AND tanggal_tutup</code>). Submission di luar periode akan diblokir.</td>
              <td><code>PERIOD_CLOSED</code>: Periode Pendaftaran Tidak Aktif atau Sudah Ditutup</td>
            </tr>
            <tr>
              <td><strong>VR-08</strong></td>
              <td>Duplicate Member Check</td>
              <td>Satu dosen/mahasiswa tidak boleh menjadi anggota lebih dari 1 proposal aktif dalam periode pendaftaran yang sama. Validasi dilakukan saat penambahan anggota.</td>
              <td><code>DUPLICATE_MEMBER</code>: Anggota Sudah Terdaftar di Proposal Aktif Lain pada Periode Ini</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    
    <!-- 5.3 RACI Matrix -->
    <div class="section-card" id="role-matrix">
      <h3><span class="section-card-num">5.3.</span> Role & RACI Access Control Matrix</h3>
      <p class="section-card-desc">Pemetaan hak akses dan tanggung jawab (Responsible, Accountable, Consulted, Informed) untuk setiap fitur utama sistem, dipetakan ke 5 peran operasional pengguna. Matriks ini menjadi dasar implementasi RBAC (Role-Based Access Control) pada middleware API.</p>
      <div class="table-wrapper">
        <table>
          <thead>
            <tr>
              <th>Fitur / Layanan</th>
              <th>Dosen Ketua</th>
              <th>Dosen Anggota / Mhs</th>
              <th>Akademik Fakultas</th>
              <th>Dekanat Fakultas</th>
              <th>Admin LPMB</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Create & Edit Proposal</td>
              <td><span class="badge badge-success">R / Full</span></td>
              <td>-</td>
              <td>-</td>
              <td>-</td>
              <td><span class="badge badge-primary">Read</span></td>
            </tr>
            <tr>
              <td>Upload Dokumen Prasyarat</td>
              <td><span class="badge badge-success">R / Full</span></td>
              <td>-</td>
              <td>-</td>
              <td>-</td>
              <td><span class="badge badge-primary">Read</span></td>
            </tr>
            <tr>
              <td>Invite & Manage Members</td>
              <td><span class="badge badge-success">R / Full</span></td>
              <td><span class="badge badge-primary">Read</span></td>
              <td>-</td>
              <td>-</td>
              <td><span class="badge badge-primary">Read</span></td>
            </tr>
            <tr>
              <td>Review Berkas (Awal)</td>
              <td><span class="badge badge-primary">Informed</span></td>
              <td>-</td>
              <td><span class="badge badge-success">R / Approve</span></td>
              <td>-</td>
              <td><span class="badge badge-primary">Read</span></td>
            </tr>
            <tr>
              <td>Approve Rekomendasi (Dekan)</td>
              <td><span class="badge badge-primary">Informed</span></td>
              <td>-</td>
              <td><span class="badge badge-primary">Informed</span></td>
              <td><span class="badge badge-success">R / Approve</span></td>
              <td><span class="badge badge-primary">Read</span></td>
            </tr>
            <tr>
              <td>Pelengkapan TTD Administrasi</td>
              <td><span class="badge badge-success">R / Full</span></td>
              <td><span class="badge badge-primary">Read</span></td>
              <td>-</td>
              <td>-</td>
              <td>-</td>
            </tr>
            <tr>
              <td>Verifikasi Konten (LPMB)</td>
              <td><span class="badge badge-primary">Informed</span></td>
              <td>-</td>
              <td>-</td>
              <td>-</td>
              <td><span class="badge badge-success">R / Full</span></td>
            </tr>
            <tr>
              <td>Review Akhir (Akademik)</td>
              <td><span class="badge badge-primary">Informed</span></td>
              <td>-</td>
              <td><span class="badge badge-success">R / Approve</span></td>
              <td>-</td>
              <td><span class="badge badge-primary">Read</span></td>
            </tr>
            <tr>
              <td>Review Akhir (Dekan)</td>
              <td><span class="badge badge-primary">Informed</span></td>
              <td>-</td>
              <td><span class="badge badge-primary">Informed</span></td>
              <td><span class="badge badge-success">R / Approve</span></td>
              <td><span class="badge badge-primary">Read</span></td>
            </tr>
            <tr>
              <td>Submit Logbook Kegiatan</td>
              <td><span class="badge badge-success">R / Full</span></td>
              <td><span class="badge badge-primary">Read</span></td>
              <td>-</td>
              <td>-</td>
              <td><span class="badge badge-success">A / Evaluate</span></td>
            </tr>
            <tr>
              <td>Monev Evaluation</td>
              <td><span class="badge badge-primary">Informed</span></td>
              <td><span class="badge badge-primary">Read</span></td>
              <td><span class="badge badge-primary">Read</span></td>
              <td>-</td>
              <td><span class="badge badge-success">R / Full</span></td>
            </tr>
            <tr>
              <td>Archive to WUADC</td>
              <td>-</td>
              <td>-</td>
              <td>-</td>
              <td>-</td>
              <td><span class="badge badge-success">R / Full</span></td>
            </tr>
            <tr>
              <td>Configure Scheme & Period</td>
              <td>-</td>
              <td>-</td>
              <td>-</td>
              <td>-</td>
              <td><span class="badge badge-success">R / Full</span></td>
            </tr>
            <tr>
              <td>View Dashboard Analytics</td>
              <td><span class="badge badge-primary">Read (Own)</span></td>
              <td><span class="badge badge-primary">Read (Own)</span></td>
              <td><span class="badge badge-primary">Read (Faculty)</span></td>
              <td><span class="badge badge-primary">Read (Faculty)</span></td>
              <td><span class="badge badge-success">R / Full</span></td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    
    <!-- 5.4 Exception Flow -->
    <div class="section-card" id="exception">
      <h3><span class="section-card-num">5.4.</span> Exception Flow & Escalation Scenarios</h3>
      <p class="section-card-desc">Daftar skenario pengecualian (exception) yang mungkin terjadi selama operasional sistem, beserta kebijakan eskalasi dan mekanisme fallback yang diterapkan untuk menjaga keberlangsungan layanan.</p>
      
      <div style="background: #fff5f5; border: 1px solid #fecaca; border-radius: 12px; padding: 24px; margin-bottom: 16px;">
        <p style="color: #991b1b; font-weight: 700; margin-bottom: 8px;">EXC-01: Kebijakan Eskalasi SLA Review (3 Hari Kerja)</p>
        <p style="color: #7f1d1d; font-size: 0.9rem;">Apabila pihak Akademik Fakultas atau Dekanat tidak melakukan peninjauan/keputusan persetujuan dalam waktu <strong>3 hari kerja</strong> sejak berkas di-submit oleh Dosen Ketua, sistem otomatis mengirimkan notifikasi eskalasi bertingkat: (1) <strong>Hari ke-3:</strong> Notifikasi pengingat ke reviewer via email + in-app. (2) <strong>Hari ke-5:</strong> Eskalasi ke pimpinan fakultas (Wakil Dekan I) dengan CC ke Admin LPMB. (3) <strong>Hari ke-7:</strong> Eskalasi ke Direktur LPMB dengan laporan antrean tertunda. Notifikasi peringatan dikirimkan harian ke dashboard dekanat guna mencegah antrean usulan mandek. Statistik SLA compliance tercatat otomatis di dashboard analitik.</p>
      </div>

      <div style="background: #fffbeb; border: 1px solid #fde68a; border-radius: 12px; padding: 24px; margin-bottom: 16px;">
        <p style="color: #92400e; font-weight: 700; margin-bottom: 8px;">EXC-02: Downtime API Cyber Kampus — Fallback Mechanism</p>
        <p style="color: #78350f; font-size: 0.9rem;">Jika API Cyber Kampus mengalami downtime atau response timeout > 10 detik saat proses login atau query data anggota, sistem mengaktifkan mekanisme fallback bertingkat: (1) <strong>Level 1 — Cache Lookup:</strong> Sistem menggunakan data profil dosen/mahasiswa yang di-cache dari sinkronisasi terakhir (max 24 jam). (2) <strong>Level 2 — Manual Verification:</strong> Jika cache expired, dosen dapat login menggunakan Google OAuth (Gmail institusi) dan melakukan input NIDN/NIM anggota secara manual — data akan divalidasi secara asinkron saat API Cyber kembali online. (3) <strong>Level 3 — Degraded Mode:</strong> Jika kedua fallback gagal, portal menampilkan banner "Layanan Terbatas" dan menonaktifkan fitur penambahan anggota baru hingga API Cyber pulih. Seluruh kejadian downtime direkam di system health log.</p>
      </div>

      <div style="background: #f0fdf4; border: 1px solid #bbf7d0; border-radius: 12px; padding: 24px; margin-bottom: 16px;">
        <p style="color: #166534; font-weight: 700; margin-bottom: 8px;">EXC-03: Concurrent Upload Throttling & Queue Management</p>
        <p style="color: #14532d; font-size: 0.9rem;">Selama periode puncak submission (terutama H-3 sebelum penutupan periode), ratusan dosen dapat secara serentak mengunggah berkas proposal berukuran besar. Untuk mencegah overload server: (1) <strong>Upload Throttling:</strong> Sistem menerapkan rate limit max <strong>50 concurrent uploads</strong> secara global, dengan queue FIFO untuk request yang melebihi limit. (2) <strong>Chunked Upload:</strong> File di atas 5MB dipecah menjadi chunk 1MB untuk menghindari timeout pada koneksi lambat. (3) <strong>Cloud Storage Offload:</strong> File langsung di-stream ke cloud object storage (S3-compatible) tanpa buffering di application server, mengurangi beban memory. (4) <strong>Progress Indicator:</strong> UI menampilkan progress bar real-time dan estimasi waktu upload. (5) <strong>Auto-Retry:</strong> Jika upload terputus, sistem menyimpan state chunk terakhir dan memungkinkan resume upload tanpa mengulang dari awal.</p>
      </div>

      <div style="background: #faf5ff; border: 1px solid #e9d5ff; border-radius: 12px; padding: 24px;">
        <p style="color: #6b21a8; font-weight: 700; margin-bottom: 8px;">EXC-04: Expired Period Submission Attempt</p>
        <p style="color: #581c87; font-size: 0.9rem;">Jika Dosen Ketua telah memulai pengisian formulir (status DRAFT) namun periode pendaftaran ditutup sebelum proses submit selesai: (1) <strong>Grace Period:</strong> Sistem memberikan toleransi <strong>2 jam</strong> setelah tanggal_tutup bagi dosen yang sudah memiliki DRAFT aktif untuk menyelesaikan submit. (2) <strong>Data Preservation:</strong> Draft yang belum di-submit setelah grace period akan disimpan dengan status "EXPIRED_DRAFT" — data tidak dihapus, namun tidak dapat di-submit pada periode tersebut. (3) <strong>Carry-Over Option:</strong> Pada periode berikutnya, dosen dapat memilih opsi "Lanjutkan Draft Sebelumnya" untuk menggunakan data draft expired sebagai template pengisian baru. (4) <strong>Notification:</strong> Sistem mengirim notifikasi H-1 dan H-2 jam sebelum penutupan kepada dosen yang memiliki DRAFT belum di-submit.</p>
      </div>
    </div>

    <!-- 5.5 System Architecture -->
    <div class="section-card" id="sys-architecture">
      <h3><span class="section-card-num">5.5.</span> System Architecture Overview</h3>
      <p class="section-card-desc">Gambaran arsitektur teknis sistem SIMPPM LPMB yang menunjukkan layer-layer teknologi dari antarmuka pengguna hingga penyimpanan data, termasuk integrasi dengan sistem eksternal (Cyber Kampus, PDDIKTI) dan database master WUADC.</p>
      <div class="diagram-container">
        <h4 style="margin-bottom: 15px; color: var(--text-dark); font-weight: 700;">Architecture Diagram — Tech Stack Layers</h4>
        <div class="mermaid">
          graph TB
            subgraph "Frontend Layer"
              Browser["Web Browser<br/>(Chrome, Firefox, Safari)"]
              SPA["SPA Frontend<br/>(React / Vue.js)"]
            end

            subgraph "API Gateway & Auth"
              Gateway["API Gateway<br/>(Nginx / Kong)"]
              Auth["Auth Service<br/>(JWT + SSO Handler)"]
            end

            subgraph "Backend Services"
              ProposalSvc["Proposal Service<br/>(CRUD, Workflow Engine)"]
              ReviewSvc["Review Service<br/>(Multi-tier Approval)"]
              UploadSvc["Upload Service<br/>(Chunked Upload Handler)"]
              NotifSvc["Notification Service<br/>(Email + In-App)"]
              MonevSvc["Monev Service<br/>(Logbook + Evaluation)"]
              SyncSvc["Sync Service<br/>(WUADC Transactional Sync)"]
              DashSvc["Dashboard Service<br/>(Analytics + Reporting)"]
            end

            subgraph "Data Layer"
              PrimaryDB["Primary Database<br/>(PostgreSQL / MySQL)"]
              ReadReplica["Read Replica<br/>(Query Optimization)"]
              FileStore["Cloud Object Storage<br/>(S3-Compatible)"]
              Cache["Redis Cache<br/>(Session + API Cache)"]
              DLQ["Dead Letter Queue<br/>(Failed Sync Retry)"]
            end

            subgraph "External APIs"
              CyberAPI["Cyber Kampus API<br/>(SSO + Data Dosen/Mhs)"]
              PDDIKTI["PDDIKTI API<br/>(Validasi NIDN)"]
              WUADCDb["WUADC Database<br/>(Master Archive)"]
              EmailSMTP["SMTP Server<br/>(Email Delivery)"]
            end

            Browser --> SPA
            SPA --> Gateway
            Gateway --> Auth
            Auth --> CyberAPI
            Auth --> ProposalSvc
            Gateway --> ProposalSvc
            Gateway --> ReviewSvc
            Gateway --> UploadSvc
            Gateway --> MonevSvc
            Gateway --> DashSvc
            ProposalSvc --> PrimaryDB
            ReviewSvc --> PrimaryDB
            UploadSvc --> FileStore
            MonevSvc --> PrimaryDB
            NotifSvc --> EmailSMTP
            SyncSvc --> WUADCDb
            SyncSvc --> DLQ
            DashSvc --> ReadReplica
            ProposalSvc --> Cache
            Auth --> Cache
            ProposalSvc --> PDDIKTI
        </div>
      </div>
      <div class="bento-grid" style="margin-top: 20px;">
        <div class="bento-cell">
          <h4>Frontend Layer</h4>
          <p>Single Page Application (SPA) berbasis React/Vue.js dengan responsive design. Komunikasi ke backend melalui RESTful API via API Gateway. Mendukung Progressive Web App (PWA) untuk akses offline logbook.</p>
        </div>
        <div class="bento-cell">
          <h4>API Gateway</h4>
          <p>Nginx atau Kong sebagai reverse proxy dan load balancer. Menangani rate limiting, request throttling, SSL termination, dan routing ke microservices backend berdasarkan URL path.</p>
        </div>
        <div class="bento-cell">
          <h4>Backend Microservices</h4>
          <p>7 service terpisah yang masing-masing bertanggung jawab atas domain spesifik. Workflow Engine pada Proposal Service mengelola state machine transisi status proposal secara event-driven.</p>
        </div>
        <div class="bento-cell">
          <h4>Data Layer</h4>
          <p>PostgreSQL/MySQL sebagai primary database dengan read replica untuk query analytics. Redis untuk session caching dan API response caching. Cloud object storage untuk file dokumen.</p>
        </div>
        <div class="bento-cell">
          <h4>External Integration</h4>
          <p>Integrasi real-time dengan API Cyber Kampus (autentikasi + data master) dan PDDIKTI (validasi NIDN). Sinkronisasi transaksional ke WUADC Database dengan dead letter queue untuk fault tolerance.</p>
        </div>
        <div class="bento-cell">
          <h4>Reliability & Monitoring</h4>
          <p>Health check endpoint pada setiap service. Centralized logging (ELK Stack). Alerting otomatis untuk downtime, error rate > 1%, dan SLA breach. Backup database otomatis setiap 6 jam.</p>
        </div>
      </div>
    </div>
  </div>

  <!-- PHASE 6: TESTING & RISK -->
  <div class="phase-block">
    <div class="phase-badge pb-purple">Fase 6: Pengujian & Manajemen Risiko Proyek</div>
    
    <!-- 6.1 UAT -->
    <div class="section-card" id="uat">
      <h3><span class="section-card-num">6.1.</span> UAT Test Plan</h3>
      <p class="section-card-desc">Rencana pengujian penerimaan pengguna (User Acceptance Testing) yang mencakup 8 skenario uji kritis, mulai dari validasi berkas, alur persetujuan end-to-end, hingga sinkronisasi WUADC dan eskalasi SLA. Setiap test case dipetakan ke Functional Requirement (FR) dan dilengkapi expected result spesifik.</p>
      <div class="table-wrapper">
        <table>
          <thead>
            <tr>
              <th>ID Uji</th>
              <th>Target Fitur Uji</th>
              <th>FR Ref</th>
              <th>Langkah Percobaan</th>
              <th>Hasil yang Diharapkan</th>
              <th>Status</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>UAT-L01</td>
              <td>Mandatory Files Check</td>
              <td>FR-04</td>
              <td>Lakukan klik tombol submit saat dokumen RAB atau Pakta Integritas belum diunggah pada skema Reguler.</td>
              <td>Sistem memblokir pengiriman berkas, menampilkan tooltip peringatan spesifik per dokumen yang kurang, dan tombol submit tetap non-aktif.</td>
              <td><span class="badge badge-success">Passed</span></td>
            </tr>
            <tr>
              <td>UAT-L02</td>
              <td>End-to-End Proposal Submission</td>
              <td>FR-03, FR-04</td>
              <td>Login SSO → Pilih skema Reguler → Isi formulir lengkap → Upload 5 dokumen valid (PDF, &lt;10MB) → Submit.</td>
              <td>Proposal tersimpan dengan status SUBMITTED. Notifikasi terkirim ke Akademik Fakultas. Anggota tim menerima notifikasi partisipasi.</td>
              <td><span class="badge badge-success">Passed</span></td>
            </tr>
            <tr>
              <td>UAT-L03</td>
              <td>Multi-Tier Approval Workflow</td>
              <td>FR-06, FR-07</td>
              <td>Proposal SUBMITTED → Akademik Approve → Dekan Approve → Dosen TTD → Admin LPMB Verify → Akademik Final Approve → Dekan Final Approve.</td>
              <td>Status berubah secara berurutan: SUBMITTED → APPROVED_AKADEMIK → APPROVED_DEKAN → TTD_ADMIN → VERIFIED → REVIEW_FINAL_AKAD → APPROVED. 5 entri REVIEW_LOG tercatat.</td>
              <td><span class="badge badge-success">Passed</span></td>
            </tr>
            <tr>
              <td>UAT-L04</td>
              <td>Member Invitation & Validation</td>
              <td>FR-05</td>
              <td>Tambahkan anggota dosen (NIDN valid aktif) dan mahasiswa (NIM valid aktif) ke proposal. Lalu coba tambahkan NIDN yang sudah terdaftar di proposal lain.</td>
              <td>Anggota pertama berhasil ditambahkan (status PENDING). Anggota kedua ditolak dengan error DUPLICATE_MEMBER. Notifikasi undangan terkirim ke anggota yang berhasil.</td>
              <td><span class="badge badge-success">Passed</span></td>
            </tr>
            <tr>
              <td>UAT-L05</td>
              <td>Logbook Submission & Monev</td>
              <td>FR-08, FR-09</td>
              <td>Pada proposal IN_PROGRESS, submit 3 entri logbook dengan file lampiran. Admin LPMB buka dashboard monev dan evaluasi.</td>
              <td>3 entri logbook tercatat dengan progress percentage bertambah. Dashboard monev menampilkan detail per entri. Admin dapat memberikan catatan evaluasi dan request perbaikan.</td>
              <td><span class="badge badge-success">Passed</span></td>
            </tr>
            <tr>
              <td>UAT-L06</td>
              <td>WUADC Sync Integration</td>
              <td>FR-10</td>
              <td>Selesaikan seluruh proses hingga status COMPLETED. Admin LPMB klik "Finalisasi dan Arsipkan".</td>
              <td>Sistem melakukan INSERT transaksional ke WUADC. Status berubah menjadi ARCHIVED. Email konfirmasi terkirim ke Dosen Ketua dan Admin LPMB. Record WUADC_ARCHIVE terbuat dengan status_arsip = SYNCED.</td>
              <td><span class="badge badge-success">Passed</span></td>
            </tr>
            <tr>
              <td>UAT-L07</td>
              <td>SLA Escalation Notification</td>
              <td>FR-11</td>
              <td>Submit proposal dan biarkan tanpa review selama 4 hari kerja (simulasi dengan time manipulation).</td>
              <td>Notifikasi eskalasi terkirim ke reviewer pada hari ke-3. Eskalasi ke pimpinan fakultas pada hari ke-5. Dashboard menampilkan badge "SLA Breach" pada proposal tersebut.</td>
              <td><span class="badge badge-success">Passed</span></td>
            </tr>
            <tr>
              <td>UAT-L08</td>
              <td>SSO Login & Account Validation</td>
              <td>FR-01</td>
              <td>Login menggunakan SSO Cyber Kampus dengan NIDN valid dan aktif. Lalu coba login dengan NIDN non-aktif (cuti).</td>
              <td>Login pertama berhasil, dashboard terbuka dengan data profil lengkap (nama, jabatan, fakultas, prodi). Login kedua gagal dengan pesan "Akun tidak aktif — hubungi admin kepegawaian".</td>
              <td><span class="badge badge-success">Passed</span></td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    
    <!-- 6.2 RTM -->
    <div class="section-card" id="rtm">
      <h3><span class="section-card-num">6.2.</span> Requirements Traceability Matrix (RTM)</h3>
      <p class="section-card-desc">Pemetaan komprehensif dari Business Requirements (BR) → Functional Requirements (FR) → UAT Test Cases, memastikan setiap kebutuhan bisnis tercover oleh spesifikasi fungsional dan tervalidasi oleh skenario pengujian.</p>
      <div class="table-wrapper">
        <table>
          <thead>
            <tr>
              <th>ID Kebutuhan Bisnis</th>
              <th>ID Fungsional (FR)</th>
              <th>Skenario Kasus Uji</th>
              <th>Modul Evaluasi</th>
              <th>Status Coverage</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>BR-01 (Digitalisasi Berkas)</td>
              <td>FR-03, FR-04</td>
              <td>UAT-L01 (Mandatory Files), UAT-L02 (E2E Submission)</td>
              <td>Submission & Validation Module</td>
              <td><span class="badge badge-success">Covered</span></td>
            </tr>
            <tr>
              <td>BR-02 (WUADC Archiving)</td>
              <td>FR-10</td>
              <td>UAT-L06 (WUADC Sync Integration)</td>
              <td>Monev & Archiving Module</td>
              <td><span class="badge badge-success">Covered</span></td>
            </tr>
            <tr>
              <td>BR-03 (SSO Integration)</td>
              <td>FR-01</td>
              <td>UAT-L08 (SSO Login & Validation)</td>
              <td>Authentication & Identity Module</td>
              <td><span class="badge badge-success">Covered</span></td>
            </tr>
            <tr>
              <td>BR-04 (Multi-Tier Review)</td>
              <td>FR-06, FR-07, FR-11</td>
              <td>UAT-L03 (Approval Workflow), UAT-L07 (SLA Escalation)</td>
              <td>Review Workflow & Audit Module</td>
              <td><span class="badge badge-success">Covered</span></td>
            </tr>
            <tr>
              <td>BR-05 (Monev Lifecycle)</td>
              <td>FR-08, FR-09</td>
              <td>UAT-L05 (Logbook & Monev)</td>
              <td>Monitoring & Evaluation Module</td>
              <td><span class="badge badge-success">Covered</span></td>
            </tr>
            <tr>
              <td>BR-06 (Dashboard Analytics)</td>
              <td>FR-12</td>
              <td>UAT-L03 (status tracking), UAT-L07 (SLA metrics)</td>
              <td>Dashboard & Reporting Module</td>
              <td><span class="badge badge-success">Covered</span></td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    
    <!-- 6.3 Risk Register -->
    <div class="section-card" id="risk-reg">
      <h3><span class="section-card-num">6.3.</span> Risk Register</h3>
      <p class="section-card-desc">Identifikasi potensi hambatan kelancaran rilis dan operasional sistem beserta analisis dampak, probabilitas, dan rencana tindakan mitigasi yang terukur untuk setiap risiko.</p>
      <div class="table-wrapper">
        <table>
          <thead>
            <tr>
              <th>ID</th>
              <th>Deskripsi Risiko</th>
              <th>Probabilitas</th>
              <th>Level Dampak</th>
              <th>Dampak Operasional</th>
              <th>Rencana Tindakan Mitigasi</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>RSK-01</td>
              <td>Downtime API Cyber Kampus saat validasi dosen/mahasiswa</td>
              <td><span class="badge badge-warning">Medium</span></td>
              <td><span class="badge badge-warning">Sedang</span></td>
              <td>Dosen ketua tidak dapat login atau melakukan query data anggota secara real-time, menghambat proses pengajuan.</td>
              <td>Implementasi 3-tier fallback: (1) cache lookup 24 jam, (2) Google OAuth login + manual NIDN input, (3) degraded mode dengan banner notifikasi. Monitoring API health setiap 60 detik.</td>
            </tr>
            <tr>
              <td>RSK-02</td>
              <td>Pemuatan berkas PDF/dokumen berukuran sangat besar secara serentak</td>
              <td><span class="badge badge-danger">High</span></td>
              <td><span class="badge badge-danger">Tinggi</span></td>
              <td>Server melambat atau crash akibat ratusan dosen secara serentak mengunggah lampiran proposal/RAB mendekati deadline periode.</td>
              <td>Throttling limit 50 concurrent uploads, chunked upload untuk file >5MB, cloud storage streaming langsung (bypass app server), progress indicator real-time, auto-retry pada chunk failure.</td>
            </tr>
            <tr>
              <td>RSK-03</td>
              <td>Kegagalan sinkronisasi data ke database master WUADC</td>
              <td><span class="badge badge-warning">Medium</span></td>
              <td><span class="badge badge-danger">Tinggi</span></td>
              <td>Data arsip pengmas tidak tersimpan di WUADC, menyebabkan inkonsistensi laporan eksternal ke DIKTI dan audit trail terputus.</td>
              <td>Mekanisme retry otomatis (max 3x, exponential backoff). Dead letter queue untuk transaksi gagal. Alert ke Admin LPMB untuk manual intervention. Reconciliation job harian untuk deteksi data gap.</td>
            </tr>
            <tr>
              <td>RSK-04</td>
              <td>Concurrent submission overload pada H-1 penutupan periode</td>
              <td><span class="badge badge-danger">High</span></td>
              <td><span class="badge badge-warning">Sedang</span></td>
              <td>Spike traffic 5-10x normal load menyebabkan response time degradasi dan potensi request timeout pada proses submit.</td>
              <td>Auto-scaling infrastructure pada cloud provider. Read replica untuk query non-mutating. Queue-based processing untuk heavy operations. Grace period 2 jam post-deadline untuk draft yang sudah dimulai.</td>
            </tr>
            <tr>
              <td>RSK-05</td>
              <td>SSO outage pada provider (Cyber Kampus atau Google OAuth)</td>
              <td><span class="badge badge-primary">Low</span></td>
              <td><span class="badge badge-danger">Tinggi</span></td>
              <td>Seluruh pengguna tidak dapat login ke portal, menghentikan seluruh operasional sistem selama durasi outage.</td>
              <td>Dual SSO provider (Cyber + Google OAuth) sebagai mutual fallback. Session token validity 4 jam (pengguna yang sudah login tidak terdampak). Emergency local auth untuk Admin LPMB. Status page publik untuk komunikasi outage.</td>
            </tr>
            <tr>
              <td>RSK-06</td>
              <td>Reviewer bottleneck — Akademik/Dekanat lambat merespon</td>
              <td><span class="badge badge-danger">High</span></td>
              <td><span class="badge badge-warning">Sedang</span></td>
              <td>Antrean proposal menumpuk tanpa keputusan review, melebihi SLA 3 hari kerja dan menghambat pelaksanaan kegiatan pengmas.</td>
              <td>Notifikasi eskalasi bertingkat (hari ke-3, ke-5, ke-7). Dashboard real-time pending queue per reviewer. Laporan mingguan SLA compliance ke pimpinan fakultas. Opsi delegasi review ke staf akademik lain.</td>
            </tr>
            <tr>
              <td>RSK-07</td>
              <td>Data loss atau korupsi selama migrasi dari sistem lama</td>
              <td><span class="badge badge-warning">Medium</span></td>
              <td><span class="badge badge-danger">Tinggi</span></td>
              <td>Data historis proposal, laporan, dan arsip dari sistem lama hilang atau rusak selama proses migrasi ke portal baru.</td>
              <td>Migration script dengan dry-run validation. Checksum verification per record. Parallel run (sistem lama + baru) selama 1 bulan. Full backup sebelum migrasi. Rollback plan dengan point-in-time recovery.</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- 6.4 Performance Benchmark -->
    <div class="section-card" id="perf-benchmark">
      <h3><span class="section-card-num">6.4.</span> Performance Benchmark Target</h3>
      <p class="section-card-desc">Target metrik performa yang harus dipenuhi oleh sistem sebelum rilis produksi, divalidasi melalui load testing dan stress testing pada environment staging yang menyerupai produksi. Pengujian menggunakan tool Apache JMeter dan k6 dengan simulasi peak load scenarios.</p>
      <div class="table-wrapper">
        <table>
          <thead>
            <tr>
              <th>Metrik Performa</th>
              <th>Target Value</th>
              <th>Kondisi Pengujian</th>
              <th>Threshold Peringatan</th>
              <th>Threshold Kritis</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Page Load Time (First Contentful Paint)</strong></td>
              <td>&lt; 1.5 detik</td>
              <td>Koneksi 4G (10 Mbps), halaman dashboard utama</td>
              <td>&gt; 2.0 detik</td>
              <td>&gt; 3.0 detik</td>
            </tr>
            <tr>
              <td><strong>API Response Time (READ operations)</strong></td>
              <td>&lt; 500ms (p95)</td>
              <td>GET /proposals, GET /proposal/{id} dengan 200 concurrent users</td>
              <td>&gt; 1.0 detik (p95)</td>
              <td>&gt; 2.0 detik (p95)</td>
            </tr>
            <tr>
              <td><strong>API Response Time (WRITE operations)</strong></td>
              <td>&lt; 2.0 detik (p95)</td>
              <td>POST /proposal (create with files), PUT /review (status change)</td>
              <td>&gt; 3.0 detik (p95)</td>
              <td>&gt; 5.0 detik (p95)</td>
            </tr>
            <tr>
              <td><strong>Concurrent Users Supported</strong></td>
              <td>200 users simultaneous</td>
              <td>Mixed workload: 60% read, 30% write, 10% upload</td>
              <td>Error rate &gt; 0.5%</td>
              <td>Error rate &gt; 2.0%</td>
            </tr>
            <tr>
              <td><strong>File Upload Throughput</strong></td>
              <td>50 concurrent uploads</td>
              <td>File 10MB PDF, chunked upload 1MB/chunk</td>
              <td>Queue wait &gt; 30 detik</td>
              <td>Queue wait &gt; 120 detik</td>
            </tr>
            <tr>
              <td><strong>WUADC Sync Latency</strong></td>
              <td>&lt; 5 detik per proposal</td>
              <td>Full sync: metadata + 5 logbook entries + 3 luaran documents</td>
              <td>&gt; 10 detik</td>
              <td>&gt; 30 detik (trigger DLQ)</td>
            </tr>
            <tr>
              <td><strong>Database Query Performance</strong></td>
              <td>&lt; 100ms (p95)</td>
              <td>Complex JOIN queries pada tabel PROPOSAL + MEMBER + REVIEW_LOG</td>
              <td>&gt; 200ms (p95)</td>
              <td>&gt; 500ms (p95)</td>
            </tr>
            <tr>
              <td><strong>System Availability (Uptime)</strong></td>
              <td>99.9% (SLA)</td>
              <td>Measured monthly, excluding planned maintenance windows</td>
              <td>&lt; 99.5%</td>
              <td>&lt; 99.0%</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>

  <!-- PHASE 7: BUSINESS IMPACT -->
  <div class="phase-block">
    <div class="phase-badge pb-emerald">Fase 7: Dampak Bisnis (ROI)</div>
    
    <!-- 7.1 Business Impact -->
    <div class="section-card" id="biz-impact">
      <h3><span class="section-card-num">7.1.</span> Business Impact & ROI Metrics</h3>
      <p class="section-card-desc">Dampak riil transformasi digital terhadap efisiensi program pengmas LPMB, diukur dengan metrik kuantitatif yang membandingkan kinerja proses manual sebelumnya dengan kinerja portal digital yang telah diimplementasikan.</p>
      <div class="bento-grid">
        <div class="bento-cell">
          <h4>SLA Peninjauan Berkas</h4>
          <p style="font-size: 2.2rem; font-weight: 800; color: var(--accent-teal); line-height: 1;">-85%</p>
          <p style="font-weight: 600; margin-top: 10px;">Pangkas Birokrasi Manual</p>
          <p>Memangkas alur verifikasi berkas dari semula rata-rata 14 hari kerja (2 minggu) menjadi maksimal 3 hari kerja, berkat digitalisasi checklist, notifikasi otomatis, dan eskalasi SLA bertingkat.</p>
        </div>
        <div class="bento-cell">
          <h4>Integrasi Master Arsip</h4>
          <p style="font-size: 2.2rem; font-weight: 800; color: var(--accent-teal); line-height: 1;">100%</p>
          <p style="font-weight: 600; margin-top: 10px;">WUADC Archiving Sync</p>
          <p>Menjamin arsip pelaporan, logbook, dan berkas luaran pengmas tersimpan otomatis secara transaksional ke database master WUADC tanpa input ganda manual — dengan target sync failure rate 0%.</p>
        </div>
        <div class="bento-cell">
          <h4>Paperless Savings</h4>
          <p style="font-size: 2.2rem; font-weight: 800; color: var(--accent-teal); line-height: 1;">100%</p>
          <p style="font-weight: 600; margin-top: 10px;">Eliminasi Cetak Berkas</p>
          <p>Menghilangkan pencetakan fisik seluruh berkas proposal, RAB, CV, SP, dan Pakta secara total — menghemat estimasi 15.000+ lembar kertas per tahun untuk 200+ proposal.</p>
        </div>
        <div class="bento-cell">
          <h4>Error Reduction</h4>
          <p style="font-size: 2.2rem; font-weight: 800; color: var(--accent-teal); line-height: 1;">-95%</p>
          <p style="font-weight: 600; margin-top: 10px;">Kesalahan Pengisian Berkas</p>
          <p>Validasi otomatis real-time (tipe file, ukuran, kelengkapan, format) mengurangi tingkat penolakan berkas karena kesalahan teknis dari 35% menjadi kurang dari 2%.</p>
        </div>
        <div class="bento-cell">
          <h4>Reviewer Throughput</h4>
          <p style="font-size: 2.2rem; font-weight: 800; color: var(--accent-teal); line-height: 1;">+300%</p>
          <p style="font-weight: 600; margin-top: 10px;">Kapasitas Review Fakultas</p>
          <p>Digitalisasi checklist review dan notifikasi proaktif meningkatkan jumlah proposal yang dapat direview per hari oleh Akademik Fakultas dari rata-rata 5 menjadi 20 proposal.</p>
        </div>
        <div class="bento-cell">
          <h4>Compliance Audit</h4>
          <p style="font-size: 2.2rem; font-weight: 800; color: var(--accent-teal); line-height: 1;">100%</p>
          <p style="font-weight: 600; margin-top: 10px;">Audit Readiness</p>
          <p>Immutable audit trail (REVIEW_LOG) dengan retensi 5 tahun memastikan setiap keputusan review dapat dilacak dan diverifikasi kapan saja untuk keperluan audit internal dan akreditasi.</p>
        </div>
      </div>
    </div>

    <!-- 7.2 Before vs After -->
    <div class="section-card" id="before-after">
      <h3><span class="section-card-num">7.2.</span> Before vs After Comparison</h3>
      <p class="section-card-desc">Perbandingan langsung antara proses manual (sistem lama) dan proses digital (portal SIMPPM) di seluruh dimensi operasional, menunjukkan transformasi signifikan yang dicapai melalui implementasi sistem.</p>
      <div class="table-wrapper">
        <table>
          <thead>
            <tr>
              <th>Dimensi Operasional</th>
              <th>Before (Manual / Sistem Lama)</th>
              <th>After (Portal SIMPPM Digital)</th>
              <th>Improvement</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>Waktu Submission Proposal</strong></td>
              <td>3-5 hari (cetak dokumen, antar fisik ke bagian akademik, revisi manual berulang)</td>
              <td>30 menit - 2 jam (isi form online, upload file digital, validasi real-time)</td>
              <td><span class="badge badge-success">-95%</span></td>
            </tr>
            <tr>
              <td><strong>Siklus Review Lengkap</strong></td>
              <td>14-21 hari kerja (berkas fisik berpindah antar meja, sering hilang/tercecer di tumpukan)</td>
              <td>3-5 hari kerja (antrean digital, notifikasi otomatis, eskalasi SLA otomatis)</td>
              <td><span class="badge badge-success">-75%</span></td>
            </tr>
            <tr>
              <td><strong>Penyimpanan Dokumen</strong></td>
              <td>Arsip fisik di lemari/gudang per fakultas, rentan hilang/rusak, sulit dicari</td>
              <td>Cloud object storage terenkripsi, searchable, backup otomatis, akses instant</td>
              <td><span class="badge badge-success">Digital</span></td>
            </tr>
            <tr>
              <td><strong>Traceability / Lacak Jejak</strong></td>
              <td>Tidak ada. Keputusan review tidak tercatat. Sulit mengetahui siapa melakukan apa dan kapan</td>
              <td>Immutable audit trail (REVIEW_LOG) untuk setiap aksi, lengkap dengan timestamp dan identitas reviewer</td>
              <td><span class="badge badge-success">100%</span></td>
            </tr>
            <tr>
              <td><strong>Kecepatan Pelaporan</strong></td>
              <td>Kompilasi manual per fakultas (2-3 minggu), rawan inkonsistensi data, sulit agregasi</td>
              <td>Dashboard real-time dengan filter per status/skema/fakultas, export otomatis, data selalu terkini</td>
              <td><span class="badge badge-success">Real-time</span></td>
            </tr>
            <tr>
              <td><strong>Tingkat Error Berkas</strong></td>
              <td>35% proposal dikembalikan karena berkas tidak lengkap, format salah, atau dokumen tertukar</td>
              <td>&lt;2% penolakan teknis berkat validasi otomatis (tipe file, ukuran, kelengkapan) sebelum submit</td>
              <td><span class="badge badge-success">-95%</span></td>
            </tr>
            <tr>
              <td><strong>Arsip ke WUADC</strong></td>
              <td>Input manual oleh staf LPMB (1 proposal = 30 menit input), rentan typo, sering tertunda berminggu-minggu</td>
              <td>Sinkronisasi transaksional otomatis (&lt;5 detik per proposal), zero manual input, retry mechanism</td>
              <td><span class="badge badge-success">Auto</span></td>
            </tr>
            <tr>
              <td><strong>Notifikasi & Komunikasi</strong></td>
              <td>WhatsApp/telepon manual, tidak tercatat, sering missed atau terlambat</td>
              <td>Email + in-app notification otomatis pada setiap transisi status, eskalasi SLA otomatis</td>
              <td><span class="badge badge-success">Auto</span></td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- 7.3 Lessons Learned & Roadmap -->
    <div class="section-card" id="lessons-roadmap">
      <h3><span class="section-card-num">7.3.</span> Lessons Learned & Future Roadmap</h3>
      <p class="section-card-desc">Rangkuman pembelajaran kunci selama proses pengembangan dan implementasi portal SIMPPM, serta rencana pengembangan fitur di fase-fase berikutnya untuk meningkatkan cakupan dan kualitas layanan sistem.</p>
      
      <h4 style="margin-bottom: 16px; font-size: 1.1rem; color: var(--text-dark);">📝 Key Lessons Learned</h4>
      <div class="sticky-grid">
        <div class="sticky-note sticky-yellow">
          <h4>Stakeholder Alignment is Critical</h4>
          <p>Proses review berjenjang melibatkan 5+ aktor dengan kepentingan berbeda. Workshop alignment di awal proyek dengan seluruh stakeholder (Akademik, Dekanat, LPMB) sangat krusial untuk menyepakati flow dan SLA sebelum development dimulai.</p>
        </div>
        <div class="sticky-note sticky-blue">
          <h4>API Integration Resilience</h4>
          <p>Ketergantungan pada API Cyber Kampus yang tidak selalu stabil mengajarkan pentingnya desain fallback mechanism dari awal (cache, degraded mode, manual override) — bukan sebagai afterthought.</p>
        </div>
        <div class="sticky-note sticky-green">
          <h4>User Training is Underestimated</h4>
          <p>Banyak dosen senior yang tidak terbiasa dengan workflow digital. Investasi di video tutorial, tooltips kontekstual, dan sesi pelatihan per fakultas terbukti krusial untuk meningkatkan adoption rate dari 60% menjadi 95%.</p>
        </div>
        <div class="sticky-note sticky-rose">
          <h4>Deadline-Driven Peak Load</h4>
          <p>80% submission terjadi di 3 hari terakhir periode. Capacity planning dan load testing harus mensimulasikan peak scenario ini, bukan average load. Auto-scaling dan grace period terbukti menjadi fitur penyelamat.</p>
        </div>
      </div>

      <h4 style="margin: 30px 0 16px; font-size: 1.1rem; color: var(--text-dark);">🚀 Future Roadmap</h4>
      <div class="sticky-grid">
        <div class="sticky-note sticky-purple">
          <h4>📱 Mobile App (Phase 2)</h4>
          <p>Pengembangan aplikasi mobile (React Native / Flutter) untuk memudahkan Dosen Ketua mengisi logbook di lapangan dengan fitur kamera langsung untuk dokumentasi kegiatan, GPS tagging lokasi, dan offline sync capability.</p>
        </div>
        <div class="sticky-note sticky-blue">
          <h4>🤖 AI-Powered Plagiarism Check</h4>
          <p>Integrasi tool pengecekan plagiarisme otomatis pada proposal yang di-submit, menggunakan engine Turnitin API atau solusi open-source iThenticate, untuk memastikan orisinalitas konten sebelum review substansi dimulai.</p>
        </div>
        <div class="sticky-note sticky-green">
          <h4>🔗 Integrasi SINTA</h4>
          <p>Sinkronisasi profil penelitian dosen dengan database SINTA (Science and Technology Index) untuk auto-populate CV dan track record pengabdian sebelumnya, serta validasi H-Index dan jumlah publikasi sebagai kriteria kelayakan pengusul.</p>
        </div>
        <div class="sticky-note sticky-yellow">
          <h4>💰 Automated RAB Validation</h4>
          <p>Implementasi rule engine untuk validasi otomatis Rencana Anggaran Biaya (RAB) terhadap standar biaya umum (SBU) universitas — mendeteksi item yang melebihi pagu, komponen yang tidak eligible, dan proporsi anggaran yang tidak seimbang.</p>
        </div>
      </div>
    </div>
  </div>
    """
    
    return build_html(title, project_name, role, meta_units, meta_platform, meta_author, sidebar_nav_html, main_content_html, accent_class, color_theme_style)

if __name__ == '__main__':
    portfolio_dir = '/Users/fitrianovitasari/.gemini/antigravity/scratch/portfolio'
    
    # 1. GAV
    gav_html = generate_gav()
    with open(os.path.join(portfolio_dir, 'gav-smartprocure.html'), 'w', encoding='utf-8') as f:
        f.write(gav_html)
    with open(os.path.join(portfolio_dir, 'gav-canvas.html'), 'w', encoding='utf-8') as f:
        f.write(gav_html)
    print("[✓] Generated GAV SmartProcure HTML pages.")
    
    # 2. SRS
    srs_html = generate_srs()
    with open(os.path.join(portfolio_dir, 'sa-wellbe.html'), 'w', encoding='utf-8') as f:
        f.write(srs_html)
    print("[✓] Generated SRS Well-Be Care App HTML page.")
    
    # 3. PSDP
    psdp_html = generate_psdp()
    with open(os.path.join(portfolio_dir, 'psdp-ketan.html'), 'w', encoding='utf-8') as f:
        f.write(psdp_html)
    print("[✓] Generated PSDP Ketan Bersaudara ERP HTML page.")

    # 4. LPPM SIMPPM
    lppm_html = generate_lppm()
    with open(os.path.join(portfolio_dir, 'lppm-portal.html'), 'w', encoding='utf-8') as f:
        f.write(lppm_html)
    print("[✓] Generated LPPM SIMPPM Portal HTML page.")

