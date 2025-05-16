# Hello Mom!!!!!!!!

This is a Readme.  It's the documentation for a repository.

## Explanation

This repo is for all the projects mom asks me to work on for Basic Skills.  Currently there are two:

- **PER**: Landing page with PER forms for each grade.  PER forms tally up the inputed scores and allows the user to print, save, and score more.
    - Exacutable: `/PER/dist/PER_Script.exe`
- **ReportGenerator**: Generates a formatted report based on inputted values.  Incomplete.
    - Exacutable: `/ReportGenerator/scriptForInstaller.exe`

## Usage
The actual script that contains all the logic for these projects is in a .py file, but I am bundling everything up into an exacutable so your computer does not need to have anything extra isntalled (python, libraries, etc).

**To run one of these projects all you need is the executable file, and you can just double click to run it**.

## Development

### Updating Exacutable
```
pyinstaller -F --paths=C:\Users\ginny\Documents\BasicSkillsWork\BasicSkills\...\  yourprogram.py
```
`-F` : condenses everything into single executable file \
`-paths` : location you want it to land


