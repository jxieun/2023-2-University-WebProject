import os
import re

def fix_index_html():
    path = 'index.html'
    if not os.path.exists(path): return
    with open(path, 'r', encoding='utf-8') as f: content = f.read()

    # Update links to new locations
    content = content.replace('href="./pages/genre.html"', 'href="./pages/genre/index.html"')
    content = content.replace('href="./pages/theme.html"', 'href="./pages/theme/index.html"')
    content = content.replace('href="./pages/IN.html"', 'href="./pages/new/domestic.html"')
    content = content.replace('href="./pages/OUT.html"', 'href="./pages/new/overseas.html"')
    content = content.replace('href="./pages/Re.html"', 'href="./pages/recommend/index.html"')
    content = content.replace('href="./pages/Top10.html"', 'href="./pages/recommend/top10.html"')
    content = content.replace('href="./pages/Today.html"', 'href="./pages/recommend/today.html"')
    content = content.replace('href="./pages/vote.html"', 'href="./pages/vote/index.html"')
    
    with open(path, 'w', encoding='utf-8') as f: f.write(content)
    print(f"Updated {path}")

def fix_subpages():
    # Walk through all pages in subdirectories
    for root, dirs, files in os.walk('pages'):
        for filename in files:
            if not filename.endswith('.html'): continue
            
            path = os.path.join(root, filename)
            with open(path, 'r', encoding='utf-8') as f: content = f.read()
            original_content = content
            
            # 1. Fix CSS/JS paths (now 2 levels deep)
            content = content.replace('../css/style.css', '../../css/style.css')
            
            # 2. Fix Image paths
            # ../assets/images/... -> ../../assets/images/...
            content = content.replace('../assets/images/', '../../assets/images/')
            
            # 3. Fix Navigation Links (sibling to sibling or parent)
            mapping = {
                '../index.html': '../../index.html',
                '../pages/genre.html': '../genre/index.html',
                '../pages/theme.html': '../theme/index.html',
                '../pages/IN.html': '../new/domestic.html',
                '../pages/OUT.html': '../new/overseas.html',
                '../pages/Re.html': '../recommend/index.html',
                '../pages/Top10.html': '../recommend/top10.html',
                '../pages/Today.html': '../recommend/today.html',
                '../pages/vote.html': '../vote/index.html',
                '../pages/Introduce.html': '../about/Introduce.html',
                
                './IN.html': '../new/domestic.html',
                './OUT.html': '../new/overseas.html',
                './Re.html': '../recommend/index.html',
                './Top10.html': '../recommend/top10.html',
                './Today.html': '../recommend/today.html',
                './vote.html': '../vote/index.html',
                './Introduce.html': '../about/Introduce.html',
                './genre.html': '../genre/index.html',
                './theme.html': '../theme/index.html',
                'genre.html': '../genre/index.html',
                'theme.html': '../theme/index.html'
            }
            
            for old, new in mapping.items():
                content = content.replace(f'href="{old}"', f'href="{new}"')
                content = content.replace(f"href='{old}'", f"href='{new}'")

             # Fix specific image issues
            def replace_bg(match):
                url = match.group(1)
                if url.startswith('http') or url.startswith('..') or '/' in url:
                    return match.group(0)
                return f'url(\'../../assets/images/pages/{url}\')'
            
            content = re.sub(r'url\(\'([^\']+)\'\)', replace_bg, content)

            if content != original_content:
                with open(path, 'w', encoding='utf-8') as f: f.write(content)
                print(f"Updated {path}")

if __name__ == '__main__':
    fix_index_html()
    fix_subpages()
