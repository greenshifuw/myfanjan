import glob
import os

def update_text():
    files_fr = glob.glob('*.html')
    files_en = glob.glob('en/*.html')
    
    # FR Replacements
    old_fr = "une marque de NEOPHYTA"
    new_fr = "est une marque déposée par la société NEOPHYTA"
    
    # EN Replacements
    old_en = "a brand of NEOPHYTA"
    # "is a registered trademark of NEOPHYTA" seems appropriate translation
    new_en = "is a registered trademark of NEOPHYTA"
    
    print("Updating FR Files...")
    for filepath in files_fr:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if old_fr in content:
            new_content = content.replace(old_fr, new_fr)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {filepath}")
        else:
            print(f"Skipped {filepath} (text not found)")

    print("Updating EN Files...")
    for filepath in files_en:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if old_en in content:
            new_content = content.replace(old_en, new_en)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {filepath}")
        else:
            print(f"Skipped {filepath} (text not found)")

if __name__ == "__main__":
    update_text()
