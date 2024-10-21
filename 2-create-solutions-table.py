import os
import pathlib
import re


def extract_difficulty(filename):
    parts = filename.split("-")
    if parts and parts[0].lower() in ["easy", "medium", "hard"]:
        return parts[0].capitalize()
    return "Unknown"


def extract_number(filename):
    match = re.search(r"-(\d+)-", filename)
    if match:
        return match.group(1)
    return "N/A"


def clean_filename(filename):
    parts = filename.split("-")
    if len(parts) > 2:
        return "-".join(parts[2:])
    return filename


def generate_markdown_table(directory):
    # Get all files in the directory
    files = [
        f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))
    ]

    # Sort files based on the extracted number
    files.sort(
        key=lambda f: (
            int(extract_number(f)) if extract_number(f).isdigit() else float("inf")
        )
    )

    # Start the markdown content
    markdown_content = "# Solutions\n\n"
    markdown_content += "| Sr. No. | Type | Difficulty | File Name |\n"
    markdown_content += "|---------|------|------------|-----------|\n"

    # Add each file to the table
    for file in files:
        file_path = os.path.join(directory, file)
        file_type = pathlib.Path(file).suffix.lower()

        if file_type == ".py":
            file_type = "Python"
        elif file_type == ".sql":
            file_type = "SQL"
        else:
            file_type = "Unknown"

        difficulty = extract_difficulty(file)
        sr_no = extract_number(file)
        clean_name = clean_filename(file)

        markdown_content += (
            f"| {sr_no} | {file_type} | {difficulty} | [{clean_name}]({file_path}) |\n"
        )

    return markdown_content


def update_readme(solutions_table_content):
    readme_path = "README.md"
    start_marker = "<!-- START_SOLUTIONS_TABLE -->"
    end_marker = "<!-- END_SOLUTIONS_TABLE -->"

    with open(readme_path, "r", encoding="utf-8") as f:
        readme_content = f.read()

    # Find the section to replace
    start_index = readme_content.find(start_marker)
    end_index = readme_content.find(end_marker)

    if start_index != -1 and end_index != -1:
        # Replace the content between markers
        updated_content = (
            readme_content[: start_index + len(start_marker)]
            + "\n"
            + solutions_table_content
            + "\n"
            + readme_content[end_index:]
        )

        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(updated_content)
        print("README.md has been updated with the latest solutions table.")
    else:
        print(
            "Markers not found in README.md. Please add the markers to your README.md file."
        )


# Specify the directory path
solutions_directory = "Solutions"

# Generate the markdown content
markdown_table = generate_markdown_table(solutions_directory)


# Write the markdown content to a file
with open("solutions_table.md", "w") as f:
    f.write(markdown_table)

print("Markdown file 'solutions_table.md' has been created.")

# Update README.md with the new table
update_readme(markdown_table)


print("README.md has been updated with the latest solutions table.")
