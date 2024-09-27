<a herf =  https://www.markdownguide.org/basic-syntax/ > MarkDown Basic-Syntax link </a>

# Header Level 1

Header Level 1
==========



## Header Level 2

Header Level 3 （Actually 2） 
-------------   


### Header Level 3



###### Header Level 6

### Header Leve 3 -- Paragraph/Line Breaks

* Let's test for non-\<p> and \<p> 
    * Paragraph - \<p>
        <p> This is a test </p>
        <p> This is a test for two lines 
        codes showing in same line </p>
    * Line Breaks - \<br>
        <p> This is a test for two lines<br>codes showing in same line </p>


### Header Leve 3 -- Bold Italic

* **bold**, __bold__
    * Love**is**bold
    * html stype -- <strong>bold</strong>

* *italic*, _italic_
    * love*is*italic
    * html stype -- <em>italic</em>

* ***Bold and Italic***, ___Bold and Italic___;
    *  You will be able to use the *&_ combinaitons to make it bold and italic;<br> and the order to the symbol should be in reverse order. 
    * But if you want to use HTML stype, remember the \<em> and \<strong> shall be closed in reverse order.  

### Header Level 3 -- BlockQuotes

> Blockquotes

> Blockquotes Line 1 

> Blockquotes Line 2

> Blockquotes Blocks
>
> Blockquotes Finishes

> Blockquotes Nested inside a Blockquotes
>
>> Blockquote inside Nested.
>>>Blockquote Finishes.
>
>> test
> 
> End

### Header Level 3 -- Blockquotes with elements

> # Line 1
> ## Line 2
> ### Line 3
> #### Line 4
> ##### Line 5
>
> - adding a dot
> - adding another dot
> 
> Elements adding with **bold** and *italic* 



### Headler Level 3 -- LISTs

#### Headler Leve 4 - order list

*  Markdown Style 
    > the number does not have to be in numerical order 
1. first
2. second
3. third
1. Fourth  - render in 4
1. Fifth   - render in 5
    1. second first
    1. second Second

<br>

* HTML style
<ol>
<li>First</li>
    <li>Second</li>
    <li>Third</li>
    <ol>
        <li>second first</li>
        <li>second Second</li>
    </ol>
    <li>Fourth</li>
    <li>a</li>
</ol>

#### Headler Leve 4 - unordered list

##### MD style
* First
- Second
+ Third -- Avoid un-comsistancy of the symbol
    - Indented 1
    - Indented 2
    - Indented 3 

##### HTML style

<ul>  
  <li>First item</li>
  <li>Second item</li>
  <li>Third item
    <ul>
      <li>Indented item</li>
      <li>Indented item</li>
    </ul>
  </li>
  <li>Fourth item</li>
</ul>


#### Headler Leve 4 - unordered list starting with number 

- 1.  is a great year
- 2.  number become i ii/1 2
- 2\.  "2\\." will singal \ before . will shows as character, instead of Order number or symbol. 

"""<br>
\#
with backslash, the number is a number<br>\# without the backslash, the number is Order List<br>
"""


#### Headler Leve 4 - Adding Elements in Lists


+ first item without elements
+ second item with elements but not interrupt Order lists, by using a tab or four space in line after next line.

    Paragraphs: Knowledge 1- Adding a elements with one tab
    > Blockquotes: Knowledge 2- Adding a blockquotes

+ third item with elements with two tabs, github will shows a copy button, which is a Knowledge 3 -  **CODE Blocks**. 

        - Adding a elements with two tabs
        - Adding another one
        <html>
        </html>

    * Adding a mark

            <html>
            </html>

    * Knowledge 4 - Adding a image

        <div style="text-align: center;">
            <img src = "/Pics/image-1.png" alt="Tux" width = 350 Height = '400'>
        </dev>
    

+ fourth one to finish this test 


#### Headler Leve 4 - Code

Use   `Backticks` to denote a coding.

<code>Use html language "\<code>" to conduct the same function</code>

![alt text](/Pics/image-2.png#pic_center=400x)




