<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width,initial-scale=1.0"/>
  <title>GAV SmartProcure - UX Research Canvas</title>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet"/>
  <!-- Mermaid JS for diagrams -->
  <script src="https://cdn.jsdelivr.net/npm/mermaid/dist/mermaid.min.js"></script>
  <script>
    mermaid.initialize({ 
      startOnLoad: true, 
      theme: 'base',
      themeVariables: {
        primaryColor: '#eff6ff',
        primaryTextColor: '#1e3a8a',
        primaryBorderColor: '#93c5fd',
        lineColor: '#94a3b8',
        secondaryColor: '#f0fdf4',
        tertiaryColor: '#fffbeb'
      },
      fontFamily: 'Plus Jakarta Sans'
    });
  </script>
  <style>
    :root {
      --bg-canvas: #f8fafc;
      --c-purple: #8b5cf6;
      --c-blue: #3b82f6;
      --c-green: #10b981;
      --c-orange: #f59e0b;
      --c-red: #ef4444;
      --text-main: #0f172a;
      --text-muted: #64748b;
    }
    
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body { font-family: 'Plus Jakarta Sans', sans-serif; background: var(--bg-canvas); color: var(--text-main); line-height: 1.6; overflow-x: hidden;
           background-image: radial-gradient(#cbd5e1 1px, transparent 1px); background-size: 40px 40px; /* Dot grid pattern */ }
    
    .nav { position: sticky; top: 0; background: rgba(255, 255, 255, 0.9); backdrop-filter: blur(8px); padding: 16px 40px; border-bottom: 1px solid #e2e8f0; z-index: 100; display: flex; justify-content: space-between; align-items: center; }
    .nav a { color: var(--c-blue); text-decoration: none; font-weight: 600; }
    
    .canvas-container { padding: 80px 60px; display: flex; flex-direction: column; gap: 100px; max-width: 1800px; margin: 0 auto; }
    
    .canvas-header { text-align: left; max-width: 900px; margin-bottom: -40px; }
    .canvas-header h1 { font-size: 4rem; font-weight: 800; line-height: 1.1; letter-spacing: -0.03em; margin-bottom: 20px; }
    .canvas-header p { font-size: 1.4rem; color: var(--text-muted); }
    
    /* Phase Row Styles */
    .phase-row { position: relative; padding-left: 60px; }
    .phase-row::before { content: ''; position: absolute; left: 0; top: 0; bottom: 0; width: 16px; border-radius: 16px; }
    .phase-purple::before { background: var(--c-purple); }
    .phase-blue::before { background: var(--c-blue); }
    .phase-green::before { background: var(--c-green); }
    .phase-orange::before { background: var(--c-orange); }
    .phase-red::before { background: var(--c-red); }

    .phase-title { font-size: 2.5rem; font-weight: 800; color: var(--text-main); margin-bottom: 8px; display: flex; align-items: center; gap: 16px; }
    .phase-subtitle { font-size: 1.2rem; color: var(--text-muted); margin-bottom: 40px; font-weight: 500; }
    
    /* Board Grid & Cards */
    .board-flex { display: flex; flex-wrap: wrap; gap: 30px; align-items: stretch; margin-bottom: 40px; }
    
    .sticky { background: #ffffff; padding: 30px; border-radius: 12px; box-shadow: 0 10px 25px -5px rgba(0,0,0,0.05); width: 350px; flex-shrink: 0; border: 1px solid #e2e8f0; position: relative; }
    .sticky-wide { width: 100%; max-width: 800px; }
    .sticky::after { content: ''; position: absolute; top: 0; left: 0; right: 0; height: 6px; border-radius: 12px 12px 0 0; }
    
    .sticky-purple::after { background: var(--c-purple); }
    .sticky-blue::after { background: var(--c-blue); }
    .sticky-green::after { background: var(--c-green); }
    .sticky-orange::after { background: var(--c-orange); }
    
    .sticky-note-yellow { background: #fef3c7; border: 1px solid #fde68a; box-shadow: 4px 4px 15px rgba(0,0,0,0.05); transform: rotate(-1deg); width: 280px; border-radius: 4px; padding: 24px; position: relative; }
    .sticky-note-yellow:nth-child(even) { transform: rotate(2deg); }
    
    .card-label { font-size: 0.8rem; text-transform: uppercase; letter-spacing: 0.1em; color: var(--text-muted); margin-bottom: 10px; font-weight: 700; }
    .sticky h3 { font-size: 1.3rem; margin-bottom: 12px; color: var(--text-main); }
    .sticky p, .sticky-note-yellow p { font-size: 1rem; color: #334155; }
    
    /* Flowchart / Journey Map Styles */
    .flow-container { display: flex; align-items: center; gap: 15px; overflow-x: auto; padding-bottom: 20px; }
    .flow-node { background: white; border: 2px solid #cbd5e1; padding: 20px; border-radius: 50px; min-width: 220px; text-align: center; font-weight: 600; box-shadow: 0 4px 6px rgba(0,0,0,0.02); }
    .flow-arrow { color: #cbd5e1; font-size: 1.5rem; font-weight: bold; }
    .flow-node.tobe { border-color: var(--c-green); background: #f0fdf4; color: #166534; }
    .flow-node.asis { border-color: var(--c-red); background: #fef2f2; color: #991b1b; }
    
    /* Mermaid Wrapper */
    .mermaid-canvas { background: white; padding: 40px; border-radius: 16px; box-shadow: 0 10px 25px -5px rgba(0,0,0,0.05); border: 1px solid #e2e8f0; margin-bottom: 30px; width: 100%; display: flex; flex-direction: column; align-items: center; }
    .mermaid-title { align-self: flex-start; margin-bottom: 20px; font-size: 1.4rem; font-weight: 700; color: var(--text-main); }
    
    /* Big Metrics */
    .metrics-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 30px; }
    .metric-card { background: white; padding: 40px; border-radius: 16px; text-align: center; box-shadow: 0 10px 25px -5px rgba(0,0,0,0.05); border: 1px solid #e2e8f0; }
    .metric-card h2 { font-size: 4rem; font-weight: 800; color: var(--c-red); line-height: 1; margin-bottom: 10px; }
    .metric-card p { font-size: 1.2rem; font-weight: 700; margin-bottom: 8px; }
    .metric-card span { color: var(--text-muted); font-size: 0.95rem; }
    
    /* Badge */
    .tag { display: inline-block; padding: 4px 12px; background: #f1f5f9; border-radius: 99px; font-size: 0.8rem; font-weight: 600; margin-right: 8px; margin-bottom: 8px; color: #475569; }
    
    @media (max-width: 1024px) {
      .canvas-container { padding: 40px 20px; }
      .metrics-grid { grid-template-columns: repeat(2, 1fr); }
    }
  </style>
</head>
<body>

<nav class="nav">
  <a href="index.html">← Kembali ke Portfolio Utama</a>
  <span style="color: #64748b; font-weight: 500;">GAV SmartProcure — Analisis Sistem Enterprise</span>
</nav>

<div class="canvas-container">

  <div class="canvas-header">
    <h1>GAV SmartProcure:<br>Enterprise Procurement<br>Digital Transformation</h1>
    <p>Dokumentasi Pemikiran Sistematis & UX Research untuk Integrasi SAP Workflow pada Industri Penerbangan (MRO).</p>
  </div>

  <!-- PHASE 1: DISCOVERY -->
  <div class="phase-row phase-purple">
    <h2 class="phase-title"><span style="color:var(--c-purple)">01</span> Plan & Discover</h2>
    <p class="phase-subtitle">Menggali konteks bisnis, memahami regulasi, dan memetakan masalah akar (*Pain Points*).</p>
    
    <div class="board-flex">
      <div class="sticky sticky-purple">
        <div class="card-label">Business Context</div>
        <h3>MRO Aviation Industry</h3>
        <p>Industri Maintenance, Repair, and Overhaul (MRO) memiliki regulasi keselamatan sangat ketat. Keterlambatan pengadaan suku cadang memicu **Aircraft On Ground (AOG)** yang merugikan hingga miliaran rupiah per jam.</p>
      </div>
      
      <div class="sticky sticky-purple">
        <div class="card-label">Project Scope</div>
        <h3>Zero-Paper Workflow</h3>
        <p>Membangun sistem *bridge* untuk mendigitalkan seluruh siklus pengadaan (PR to PO) dan sinkronisasi inventaris secara otomatis dengan **SAP ERP backend**.</p>
        <div style="margin-top: 15px;">
          <span class="tag">System Analysis</span><span class="tag">BPR</span><span class="tag">SAP Integration</span>
        </div>
      </div>
    </div>
    
    <h3 style="margin-bottom:20px; font-size:1.2rem; color:var(--text-muted);">Pain Point Mapping (Root Cause)</h3>
    <div class="board-flex">
      <div class="sticky-note-yellow">
        <h3>⏳ Approval Botol Leher</h3>
        <p>Proses persetujuan (5-7 hari) terhambat karena butuh tanda tangan basah manajer yang sering tidak berada di tempat.</p>
      </div>
      <div class="sticky-note-yellow">
        <h3>💸 Blind Budgeting</h3>
        <p>Pengecekan sisa anggaran dilakukan manual via Excel oleh Finance, menyebabkan risiko over-budget.</p>
      </div>
      <div class="sticky-note-yellow">
        <h3>⚠️ Inventory Desync</h3>
        <p>Bagian gudang mencatat penerimaan barang (GR) di kertas, lalu ditumpuk untuk diinput ke SAP besoknya.</p>
      </div>
      <div class="sticky-note-yellow">
        <h3>📉 Human Error PR</h3>
        <p>Admin mengetik ulang kode material kompleks ke SAP GUI, memicu ~12% defect pemesanan salah barang.</p>
      </div>
    </div>
  </div>

  <!-- PHASE 2: CURRENT STATE -->
  <div class="phase-row phase-blue">
    <h2 class="phase-title"><span style="color:var(--c-blue)">02</span> Current State Analysis</h2>
    <p class="phase-subtitle">Membedah alur kerja manual (AS-IS) dan mengidentifikasi pemangku kepentingan kunci.</p>
    
    <div class="board-flex">
      <div class="sticky sticky-blue sticky-wide">
        <div class="card-label">Stakeholder Matrix (RACI Mapping)</div>
        <div style="display:grid; grid-template-columns: 1fr 1fr; gap:20px;">
          <div><strong>👨‍🔧 Pemohon (Mekanik):</strong> Butuh UI yang super simpel, tanpa harus hafal T-Code SAP.</div>
          <div><strong>👔 Manajer (Approval):</strong> Butuh kemudahan setuju via smartphone (1-click approve).</div>
          <div><strong>💰 Finance:</strong> Wajib ada fitur *Hard-Stop* otomatis jika anggaran tidak cukup.</div>
          <div><strong>📦 Warehouse:</strong> Butuh scan Barcode/QR untuk update stok real-time ke SAP.</div>
        </div>
      </div>
    </div>

    <h3 style="margin-bottom:20px; font-size:1.2rem; color:var(--text-muted);">AS-IS User Journey (Manual Process)</h3>
    <div class="flow-container">
      <div class="flow-node asis">Tulis PR di Excel/Kertas</div>
      <div class="flow-arrow">➔</div>
      <div class="flow-node asis">Keliling Cari Tanda Tangan</div>
      <div class="flow-arrow">➔</div>
      <div class="flow-node asis">Finance Cek Excel Manual</div>
      <div class="flow-arrow">➔</div>
      <div class="flow-node asis">Admin Ketik Ulang ke SAP</div>
      <div class="flow-arrow">➔</div>
      <div class="flow-node asis">Kirim PO PDF via Email</div>
    </div>
  </div>

  <!-- PHASE 3: IDEATION & TARGET -->
  <div class="phase-row phase-green">
    <h2 class="phase-title"><span style="color:var(--c-green)">03</span> Target Architecture & Solution</h2>
    <p class="phase-subtitle">Merancang cetak biru solusi digital, menetapkan *Requirements*, dan memetakan alur ideal (TO-BE).</p>
    
    <h3 style="margin-bottom:20px; font-size:1.2rem; color:var(--text-muted);">TO-BE Automated Workflow (SAP Integrated)</h3>
    <div class="flow-container">
      <div class="flow-node tobe">Pilih Barang via Web Catalog</div>
      <div class="flow-arrow">➔</div>
      <div class="flow-node tobe">Sistem Auto-Check Budget API</div>
      <div class="flow-arrow">➔</div>
      <div class="flow-node tobe">Mobile Push Notification Approve</div>
      <div class="flow-arrow">➔</div>
      <div class="flow-node tobe">SAP BAPI Generate PO Otomatis</div>
      <div class="flow-arrow">➔</div>
      <div class="flow-node tobe">Gudang Scan QR (Real-time GR)</div>
    </div>

    <div class="board-flex" style="margin-top:40px;">
      <div class="sticky sticky-green sticky-wide">
        <div class="card-label">Synthesized Requirements (BRD & FR)</div>
        <ul style="margin-left:20px; color:#334155; line-height:1.8;">
          <li><strong>[FR-01] Validasi Anggaran Real-time:</strong> Sistem memblokir *submit* jika `PR.Total > AvailableBudget`.</li>
          <li><strong>[FR-02] Dynamic Routing:</strong> Persetujuan berjenjang otomatis sesuai limit harga (Threshold).</li>
          <li><strong>[FR-03] AOG Emergency Bypass:</strong> Bypass SLA standar untuk suku cadang kritis, kirim notif SMS ke Direksi.</li>
          <li><strong>[NFR-01] Response Time:</strong> Sinkronisasi API validasi ke SAP maksimal 2.5 detik.</li>
          <li><strong>[NFR-02] Security:</strong> SSO Microsoft AD & Enkripsi Data AES-256.</li>
        </ul>
      </div>
    </div>
  </div>

  <!-- PHASE 4: MODELING (UML) -->
  <div class="phase-row phase-orange">
    <h2 class="phase-title"><span style="color:var(--c-orange)">04</span> System Modeling & UML Blueprint</h2>
    <p class="phase-subtitle">Menerjemahkan *requirements* menjadi diagram teknis terstruktur sebagai panduan pengembangan perangkat lunak.</p>
    
    <!-- Mermaid Diagrams -->
    <div class="mermaid-canvas">
      <div class="mermaid-title">High-Level System Architecture</div>
      <div class="mermaid">
        graph TD
          A[Client: Web & Mobile App] -->|HTTPS / REST API| B(Node.js / Express Middleware)
          B -->|Read/Write buffer| C[(PostgreSQL App DB)]
          B -->|RFC / OData| D{SAP PI/PO Integration}
          D <-->|BAPI| E[(SAP ERP HANA)]
          
          classDef frontend fill:#dbeafe,stroke:#3b82f6,stroke-width:2px;
          classDef backend fill:#fef3c7,stroke:#f59e0b,stroke-width:2px;
          classDef sap fill:#dcfce7,stroke:#10b981,stroke-width:2px;
          
          class A frontend;
          class B,C backend;
          class D,E sap;
      </div>
    </div>

    <div class="mermaid-canvas">
      <div class="mermaid-title">Data Flow Diagram (DFD Level 0)</div>
      <div class="mermaid">
        graph LR
          U[Requestor] -->|Input PR Data| SYS((SmartProcure System))
          SYS -->|Notifikasi| M[Manager]
          M -->|Approval Decision| SYS
          SYS -->|Cek Budget & Material| S[SAP System]
          S -->|Status & Data| SYS
          SYS -->|Generate PO| V[Vendor]
          W[Warehouse] -->|Scan Barcode GR| SYS
      </div>
    </div>

    <div class="mermaid-canvas">
      <div class="mermaid-title">Entity Relationship Diagram (Core ERD Buffer)</div>
      <div class="mermaid">
        erDiagram
          USER ||--o{ PURCHASE_REQUEST : creates
          PURCHASE_REQUEST ||--|{ PR_ITEM : contains
          MATERIAL_CATALOG ||--o{ PR_ITEM : references
          PURCHASE_REQUEST ||--o| PURCHASE_ORDER : generates
          PURCHASE_ORDER ||--o{ GOODS_RECEIPT : tracks
          
          PURCHASE_REQUEST {
            string pr_id PK
            string user_id FK
            string status
            float total_amount
          }
          PR_ITEM {
            string item_id PK
            string pr_id FK
            string material_code FK
            int quantity
          }
      </div>
    </div>

    <div class="mermaid-canvas">
      <div class="mermaid-title">Sequence Diagram: PR Creation & Budget Validation</div>
      <div class="mermaid">
        sequenceDiagram
          actor User
          participant WebApp
          participant API_Gateway
          participant SAP_Backend
          
          User->>WebApp: Submit PR Form
          WebApp->>API_Gateway: POST /api/purchase-request
          API_Gateway->>SAP_Backend: Call BAPI_BUDGET_CHECK
          
          alt Budget Sufficient
              SAP_Backend-->>API_Gateway: Return OK
              API_Gateway-->>WebApp: Success, PR Saved
              WebApp-->>User: Show "Menunggu Approval"
          else Budget Insufficient
              SAP_Backend-->>API_Gateway: Return Error (Overbudget)
              API_Gateway-->>WebApp: 400 Bad Request
              WebApp-->>User: Show "Error: Budget Tidak Cukup"
          end
      </div>
    </div>
  </div>

  <!-- PHASE 5: IMPACT -->
  <div class="phase-row phase-red">
    <h2 class="phase-title"><span style="color:var(--c-red)">05</span> Validation & Business Impact (ROI)</h2>
    <p class="phase-subtitle">Mengukur kesuksesan implementasi transformasi digital terhadap KPI bisnis perusahaan.</p>
    
    <div class="metrics-grid">
      <div class="metric-card">
        <h2>70%</h2>
        <p>Lebih Cepat</p>
        <span>Waktu siklus pengadaan (PR ke PO) turun drastis dari 7 hari menjadi 1-2 hari saja berkat persetujuan mobile.</span>
      </div>
      <div class="metric-card">
        <h2>0%</h2>
        <p>Budget Overrun</p>
        <span>Integrasi API langsung menolak pengajuan jika sisa saldo Cost Center (SAP FI/CO) tidak mencukupi.</span>
      </div>
      <div class="metric-card">
        <h2>99%</h2>
        <p>Akurasi Inventaris</p>
        <span>Pencatatan Goods Receipt (GR) secara real-time via scan barcode mobile, mengeliminasi selisih stok.</span>
      </div>
      <div class="metric-card">
        <h2>100%</h2>
        <p>Audit Compliance</p>
        <span>Rekam jejak persetujuan (Digital Audit Trail) tidak bisa dimanipulasi, menjamin keamanan audit BUMN & EASA.</span>
      </div>
    </div>
  </div>

</div>
</body>
</html>