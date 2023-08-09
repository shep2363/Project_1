import os
import argparse

def create_project_folders(project_names, base_directory="."):
    for project_name in project_names:
        project_directory = os.path.join(base_directory, project_name)
        os.makedirs(project_directory, exist_ok=True)
        print(f"Created folder for project {project_name}: {project_directory}")

def main():
    parser = argparse.ArgumentParser(description="Create folder structure for multiple projects and templates")
    
    parser.add_argument("-p", "--projects", nargs="+", help="List of project names", required=True)
    parser.add_argument("-t", "--templates", nargs="+", help="List of project templates", required=True)
    parser.add_argument("-d", "--directory", help="Base directory for the folder structure", default=".")
    
    args = parser.parse_args()

    # Create project folders
    create_project_folders(args.projects, args.directory)

    # Create project template folders
    create_project_folders(args.templates, args.directory)

if __name__ == "__main__":
    main()

