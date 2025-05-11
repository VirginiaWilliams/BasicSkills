# Hello Mom!!!!!!!!

This is a Readme.  It's the documentation for a repository.

## Explanation

This repo is for all the projects mom asks me to work on for Basic Skills.  Currently there are two:

- **PER**: Landing page with PER forms for each grade.  PER forms tally up the inputed scores and allows the user to print, save, and score more.
    - Exacutable: `/PER/dist/PER_Script.exe`
- **ReportGenerator**: Generates a formatted report based on inputted values.  Incomplete.
    - Exacutable: `ReportGenerator/scriptForInstaller.exe`

## Usage
To run one of these programs all you need to do is run (double click) the executable file in the appropriate folder.

## Development

### Updating Exacutable
```
pyinstaller -F --paths=C:\Users\ginny\Documents\BasicSkillsWork\BasicSkills\...\  yourprogram.py
```
`-F` : condenses everything into single executable file \
`-paths` : location you want it to land


