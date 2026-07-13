import re

print("===== Example 1: Case-Sensitive Matching =====")
regex = re.compile(r"RoboCop")

print(regex.search("RoboCop"))
print(regex.search("robocop"))
print(regex.search("ROBOCOP"))

print("\n===== Example 2: Case-Insensitive Matching =====")
robocop = re.compile(r"robocop", re.I)

print(robocop.search("RoboCop is part man, part machine, all cop.").group())
print(robocop.search("ROBOCOP protects the innocent.").group())
print(robocop.search("I like robocop movies.").group())

print("\n===== Example 3: String Substitution =====")
namesRegex = re.compile(r"Agent \w+")

text = "Agent Alice gave the secret documents to Agent Bob."

result = namesRegex.sub("CENSORED", text)

print("Original:", text)
print("Modified:", result)

print("\n===== Example 4: Using Groups in sub() =====")
agentNamesRegex = re.compile(r"Agent (\w)\w*")

text = (
    "Agent Alice told Agent Carol that Agent Eve knew "
    "Agent Bob was a double agent."
)

result = agentNamesRegex.sub(r"\1****", text)

print("Original:", text)
print("Modified:", result)