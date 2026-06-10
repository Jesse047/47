!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>FinWise — Your Financial Literacy Guide</title>
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Sora:wght@600;700&display=swap" rel="stylesheet" />
<style>
  *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

  :root {
    --teal-50: #E1F5EE;
    --teal-100: #9FE1CB;
    --teal-400: #1D9E75;
    --teal-600: #0F6E56;
    --teal-800: #085041;
    --teal-900: #04342C;
    --blue-50: #E6F1FB;
    --blue-400: #378ADD;
    --blue-600: #185FA5;
    --blue-800: #0C447C;
    --amber-50: #FAEEDA;
    --amber-400: #BA7517;
    --amber-800: #633806;
    --bg: #F7FAF9;
    --surface: #FFFFFF;
    --border: rgba(0,0,0,0.08);
    --text-primary: #0D1F1A;
    --text-secondary: #3F5450;
    --text-muted: #7A9690;
    --font-display: 'Sora', sans-serif;
    --font-body: 'Inter', sans-serif;
    --radius-md: 10px;
    --radius-lg: 16px;
    --radius-xl: 24px;
  }

  body {
    font-family: var(--font-body);
    background: var(--bg);
    color: var(--text-primary);
    min-height: 100vh;
    display: flex;
    flex-direction: column;
  }

  /* NAV */
  nav {
    background: var(--surface);
    border-bottom: 1px solid var(--border);
    padding: 0 2rem;
    height: 60px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    position: sticky;
    top: 0;
    z-index: 100;
  }
  .logo {
    font-family: var(--font-display);
    font-size: 1.25rem;
    font-weight: 700;
    color: var(--teal-600);
    display: flex;
    align-items: center;
    gap: 8px;
  }
  .logo-dot {
    width: 8px; height: 8px;
    background: var(--teal-400);
    border-radius: 50%;
    display: inline-block;
  }
  .nav-links {
    display: flex;
    gap: 1.5rem;
    list-style: none;
  }
  .nav-links a {
    font-size: 0.875rem;
    color: var(--text-secondary);
    text-decoration: none;
    font-weight: 500;
    transition: color 0.15s;
  }
  .nav-links a:hover { color: var(--teal-600); }
  .nav-cta {
    background: var(--teal-400);
    color: #fff !important;
    padding: 6px 16px;
    border-radius: var(--radius-md);
    font-weight: 500 !important;
  }
  .nav-cta:hover { background: var(--teal-600); }

  /* HERO */
  .hero {
    max-width: 1100px;
    margin: 0 auto;
    padding: 5rem 2rem 3rem;
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 4rem;
    align-items: center;
  }
  .hero-badge {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: var(--teal-50);
    color: var(--teal-800);
    font-size: 0.75rem;
    font-weight: 600;
    padding: 4px 12px;
    border-radius: 100px;
    margin-bottom: 1.25rem;
    border: 1px solid var(--teal-100);
    letter-spacing: 0.04em;
    text-transform: uppercase;
  }
  .hero h1 {
    font-family: var(--font-display);
    font-size: 3rem;
    font-weight: 700;
    line-height: 1.1;
    color: var(--text-primary);
    margin-bottom: 1.25rem;
  }
  .hero h1 span { color: var(--teal-400); }
  .hero p {
    font-size: 1.05rem;
    color: var(--text-secondary);
    line-height: 1.7;
    margin-bottom: 2rem;
  }
  .hero-actions { display: flex; gap: 12px; flex-wrap: wrap; }
  .btn-primary {
    background: var(--teal-400);
    color: #fff;
    border: none;
    padding: 12px 24px;
    border-radius: var(--radius-md);
    font-size: 0.95rem;
    font-weight: 600;
    cursor: pointer;
    font-family: var(--font-body);
    transition: background 0.15s, transform 0.1s;
    text-decoration: none;
    display: inline-block;
  }
  .btn-primary:hover { background: var(--teal-600); }
  .btn-primary:active { transform: scale(0.98); }
  .btn-secondary {
    background: transparent;
    color: var(--teal-600);
    border: 1.5px solid var(--teal-400);
    padding: 12px 24px;
    border-radius: var(--radius-md);
    font-size: 0.95rem;
    font-weight: 600;
    cursor: pointer;
    font-family: var(--font-body);
    transition: all 0.15s;
    text-decoration: none;
    display: inline-block;
  }
  .btn-secondary:hover { background: var(--teal-50); }

  /* STATS */
  .stats-strip {
    display: flex;
    gap: 1.5rem;
    flex-wrap: wrap;
    margin-top: 2.5rem;
    padding-top: 2rem;
    border-top: 1px solid var(--border);
  }
  .stat { flex: 1; min-width: 100px; }
  .stat-value {
    font-family: var(--font-display);
    font-size: 1.6rem;
    font-weight: 700;
    color: var(--teal-600);
  }
  .stat-label {
    font-size: 0.8rem;
    color: var(--text-muted);
    margin-top: 2px;
  }

  /* CHAT PANEL PREVIEW */
  .chat-preview {
    background: var(--surface);
    border-radius: var(--radius-xl);
    border: 1px solid var(--border);
    padding: 1.5rem;
    box-shadow: 0 4px 24px rgba(15,110,86,0.08);
    min-height: 400px;
    display: flex;
    flex-direction: column;
  }
  .chat-header {
    display: flex;
    align-items: center;
    gap: 10px;
    padding-bottom: 1rem;
    border-bottom: 1px solid var(--border);
    margin-bottom: 1rem;
  }
  .chat-avatar {
    width: 36px; height: 36px;
    border-radius: 50%;
    background: var(--teal-400);
    display: flex; align-items: center; justify-content: center;
    font-weight: 700;
    color: #fff;
    font-size: 0.85rem;
    flex-shrink: 0;
  }
  .chat-header-info h4 {
    font-size: 0.875rem;
    font-weight: 600;
    color: var(--text-primary);
  }
  .online-dot {
    width: 7px; height: 7px;
    background: #22c55e;
    border-radius: 50%;
    display: inline-block;
    margin-right: 4px;
  }
  .chat-header-info span {
    font-size: 0.75rem;
    color: var(--text-muted);
  }

  .preview-messages { flex: 1; display: flex; flex-direction: column; gap: 10px; }
  .msg { max-width: 80%; }
  .msg.bot { align-self: flex-start; }
  .msg.user { align-self: flex-end; }
  .msg-bubble {
    padding: 10px 14px;
    border-radius: 14px;
    font-size: 0.875rem;
    line-height: 1.55;
  }
  .bot .msg-bubble {
    background: var(--teal-50);
    color: var(--teal-900);
    border-bottom-left-radius: 4px;
  }
  .user .msg-bubble {
    background: var(--teal-400);
    color: #fff;
    border-bottom-right-radius: 4px;
  }
  .msg-time {
    font-size: 0.7rem;
    color: var(--text-muted);
    margin-top: 3px;
    padding: 0 4px;
  }
  .user .msg-time { text-align: right; }

  /* FEATURES */
  .section {
    max-width: 1100px;
    margin: 0 auto;
    padding: 4rem 2rem;
  }
  .section-label {
    font-size: 0.75rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    color: var(--teal-400);
    margin-bottom: 0.75rem;
  }
  .section-title {
    font-family: var(--font-display);
    font-size: 2rem;
    font-weight: 700;
    color: var(--text-primary);
    margin-bottom: 0.75rem;
  }
  .section-sub {
    font-size: 1rem;
    color: var(--text-secondary);
    max-width: 540px;
    line-height: 1.65;
  }
  .features-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
    gap: 1.25rem;
    margin-top: 2.5rem;
  }
  .feature-card {
    background: var(--surface);
    border-radius: var(--radius-lg);
    border: 1px solid var(--border);
    padding: 1.5rem;
    transition: transform 0.15s, box-shadow 0.15s;
  }
  .feature-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 6px 20px rgba(15,110,86,0.08);
  }
  .feature-icon {
    width: 44px; height: 44px;
    border-radius: var(--radius-md);
    background: var(--teal-50);
    display: flex; align-items: center; justify-content: center;
    margin-bottom: 1rem;
    font-size: 1.3rem;
  }
  .feature-card h3 {
    font-size: 1rem;
    font-weight: 600;
    color: var(--text-primary);
    margin-bottom: 0.5rem;
  }
  .feature-card p {
    font-size: 0.875rem;
    color: var(--text-secondary);
    line-height: 1.6;
  }

  /* TOPICS */
  .topics-section {
    background: var(--teal-900);
    padding: 4rem 2rem;
  }
  .topics-inner {
    max-width: 1100px;
    margin: 0 auto;
  }
  .topics-inner .section-label { color: var(--teal-100); }
  .topics-inner .section-title { color: #fff; }
  .topics-inner .section-sub { color: var(--teal-100); }
  .topics-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
    gap: 12px;
    margin-top: 2.5rem;
  }
  .topic-chip {
    background: rgba(255,255,255,0.08);
    border: 1px solid rgba(255,255,255,0.15);
    color: var(--teal-50);
    padding: 10px 16px;
    border-radius: var(--radius-md);
    font-size: 0.875rem;
    font-weight: 500;
    cursor: pointer;
    transition: background 0.15s, border-color 0.15s;
    text-align: center;
  }
  .topic-chip:hover {
    background: rgba(255,255,255,0.16);
    border-color: var(--teal-100);
  }

  /* MAIN CHATBOT SECTION */
  .chatbot-section {
    background: var(--surface);
    border-top: 1px solid var(--border);
    padding: 4rem 2rem;
  }
  .chatbot-inner {
    max-width: 800px;
    margin: 0 auto;
  }
  .chatbot-inner .section-label { text-align: center; }
  .chatbot-inner .section-title { text-align: center; }
  .chatbot-inner .section-sub { text-align: center; margin: 0 auto 2.5rem; }

  .chat-window {
    background: var(--bg);
    border-radius: var(--radius-xl);
    border: 1px solid var(--border);
    overflow: hidden;
    display: flex;
    flex-direction: column;
    height: 520px;
  }
  .chat-win-header {
    background: var(--surface);
    border-bottom: 1px solid var(--border);
    padding: 1rem 1.5rem;
    display: flex;
    align-items: center;
    gap: 10px;
    flex-shrink: 0;
  }
  .chat-win-avatar {
    width: 38px; height: 38px;
    border-radius: 50%;
    background: var(--teal-400);
    display: flex; align-items: center; justify-content: center;
    color: #fff;
    font-weight: 700;
    font-size: 0.9rem;
    flex-shrink: 0;
  }
  .chat-win-info h4 {
    font-size: 0.9rem;
    font-weight: 600;
    color: var(--text-primary);
  }
  .chat-win-info p {
    font-size: 0.75rem;
    color: var(--text-muted);
  }
  .chat-win-status {
    margin-left: auto;
    font-size: 0.75rem;
    color: #22c55e;
    font-weight: 500;
    display: flex;
    align-items: center;
    gap: 5px;
  }
  .chat-win-status::before {
    content: '';
    width: 7px; height: 7px;
    background: #22c55e;
    border-radius: 50%;
    display: block;
  }

  .chat-messages {
    flex: 1;
    overflow-y: auto;
    padding: 1.25rem 1.5rem;
    display: flex;
    flex-direction: column;
    gap: 12px;
    scroll-behavior: smooth;
  }
  .chat-messages::-webkit-scrollbar { width: 4px; }
  .chat-messages::-webkit-scrollbar-track { background: transparent; }
  .chat-messages::-webkit-scrollbar-thumb { background: var(--teal-100); border-radius: 4px; }

  .cm { display: flex; gap: 8px; max-width: 85%; }
  .cm.user { align-self: flex-end; flex-direction: row-reverse; }
  .cm.bot { align-self: flex-start; }
  .cm-avatar {
    width: 30px; height: 30px;
    border-radius: 50%;
    background: var(--teal-400);
    color: #fff;
    display: flex; align-items: center; justify-content: center;
    font-size: 0.7rem;
    font-weight: 700;
    flex-shrink: 0;
    margin-top: 2px;
  }
  .cm.user .cm-avatar { background: var(--text-secondary); }
  .cm-content {}
  .cm-bubble {
    padding: 10px 14px;
    border-radius: 14px;
    font-size: 0.875rem;
    line-height: 1.6;
    white-space: pre-wrap;
  }
  .cm.bot .cm-bubble {
    background: var(--surface);
    color: var(--text-primary);
    border-bottom-left-radius: 4px;
    border: 1px solid var(--border);
  }
  .cm.user .cm-bubble {
    background: var(--teal-400);
    color: #fff;
    border-bottom-right-radius: 4px;
  }
  .cm-time {
    font-size: 0.7rem;
    color: var(--text-muted);
    margin-top: 3px;
    padding: 0 4px;
  }
  .cm.user .cm-time { text-align: right; }

  .typing-indicator {
    display: flex;
    align-items: center;
    gap: 4px;
    padding: 10px 14px;
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 14px;
    border-bottom-left-radius: 4px;
    width: fit-content;
  }
  .typing-dot {
    width: 7px; height: 7px;
    background: var(--teal-400);
    border-radius: 50%;
    animation: typingBounce 1.2s infinite;
  }
  .typing-dot:nth-child(2) { animation-delay: 0.2s; }
  .typing-dot:nth-child(3) { animation-delay: 0.4s; }
  @keyframes typingBounce {
    0%, 60%, 100% { transform: translateY(0); opacity: 0.4; }
    30% { transform: translateY(-5px); opacity: 1; }
  }

  .chat-input-area {
    background: var(--surface);
    border-top: 1px solid var(--border);
    padding: 1rem 1.5rem;
    flex-shrink: 0;
  }
  .quick-prompts {
    display: flex;
    gap: 8px;
    flex-wrap: wrap;
    margin-bottom: 10px;
  }
  .quick-btn {
    background: var(--teal-50);
    color: var(--teal-800);
    border: 1px solid var(--teal-100);
    padding: 5px 12px;
    border-radius: 100px;
    font-size: 0.78rem;
    font-weight: 500;
    cursor: pointer;
    font-family: var(--font-body);
    transition: background 0.15s;
  }
  .quick-btn:hover { background: var(--teal-100); }

  .input-row {
    display: flex;
    gap: 10px;
    align-items: flex-end;
  }
  .chat-input {
    flex: 1;
    resize: none;
    border: 1px solid var(--border);
    border-radius: var(--radius-md);
    padding: 10px 14px;
    font-size: 0.9rem;
    font-family: var(--font-body);
    color: var(--text-primary);
    background: var(--bg);
    outline: none;
    line-height: 1.5;
    min-height: 42px;
    max-height: 100px;
    transition: border-color 0.15s;
  }
  .chat-input:focus { border-color: var(--teal-400); }
  .chat-input::placeholder { color: var(--text-muted); }

  .send-btn {
    background: var(--teal-400);
    color: #fff;
    border: none;
    width: 42px; height: 42px;
    border-radius: var(--radius-md);
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
    transition: background 0.15s, transform 0.1s;
  }
  .send-btn:hover { background: var(--teal-600); }
  .send-btn:active { transform: scale(0.95); }
  .send-btn:disabled { background: var(--text-muted); cursor: not-allowed; }
  .send-btn svg { width: 18px; height: 18px; fill: #fff; }

  /* DISCLAIMER */
  .disclaimer {
    font-size: 0.75rem;
    color: var(--text-muted);
    text-align: center;
    margin-top: 1rem;
    line-height: 1.5;
  }

  /* FOOTER */
  footer {
    background: var(--teal-900);
    color: var(--teal-100);
    padding: 2rem;
    text-align: center;
    font-size: 0.85rem;
    margin-top: auto;
  }
  footer a { color: var(--teal-100); text-decoration: none; }
  footer span { color: var(--teal-400); }

  /* RESPONSIVE */
  @media (max-width: 768px) {
    .hero { grid-template-columns: 1fr; gap: 2rem; padding: 3rem 1.5rem 2rem; }
    .hero h1 { font-size: 2.2rem; }
    .chat-preview { display: none; }
    .nav-links { display: none; }
    .topics-grid { grid-template-columns: repeat(2, 1fr); }
  }
</style>
</head>
<body>

<!-- NAV -->
<nav>
  <div class="logo">
    <span class="logo-dot"></span>
    FinWise
  </div>
  <ul class="nav-links">
    <li><a href="#features">Features</a></li>
    <li><a href="#topics">Topics</a></li>
    <li><a href="#chat">Chat</a></li>
    <li><a href="#chat" class="nav-cta">Start Learning</a></li>
  </ul>
</nav>

<!-- HERO -->
<section style="background: var(--surface);">
  <div class="hero">
    <div class="hero-content">
      <div class="hero-badge">✦ AI-Powered Financial Education</div>
      <h1>Learn finance.<br />Build <span>wealth</span>.<br />Take control.</h1>
      <p>FinWise is your personal AI guide to understanding money — budgeting, investing, loans, taxes, and more. Ask anything, anytime, in plain language.</p>
      <div class="hero-actions">
        <a href="#chat" class="btn-primary">Chat with FinWise →</a>
        <a href="#topics" class="btn-secondary">Explore Topics</a>
      </div>
      <div class="stats-strip">
        <div class="stat">
          <div class="stat-value">50+</div>
          <div class="stat-label">Finance topics covered</div>
        </div>
        <div class="stat">
          <div class="stat-value">24/7</div>
          <div class="stat-label">Always available</div>
        </div>
        <div class="stat">
          <div class="stat-value">Free</div>
          <div class="stat-label">No sign-up needed</div>
        </div>
      </div>
    </div>

    <!-- PREVIEW CHAT -->
    <div class="chat-preview">
      <div class="chat-header">
        <div class="chat-avatar">FW</div>
        <div class="chat-header-info">
          <h4>FinWise AI</h4>
          <span><span class="online-dot"></span>Online now</span>
        </div>
      </div>
      <div class="preview-messages">
        <div class="msg bot">
          <div class="msg-bubble">Hi! I'm FinWise — your financial literacy guide. What money topic can I help you understand today? 💡</div>
          <div class="msg-time">Just now</div>
        </div>
        <div class="msg user">
          <div class="msg-bubble">What's the difference between a savings account and a money market account?</div>
          <div class="msg-time">Just now</div>
        </div>
        <div class="msg bot">
          <div class="msg-bubble">Great question! Both are low-risk savings tools, but here's the key difference:<br><br><strong>Savings account</strong> — simple, low fees, usually lower interest rates. Best for an emergency fund.<br><br><strong>Money market account</strong> — slightly higher interest, often comes with check-writing access, may require a higher minimum balance.</div>
          <div class="msg-time">Just now</div>
        </div>
        <div class="msg user">
          <div class="msg-bubble">Which one should I start with?</div>
          <div class="msg-time">Just now</div>
        </div>
        <div class="msg bot">
          <div class="msg-bubble">Start with a regular savings account if you're just building your emergency fund. Once you have 3–6 months of expenses saved, a money market account can help your money grow a bit faster. 🎯</div>
          <div class="msg-time">Just now</div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- FEATURES -->
<section class="section" id="features">
  <div class="section-label">Why FinWise</div>
  <h2 class="section-title">Financial education, made simple</h2>
  <p class="section-sub">No jargon. No fees. Just clear, honest answers to your money questions — tailored to where you are financially.</p>
  <div class="features-grid">
    <div class="feature-card">
      <div class="feature-icon">🧠</div>
      <h3>Plain-language answers</h3>
      <p>Complex finance concepts broken down into everyday language you can actually use.</p>
    </div>
    <div class="feature-card">
      <div class="feature-icon">📊</div>
      <h3>Personal context</h3>
      <p>Ask about your specific situation — salary, debt, goals — and get advice that fits your reality.</p>
    </div>
    <div class="feature-card">
      <div class="feature-icon">🔒</div>
      <h3>No personal data stored</h3>
      <p>Your conversations are never saved or sold. Learn freely without privacy concerns.</p>
    </div>
    <div class="feature-card">
      <div class="feature-icon">📚</div>
      <h3>From basics to advanced</h3>
      <p>Whether you're opening your first bank account or structuring a portfolio, FinWise has you covered.</p>
    </div>
    <div class="feature-card">
      <div class="feature-icon">⚡</div>
      <h3>Instant responses</h3>
      <p>Get answers in seconds — no waiting rooms, no appointments, no confusing websites.</p>
    </div>
    <div class="feature-card">
      <div class="feature-icon">🌍</div>
      <h3>Local & global finance</h3>
      <p>Covers personal finance principles relevant across different economies and markets.</p>
    </div>
  </div>
</section>

<!-- TOPICS -->
<section class="topics-section" id="topics">
  <div class="topics-inner">
    <div class="section-label">Topics</div>
    <h2 class="section-title">What do you want to learn?</h2>
    <p class="section-sub">Click any topic to start a conversation about it in the chat below.</p>
    <div class="topics-grid">
      <div class="topic-chip" onclick="startTopic('Budgeting basics')">💰 Budgeting Basics</div>
      <div class="topic-chip" onclick="startTopic('How to invest for beginners')">📈 Investing 101</div>
      <div class="topic-chip" onclick="startTopic('How credit scores work')">⭐ Credit Scores</div>
      <div class="topic-chip" onclick="startTopic('Understanding compound interest')">🔄 Compound Interest</div>
      <div class="topic-chip" onclick="startTopic('Emergency fund: how much do I need and how to build one?')">🛡️ Emergency Fund</div>
      <div class="topic-chip" onclick="startTopic('Stock market basics')">📉 Stock Market</div>
      <div class="topic-chip" onclick="startTopic('How do loans and interest rates work?')">🏦 Loans & Rates</div>
      <div class="topic-chip" onclick="startTopic('How to pay off debt faster')">💳 Debt Management</div>
      <div class="topic-chip" onclick="startTopic('Retirement planning basics')">🏖️ Retirement</div>
      <div class="topic-chip" onclick="startTopic('Tax basics everyone should know')">📋 Taxes</div>
      <div class="topic-chip" onclick="startTopic('What is inflation and how does it affect me?')">📊 Inflation</div>
      <div class="topic-chip" onclick="startTopic('How to start a side hustle and manage the income')">💼 Side Hustles</div>
    </div>
  </div>
</section>

<!-- CHATBOT -->
<section class="chatbot-section" id="chat">
  <div class="chatbot-inner">
    <div class="section-label">Live Chatbot</div>
    <h2 class="section-title">Ask FinWise anything</h2>
    <p class="section-sub">Your AI financial literacy guide is ready. No judgment, no jargon — just real answers.</p>

    <div class="chat-window">
      <div class="chat-win-header">
        <div class="chat-win-avatar">FW</div>
        <div class="chat-win-info">
          <h4>FinWise AI</h4>
          <p>Financial literacy guide</p>
        </div>
        <div class="chat-win-status">Online</div>
      </div>

      <div class="chat-messages" id="chatMessages">
        <div class="cm bot">
          <div class="cm-avatar">FW</div>
          <div class="cm-content">
            <div class="cm-bubble">👋 Hello! I'm FinWise, your AI-powered financial literacy guide.

I can help you understand budgeting, investing, credit, loans, taxes, saving strategies, and much more.

What money topic would you like to explore today?</div>
            <div class="cm-time">Now</div>
          </div>
        </div>
      </div>

      <div class="chat-input-area">
        <div class="quick-prompts">
          <button class="quick-btn" onclick="sendQuick('How do I create a budget?')">How do I budget?</button>
          <button class="quick-btn" onclick="sendQuick('Explain investing for beginners')">Investing basics</button>
          <button class="quick-btn" onclick="sendQuick('How do I improve my credit score?')">Credit score tips</button>
          <button class="quick-btn" onclick="sendQuick('What is compound interest?')">Compound interest</button>
        </div>
        <div class="input-row">
          <textarea
            id="chatInput"
            class="chat-input"
            placeholder="Ask any finance question…"
            rows="1"
            onkeydown="handleKey(event)"
            oninput="autoResize(this)"
          ></textarea>
          <button class="send-btn" id="sendBtn" onclick="sendMessage()" title="Send">
            <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
              <path d="M2.01 21L23 12 2.01 3 2 10l15 2-15 2z"/>
            </svg>
          </button>
        </div>
      </div>
    </div>

    <p class="disclaimer">⚠️ FinWise provides financial education only — not personal financial advice. Always consult a qualified financial advisor for decisions specific to your situation.</p>
  </div>
</section>

<!-- FOOTER -->
<footer>
  <p>Built with ♥ by <span>FinWise</span> · Powered by Claude AI · Financial literacy for everyone</p>
  <p style="margin-top: 8px; font-size: 0.78rem; opacity: 0.6;">For educational purposes only. Not regulated financial advice.</p>
</footer>

<script>
const SYSTEM_PROMPT = `You are FinWise, a friendly and knowledgeable financial literacy AI guide. Your role is to educate users about personal finance, investing, budgeting, credit, loans, taxes, and related topics.

Guidelines:
- Explain financial concepts clearly and in plain, accessible language — avoid unnecessary jargon
- When jargon is needed, always define it immediately
- Be warm, encouraging, and non-judgmental — many users are beginners
- Use real-world examples and analogies to illustrate concepts
- Break down complex topics into digestible steps or bullet points when helpful
- Always remind users you provide financial education, not personal financial advice
- If asked about specific investment picks or regulated financial decisions, explain you can educate but recommend consulting a licensed financial advisor
- Keep responses concise but complete — aim for clarity over comprehensiveness
- Use occasional emojis to keep the tone approachable (but not excessive)
- Celebrate users' efforts to learn about finance`;

const messages = [];
let isLoading = false;

function getTime() {
  return new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
}

function autoResize(el) {
  el.style.height = 'auto';
  el.style.height = Math.min(el.scrollHeight, 100) + 'px';
}

function handleKey(e) {
  if (e.key === 'Enter' && !e.shiftKey) {
    e.preventDefault();
    sendMessage();
  }
}

function sendQuick(text) {
  document.getElementById('chatInput').value = text;
  sendMessage();
}

function startTopic(topic) {
  document.getElementById('chat').scrollIntoView({ behavior: 'smooth' });
  setTimeout(() => {
    document.getElementById('chatInput').value = topic;
    sendMessage();
  }, 600);
}

function appendMessage(role, text) {
  const container = document.getElementById('chatMessages');
  const div = document.createElement('div');
  div.className = `cm ${role}`;
  const initials = role === 'bot' ? 'FW' : 'You';
  div.innerHTML = `
    <div class="cm-avatar">${initials}</div>
    <div class="cm-content">
      <div class="cm-bubble">${escapeHtml(text)}</div>
      <div class="cm-time">${getTime()}</div>
    </div>
  `;
  container.appendChild(div);
  container.scrollTop = container.scrollHeight;
  return div;
}

function showTyping() {
  const container = document.getElementById('chatMessages');
  const div = document.createElement('div');
  div.className = 'cm bot';
  div.id = 'typingIndicator';
  div.innerHTML = `
    <div class="cm-avatar">FW</div>
    <div class="cm-content">
      <div class="typing-indicator">
        <div class="typing-dot"></div>
        <div class="typing-dot"></div>
        <div class="typing-dot"></div>
      </div>
    </div>
  `;
  container.appendChild(div);
  container.scrollTop = container.scrollHeight;
}

function hideTyping() {
  const t = document.getElementById('typingIndicator');
  if (t) t.remove();
}

function escapeHtml(text) {
  return text
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/\n/g, '<br>');
}

async function sendMessage() {
  if (isLoading) return;
  const input = document.getElementById('chatInput');
  const text = input.value.trim();
  if (!text) return;

  input.value = '';
  input.style.height = 'auto';
  isLoading = true;
  document.getElementById('sendBtn').disabled = true;

  appendMessage('user', text);
  messages.push({ role: 'user', content: text });

  showTyping();

  try {
    const response = await fetch('https://api.anthropic.com/v1/messages', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        model: 'claude-sonnet-4-20250514',
        max_tokens: 1000,
        system: SYSTEM_PROMPT,
        messages: messages
      })
    });

    const data = await response.json();
    hideTyping();

    if (data.content && data.content[0]) {
      const reply = data.content[0].text;
      messages.push({ role: 'assistant', content: reply });
      appendMessage('bot', reply);
    } else {
      appendMessage('bot', "Sorry, I couldn't process that. Please try again.");
    }
  } catch (err) {
    hideTyping();
    appendMessage('bot', "I'm having trouble connecting right now. Please check your connection and try again.");
    console.error(err);
  } finally {
    isLoading = false;
    document.getElementById('sendBtn').disabled = false;
    input.focus();
  }
}
</script>
</body>
</html>
