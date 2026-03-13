# Windows Task Scheduler Setup

## Daily Automation (No Browser Needed)

This runs the sales engine daily and outputs the content to post.

### Setup Steps:

1. **Open Task Scheduler**
   - Press `Win + R`
   - Type: `taskschd.msc`
   - Press Enter

2. **Create New Task**
   - Click "Create Task" (not "Create Basic Task")
   - Name: `Affiliate Sales Engine`
   - Description: `Daily content generation for affiliate marketing`

3. **Triggers Tab**
   - Click "New"
   - Begin the task: `On a schedule`
   - Settings: `Daily`
   - Start: `2026-03-14 09:00:00` (9 AM)
   - Recur every: `1 days`
   - Click OK

4. **Actions Tab**
   - Click "New"
   - Action: `Start a program`
   - Program/script: `python`
   - Add arguments: `sales-engine-simple.py`
   - Start in: `C:\Users\krish\.openclaw\workspace\affiliate-funnels`
   - Click OK

5. **Conditions Tab**
   - Uncheck: "Start the task only if computer is on AC power"
   - Check: "Wake the computer to run this task" (optional)

6. **Settings Tab**
   - Check: "Allow task to be run on demand"
   - Check: "Run task as soon as possible after a scheduled start is missed"

7. **Click OK**
   - Enter your Windows password if prompted

### Test the Task:

1. Right-click the task → "Run"
2. Check `logs/today-checklist.txt` was created
3. Should see today's content ready to post

### Manual Run:

If Task Scheduler fails, just run manually:
```
cd C:\Users\krish\.openclaw\workspace\affiliate-funnels
python sales-engine-simple.py
```

### Output:

The script generates:
- Daily content for LinkedIn
- Daily content for X/Twitter
- Checklist of actions to complete
- Saved to: `logs/today-checklist.txt`

### Next Steps:

1. **Morning (9 AM):** Run script → Get content
2. **Post to LinkedIn:** 10 AM IST (peak engagement)
3. **Post to X/Twitter:** 2 PM IST (peak engagement)
4. **Check Tally:** https://tally.so for leads
5. **Review:** Affiliate dashboards for clicks

---

## Browser Automation (Optional)

For full automation (posts automatically), you need:
- LinkedIn API access
- X/Twitter API access (limited credits)
- Or browser automation with OpenClaw

Current setup: **Manual posting with generated content** (more reliable)
