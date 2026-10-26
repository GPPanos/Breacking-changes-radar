````markdown
Breaking Changes Radar

 Overview
"Breaking Changes Radar" is an automated static code analysis and developer operations tool. It analyzes Python codebases, Git diffs, ASTs (Abstract Syntax Trees), and API schemas to detect breaking changes (e.g., modified function signatures, deprecated class attributes, breaking REST/Pydantic model changes, altered return types, or deleted public interfaces) before merging or deploying software updates.

Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/your-repo/breaking_changes_radar.git
````

2. Navigate to the project directory:

   ```sh
   cd breaking_changes_radar
   ```

3. Install dependencies:

   ```sh
   python3 -m pip install -r requirements.txt
   ```

Usage

Run the `scan` command to analyze your codebase:

```sh
python3 breaking_changes_radar/cli/main.py scan
```

Contribution Guidelines

1. Fork the repository.
2. Create a new branch for each feature or bug fix.
3. Make your changes and commit them.
4. Push the branch to your forked repository.
5. Open a pull request with a clear description of your changes.


