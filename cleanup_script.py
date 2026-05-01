import os
import shutil
import hashlib
from collections import defaultdict

root_dir = r'c:\Users\USER\Desktop\자료 지식화 에이전트 핵두뇌'
skip_dirs = {'.git', '.github', '.gemini'}

def get_hash(filepath):
    hasher = hashlib.md5()
    try:
        with open(filepath, 'rb') as f:
            buf = f.read(65536)
            while buf:
                hasher.update(buf)
                buf = f.read(65536)
        return hasher.hexdigest()
    except Exception:
        return None

def merge_dir_recursive(src, dst):
    if not os.path.exists(dst):
        shutil.move(src, dst)
        return
    for item in os.listdir(src):
        s_path = os.path.join(src, item)
        t_path = os.path.join(dst, item)
        if os.path.isdir(s_path):
            merge_dir_recursive(s_path, t_path)
            try:
                os.rmdir(s_path)
            except OSError:
                pass
        else:
            if os.path.exists(t_path):
                h_s = get_hash(s_path)
                h_t = get_hash(t_path)
                if h_s == h_t:
                    os.remove(s_path)
                else:
                    base, ext = os.path.splitext(item)
                    counter = 1
                    while os.path.exists(t_path):
                        t_path = os.path.join(dst, f"{base}_dup{counter}{ext}")
                        counter += 1
                    shutil.move(s_path, t_path)
            else:
                shutil.move(s_path, t_path)

def merge_directories():
    while True:
        dirs_by_name = defaultdict(list)
        for dirpath, dirnames, filenames in os.walk(root_dir):
            if any(skip in dirpath.split(os.sep) for skip in skip_dirs):
                continue
            if dirpath == root_dir:
                continue
            name = os.path.basename(dirpath)
            dirs_by_name[name].append(dirpath)
        
        merged_any = False
        for name, paths in dirs_by_name.items():
            if len(paths) > 1:
                paths.sort(key=lambda p: p.count(os.sep))
                target_dir = paths[0]
                source_dirs = paths[1:]
                
                for source_dir in source_dirs:
                    if not os.path.exists(source_dir): continue
                    if target_dir.startswith(source_dir + os.sep): continue
                    print(f"Merging {source_dir} -> {target_dir}")
                    merge_dir_recursive(source_dir, target_dir)
                    try:
                        os.rmdir(source_dir)
                    except OSError:
                        pass
                    merged_any = True
                
                if merged_any:
                    break
        if not merged_any:
            break

def deduplicate_files():
    files_by_hash = defaultdict(list)
    for dirpath, dirnames, filenames in os.walk(root_dir):
        if any(skip in dirpath.split(os.sep) for skip in skip_dirs):
            continue
        for f in filenames:
            fp = os.path.join(dirpath, f)
            h = get_hash(fp)
            if h:
                files_by_hash[h].append(fp)
                
    for h, paths in files_by_hash.items():
        if len(paths) > 1:
            paths.sort(key=lambda p: p.count(os.sep))
            keep_file = paths[0]
            remove_files = paths[1:]
            for rf in remove_files:
                print(f"Removing duplicate file: {rf}")
                try:
                    os.remove(rf)
                except Exception as e:
                    print(f"Failed to remove {rf}: {e}")

print("Starting directory merge...")
merge_directories()
print("Starting file deduplication...")
deduplicate_files()
print("Done.")
