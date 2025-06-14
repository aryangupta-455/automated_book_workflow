
def get_human_feedback(original, spun, reviewed):
    print("\n========== ORIGINAL (First 500 characters) ==========")
    print(original[:500], "\n")

    print("========== SPUN VERSION (First 500 characters) ==========")
    print(spun[:500], "\n")

    print("========== REVIEWED VERSION (First 500 characters) ==========")
    print(reviewed[:500], "\n")

    choice = input("Do you want to [a]ccept reviewed, [e]dit manually? (a/e): ").strip().lower()

    if choice == "e":
        print("\nEnter your edited version (press CTRL+D or CTRL+Z when done):")
        import sys
        edited_text = sys.stdin.read()
        return edited_text.strip()

    print("Accepted reviewed version.")
    return reviewed
