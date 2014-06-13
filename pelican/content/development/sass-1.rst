=================================================================
Taking stylesheets to school with Sass, Compass and Susy (Part 1)
=================================================================

:date: 2013-05-14


At work our development teams strive to be more efficient and develop in a way that lets us scale as needed while not coding ourselves into a corner when a client's needs change and grow. Implementing the fantastic creative we receive from our design and user experience experts must be done with a solid foundation of markup and stylesheets.

----------------------------
Part 1: The problem with CSS
----------------------------
Any web developer understands the power and frustration of stylesheets. Ever since browsers adopted CSS, web developers have been bringing more design elements into websites. One of the greatest benefits of stylesheets is keeping all your site styles in one location. But there's a problem with stylesheets. CSS has a terrible syntax for selector hierarchy, making it difficult to manage when you have a lot of styles.

Why not use presentational class names?
---------------------------------------
I know some will say, "You're doing it wrong if your selectors are too long. Use presentational class names. Just make a bunch of classes for each of the common design aspects (for example, font color, font size, background color, borders) and just slap them on your markup element whenever you need them.”

So let's follow that solution through. If we have a common font color of green in a number of places and we make a common class style called ".green-font,” we can put this class name on all the elements on the site that need a green font. So far, so good. Then we get an email from the creative team stating that the client wants to change the font color to blue. OK. We change the "color” attribute to blue in our CSS, but our class name is still ".green-font.” So we can either leave the class name as is and confuse ourselves later when we try to find that blue font color, or we can change the class name and go through all of our markup and replace the "green-font” with the new "blue-font” class. I think we'd rather avoid that potential problem.

One solution is to use more abstract classes, such as "loud-text,” but we'll still run into a problem of really cluttered class attributes on our elements:

.. code-block:: html

    <div class="loud-text border1 background-dark body-font">

This can quickly get unmanageable, especially when you're dealing with multiple nested templates in a CMS. This is why presentational class names should be avoided. This also goes for traditional CSS frameworks (for example, Blueprint and Skeleton). Put simply, your markup should not mention your design aspects, only the semantics of your content. For tips on creating semantic markup see http://css-tricks.com/semantic-class-names/.

Use the right tool for the job
------------------------------
There's a practice going on in web development of using almost nothing but DIV and SPAN as elements (tags) in markup. While they have their place in our tool box, these elements should be used if nothing else seems to apply. I've seen code that doesn't use any header tags (H1, H2, H3, etc.). The heading copy was wrapped in DIVs and styled to look like headings. I understand that a developer may be trying to avoid the variance in default browser styles, but this fails in many situations, including search engine optimization (SEO) and accessibility. Sometimes we miss out on the additional markup elements such as EM, STRONG, CODE, CITE, DL/DT/DD, etc. And that's only HTML4. HTML5 gives us many extra elements to structure our markup. Used appropriately, these can actually make your markup more understandable. It's a good practice to occasionally disable stylesheets in your browser while you're developing and see if the page looks properly structured. To review all of the new elements in HTML5, see `here <http://dev.w3.org/html5/html4-differences/#new-elements>`__ and `here <http://joshduck.com/periodic-table.html>`__.

Lastly, you shouldn't put a class or ID on an element unless you need to. Developers sometimes forget that you can style elements without an ID or class. I understand that you need to differentiate the same element when it's used in different contexts, but you can use far fewer class attributes by referencing a parent element class to determine your context.

But what about the other problems with CSS?
-------------------------------------------
Ok, so we understand the reasons to use semantic markup, but we still have to deal with the shortfalls of CSS:

*	Long and repetitive selectors
*	No way to reuse colors and sizes (i.e., no variables)
*	No arithmetic operators
*	No reusable functions for common design tasks

What we need is a CSS scripting language to handle all of these shortcomings — some sort of **S**\ yntactically **A**\ wesome **S**\ tyle\ **S**\ heet language. Hmm...

`Continue to Part 2 <{filename}sass-2.rst>`_
