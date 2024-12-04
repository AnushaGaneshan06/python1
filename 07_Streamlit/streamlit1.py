# STREAMLIT - OPEN SOURCE APP FRAME WORK INTERACTIVE WEB APPLICATION

# EVERY TEXT IN SREAMLIT IS PRE-FORMATTED

import streamlit as st


# ===========================================================🔅HEADER==========================================================

#  Streamlit, you can emphasize text using Markdown formatting within the st.markdown() or st.write() functions. Here are ways to add emphasis:

# =============================================================================================================================

st.title("-----------***Text***-------------")
st.markdown('''
# h1
## h2
### h3
#### h4
###### h5
''')

# ALTERNATIVE WAY FOR H1 AND H2 ANS UNDERLINE-ISH STYLE

st.markdown('''
header1
======
header2
-------
            ''')

st.markdown('''
#### EMPASIS
**asterisks** <br>
*italic text*<br>
***Bold and italic***<br>
<span style="background-color:yellow;color:black;">Highlighted text and color emphasis</span><br>
This is `inline code or monospace`<br>
~~Scratch this~~
<u>The text is underscored</u>

''', unsafe_allow_html= True)


# ======================================================LIST IN STREAMLIT=====================================================

st.title("-----------***List***-------------")

st.markdown('''
#### Ordered list
1. First item
2. Second item
    1. Sub item 1
    2. Sub item 2
3. Third item
''')

st.markdown('''
#### UnOrdered list
- First item
- Second item
    -Sub-item 1
    -Sub-item 2
* Third item
    * sub-item 3
    * sub-item 4
''')

st.markdown('''
#### Mixed list Example
1. First ordered item
    - unordered item 1
    * unordered item 2
2. Second ordered item
    - unordered sub item 3
3. Third ordered item
    * undordered list item 4
    - undordered list item 5
    + undordered list item 6
''')

# =======================================================LINKS IN STREAMLIT =================================================
st.title("-----------***Links***-------------")

st.markdown('''
1. An **inline-style** link uses square brackets for the link text and parentheses for the URL. Optionally, you can add a title in quotes after the URL.
            
    [I'm an inline-style link](https://www.google.com)
''')

st.markdown('''
2. Inline-style Link with Title Shows the hover word over link<br>
[I'm an inline-style link with title](https://www.google.com "Google's Homepage")
''', True )

st.markdown('''
3. Reference-style Link
A reference-style link allows you to define a link reference separately, making it easier to reuse the same URL throughout the document.

    [I'm reference link] [1]
''')
st.markdown('''
    [1]: https://www.mozilla.org
''')

st.markdown('''
4. Relative Reference to a Repository File
You can use relative URLs to link to files within a repository (for example, in GitHub).
            
    [I'm a relative refernce to a resitory file](../blob/master/LICENSE)

''')

st.markdown('''
5. Link Text Itself
You can also use the link text directly in the document without a defined reference.
            
    [link text itself](https://www.google.com)

''')

st.markdown('''
6. normal link. 
            
    https://www.google.com

''')








st.title("Hello Streamlit !!!")

st.header("Header")

st.subheader("Sub header")

st.text("I can do it !!!!!😊😊")

st.markdown(""" # h1 tag
## h2 tag
### h3 tag
:moon:<br>
:sunglasses:
**bold **
            """ ,True) # true make br work


st.latex(r''' \[
\begin{align*}
F(x) &= \int_{a}^{b} \left[ \frac{\partial}{\partial x} \Big( e^{x^2} \sin(x) \Big) + \sqrt{\frac{1}{x^2 + 1}} \right] dx \\
&
''')

st.write("harsh", "gupta", "liina")

st.write(st) # pass the basic documents

st.write(sum) # use of sum


# dictionary
d = {
    "name" : "leena",
    "langiage" : "python",
    "topic" : "streamlit"
}
st.write(d)