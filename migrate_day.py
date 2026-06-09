import os
import shutil

base_dir = r"c:\Users\Venkatesh\Desktop\MalliNeni"
day6_dir = os.path.join(base_dir, "Day6")
day7_dir = os.path.join(base_dir, "Day7")

if os.path.exists(day7_dir):
    shutil.rmtree(day7_dir)

if os.path.exists(day6_dir):
    os.rename(day6_dir, day7_dir)

# Now iterate and rename files + contents
for root, dirs, files in os.walk(day7_dir):
    for filename in files:
        old_path = os.path.join(root, filename)
        new_filename = filename.replace("Day6", "Day7")
        new_path = os.path.join(root, new_filename)
        
        # Rename file if needed
        if old_path != new_path:
            os.rename(old_path, new_path)
            
        # Read and replace contents
        try:
            with open(new_path, "r", encoding="utf-8") as f:
                content = f.read()
            
            content = content.replace("Day 6", "Day 7")
            content = content.replace("Day6", "Day7")
            
            # For the blog navigation back to Day 6
            if new_filename == "blog.html":
                content = content.replace("../Day5/blog.html", "../Day6/blog.html")
                content = content.replace("Back to Day 5", "Back to Day 6")
                
            with open(new_path, "w", encoding="utf-8") as f:
                f.write(content)
        except Exception as e:
            print(f"Failed to process {new_filename}: {e}")

print("Migration to Day 7 complete.")
