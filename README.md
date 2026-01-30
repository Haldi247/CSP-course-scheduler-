# IBA Course Scheduling System

A backend scheduling engine built for IBA students to generate clash-free timetables based on their course selections and preferences.

## Overview

This project was developed as part of the Introduction to Artificial Intelligence course. It uses a **Constraint Satisfaction Problem (CSP)** approach with backtracking to find valid schedules that satisfy both hard and soft constraints.

## How It Works

### The Problem
Students need to select multiple courses, each with several available sections (different teachers, timings, days). Some courses also have mandatory lab components. The goal is to find a combination of sections that:
- Never clash in timing
- Respect teacher preferences
- Align with preferred days and time slots when possible

### CSP Formulation

| CSP Component | Mapping |
|---------------|---------|
| **Variables** | Courses the student wants to take |
| **Domains** | All available sections for each course (theory + lab pairs) |
| **Constraints** | Timing conflicts, teacher preferences |

### Constraint Types

**Hard Constraints** (must be satisfied):
- No two classes can overlap in time on the same day
- Lab sessions cannot conflict with any theory class

**Soft Constraints** (optimized via domain ordering):
- Teacher preference — prioritized sections taught by preferred instructors
- Day preference — sections on preferred days ranked higher
- Time preference — sections within preferred time windows ranked higher

### Custom Data Structure

Each course maps to a list of `(theory, lab)` tuples where:

```
theory / lab = (course_name, teacher, (day1, day2), start_time, end_time, section_code)
```

Courses without labs have `lab = None`.

This structure allows the CSP solver to treat each theory-lab pairing as a single assignable unit, ensuring that when a theory section is selected, its corresponding lab is automatically included.

### Algorithm

1. **Domain Filtering** — Remove sections not taught by any preferred teacher
2. **Domain Reordering** — Sort remaining options by soft constraint satisfaction (time → day → lab time → lab day)
3. **Backtracking Search** — Assign courses one by one, checking clash constraints at each step
4. **Conflict Detection** — Binary constraints check all pairwise timing overlaps (theory-theory, theory-lab, lab-lab)

