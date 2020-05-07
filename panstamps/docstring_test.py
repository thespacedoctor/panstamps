"""
*Testing the rendering of docstings - feel free to remove this module*

Check the API output here: file:///Users/Dave/git_repos/_templates_/python-package-template/panstamps/docs/build/html/_api/panstamps.docstring_test.html
"""


def docsting_test(self):
    """
    *the database object for sherlock, setting up ssh tunnels and various database connections*

    The returned dictionary of database connections contain the following databases:

        - ``transients`` -- the database hosting the transient source data
        - ``catalogues`` -- connection to the database hosting the contextual catalogues the transients are to be crossmatched against
        - ``marshall`` -- connection to the PESSTO Marshall database

    **Key Arguments:**
        - ``log`` -- logger
        - ``settings`` -- the settings dictionary

    **Return:**
        - ``dbConns`` -- a dictionary of the database connections required by sherlock

    **Usage:**

        To setup the sherlock database connections, run the following:

        .. code-block:: python 

            # SETUP ALL DATABASE CONNECTIONS
            from sherlock import database
            db = database(
                log=log,
                settings=settings
            )
            dbConns, dbVersions = db.connect()
            transientsDbConn = dbConns["transients"]
            cataloguesDbConn = dbConns["catalogues"]
            pmDbConn = dbConns["marshall"]

    .. todo ::

        - update key arguments values and definitions with defaults
        - update return values and definitions
        - update usage examples and text
        - update docstring text
        - check sublime snippet exists
        - clip any useful text to docs mindmap
        - regenerate the docs and check redendering of this docstring


    **Embed reStructuredText**

    ```eval_rst
    .. todo::

        - nice!
    ```

    **Code and Syntax Highlighting**

    Inline `code` has `back-ticks around` it.

    ```javascript
    var s = "JavaScript syntax highlighting";
    alert(s);
    ```

    ```python
    s = "Python syntax highlighting"
    print(s)
    myString = "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
    ```

    ```
    No language indicated, so no syntax highlighting. 
    But let's throw in a <b>tag</b>.
    ```

    **Mermaid**

    ```mermaid
    gantt
            dateFormat  YYYY-MM-DD
            title Adding GANTT diagram functionality to mermaid
            section A section
            Completed task            :done,    des1, 2014-01-06,2014-01-08
            Active task               :active,  des2, 2014-01-09, 3d
            Future task               :         des3, after des2, 5d
            Future task2               :         des4, after des3, 5d
            section Critical tasks
            Completed task in the critical line :crit, done, 2014-01-06,24h
            Implement parser and jison          :crit, done, after des1, 2d
            Create tests for parser             :crit, active, 3d
            Future task in critical line        :crit, 5d
            Create tests for renderer           :2d
            Add to mermaid                      :1d
    ```

    **Flowchart**

    ```flow
    s=>start: start
    e=>end: end
    o=>operation: operation
    sr=>subroutine: subroutine
    c=>condition: condition
    i=>inputoutput: inputoutput
    p=>parallel: parallel

    s->o->c
    c(yes)->i->e
    c(no)->p
    p(path1, bottom)->sr(right)->o
    p(path2, top)->o
    ```

    **Tables**

    Colons can be used to align columns.

    | Tables        | Are           | Cool  |
    | ------------- |:-------------:| -----:|
    | col 3 is      | right-aligned | $1600 |
    | col 2 is      | centered      |   $12 |
    | zebra stripes | are neat      |    $1 |

    **Definitions**

    term
    : definition

    what
        Definition lists associate a term with a definition.

    **Math**

    A formula, ${e}^{i\pi }+1=0$, inside a paragraph.

    $${e}^{i\pi }+1=0$$

    **Super/Sub Scripts**

    m^2

    x^2,y^

    x~z

    C~6~H~12~O~6


    **Citations**

    Cite a source.[p. 42][#source]

    [#source]: John Doe. *A Totally Fake Book*. Vanity Press, 2006.

    Black (2015)[#Black:2015tz]

    [#Black:2015tz]: A Bryden Black 2015, *The Lion, the Dove, & the Lamb*, Wipf and Stock Publishers

    **Task Lists**

    - [x] Completed task item
    - [ ] Unfinished task item

    **Footnote**

    Here's a sentence with a footnote[^1] in the middle of it!

    [^1]: This is the footnote.

    **Emphasis**

    Emphasis, aka italics, with *asterisks* 

    Strong emphasis, aka bold, with **asterisks**.

    Strikethrough ~~deleted~~.

    **Lists**


    1. First ordered list item
    2. Another item
        * Unordered sub-list. 
    1. Actual numbers don't matter, just that it's a number
        1. Ordered sub-list
    4. And another item.

        You can have properly indented paragraphs within list items.   

    and unordered lists:

    * Unordered list can use asterisks
    - Or minuses
    + Or pluses

    **Links**

    [I'm an inline-style link](https://www.google.com)

    **Images**

    Here's our logo (hover to see the title text):

    Inline-style: 
    ![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1")

    Reference-style: 
    ![alt text][logo]

    [logo]: https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 2"

    **Blockquotes**

    > Blockquotes are very handy in email to emulate reply text.
    > This line is part of the same quote.

    Quote break.

    > This is a very long line that will still be quoted properly when it wraps. Oh boy let's keep writing to make sure this is long enough to actually wrap for everyone. Oh, you can *put* **Markdown** into a blockquote. 

    **Abbreviations**

    The HTML specification is maintained by the W3C.

    *[HTML]: Hyper Text Markup Language
    *[W3C]:  World Wide Web Consortium


    **Horizontal Rule**

    Three or more...

    ---

    Hyphens
    """
    import os
    rootPath = os.path.dirname(__file__)

    return rootPath
