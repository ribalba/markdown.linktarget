"""Adds a taget="_blank" attribute to HTML links in Markdown

This extension adds a taget="_blank" attribute to the HTML output when links are parsed from markdown. 
It is not added if the href starts with a # so 
"""
from markdown.treeprocessors import Treeprocessor
from markdown.extensions import Extension


class TargetLinkTreeprocessor(Treeprocessor):

    def set_link_target(self, element):
        for child in element:
            if child.tag == "a" and "href" in child.keys():
                if not child.get("href").strip().startswith("#"):
                    child.set("target", "_blank")
            self.set_link_target(child)


    def run(self, root):
        return self.set_link_target(root)


class TargetLinkExtension(Extension):
    def extendMarkdown(self, md, md_globals):
        md.treeprocessors['targetLink'] = TargetLinkTreeprocessor(md)


def makeExtension(configs=None):
    return TargetLinkExtension(configs=configs)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
