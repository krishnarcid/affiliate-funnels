# HEARTBEAT.md - Daily Automation Tasks
# SOURCE OF TRUTH: PORTFOLIO.md (Read first, execute second)

## 🕐 When This Runs
- **Frequency:** Every 30 minutes during work hours (9 AM - 6 PM IST)
- **Trigger:** System heartbeat
- **Action:** Read PORTFOLIO.md → Execute tasks below

---

## 📋 Daily Tasks (In Priority Order)

### 1. Authority Engine (9:00 AM) - PRIMARY
- [ ] Run `python authority-engine-v4.py`
- [ ] Generate 5 LinkedIn blogs + 10 social posts
- [ ] Generate 15 visual assets (isometric 3D + glass-morphism)
- [ ] Deploy via browser (LinkedIn + X, 45-min spacing)
- [ ] Update PORTFOLIO.md status → "DEPLOYED"
- [ ] Log to logs/daily-output.txt

### 2. SDR Hunter (Every 2 hours) - PROSPECTING
- [ ] Search LinkedIn for SaaS/Coaching prospects
- [ ] Search Twitter for tool cost complaints  
- [ ] Search Google Maps for local businesses
- [ ] Audit 5 landing pages (Your Copy Sucks protocol)
- [ ] Reply to 5 complaints (Sacredbod protocol)
- [ ] Update LEADS.md in real-time
- [ ] Send 5 audit emails via Gmail

### 3. Social Media Posting (10:00 AM - 4:30 PM)
- [ ] Post generated content to LinkedIn
- [ ] Post generated content to X/Twitter (3 posts)
- [ ] Check Tally dashboard: https://tally.so
- [ ] Note new email captures
- [ ] Record in memory/today-leads.md
- **Action:** If leads > 0, alert user

### 4. Affiliate Dashboard Check (5:00 PM)
- [ ] Check GoHighLevel affiliate dashboard for clicks
- [ ] Check Systeme.io affiliate dashboard
- [ ] Record any conversions
- **Action:** If conversions > 0, celebrate and notify

### 5. Semrush Status Check (Once daily, 3:00 PM)
- [ ] Check email for Semrush approval
- [ ] If approved, update PORTFOLIO.md (Pending → Active)
- [ ] Deploy Semrush funnel to sacredbod.in/semrush/
- **Status:** ⏳ Currently waiting

---

## 📊 Status Tracking

| Task | Last Run | Status | Next Run |
|------|----------|--------|----------|
| Sales Engine | 2026-03-13 16:11 | ✅ DONE | Tomorrow 9:00 AM |
| LinkedIn Post | 2026-03-13 14:35 | ✅ DONE | Tomorrow 10:00 AM |
| X/Twitter Post | 2026-03-13 14:47 | ✅ DONE | Tomorrow 2:00 PM |
| Lead Check | - | ⏳ PENDING | Today 4:00 PM |
| Semrush Status | - | ⏳ PENDING | Today 3:00 PM |

---

## 🔄 Content Rotation

**Current Rotation:**
- Day 1: GoHighLevel
- Day 2: Systeme.io
- Day 3: GoHighLevel
- Day 4: Systeme.io
- (Repeat)

**Tomorrow (2026-03-14):** Systeme.io

---

## 🎯 Key Metrics to Track

| Metric | Target | Current | Status |
|--------|--------|---------|--------|
| Daily Posts | 2 (LI + X) | 2 today | ✅ |
| Weekly Leads | 10 | 0 | ⏳ |
| First Sale | 1 | 0 | ⏳ |
| Monthly Revenue | $500 | $0 | ⏳ |

---

## 🚨 Alert Conditions

**Notify immediately if:**
- ✅ New lead captured (Tally notification)
- ✅ Affiliate sale made (check dashboards)
- ✅ Semrush approval received
- ⚠️ X/Twitter API credits depleted
- ⚠️ Any funnel goes down (404 error)
- ⚠️ GitHub sync fails

---

## 📝 Quick Commands

```bash
# Run sales engine manually
python sales-engine-v2.py

# Check git status
git status

# Deploy latest changes
git add . && git commit -m "Update" && git push

# Check logs
type logs\today-brief.txt
```

---

## 📁 File Locations

| File | Purpose | Path |
|------|---------|------|
| PORTFOLIO.md | Master checklist | C:\Users\krish\.openclaw\workspace\ |
| sales-engine-v2.py | Content generator | affiliate-funnels\ |
| MEMORY.md | Long-term memory | C:\Users\krish\.openclaw\workspace\ |
| logs/ | Daily outputs | affiliate-funnels\logs\ |

---

## 💡 Reminders

- **Small batches:** Complete end-to-end before starting new project
- **Daily focus:** One funnel promoted per day
- **Track everything:** Log all actions in memory files
- **Autonomous:** Run without asking, report results

---

Last updated: 2026-03-13 16:15 IST
Next review: Tomorrow 9:00 AM
