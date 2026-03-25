import re

def analyze_code(code, language="python"):
    issues = []
    suggestions = []
    score = 10

    # Nested loops
    nested_loops = len(re.findall(r'for .*:\n\s+for ', code))
    if nested_loops > 0:
        issues.append("Nested loops detected → may lead to O(n²) complexity")
        suggestions.append("Consider using optimized data structures like hash maps")
        score -= 2

    # Split lines (we'll reuse this)
    lines = code.split('\n')

    # Long code
    if len(lines) > 50:
        issues.append("Code length is too long")
        suggestions.append("Break code into smaller functions")
        score -= 1

    # Unused variables
    variables = re.findall(r'(\w+)\s*=', code)
    for var in variables:
        if code.count(var) == 1:
            issues.append(f"Unused variable: {var}")
            suggestions.append(f"Remove unused variable '{var}' to clean code")
            score -= 1

    # Duplicate lines
    if len(lines) != len(set(lines)):
        issues.append("Duplicate lines found")
        suggestions.append("Avoid repeating code — use functions or loops")
        score -= 1

    # 🔥 NEW: Java semicolon check
    if language == "java":
        for i, line in enumerate(lines):
            line = line.strip()
            if line.startswith("//") or line.startswith("/*") or line.startswith("*"):
               continue

            if (
                line
                and not line.endswith(";")
                and "{" not in line
                and "}" not in line
                and not line.startswith("if")
                and not line.startswith("for")
                and not line.startswith("while")
                and not line.startswith("public")
                and not line.startswith("class")
            ):
                issues.append(f"Possible missing semicolon at line {i+1}")
                suggestions.append("Check statement termination with ';'")
                score -= 1

    score = max(score, 1)
    
    
    explanation = "This code has "

    if issues:
       explanation += f"{len(issues)} issue(s). "
    else:
       explanation += "no major issues. "

    if "Nested loops" in " ".join(issues):
       explanation += "Nested loops may increase time complexity."

    if "Unused variable" in " ".join(issues):
       explanation += "Unused variables reduce code clarity."

    
    
    

    return {
        "score": score,
        "issues": issues or ["No major issues ✅"],
        "suggestions": suggestions or ["Wohoo ,Code looks good 👍"],
        "explanation": explanation
        
    }
    