markdown.linktarget
==================

Adds a taget="_blank" attribute to HTML links in Markdown

This extension adds a taget="_blank" attribute to the HTML output when links are parsed from markdown. 
It is not added if the href starts with a # so 

    [link](#something) 
    
will not be touched. Whereas:

    [link_text](url) will become <p><a href="url" target="_blank">link_text</a><

Install through pip:

    $ pip install MarkdownLinkTaget
    
To enable the MarkdownLinkTaget package and use it in your markdown generation just add it like so:

    import markdown
    from MarkdownLinkTaget.linktarget import TargetLinkExtension
    
    result = markdown.markdown(textToRender, extensions=[TargetLinkExtension,]))

