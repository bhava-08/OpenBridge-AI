# OpenBridge AI - Problem Analyzer

def analyze_problem(problem):
    problem_lower = problem.lower()

    skills = []

    if "crop" in problem_lower or "disease" in problem_lower:
        skills += ["Machine Learning", "Computer Vision", "Agriculture"]

    if "app" in problem_lower or "website" in problem_lower:
        skills += ["Python", "Web Development"]

    if "sensor" in problem_lower or "iot" in problem_lower:
        skills += ["IoT", "Arduino"]

    if "ai" in problem_lower or "machine learning" in problem_lower:
        skills += ["Python", "Machine Learning"]

    # Remove duplicate skills
    skills = list(dict.fromkeys(skills))

    if "crop" in problem_lower or "farmer" in problem_lower:
        category = "Agriculture"
    elif "hospital" in problem_lower or "health" in problem_lower:
        category = "Healthcare"
    else:
        category = "General"

    return {
        "category": category,
        "required_skills": skills
    }


# Test the program
problem = input("Enter your problem: ")

result = analyze_problem(problem)

print("\n--- AI Analysis ---")
print("Category:", result["category"])
print("Required Skills:")

for skill in result["required_skills"]:
    print("-", skill)
    # Match contributors with required skills

from contributors import contributors

print("\n--- Recommended Contributors ---")

for person in contributors:
    matched_skills = set(result["required_skills"]) & set(person["skills"])

    if matched_skills:
        score = len(matched_skills)

        print("\nName:", person["name"])
        print("Matching Skills:", ", ".join(matched_skills))
        print("Match Score:", score)