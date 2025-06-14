from dotenv import load_dotenv
from storage.chroma_store import save_version
import os

load_dotenv()

from agents.writer import spin_text
from agents.reviewer import review_text
from human_interface.editor import get_human_feedback


with open("chapter1.txt", "r", encoding="utf-8") as f:
    original = f.read()


spun = spin_text(original)
reviewed = review_text(spun)


final = get_human_feedback(original, spun, reviewed)


with open("final_version.txt", "w", encoding="utf-8") as f:
    f.write(final)


save_version("chapter1_original", original, {"type": "original", "chapter": 1})
save_version("chapter1_spun", spun, {"type": "spun", "chapter": 1})
save_version("chapter1_reviewed", reviewed, {"type": "reviewed", "chapter": 1})
save_version("chapter1_final", final, {"type": "final", "chapter": 1})
