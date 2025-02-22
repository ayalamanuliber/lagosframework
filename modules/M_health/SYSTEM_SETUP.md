# Health System Structure 🏗️

## Directory Organization

```
modules/health/
├── plans/                  # All core plans in one place
│   ├── WORKOUT_PLAN.md    # Current workout routine
│   ├── NUTRITION_PLAN.md  # Meal planning & macros
│   └── RECOVERY_PLAN.md   # Sleep & recovery protocols
│
├── tracking/              # Daily operations
│   ├── YYYY/             # Year-specific logs
│   │   ├── daily/        # Daily entries
│   │   ├── weekly/       # Weekly summaries
│   │   └── quarterly/    # Quarterly reviews
│   └── templates/        # Log templates
│       ├── WORKOUT_DAY.md  # Training day template
│       └── REST_DAY.md     # Recovery day template
│
├── profiles/             # Personal data
│   └── HEALTH_PROFILE.md # Combined profile
│
└── reference/           # Knowledge base
    └── QUICK_GUIDE.md   # Quick reference
```

## Key Files & Usage

### Core Plans (Your Go-To Files)
- `plans/WORKOUT_PLAN.md`: Current training program
- `plans/NUTRITION_PLAN.md`: Diet & meal strategies
- `plans/RECOVERY_PLAN.md`: Sleep & recovery protocols

### Daily Operations
- `tracking/templates/WORKOUT_DAY.md`: Training day logs
- `tracking/templates/REST_DAY.md`: Recovery day logs
- `tracking/YYYY/daily/`: Your daily entries

### Reference
- `profiles/HEALTH_PROFILE.md`: Your complete profile
- `reference/QUICK_GUIDE.md`: Essential info & protocols

## Best Practices

### Daily Workflow
1. Open `plans/` for your current plans
2. Use appropriate template (workout/rest)
3. Track in `tracking/YYYY/daily/`
4. Weekly review on Sundays

### File Naming
- Daily: `YYYY_MM_DD.md`
- Weekly: `WEEK_XX.md`
- Quarterly: `QX_YYYY.md`

## Quick Links
- [Current Workout Plan](plans/WORKOUT_PLAN.md)
- [Nutrition Plan](plans/NUTRITION_PLAN.md)
- [Workout Template](tracking/templates/WORKOUT_DAY.md)
- [Rest Template](tracking/templates/REST_DAY.md)
