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


        <div style="text-align: right;">

        <img src = "/Pics/image-1.png" alt="Tux" width = 350 Height = '400'>
        
        </dev>
    

+ fourth one to finish this test 


### Headler Leve 3 - Code

1. Backticks - denote a word

    - Use   `Backticks` to denote a coding.

    - <code>Use html language "\<code>" to conduct the same function</code>

        ![alt text](/Pics/image-2.png#pic_center=400x)


2. Escaping Backticks - decode word in a code
    
    - double ``
    
        `To `demo` effect of double backticks`


### Headler Leve 3 - Horizontal Rules

1. Three * / - / _ 

    *** 
    ---
    ___

        Code for above phenomenon:

        ***
        ---
        ___

    it will turns out to be a seperate line

### Headler Leve 3 - Links

1. #### brackets

    This is an example for using **LINKS** [BOCHK Website](https://www.bochk.com)

        [BOCHK Website](https://www.bochk.com)

2. #### Angle brackets - URL and email address

    <fake@example.local><br>
    <https://www.google.com>

        <fake@example.local><br>
        <https://www.google.com>


3. #### Formatting Links

    combine usage of 
    - BOLD |** ** |  
    - ITALIC |* *| 
    - CODE | `  ` | , etc. 

        I love supporting the **[EFF](https://eff.org)**.
            
            I love supporting the **[EFF](https://eff.org)**.

4. #### Reference-style Links

    Format：
        
    + part that keep inline
    + part that stored swh in file to keep it easy to ready 

    #####  4-1 Formatting the first part and second part


    [bochk official website][1]

    [1]: https://www.bock.com

         [bochk official website][1]

         [1]: https://www.bock.com
    
    * First \[ ]
        
        the name showing for link

    * Second \[ ]

        - label to point to the link stored already 

        - the label in branket, followed by colon and at lease one space. 

        - url can be enclosed in Angel Brackets. 

                [2]: <https://www.bock.com>

        - Optional title for the link, use quote/double quote/ branket.

                [3]: <https://www.google.com> "GOOGLE title" 

            [Test GOOGLE Title][3]
             
            [3]: <https://www.google.com> "BOCHK title" 

            ![alt text](/Pics/image-URL-title.png)


    ##### Better way to combind two parts

    - Method 1 [LINK](<www.example.com> "www.example.com")

    - Method 2 [LINK][4]

        [4]:(www.example.com)

             - Method 1 [LINK](<www.example.com> "www.example.com")

             - Method 2 [LINK][4]

                [4]:(www.example.com)
    
*  Above two methods will have the same output.
*  Adding "www.example.com" will be shown up when you move cursor on the LINK.
*  \<a herf="www.example.com">link\</a> can also  be used.
    
    - %28 - (
    - %29 - )
    - %20 - space
            
            [a novel](https://en.wikipedia.org/wiki/The_Milagro_Beanfield_War_%28novel%29)


### Headler Leve 3 - Image

#### Adding Image

Example:
        
        ![The San Juan Mountains are beautiful!](/assets/images/san-juan-mountains.jpg "San Juan Mountains")

* Markdown does not allow spefify size or captions.
* Use HTML to resize and captions.

        <figure>
            <img src="/assets/images/albuquerque.jpg"
         alt="Albuquerque, New Mexico">
            <figcaption>A single track trail outside of Albuquerque, New Mexico.</figcaption>
        </figure>

#### Adding link to iamge

Example:

* \[ ]( ) to include \!\[ ]( )

    To insert a pic, and give it a link. 
    

        [![An old rock in the desert](/assets/images/shiprock.jpg "Shiprock, New Mexico by Beau Rogers")](https://www.flickr.com/photos/beaurogers/31833779864/in/photolist-Qv3rFw-34mt9F-a9Cmfy-5Ha3Zi-9msKdv-o3hgjr-hWpUte-4WMsJ1-KUQ8N-deshUb-vssBD-6CQci6-8AFCiD-zsJWT-nNfsgB-dPDwZJ-bn9JGn-5HtSXY-6CUhAL-a4UTXB-ugPum-KUPSo-fBLNm-6CUmpy-4WMsc9-8a7D3T-83KJev-6CQ2bK-nNusHJ-a78rQH-nw3NvT-7aq2qf-8wwBso-3nNceh-ugSKP-4mh4kh-bbeeqH-a7biME-q3PtTf-brFpgb-cg38zw-bXMZc-nJPELD-f58Lmo-bXMYG-bz8AAi-bxNtNT-bXMYi-bXMY6-bXMYv)
   


### Headler Leve 3 - Escaping characters

| Syntax | Description | 
|---|-------------|
| \      | Backslash   |
|`| Backticks [Escaping Backticks in code](https://www.markdownguide.org/basic-syntax/#escaping-backticks)|
| *	| asterisk
| _	| underscore
| { }	| curly braces
| [ ]	| brackets
| < >	| angle brackets
| ( )	| parentheses
| #	| pound sign
| +	| plus sign
| -	| minus sign (hyphen)
| .	| dot
| !	| exclamation mark
| |	| pipe (see also escaping pipe in tables)







