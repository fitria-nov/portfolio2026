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
    project_name = "SIMPPM LPPM Portal"
    title = "SIMPPM Portal: Research & Community Service Proposal Management System"
    role = "Senior Business & System Analyst"
    meta_units = "LPPM (Lembaga Penelitian dan Pengabdian kepada Masyarakat)"
    meta_platform = "LPPM Proposal Workflow Portal, REST API Integration & Reviewer Matrix"
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
    <a href="#org-structure" class="nav-item"><span class="nav-num">1.2</span> Struktur Organisasi</a>
    <a href="#current-system" class="nav-item"><span class="nav-num">1.3</span> Sistem Saat Ini</a>
    
    <div class="nav-group-title">Fase 2: Proses Bisnis</div>
    <a href="#bpmn-swimlane" class="nav-item"><span class="nav-num">2.1</span> BPMN Swimlane Alur</a>
    <a href="#workflow-breakdown" class="nav-item"><span class="nav-num">2.2</span> Breakdown Alur Kerja</a>
    
    <div class="nav-group-title">Fase 3: Kebutuhan Sistem</div>
    <a href="#brd" class="nav-item"><span class="nav-num">3.1</span> BRD Overview</a>
    <a href="#func-req" class="nav-item"><span class="nav-num">3.2</span> Functional Specs</a>
    <a href="#nonfunc-req" class="nav-item"><span class="nav-num">3.3</span> Non-Functional Specs</a>
    <a href="#accept-crit" class="nav-item"><span class="nav-num">3.4</span> Acceptance Criteria</a>
    
    <div class="nav-group-title">Fase 4: Pemodelan Sistem</div>
    <a href="#activity" class="nav-item"><span class="nav-num">4.1</span> Activity Diagram</a>
    <a href="#sequence" class="nav-item"><span class="nav-num">4.2</span> Sequence Diagram</a>
    <a href="#erd" class="nav-item"><span class="nav-num">4.3</span> ERD Database</a>
    
    <div class="nav-group-title">Fase 5: Teknis & Integrasi</div>
    <a href="#api-doc" class="nav-item"><span class="nav-num">5.1</span> API Documentation</a>
    <a href="#val-rules" class="nav-item"><span class="nav-num">5.2</span> Validation Rules</a>
    <a href="#role-matrix" class="nav-item"><span class="nav-num">5.3</span> Role & RACI Matrix</a>
    <a href="#exception" class="nav-item"><span class="nav-num">5.4</span> Exception Flow</a>
    
    <div class="nav-group-title">Fase 6: Pengujian & Risiko</div>
    <a href="#uat" class="nav-item"><span class="nav-num">6.1</span> UAT Test Plan</a>
    <a href="#rtm" class="nav-item"><span class="nav-num">6.2</span> RTM Document</a>
    <a href="#risk-reg" class="nav-item"><span class="nav-num">6.3</span> Risk Register</a>
    
    <div class="nav-group-title">Fase 7: Dampak Bisnis</div>
    <a href="#biz-impact" class="nav-item"><span class="nav-num">7.1</span> Business Impact</a>
    """
    
    main_content_html = """
  <!-- PHASE 1: CASE STUDY -->
  <div class="phase-block">
    <div class="phase-badge pb-purple">Fase 1: Case Study & Context</div>
    
    <!-- 1.1 Gambaran Umum -->
    <div class="section-card" id="general-overview">
      <h3><span class="section-card-num">1.1.</span> Gambaran Perusahaan</h3>
      <p class="section-card-desc">Latar belakang bisnis tata kelola administrasi penelitian perguruan tinggi.</p>
      <div class="bento-grid">
        <div class="bento-cell bento-wide">
          <h4>LPPM Research & Community Service Portal</h4>
          <p>Lembaga Penelitian dan Pengabdian kepada Masyarakat (LPPM) memegang tanggung jawab mutlak dalam pengelolaan siklus hibah internal perguruan tinggi. Portal SIMPPM dirancang untuk mendigitalisasi proses administrasi proposal pengajuan dana penelitian dosen dan mahasiswa secara transparan. Sistem baru ini mengintegrasikan seluruh pihak terkait secara online guna memastikan tata kelola administrasi riset yang efisien, cepat, dan bebas manipulasi.</p>
        </div>
        <div class="bento-cell">
          <h4>Target Efisiensi</h4>
          <p style="font-size: 2.2rem; font-weight: 800; color: var(--accent-amber); line-height: 1;">7 Hari</p>
          <p style="font-weight: 600; margin-top: 10px;">Siklus Verifikasi Proposal</p>
          <p>Memotong birokrasi manual dari rata-rata 35 hari kerja menjadi di bawah 1 minggu kerja secara online.</p>
        </div>
      </div>
    </div>
    
    <!-- 1.2 Struktur Organisasi -->
    <div class="section-card" id="org-structure">
      <h3><span class="section-card-num">1.2.</span> Struktur Organisasi & Peran Kerja</h3>
      <p class="section-card-desc">Definisi peran operasional utama yang terlibat dalam siklus proposal.</p>
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
              <td><strong>Admin LPPM</strong></td>
              <td>Mengaktifkan periode hibah, melakukan verifikasi administratif akhir, dan melakukan plotting reviewer.</td>
              <td>Dashboard monitoring penerimaan, menu plotting reviewer, dan audit log pendaftaran.</td>
            </tr>
            <tr>
              <td><strong>Dosen Ketua</strong></td>
              <td>Menyusun judul riset, membentuk usulan proposal, dan mengundang dosen/mahasiswa anggota.</td>
              <td>Formulir isian proposal, menu pencarian NIDN/NIM, dan pengunggahan dokumen PDF.</td>
            </tr>
            <tr>
              <td><strong>Anggota (Dosen & Mhs)</strong></td>
              <td>Melakukan konfirmasi kesediaan bergabung ke dalam proyek riset.</td>
              <td>Notifikasi digital dan satu-klik persetujuan (Approve/Reject) undangan di portal.</td>
            </tr>
            <tr>
              <td><strong>Akademik Fakultas</strong></td>
              <td>Melakukan pengecekan kelengkapan administrasi proposal tingkat fakultas.</td>
              <td>Daftar antrean proposal fakultas dan checkbox kelayakan format berkas.</td>
            </tr>
            <tr>
              <td><strong>Dekanat Fakultas</strong></td>
              <td>Memberikan rekomendasi strategis kelayakan riset di tingkat fakultas.</td>
              <td>Formulir rilis surat rekomendasi elektronik bertanda tangan digital.</td>
            </tr>
            <tr>
              <td><strong>Reviewer Ahli</strong></td>
              <td>Melakukan review substansi akademis proposal secara independen (blind review).</td>
              <td>Formulir input nilai kuantitatif dan feedback kualitatif riset secara acak.</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    
    <!-- 1.3 Sistem Lama & Tantangan -->
    <div class="section-card" id="current-system">
      <h3><span class="section-card-num">1.3.</span> Analisis Sistem Lama & Tantangan Operasional</h3>
      <p class="section-card-desc">Masalah utama alur kerja berbasis kertas fisik (hardcopy) sebelum sistem terintegrasi.</p>
      <div class="sticky-grid">
        <div class="sticky-note sticky-yellow">
          <h4>Berkas Rangkap 5</h4>
          <p>Dosen harus mencetak proposal sebanyak 5 rangkap untuk dikirimkan secara manual ke validator fakultas dan dekan.</p>
        </div>
        <div class="sticky-note sticky-blue">
          <h4>Klaim Anggota Sepihak</h4>
          <p>Pencantuman nama dosen/mahasiswa sebagai anggota riset sering dilakukan sepihak tanpa adanya konfirmasi tertulis.</p>
        </div>
        <div class="sticky-note sticky-green">
          <h4>Plotting Manual Excel</h4>
          <p>Penunjukan reviewer oleh admin LPPM dilakukan via Excel, rentan terhadap kolusi dan konflik kepentingan (conflict of interest).</p>
        </div>
        <div class="sticky-note sticky-rose">
          <h4>Verifikasi Terlambat</h4>
          <p>Kesalahan format atau kelengkapan berkas baru terdeteksi setelah proposal dinilai reviewer, membuang waktu dan biaya penilaian.</p>
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
      <p class="section-card-desc">Visualisasi alur proses bisnis lintas peran dari pembukaan periode hingga penandatanganan kontrak riset.</p>
      
      <div class="img-container" style="margin-bottom: 30px;">
        <img src="img/lppm-swimlane.png" alt="Orisinal Swimlane Diagram LPPM SIMPPM"/>
        <div class="img-caption">Gambar 2.1: Diagram Swimlane Proses Bisnis Orisinal SIMPPM LPPM (File Input User)</div>
      </div>

      <div class="diagram-container">
        <h4 style="margin-bottom: 15px; color: var(--text-dark); font-weight: 700;">Model Digital Alur Kerja (Mermaid Flowchart)</h4>
        <div class="mermaid">
          graph TD
            subgraph Admin LPPM
              Mulai([Mulai]) --> ActPeriod[Mengaktifkan Periode & Pengumuman]
              ActPeriod --> WaitSubmit{Menunggu Submit Proposal}
              FinalVerify[Verifikasi Administratif Akhir] --> FinalLolos{Lolos Seleksi?}
              FinalLolos -- Tidak --> StatusNoLolosAdmin[Status: Tidak Lolos Seleksi Administrasi] --> End([Selesai])
              FinalLolos -- Ya --> PlotReviewer[Plotting Reviewer]
              PlotReviewer --> Review1[Penilaian Reviewer 1]
              PlotReviewer --> Review2[Penilaian Reviewer 2]
              Review1 --> JoinReviews
              Review2 --> JoinReviews
              JoinReviews[Konsolidasi Nilai] --> GradeLolos{Lolos Passing Grade?}
              GradeLolos -- Tidak --> StatusNoLolosSubstansi[Status: Tidak Lolos Seleksi/Cadangan] --> End
              GradeLolos -- Ya --> StatusDiterima[Status: Proposal Diterima / Didanai] --> Contract[Kontrak & Pendanaan]
              Contract --> ProgressReport[Pelaksanaan & Pelaporan] --> End
            end

            subgraph Dosen Ketua
              ActPeriod -.-> CreateProp[Membuat Proposal Baru]
              CreateProp --> PilihAnggota{Pilih Anggota?}
              PilihAnggota -- Ya --> InviteMembers[Kirim Undangan Anggota]
              PilihAnggota -- No --> UploadDocs[Upload Proposal & Lampiran]
              InviteMembers -.-> ApproveDosen
              InviteMembers -.-> ApproveMhs
              ConfirmJoin[Gabungkan Persetujuan] --> UploadDocs
              UploadDocs --> SubmitProp[Submit Proposal]
              SubmitProp --> VerifyFakultas
            end

            subgraph Dosen Anggota
              ApproveDosen[Konfirmasi & Persetujuan Anggota Dosen] --> ConfirmJoin
            end

            subgraph Mahasiswa
              ApproveMhs[Konfirmasi & Persetujuan Anggota Mahasiswa] --> ConfirmJoin
            end

            subgraph Akademik Fakultas
              VerifyFakultas[Verifikasi Kelengkapan & Validasi] --> LolosVerify{Lolos Verifikasi?}
              LolosVerify -- Tidak --> StatusReject[Status: Ditolak / Perbaikan Draft] --> CreateProp
              LolosVerify -- Ya --> ForwardDean[Teruskan ke Dekanat]
            end

            subgraph Dekanat Fakultas
              ForwardDean --> DeanReview[Review & Rekomendasi Dekan]
              DeanReview --> RecDean{Rekomendasi?}
              RecDean -- Tidak --> StatusNoRec[Status: Tidak Rekomendasi] --> End
              RecDean -- Ya --> StatusRec[Status: Direkomendasikan] --> FinalVerify
            end
        </div>
      </div>
    </div>
    
    <!-- 2.2 Workflow Breakdown -->
    <div class="section-card" id="workflow-breakdown">
      <h3><span class="section-card-num">2.2.</span> Breakdown Detil Alur Kerja LPPM</h3>
      <p class="section-card-desc">Penjelasan langkah-langkah logis operasional lintas peran berdasarkan swimlane diagram.</p>
      <div class="workflow-timeline">
        <div class="timeline-item">
          <div class="timeline-dot">1</div>
          <div class="timeline-content">
            <h4>Inisiasi & Publikasi (Admin LPPM)</h4>
            <p>Admin LPPM membuka periode pendaftaran hibah tahunan di portal SIMPPM. Sistem mempublikasikan dokumen panduan format riset secara otomatis.</p>
          </div>
        </div>
        <div class="timeline-item">
          <div class="timeline-dot">2</div>
          <div class="timeline-content">
            <h4>Penyusunan Usulan & Undang Anggota (Dosen Ketua)</h4>
            <p>Dosen Ketua membuat berkas usulan di portal. Jika riset melibatkan anggota dosen atau mahasiswa, sistem otomatis mengirimkan undangan verifikasi digital.</p>
          </div>
        </div>
        <div class="timeline-item">
          <div class="timeline-dot">3</div>
          <div class="timeline-content">
            <h4>Konfirmasi Persetujuan Anggota (Dosen Anggota & Mahasiswa)</h4>
            <p>Anggota wajib melakukan konfirmasi bergabung. Tombol "Submit Proposal" pada layar Dosen Ketua hanya akan aktif (unlock) apabila status persetujuan semua anggota bernilai "Approved".</p>
          </div>
        </div>
        <div class="timeline-item">
          <div class="timeline-dot">4</div>
          <div class="timeline-content">
            <h4>Verifikasi Kelayakan Format (Akademik & Dekanat Fakultas)</h4>
            <p>Akademik Fakultas memeriksa format berkas administrasi. Berkas yang lolos diserahkan ke Dekanat untuk mendapatkan surat rekomendasi dekanat. Berkas yang tidak lengkap dikembalikan ke status Draf Dosen Ketua untuk direvisi.</p>
          </div>
        </div>
        <div class="timeline-item">
          <div class="timeline-dot">5</div>
          <div class="timeline-content">
            <h4>Plotting & Penilaian Independen (Reviewer LPPM)</h4>
            <p>Admin LPPM melakukan plotting reviewer secara acak menggunakan sub-sistem Subject Area Matching. Dua reviewer secara independen memberikan penilaian numerik di portal. Proposal dengan rata-rata nilai di atas passing grade ditetapkan sebagai "Diterima / Didanai".</p>
          </div>
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
      <p class="section-card-desc">Target bisnis utama dalam digitalisasi sistem hibah riset LPPM.</p>
      <div style="background: #fafafb; padding: 24px; border-radius: 12px; border: 1px solid var(--border-color);">
        <p><strong>BR-01:</strong> Sistem harus mampu memotong siklus waktu verifikasi dan penilaian dari rata-rata 35 hari kerja menjadi maksimum 7 hari kerja.</p>
        <p style="margin-top: 8px;"><strong>BR-02:</strong> Sistem wajib menjamin transparansi review dengan mekanisme double-blind scoring, mengeliminasi bias penunjukan reviewer sebesar 100%.</p>
      </div>
    </div>
    
    <!-- 3.2 Functional Requirements -->
    <div class="section-card" id="func-req">
      <h3><span class="section-card-num">3.2.</span> Functional Requirements</h3>
      <p class="section-card-desc">Spesifikasi fungsional portal pengajuan proposal SIMPPM.</p>
      <div class="table-wrapper">
        <table>
          <thead>
            <tr>
              <th>ID Kebutuhan</th>
              <th>Deskripsi Spesifikasi Kebutuhan</th>
              <th>Prasyarat Validasi (Trigger)</th>
              <th>Prioritas</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>FR-01</strong></td>
              <td>Sistem harus mengunci tombol submit proposal apabila status persetujuan salah satu anggota riset masih 'Pending' atau 'Rejected'.</td>
              <td>Database Status Table (Confirmations)</td>
              <td><span class="badge badge-danger">Critical</span></td>
            </tr>
            <tr>
              <td><strong>FR-02</strong></td>
              <td>Sistem wajib menolak upload proposal jika file bukan berformat PDF atau ukuran melebihi limit 10MB.</td>
              <td>MIME Type File Check API</td>
              <td><span class="badge badge-danger">Critical</span></td>
            </tr>
            <tr>
              <td><strong>FR-03</strong></td>
              <td>Sistem otomatis melakukan plotting reviewer secara acak berdasarkan kesesuaian rumpun ilmu (Subject Area Match).</td>
              <td>Plotting Reviewer Engine</td>
              <td><span class="badge badge-primary">High</span></td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    
    <!-- 3.3 Non-Functional -->
    <div class="section-card" id="nonfunc-req">
      <h3><span class="section-card-num">3.3.</span> Non-Functional Requirements</h3>
      <p class="section-card-desc">Persyaratan performa, keamanan, dan ketersediaan sistem portal.</p>
      <div class="bento-grid">
        <div class="bento-cell">
          <h4>Ketersediaan Sistem</h4>
          <p>Portal wajib memiliki uptime minimal <strong>99.9%</strong> selama periode puncak pengiriman proposal.</p>
        </div>
        <div class="bento-cell">
          <h4>Keamanan Berkas</h4>
          <p>Seluruh berkas proposal yang diunggah wajib dienkripsi menggunakan algoritma standar <strong>AES-256</strong>.</p>
        </div>
        <div class="bento-cell">
          <h4>Integrasi Data</h4>
          <p>Proses pengecekan NIDN dan NIM terintegrasi API PDDIKTI dengan jaminan integritas data <strong>100%</strong>.</p>
        </div>
      </div>
    </div>
    
    <!-- 3.4 Acceptance Criteria -->
    <div class="section-card" id="accept-crit">
      <h3><span class="section-card-num">3.4.</span> Acceptance Criteria (Gherkin Scenario)</h3>
      <p class="section-card-desc">Kriteria pengujian penerimaan sistem untuk persetujuan anggota riset.</p>
      <pre>Scenario: Percobaan Submit Proposal Tanpa Persetujuan Anggota Lengkap
  Given Dosen Ketua mengundang 1 Dosen Anggota dan 1 Mahasiswa Anggota
  And Dosen Anggota mengubah status persetujuan menjadi "Approved"
  And Mahasiswa Anggota masih berstatus "Pending"
  When Dosen Ketua membuka halaman review proposal
  Then Sistem mengunci tombol "Submit Proposal ke Fakultas"
  And Menampilkan pesan warning "Menunggu Persetujuan dari Anggota Mahasiswa"</pre>
    </div>
  </div>

  <!-- PHASE 4: SYSTEM DESIGN & MODELING -->
  <div class="phase-block">
    <div class="phase-badge pb-amber">Fase 4: Desain & Pemodelan Sistem (UML & Database)</div>
    
    <!-- 4.1 Activity Diagram -->
    <div class="section-card" id="activity">
      <h3><span class="section-card-num">4.1.</span> Activity Diagram</h3>
      <p class="section-card-desc">Alur logis aktivitas validasi dan seleksi proposal.</p>
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
    </div>
    
    <!-- 4.2 Sequence Diagram -->
    <div class="section-card" id="sequence">
      <h3><span class="section-card-num">4.2.</span> Sequence Diagram</h3>
      <p class="section-card-desc">Aliran pesan dalam runtime untuk persetujuan keanggotaan riset.</p>
      <div class="diagram-container">
        <div class="mermaid">
          sequenceDiagram
            actor Ketua as Dosen Ketua
            participant Portal as Portal SIMPPM
            actor Anggota as Anggota (Dosen/Mhs)
            participant DB as Database Server
            
            Ketua->>Portal: Input Anggota (NIDN/NIM)
            Portal->>DB: Check User & Status Aktif
            DB-->>Portal: User Found
            Portal->>DB: Create Member Entry (status: PENDING)
            Portal-->>Anggota: Kirim Email Undangan & Notifikasi
            Anggota->>Portal: Login & Buka Undangan Keanggotaan
            Anggota->>Portal: Klik "Setujui Gabung"
            Portal->>DB: Update Member Entry (status: APPROVED)
            DB-->>Portal: Confirmed Successful
            Portal-->>Ketua: Update Status UI (Tombol Submit Aktif)
        </div>
      </div>
    </div>
    
    <!-- 4.3 ERD -->
    <div class="section-card" id="erd">
      <h3><span class="section-card-num">4.3.</span> Entity Relationship Diagram (ERD Schema)</h3>
      <p class="section-card-desc">Struktur relasi database portal untuk mengelola siklus riset dan pengabdian.</p>
      <div class="diagram-container">
        <div class="mermaid">
          erDiagram
            USER ||--o{ PROPOSAL : creates
            PROPOSAL ||--|{ MEMBER : contains
            USER ||--o{ MEMBER : joins
            PROPOSAL ||--o{ REVIEW : receives
            USER ||--o{ REVIEW : evaluates
            PROPOSAL ||--o| CONTRACT : generates
            
            USER {
              int user_id PK
              string nama
              string email
              string nidn_nim
              string unit_kerja
            }
            PROPOSAL {
              int proposal_id PK
              int ketua_id FK
              string judul
              string skema_riset
              string file_path
              string status
            }
            MEMBER {
              int member_id PK
              int proposal_id FK
              int user_id FK
              string tipe_anggota
              string status_persetujuan
            }
            REVIEW {
              int review_id PK
              int proposal_id FK
              int reviewer_id FK
              float skor_nilai
              string komentar
            }
            CONTRACT {
              int contract_id PK
              int proposal_id FK
              string nomor_kontrak
              float nilai_pendanaan
            }
        </div>
      </div>
    </div>
  </div>

  <!-- PHASE 5: TECHNICAL SPECS -->
  <div class="phase-block">
    <div class="phase-badge pb-rose">Fase 5: Spesifikasi Teknis & Integrasi API</div>
    
    <!-- 5.1 API Doc -->
    <div class="section-card" id="api-doc">
      <h3><span class="section-card-num">5.1.</span> API Documentation (RESTful Endpoints)</h3>
      <p class="section-card-desc">Endpoints krusial untuk membuat proposal baru dan persetujuan anggota riset.</p>
      
      <strong>1. Endpoint:</strong> <code style="background:#e2e8f0; padding:2px 6px; border-radius:4px; font-family:'JetBrains Mono';">POST /api/v1/proposal</code>
      <pre>{
  "judul": "Analisis Preprocessing Teks NLP Bahasa Daerah Jawa Timur",
  "skema_riset": "HIBAH_INTERNAL_PEMULA",
  "anggota_dosen": ["0423108821"],
  "anggota_mahasiswa": ["434231055"]
}</pre>

      <strong style="display:block; margin-top:20px;">2. Endpoint:</strong> <code style="background:#e2e8f0; padding:2px 6px; border-radius:4px; font-family:'JetBrains Mono';">POST /api/v1/proposal/{id}/confirm-member</code>
      <pre>{
  "user_id": 10293,
  "status_persetujuan": "APPROVED"
}</pre>
    </div>
    
    <!-- 5.2 Validation Rules -->
    <div class="section-card" id="val-rules">
      <h3><span class="section-card-num">5.2.</span> Validation Rules (Logika Bisnis)</h3>
      <p class="section-card-desc">Pengecekan integritas data sebelum didorong ke database sistem.</p>
      <div class="table-wrapper">
        <table>
          <thead>
            <tr>
              <th>Aturan Validasi</th>
              <th>Syarat Kriteria Sistem</th>
              <th>Pesan Kesalahan (Error Code)</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>NIDN/NIM Check</td>
              <td>Nomor NIDN/NIM terdaftar aktif di server database PDDIKTI.</td>
              <td>USER_NOT_ACTIVE: Pengguna Tidak Aktif / Tidak Terdaftar</td>
            </tr>
            <tr>
              <td>Conflict of Interest</td>
              <td>Reviewer tidak boleh berasal dari program studi yang sama dengan Dosen Ketua.</td>
              <td>COI_DETECTED: Reviewer Berasal dari Prodi Pengusul</td>
            </tr>
            <tr>
              <td>Double Proposal Block</td>
              <td>Dosen Ketua hanya boleh mengusulkan maksimal 2 proposal dalam 1 periode aktif.</td>
              <td>LIMIT_EXCEEDED: Batas Pengajuan Proposal Terlampaui</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    
    <!-- 5.3 RACI Matrix -->
    <div class="section-card" id="role-matrix">
      <h3><span class="section-card-num">5.3.</span> Role & RACI Access Control Matrix</h3>
      <p class="section-card-desc">Manajemen hak akses berdasarkan peran pengguna akhir (RBAC).</p>
      <div class="table-wrapper">
        <table>
          <thead>
            <tr>
              <th>Fitur / Layanan</th>
              <th>Dosen Ketua</th>
              <th>Akademik</th>
              <th>Dekan</th>
              <th>Reviewer</th>
              <th>Admin LPPM</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Create & Edit Proposal</td>
              <td><span class="badge badge-success">Full Access</span></td>
              <td>-</td>
              <td>-</td>
              <td>-</td>
              <td><span class="badge badge-primary">Read</span></td>
            </tr>
            <tr>
              <td>Rilis Rekomendasi Dekan</td>
              <td>-</td>
              <td><span class="badge badge-primary">Read</span></td>
              <td><span class="badge badge-success">Approve</span></td>
              <td>-</td>
              <td>-</td>
            </tr>
            <tr>
              <td>Plotting Reviewer acak</td>
              <td>-</td>
              <td>-</td>
              <td>-</td>
              <td>-</td>
              <td><span class="badge badge-success">Full Access</span></td>
            </tr>
            <tr>
              <td>Input Nilai Evaluasi</td>
              <td>-</td>
              <td>-</td>
              <td>-</td>
              <td><span class="badge badge-success">Approve</span></td>
              <td>-</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    
    <!-- 5.4 Exception Flow -->
    <div class="section-card" id="exception">
      <h3><span class="section-card-num">5.4.</span> Exception Flow (SLA Breach Mitigation)</h3>
      <p class="section-card-desc">Mitigasi keterlambatan proses penilaian oleh reviewer.</p>
      <div style="background: #fff5f5; border: 1px solid #fecaca; border-radius: 12px; padding: 24px;">
        <p style="color: #991b1b; font-weight: 700; margin-bottom: 8px;">Kebijakan Reviewer Timeout (SLA 7 Hari):</p>
        <p style="color: #7f1d1d; font-size: 0.9rem;">Apabila reviewer yang di-plot tidak memasukkan nilai evaluasi dalam batas waktu 7 hari kerja, sistem otomatis mengirimkan notifikasi penarikan tugas. Engine Plotting LPPM akan langsung berjalan untuk merekrut reviewer cadangan (Backup Reviewer) secara otomatis tanpa intervensi manual admin.</p>
      </div>
    </div>
  </div>

  <!-- PHASE 6: TESTING & RISK -->
  <div class="phase-block">
    <div class="phase-badge pb-purple">Fase 6: Pengujian & Manajemen Risiko Proyek</div>
    
    <!-- 6.1 UAT -->
    <div class="section-card" id="uat">
      <h3><span class="section-card-num">6.1.</span> UAT Test Plan</h3>
      <p class="section-card-desc">Uji kelayakan sistem untuk validasi persetujuan anggota.</p>
      <div class="table-wrapper">
        <table>
          <thead>
            <tr>
              <th>ID Uji</th>
              <th>Target Fitur Uji</th>
              <th>Langkah Percobaan</th>
              <th>Hasil yang Diharapkan</th>
              <th>Status</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>UAT-L01</td>
              <td>Bypass Submit Block</td>
              <td>Lakukan klik tombol submit saat ada anggota berstatus 'Pending'.</td>
              <td>Sistem mengunci tombol submit dan menampilkan tooltip peringatan.</td>
              <td><span class="badge badge-success">Passed</span></td>
            </tr>
            <tr>
              <td>UAT-L02</td>
              <td>Double-Blind Integrity</td>
              <td>Buka halaman input nilai pada akun Reviewer 1.</td>
              <td>Nama pengusul dan instansi disamarkan (sensor), hanya menampilkan dokumen proposal tanpa identitas.</td>
              <td><span class="badge badge-success">Passed</span></td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    
    <!-- 6.2 RTM -->
    <div class="section-card" id="rtm">
      <h3><span class="section-card-num">6.2.</span> Requirements Traceability Matrix (RTM)</h3>
      <p class="section-card-desc">Pemetaan dari kebutuhan fungsional hingga rencana kasus uji UAT.</p>
      <div class="table-wrapper">
        <table>
          <thead>
            <tr>
              <th>ID Kebutuhan Bisnis</th>
              <th>ID Fungsional (FR)</th>
              <th>Skenario Kasus Uji</th>
              <th>Modul Evaluasi</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>BR-01 (SLA Reduction)</td>
              <td>FR-03 (Automated Plotting Engine)</td>
              <td>UAT-L03 (Auto-Assign review)</td>
              <td>Plotting Reviewer Cluster</td>
            </tr>
            <tr>
              <td>BR-02 (Anti-Bias Scoring)</td>
              <td>FR-01 (Double-Blind Privacy Filter)</td>
              <td>UAT-L02 (Double-Blind Integrity)</td>
              <td>Review & Grading Module</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    
    <!-- 6.3 Risk Register -->
    <div class="section-card" id="risk-reg">
      <h3><span class="section-card-num">6.3.</span> Risk Register</h3>
      <p class="section-card-desc">Potensi hambatan kelancaran rilis sistem dan rencana rencana mitigasi.</p>
      <div class="table-wrapper">
        <table>
          <thead>
            <tr>
              <th>Deskripsi Risiko</th>
              <th>Level Risiko</th>
              <th>Dampak Operasional</th>
              <th>Rencana Tindakan Mitigasi</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Downtime API PDDIKTI saat validasi mahasiswa</td>
              <td><span class="badge badge-warning">Sedang</span></td>
              <td>Staf tidak dapat memvalidasi NIM mahasiswa secara real-time.</td>
              <td>Gunakan caching data mahasiswa lokal yang disinkronisasi berkala di malam hari.</td>
            </tr>
            <tr>
              <td>Beban server saat overload upload PDF</td>
              <td><span class="badge badge-danger">Tinggi</span></td>
              <td>Server melambat akibat upload ratusan berkas proposal berukuran besar secara serentak.</td>
              <td>Implementasikan CDN dan upload buffer file langsung ke cloud storage (seperti AWS S3/Cloud Storage) dengan throttling limit.</td>
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
      <p class="section-card-desc">Dampak riil transformasi digital terhadap pengelolaan riset LPPM.</p>
      <div class="bento-grid">
        <div class="bento-cell">
          <h4>SLA Verifikasi Riset</h4>
          <p style="font-size: 2.2rem; font-weight: 800; color: var(--accent-teal); line-height: 1;">-80%</p>
          <p style="font-weight: 600; margin-top: 10px;">Cycle Time Pengajuan</p>
          <p>Memangkas alur verifikasi berkas dari 35 hari kerja menjadi kurang dari 7 hari.</p>
        </div>
        <div class="bento-cell">
          <h4>Penyelamatan Anggaran (Review)</h4>
          <p style="font-size: 2.2rem; font-weight: 800; color: var(--accent-teal); line-height: 1;">100%</p>
          <p style="font-weight: 600; margin-top: 10px;">Double-Blind Compliance</p>
          <p>Menghilangkan potensi konflik kepentingan reviewer secara total melalui sistem blind plotting.</p>
        </div>
        <div class="bento-cell">
          <h4>Paperless Savings</h4>
          <p style="font-size: 2.2rem; font-weight: 800; color: var(--accent-teal); line-height: 1;">98%</p>
          <p style="font-weight: 600; margin-top: 10px;">Efisiensi Cetak Berkas</p>
          <p>Menghilangkan pencetakan proposal rangkap 5 secara fisik ke format digital PDF.</p>
        </div>
      </div>
    </div>
  </div>
    """
    
    return build_html(title, project_name, role, meta_units, meta_platform, meta_author, sidebar_nav_html, main_content_html, accent_class, color_theme_style)

# Generate and write all files
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

