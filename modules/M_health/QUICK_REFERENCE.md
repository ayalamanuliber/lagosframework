# Quick Reference Guide

## Daily Targets 🎯
### Nutrition
- Protein: 140-150g
- Calories: 2300-2500 (training) / 2100-2300 (rest)
- Water: 2.5-3L
- Caffeine: 90min post-wake

### Training
- Upper body focus (3x/week)
- Soccer (1x/week)
- Track all sets/reps/weights
- Log energy levels

### Health Practices
- Morning sunlight
- Oil pulling
- No-rinse brushing
- Skin care routine

## Red Flags 🚨
### Nutrition
- Protein < 140g
- Water < 2L
- Fats > 35%
- Late caffeine

### Training
- Form issues
- Persistent fatigue
- Joint pain
- Missing logs

### Health
- Sleep issues
- Skin problems
- Oral health decline
- Energy drops

## Quick Fixes 🔧
### Low Energy
1. Check water intake
2. Review last meal
3. Assess sleep quality
4. Consider rest day

### Missed Targets
1. Protein shake
2. Extra water
3. Adjust next meal
4. Log for patterns

### Recovery Needs
1. NSDR session
2. Extra hydration
3. Light mobility work
4. Sleep optimization

## System Commands
### Health Module Commands

#### [HEALTH_UPDATE]
Triggers when adding daily logs or updates. This command will:
1. Generate visual graphs for the daily log
2. Update PROGRESS_TRACKER.md with latest metrics
3. Check for alerts (missing data, targets not met)
4. Update weekly and monthly summaries
5. Generate health insights based on patterns

Usage:
```markdown
[HEALTH_UPDATE]
<your daily log content>
[END_UPDATE]
```

#### [HEALTH_REVIEW]
Triggers a comprehensive health review. This command will:
1. Generate weekly/monthly progress graphs
2. Compare against set goals
3. Identify trends and patterns
4. Provide recommendations
5. Update long-term tracking metrics

Usage:
```markdown
[HEALTH_REVIEW]
period: weekly | monthly
focus: nutrition | training | all
[END_REVIEW]
```

#### [HEALTH_ALERT]
Quick check of health metrics against targets. Use this for rapid feedback.

Usage:
```markdown
[HEALTH_ALERT]
metrics: protein,water,steps
[END_ALERT]
```

## Interactive Commands
### Interactive Prompts

#### [LOG_DAY]
Start an interactive logging session. I'll prompt you for:
1. Daily vitals (weight, sleep, energy, stress)
2. Meals and nutrition
3. Training details
4. Recovery metrics
5. Notes and observations

Usage:
```markdown
[LOG_DAY]
Just tell me what you did today, I'll organize it and prompt for any missing info!
[END_LOG]
```

Example:
```markdown
User: [LOG_DAY]
"Had eggs for breakfast, then hit the gym for push day. Did some coding, had chicken for lunch. Went out for ribs at night."
```

## File Locations 📁
- Daily Protocol: `/protocols/DAILY_PROTOCOL.md`
- Progress Tracker: `/tracking/progress/PROGRESS_TRACKER.md`
- Workout Library: `/library/workouts/WORKOUT_LIBRARY.md`
- Knowledge Base: `/knowledge/raw/`

## Emergency Protocols 🆘
### Energy Crash
1. Hydrate immediately
2. Light protein/carb snack
3. 10min movement
4. Reassess in 30min

### Recovery Issues
1. Extra rest day
2. Increase protein
3. Sleep focus
4. Log symptoms

_Update this reference weekly based on Progress Tracker insights_
