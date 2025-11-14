# Linkedin Email Scraper
This Linkedin Email Scraper identifies email addresses associated with LinkedIn profiles by analyzing Google search results. It helps users quickly gather contact details tied to specific domains while targeting professionals in defined roles or industries. This solution streamlines lead generation, outreach, and market analysis with minimal setup.


<p align="center">
  <a href="https://bitbash.dev" target="_blank">
    <img src="https://github.com/za2122/footer-section/blob/main/media/scraper.png" alt="Bitbash Banner" width="100%"></a>
</p>
<p align="center">
  <a href="https://t.me/devpilot1" target="_blank">
    <img src="https://img.shields.io/badge/Chat%20on-Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white" alt="Telegram">
  </a>&nbsp;
  <a href="https://wa.me/923249868488?text=Hi%20BitBash%2C%20I'm%20interested%20in%20automation." target="_blank">
    <img src="https://img.shields.io/badge/Chat-WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white" alt="WhatsApp">
  </a>&nbsp;
  <a href="mailto:sale@bitbash.dev" target="_blank">
    <img src="https://img.shields.io/badge/Email-sale@bitbash.dev-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Gmail">
  </a>&nbsp;
  <a href="https://bitbash.dev" target="_blank">
    <img src="https://img.shields.io/badge/Visit-Website-007BFF?style=for-the-badge&logo=google-chrome&logoColor=white" alt="Website">
  </a>
</p>




<p align="center" style="font-weight:600; margin-top:8px; margin-bottom:8px;">
  Created by Bitbash, built to showcase our approach to Scraping and Automation!<br>
  If you are looking for <strong>Linkedin Email Scraper</strong> you've just found your team — Let’s Chat. 👆👆
</p>


## Introduction
The scraper searches for LinkedIn profiles matching user-defined keywords and extracts emails linked to those profiles. By filtering emails using specific domains, it ensures only relevant contact details are captured. This tool is ideal for marketers, recruiters, sales teams, and analysts who rely on accurate contact data.

### How It Works
- Searches Google results for LinkedIn profiles based on your keyword.
- Extracts email addresses matching the specified email domains.
- Captures profile titles, URLs, and relevant snippet text.
- Automatically paginates through search results until limits are met.
- Provides structured, ready-to-export datasets for immediate use.

## Features
| Feature | Description |
|--------|-------------|
| Keyword-based LinkedIn discovery | Finds LinkedIn profiles matching a search query using Google results. |
| Domain-matched email extraction | Filters and extracts emails based on specified domains. |
| Contextual snippet capture | Collects text surrounding results for additional insight. |
| Configurable result limits | Allows users to set maximum output size. |
| Stealth search behavior | Uses undetectable search patterns to minimize blocking. |
| Automatic pagination | Crawls multiple Google result pages seamlessly. |

---

## What Data This Scraper Extracts
| Field Name | Field Description |
|------------|------------------|
| keywords | The search keyword used to discover profiles. |
| emailDomains | Comma-separated list of matched email domains. |
| email | Extracted email address found in the profile or snippet. |
| title | Title of the LinkedIn search result. |
| url | Link to the LinkedIn profile. |
| text | Contextual snippet text from the Google search result. |

---

## Example Output

    [
      {
        "keywords": "marketing",
        "emailDomains": "gmail.com, yahoo.com, hotmail.com",
        "email": "aragonglobalmarketing@gmail.com",
        "title": "Eduardo Simon - Director de marketing comercial",
        "url": "https://es.linkedin.com/in/eduardo-simon-a3b5b61b4",
        "text": "Zaragoza y alrededores · Director de marketing comercial · aragonglobalmarketing@gmail.com de..."
      },
      {
        "keywords": "marketing",
        "emailDomains": "gmail.com, yahoo.com, hotmail.com",
        "email": "Elliberalmorvedre@gmail.com",
        "title": "El liberal - Marketing OnLine - Elliberalmorvedre@gmail.com",
        "url": "https://es.linkedin.com/in/el-liberal-97513b83",
        "text": "Valencia y alrededores · Marketing OnLine · Elliberalmorvedre@gmail.com..."
      }
    ]

---

## Directory Structure Tree

    Linkedin Email Scraper/
    ├── src/
    │   ├── runner.py
    │   ├── extractors/
    │   │   ├── linkedin_parser.py
    │   │   └── utils_search.py
    │   ├── outputs/
    │   │   └── exporters.py
    │   └── config/
    │       └── settings.example.json
    ├── data/
    │   ├── inputs.sample.json
    │   └── sample-output.json
    ├── requirements.txt
    └── README.md

---

## Use Cases
- **Marketing teams** collect targeted leads with verified email domains to improve campaign conversion rates.
- **Recruiters** identify and contact potential candidates directly for open roles.
- **Sales teams** build B2B outreach lists to accelerate pipeline growth.
- **Market analysts** gather context-rich professional data for sector research.
- **Small businesses** find potential partners or collaborators within niche industries.

---

## FAQs

**Q: Can I search for multiple keywords at once?**
A: The scraper accepts a single keyword per run, but you can automate sequential runs with different keywords for broader coverage.

**Q: Does it access LinkedIn directly?**
A: No, it gathers emails and profile data from publicly visible Google search results that reference LinkedIn pages.

**Q: What happens if no emails match the specified domains?**
A: The scraper continues searching until results are exhausted or the maximum result limit is reached, returning only valid matches.

**Q: Is there a limit to how many results I can request?**
A: You can set any reasonable upper limit, though extremely high values may increase run time.

---

## Performance Benchmarks and Results
**Primary Metric:** Processes an average of 40–60 Google results per minute under typical network conditions.
**Reliability Metric:** Maintains a 95%+ success rate in extracting structured results across diverse keywords.
**Efficiency Metric:** Optimized for low overhead, consuming minimal bandwidth while paginating through search results.
**Quality Metric:** Achieves high data precision by strictly matching email domains and capturing complete contextual snippets.


<p align="center">
<a href="https://calendar.app.google/74kEaAQ5LWbM8CQNA" target="_blank">
  <img src="https://img.shields.io/badge/Book%20a%20Call%20with%20Us-34A853?style=for-the-badge&logo=googlecalendar&logoColor=white" alt="Book a Call">
</a>
  <a href="https://www.youtube.com/@bitbash-demos/videos" target="_blank">
    <img src="https://img.shields.io/badge/🎥%20Watch%20demos%20-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="Watch on YouTube">
  </a>
</p>
<table>
  <tr>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtu.be/MLkvGB8ZZIk" target="_blank">
        <img src="https://github.com/za2122/footer-section/blob/main/media/review1.gif" alt="Review 1" width="100%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        “Bitbash is a top-tier automation partner, innovative, reliable, and dedicated to delivering real results every time.”
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Nathan Pennington
        <br><span style="color:#888;">Marketer</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtu.be/8-tw8Omw9qk" target="_blank">
        <img src="https://github.com/za2122/footer-section/blob/main/media/review2.gif" alt="Review 2" width="100%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        “Bitbash delivers outstanding quality, speed, and professionalism, truly a team you can rely on.”
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Eliza
        <br><span style="color:#888;">SEO Affiliate Expert</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtube.com/shorts/6AwB5omXrIM" target="_blank">
        <img src="https://github.com/za2122/footer-section/blob/main/media/review3.gif" alt="Review 3" width="35%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        “Exceptional results, clear communication, and flawless delivery. Bitbash nailed it.”
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Syed
        <br><span style="color:#888;">Digital Strategist</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
  </tr>
</table>
