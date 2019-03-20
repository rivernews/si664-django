# Development Diary

## Goal: no vertical duplication

Referring to [instructional document](https://www.dj4e.com/assn/dj4e_model.md).

- What we have in csv file:

`✅name,✅description,✅justification,✅year,✅longitude,✅latitude,✅area_hectares,✅category,✅states,✅region,✅iso`

*`iso` means ISO country code. E.g., country: Algeria, ISO country code: dz.
*`justification` - justification to become a world heritage?
*`state` is actually country.

```
Site
---
name
year
description
justification
longitude
latitude
area_hectares
category >-
state >-

Category
---
name

State
---
name
iso
region >-

Region
---
name

```

## Data Model

- [x] After we designed our schema, it's time to implement `models.py`. 🔥🔥🔥

- [ ] When finish the data model, `makemigration` and `migrate`.

## Read CSV File

- [ ] The instructor uses Python's CSV module, but pandas is more powerful.
- Data sanitizing: develop a policy.
    - [ ] Check format, e.g. year complies integer format. If not, drop such that database will store as `null`.

## Load in database

- [ ] The script: either use a plain python file, or use Django's script integrated with `./manage.py` (recommended).
- [ ] Make the script wipe out database everytime it is load, better for debugging.
- Big idea: flat data --> structured data.
    - [ ] You'll probably read in row by row using a for loop. Then, write to the database, considering foreign key relationships. 
    - (The instruction has an example using `Membership`, but that's likely because a Many to Many field is used. If we're not using that, we probably don't need `Membership`)
- [ ] Run and fix the script until the result looks correct.
- Additional tooling - if you need to check out database manually, you can use sqlite cli tools, as described in instruction.

## You are very close: upload your database `sqlite` to autograder

The autograder only looks at the database. Make sure this final outcome is right.