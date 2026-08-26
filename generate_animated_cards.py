import os

def create_top_langs_svg(file_path):
    svg_content = """<svg xmlns="http://www.w3.org/2000/svg" width="400" height="230" viewBox="0 0 400 230" fill="none">
  <defs>
    <linearGradient id="card-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0B0F19"/>
      <stop offset="100%" stop-color="#05070C"/>
    </linearGradient>
    <linearGradient id="card-border" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#00F0FF" stop-opacity="0.6"/>
      <stop offset="50%" stop-color="#7000FF" stop-opacity="0.3"/>
      <stop offset="100%" stop-color="#FF007A" stop-opacity="0.6"/>
    </linearGradient>
    <linearGradient id="header-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00F0FF"/>
      <stop offset="100%" stop-color="#7000FF"/>
    </linearGradient>
    <linearGradient id="python-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#3776AB"/>
      <stop offset="100%" stop-color="#00F0FF"/>
    </linearGradient>
    <linearGradient id="php-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#777BB4"/>
      <stop offset="100%" stop-color="#A855F7"/>
    </linearGradient>
    <linearGradient id="js-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#F7DF1E"/>
      <stop offset="100%" stop-color="#FF9900"/>
    </linearGradient>
    <linearGradient id="html-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#E34F26"/>
      <stop offset="100%" stop-color="#FF6D5A"/>
    </linearGradient>
    <linearGradient id="ts-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#3178C6"/>
      <stop offset="100%" stop-color="#00F0FF"/>
    </linearGradient>
    <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="4" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
  </defs>

  <style>
    .header { font: 700 18px 'Inter', -apple-system, sans-serif; fill: url(#header-grad); letter-spacing: 0.5px; }
    .subtitle { font: 500 11px 'Inter', -apple-system, sans-serif; fill: #64748B; }
    .lang-name { font: 600 13px 'Inter', -apple-system, sans-serif; fill: #F1F5F9; }
    .lang-percent { font: 500 13px 'Inter', -apple-system, sans-serif; fill: #94A3B8; }
  </style>

  <!-- Base Card background -->
  <rect width="398" height="228" x="1" y="1" rx="14" fill="url(#card-bg)" stroke="url(#card-border)" stroke-width="1.5"/>

  <!-- Header -->
  <g transform="translate(24, 34)">
    <text class="header">Most Used Languages</text>
    <text y="18" class="subtitle">Based on GitHub repository breakdown</text>
  </g>

  <!-- Stacked Progress Bar -->
  <g transform="translate(24, 75)">
    <rect x="0" y="0" width="352" height="12" rx="6" fill="#1E293B"/>
    <!-- Python 45.2% -> 159.1px -->
    <rect x="0" y="0" width="159.1" height="12" rx="6" fill="url(#python-grad)"/>
    <!-- PHP 28.6% -> 100.6px -->
    <rect x="156.1" y="0" width="103.6" height="12" fill="url(#php-grad)"/>
    <!-- JS 14.8% -> 52.1px -->
    <rect x="256.7" y="0" width="55.1" height="12" fill="url(#js-grad)"/>
    <!-- HTML/CSS 7.4% -> 26.0px -->
    <rect x="308.8" y="0" width="29.0" height="12" fill="url(#html-grad)"/>
    <!-- TS 4.0% -> 14.1px -->
    <rect x="334.8" y="0" width="17.2" height="12" rx="6" fill="url(#ts-grad)"/>
  </g>

  <!-- Legend Grid -->
  <g transform="translate(24, 118)">
    <!-- Column 1 -->
    <g transform="translate(0, 0)">
      <circle cx="6" cy="6" r="6" fill="url(#python-grad)"/>
      <text x="20" y="10" class="lang-name">Python</text>
      <text x="120" y="10" class="lang-percent">45.2%</text>
    </g>
    <g transform="translate(0, 32)">
      <circle cx="6" cy="6" r="6" fill="url(#php-grad)"/>
      <text x="20" y="10" class="lang-name">PHP</text>
      <text x="120" y="10" class="lang-percent">28.6%</text>
    </g>
    <g transform="translate(0, 64)">
      <circle cx="6" cy="6" r="6" fill="url(#js-grad)"/>
      <text x="20" y="10" class="lang-name">JavaScript</text>
      <text x="120" y="10" class="lang-percent">14.8%</text>
    </g>

    <!-- Column 2 -->
    <g transform="translate(180, 0)">
      <circle cx="6" cy="6" r="6" fill="url(#html-grad)"/>
      <text x="20" y="10" class="lang-name">HTML/CSS</text>
      <text x="120" y="10" class="lang-percent">7.4%</text>
    </g>
    <g transform="translate(180, 32)">
      <circle cx="6" cy="6" r="6" fill="url(#ts-grad)"/>
      <text x="20" y="10" class="lang-name">TypeScript</text>
      <text x="120" y="10" class="lang-percent">4.0%</text>
    </g>
  </g>
</svg>"""
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(svg_content)
    print(f"Updated {file_path}")

def create_github_stats_svg(file_path):
    svg_content = """<svg xmlns="http://www.w3.org/2000/svg" width="500" height="230" viewBox="0 0 500 230" fill="none">
  <defs>
    <linearGradient id="card-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0B0F19"/>
      <stop offset="100%" stop-color="#05070C"/>
    </linearGradient>
    <linearGradient id="card-border" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#00F0FF" stop-opacity="0.6"/>
      <stop offset="50%" stop-color="#7000FF" stop-opacity="0.3"/>
      <stop offset="100%" stop-color="#FF007A" stop-opacity="0.6"/>
    </linearGradient>
    <linearGradient id="header-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00F0FF"/>
      <stop offset="100%" stop-color="#7000FF"/>
    </linearGradient>
    <linearGradient id="rank-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#00F0FF"/>
      <stop offset="100%" stop-color="#FF007A"/>
    </linearGradient>
    <filter id="glow-icon" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="2" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
  </defs>

  <style>
    .header { font: 700 18px 'Inter', -apple-system, sans-serif; fill: url(#header-grad); letter-spacing: 0.5px; }
    .subtitle { font: 500 11px 'Inter', -apple-system, sans-serif; fill: #64748B; }
    .stat-label { font: 500 13px 'Inter', -apple-system, sans-serif; fill: #94A3B8; }
    .stat-value { font: 700 14px 'Inter', -apple-system, sans-serif; fill: #00F0FF; }
    .icon { fill: #00F0FF; filter: url(#glow-icon); }
    .rank-text { font: 800 32px 'Inter', -apple-system, sans-serif; fill: url(#rank-grad); }
    .rank-label { font: 700 10px 'Inter', -apple-system, sans-serif; fill: #64748B; letter-spacing: 1.5px; }
  </style>

  <!-- Base Card background -->
  <rect width="498" height="228" x="1" y="1" rx="14" fill="url(#card-bg)" stroke="url(#card-border)" stroke-width="1.5"/>

  <!-- Header -->
  <g transform="translate(24, 34)">
    <text class="header">Biswajit's GitHub Overview</text>
    <text y="18" class="subtitle">Verified developer metrics &amp; contribution stats</text>
  </g>

  <!-- Left Stats Column -->
  <g transform="translate(24, 78)">
    <!-- Total Stars -->
    <g transform="translate(0, 0)">
      <path class="icon" d="M8 .25a.75.75 0 01.673.418l1.882 3.815 4.21.612a.75.75 0 01.416 1.279l-3.046 2.97.719 4.192a.75.75 0 01-1.088.791L8 12.347l-3.766 1.98a.75.75 0 01-1.088-.79l.72-4.194L.818 6.374a.75.75 0 01.416-1.28l4.21-.611L7.327.668A.75.75 0 018 .25z"/>
      <text x="26" y="12" class="stat-label">Total Stars:</text>
      <text x="160" y="12" class="stat-value">12</text>
    </g>
    <!-- Total Commits -->
    <g transform="translate(0, 30)">
      <path class="icon" d="M1.75 0A1.75 1.75 0 000 1.75v12.5C0 15.22.78 16 1.75 16h12.5A1.75 1.75 0 0016 14.25V1.75A1.75 1.75 0 0014.25 0H1.75zM1.5 1.75a.25.25 0 01.25-.25h12.5a.25.25 0 01.25.25v12.5a.25.25 0 01-.25.25H1.75a.25.25 0 01-.25-.25V1.75zM11.75 7.5a.75.75 0 000 1.5h.5a.75.75 0 000-1.5h-.5z"/>
      <text x="26" y="12" class="stat-label">Total Commits:</text>
      <text x="160" y="12" class="stat-value">485</text>
    </g>
    <!-- Total PRs -->
    <g transform="translate(0, 60)">
      <path class="icon" d="M7.177 3.073L9.573.677A.25.25 0 0110 .854v4.792a.25.25 0 01-.427.177L7.177 3.427a.25.25 0 010-.354zM3.75 2.5a.75.75 0 100 1.5.75.75 0 000-1.5zm-2.25.75a2.25 2.25 0 113 2.122v5.256a2.251 2.251 0 11-1.5 0V5.372A2.25 2.25 0 011.5 3.25z"/>
      <text x="26" y="12" class="stat-label">Total PRs:</text>
      <text x="160" y="12" class="stat-value">38</text>
    </g>
    <!-- Total Issues -->
    <g transform="translate(0, 90)">
      <path class="icon" d="M8 1.5a6.5 6.5 0 100 13 6.5 6.5 0 000-13zM0 8a8 8 0 1116 0A8 8 0 010 8zm9 3a1 1 0 11-2 0 1 1 0 012 0zm-.25-6.25a.75.75 0 00-1.5 0v3.5a.75.75 0 001.5 0v-3.5z"/>
      <text x="26" y="12" class="stat-label">Total Issues:</text>
      <text x="160" y="12" class="stat-value">14</text>
    </g>
  </g>

  <!-- Right Rank Badge Circle -->
  <g transform="translate(385, 125)">
    <!-- Outer Glow Ring -->
    <circle cx="0" cy="0" r="46" fill="#0F172A" stroke="#1E293B" stroke-width="3"/>
    <circle cx="0" cy="0" r="46" fill="none" stroke="url(#rank-grad)" stroke-width="3.5" stroke-dasharray="289" stroke-dashoffset="35" stroke-linecap="round"/>
    <text x="0" y="8" text-anchor="middle" class="rank-text">A+</text>
    <text x="0" y="26" text-anchor="middle" class="rank-label">OVERALL RANK</text>
  </g>
</svg>"""
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(svg_content)
    print(f"Updated {file_path}")

if __name__ == "__main__":
    os.makedirs("images", exist_ok=True)
    create_top_langs_svg("images/top_langs.svg")
    create_github_stats_svg("images/github_stats.svg")
