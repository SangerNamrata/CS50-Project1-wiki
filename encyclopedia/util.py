import re

from django.core.files.base import ContentFile
from django.core.files.storage import default_storage


def list_entries():
    """
    Returns a list of all names of encyclopedia entries.
    """
    _, filenames = default_storage.listdir("entries")
    return list(sorted(re.sub(r"\.md$", "", filename)
                for filename in filenames if filename.endswith(".md")))
    

def save_entry(title, content):
    """
    Saves an encyclopedia entry, given its title and Markdown
    content. If an existing entry with the same title already exists,
    it is replaced.
    """
    filename = f"entries/{title}.md"
    if default_storage.exists(filename):
        return False
    else:
        default_storage.delete(filename)
    default_storage.save(filename, ContentFile(content))


def get_entry(title):
    """
    Retrieves an encyclopedia entry by its title. If no such
    entry exists, the function returns None.
    """
    try:
        f = default_storage.open(f"entries/{title}.md")
        return f.read().decode("utf-8")
    except FileNotFoundError:
        return False

def sub_entries(stringname):
    """
    Returns a list of names of sub string entries.
    """
    filename = []
    _, filenames = default_storage.listdir("entries")
    for stringlist in filenames:
        if stringlist.find(stringname) >  -1:
            filename.append(stringlist) 
    return list(sorted(re.sub(r"\.md$", "", files)
        for files in filename if files.endswith(".md")))

def modify(title,content):
    filename = f"entries/{title}.md"
    default_storage.delete(filename)
    default_storage.save(filename, ContentFile(content))
    return True