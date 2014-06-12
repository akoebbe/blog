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
There's a practice going on in web development of using almost nothing but DIV and SPAN as elements (tags) in markup. While they have their place in our tool box, these elements should be used if nothing else seems to apply. I've seen code that doesn't use any header tags (H1, H2, H3, etc.). The heading copy was wrapped in DIVs and styled to look like headings. I understand that a developer may be trying to avoid the variance in default browser styles, but this fails in many situations, including search engine optimization (SEO) and accessibility. Sometimes we miss out on the additional markup elements such as EM, STRONG, CODE, CITE, DL/DT/DD, etc. And that's only HTML4. HTML5 gives us many extra elements to structure our markup. Used appropriately, these can actually make your markup more understandable. It's a good practice to occasionally disable stylesheets in your browser while you're developing and see if the page looks properly structured. To review all of the new elements in HTML5, see:
http://dev.w3.org/html5/html4-differences/#new-elements
http://joshduck.com/periodic-table.html

Lastly, you shouldn't put a class or ID on an element unless you need to. Developers sometimes forget that you can style elements without an ID or class. I understand that you need to differentiate the same element when it's used in different contexts, but you can use far fewer class attributes by referencing a parent element class to determine your context.

But what about the other problems with CSS?
-------------------------------------------
Ok, so we understand the reasons to use sematic markup, but we still have to deal with the shortfalls of CSS:

*	Long and repetitive selectors
*	No way to reuse colors and sizes (i.e., no variables)
*	No arithmetic operators
*	No reusable functions for common design tasks

What we need is a CSS scripting language to handle all of these shortcomings — some sort of Syntactically Awesome Stylesheet language. Hmm …

----------------------------------------------
Part 2: Sass, you had me at "nested selectors”
----------------------------------------------
In the previous article we bemoaned the failures and shortcomings of the CSS syntax. Sass shores up all of those failings and give us the power to logically structure and generate semantic stylesheets.

Sass is a scripting language that processes its own stylesheet syntax into regular CSS files (a CSS pre-processor). This is not done browser-side or server-side. The resulting CSS is compiled on save as you develop.

Before I get in to the details of Sass, there are a number of other CSS pre-processors that are great, such as Stylus (http://learnboost.github.io/stylus/) and Less (http://lesscss.org/). In my opinion, it's a matter of preference, as they can handle nearly all the same functionality and their syntaxes are similarly structured. I personally prefer Sass, but I hold no ill will to those who prefer alternatives.

Sass has two syntaxes to choose from: SCSS and SASS. SCSS looks similar to the syntax of plain CSS and so I recommend that syntax for newcomers. SASS syntax is akin to Ruby or Python's syntax. Switching between the two syntaxes is easy with the "sass-convert” command. So you can start with one syntax and switch whenever you like. In this article, we'll use SCSS syntax for examples.

Sass isn't just for Ruby developers
-----------------------------------

Sass is written in Ruby, but don't freak out if you don't know Ruby. It can stand alone on any project, regardless of your development stack. Sass can be installed on any system with Ruby or you can use one of the GUIs available, which have a self-contained Ruby environment built in (though adding Sass extension Ruby gems can be problematic with the latter).

Nested selectors
----------------
One of the simplest yet most appreciated features of Sass is the ability to nest your styles within other styles.

Sass (SCSS Syntax)

.. code-block:: scss

    article, .post {
      width: 50%;
      .title {
        font-weight: bold;
      }
      .body {
        font-size: .9em;
      }
    }

Compiled CSS

.. code-block:: css

    article, .post {
      width: 50%;
    }
    article .title, .post .title {
      font-weight: bold;
    }
    article .body, .post .body {
      font-size: .9em;
    }

This makes refactoring your class names a piece of cake. Just change the ".post” class selector in one place and you're done. This also makes organizing your styles nearly automatic.

Variables
---------
One of my biggest frustrations with CSS is the lack of variables. Sass provides you with a standard set of variables types: strings, numbers, colors, Booleans and lists — pretty much anything you might need to store when building your styles. Variables are denoted by the prefix of the familiar dollar sign ($) and values are assigned with a colon, just as values are assigned to CSS attributes.

Arithmetic, color functions and parent selectors
------------------------------------------------
We can use the aforementioned variables to hold things such as common colors, lengths and font families, but we can use some built-in Sass functions to gain more flexibility in our styles. There are the basic math functions we're used to (+, -, \*, /, %), which take into account units of measure. But we also have some great color functions such as lighten, darken, saturate, desaturate, adjust-hue, complement and invert. These color functions can make color schemes programmatic rather than a guessing game.

Sass (SCSS syntax)

.. code-block:: scss

    $link-color: #2e6d5a;

    a {
      color: $link-color;
      &:hover {
        color: complement($link-color);
        text-decoration: none;
        background-color: lighten($link-color, 50);
      }
    }

Compiled CSS

.. code-block:: css

    a {
      color: #2e6d5a;
    }
    a:hover {
      color: #6d2e41;
      text-decoration: none;
      background-color: #b9e1d5;
    }

We can change the $link-color variable to another color and the rest of the colors will be recalculated automatically.. In theory you could have Sass build the entire color scheme for your site based on one color variable.

Ok, so what's that ampersand (&) doing there? The ampersand allows you to bring the parent selector into the mix without having to reiterate the parent with a class in another selector. Without the ampersand, the ":hover” pseudo class would only apply to the children of the "a” selector, not the "a” itself. This is not limited to pseudo classes (for example, hover). Any class or ID can be used with an ampersand prefix.

Mixins
------
The most powerful part of Sass is scripting functions, called mixins, that accept parameters and output computed styles or values. These work similarly to functions that we are used to in our front-end or back-end coding languages. First we define a mixin with the "@mixin” directive and then we use the mixin with the "@include” directive.

Sass (SCSS syntax)

.. code-block:: scss

    @mixin big-and-bold($color) {
      font-family: Arial;
      font-size: 36px;
      font-weight: bold;
      color: $color;
      border: 1px solid darken($color, 20);
    }

    h1 {
      @include big-and-bold(#ffee55);
    }

Compiled CSS

.. code-block:: css

    h1 {
      font-family: Arial;
      font-size: 36px;
      font-weight: bold;
      color: #ffee55;
      border: 1px solid #eed600;
    }

If you just want to reuse a block of styles in other selectors (without parameter input), check out the "@extend” directive to bring in another selector's styles.

Pimp your Sass with Compass
---------------------------
With all of these features of Sass (and more), other tools can be built to provide mixins and additional useful functionality to Sass. That's exactly what Compass does. It extends Sass with tons of cross-browser mixins and functions that make styling even easier and more powerful. We'll touch on only a few of my favorite features of Compass.

Cross-browser Mixins
--------------------
The bane of every web developer's existence is dealing with the inconsistencies across browsers. While the worst offender shall remain unnamed, even some of the most standards-compliant browsers have their differences. Compass has a number of mixins meant to ease the coding of certain tasks that tend to need extra help when working in differing browsers. Gradients and shadows are commonly cross-browser incompatible without knowing exactly the right syntax and attributes to use. Compass has mixins for those.

Sass (SCSS syntax)

.. code-block:: scss

    .cool-section {
      @include box-shadow(red 2px 2px 10px);
      @include filter-gradient(white, #aaaaaa);
      @include background-image(linear-gradient(white, #aaaaaa));
    }

Compiled CSS

.. code-block:: css

    .cool-section {
      -webkit-box-shadow: 0px 0px 5px #333333;
      -moz-box-shadow: 0px 0px 5px #333333;
      box-shadow: 0px 0px 5px #333333;
      *zoom: 1;
      filter: progid:DXImageTransform.Microsoft.gradient(gradientType=0, startColorstr='#FFFFFFFF', endColorstr='#FFAAAAAA');
      background-image: -webkit-gradient(linear, 50% 0%, 50% 100%, color-stop(0%, #ffffff), color-stop(100%, #aaaaaa));
      background-image: -webkit-linear-gradient(#ffffff, #aaaaaa);
      background-image: -moz-linear-gradient(#ffffff, #aaaaaa);
      background-image: -o-linear-gradient(#ffffff, #aaaaaa);
      background-image: -ms-linear-gradient(#ffffff, #aaaaaa);
      background-image: linear-gradient(#ffffff, #aaaaaa);
    }

You can see how the Compass mixins can make life a lot easier when dealing with cross-browser development.

Automatic sprites
-----------------
Compass has some magical sprite functions that blew my mind when I first saw them in action. Let's be honest, sprites are great for load times and bandwidth management, but making sprite maps can be a pain, especially if you have to add sprites to your map as you develop. While there are services and applications to help ease the pain, but with Compass you don't even have to think about it. Just throw your new sprite in a directory and Compass does the rest.

Just set up a directory in your images folder to hold your individual sprites. Let's say "danger.png” and "alert.png” are in "images/my-icons.” In your Sass file, import that directory and use the auto-prefixed mixins to bring in each sprite.



Sass (SCSS syntax)

.. code-block:: scss

    @import "my-icons/*.png";

    .warning {
      @include my-icons-sprite('danger');
    }
    .notice {
      @include my-icons-sprite('alert');
    }

Compiled CSS

.. code-block:: css

    .warning, .notice {
      background: url('../../images/my-icons-sb224dcc2e7.png') no-repeat;
    }
    .warning {
      background-position: 0 -56px;
    }
    .notice {
      background-position: 0 0;
    }

Now you have automatic sprite management. Compass creates the sprite map during compilation and keeps track of the location of the sprites on the map. Adding a sprite is easy. Put the new sprite into your sprite directory, add the selector, call the "my-icons-sprite” mixin in your Sass file and you're finished.

These are just two of the many features of Compass. More information can be found at http://compass-style.org/.

Sass and Compass make light work of complex and scalable styles. Wouldn't it be great if there were a way to do the same with responsive design and media queries? Have you met my friend Susy?

--------------------------------------------------------
Part 3: Responsive stylesheets and grid layout with Susy
--------------------------------------------------------
There are a number of widely used CSS grid frameworks. They help keep content aligned and offer standardized units (columns) to size and place your content on the page. These can be great for prototyping, but the downfall of most of these frameworks is the use of presentational class names. And we know that's a no-no.

Responsive design is becoming a common feature of most of our projects as mobile browsing is on its way to surpassing desktop browsing. CSS Media Queries allow different styles to be applied based on different capabilities of the screen displaying the website, though screen width is by far the most common condition. Media queries are great because of what they allow us to do, but they can be unwieldy as well.

Let's say we've got a two-column section of our site that needs to respond to smaller screens by adjusting to a one-column layout. We'd set our "columns” to "50%” and float them. Then we'd create a media query and adjust them.

CSS

.. code-block:: css

    section.overview, section.detail {
      width: 50%;
      float: left;
    }
    @media (min-width: 600px) {
      section.overview, section.detail {
        width: 100%;
        float: none;
      }
    }


This is fine for a handful of layout adjustments, but when you have a large number, you are forced to either have a number of @media statements throughout your code or set up one block of all the adjustments even though they may not be near the original style.

It would be great to harness the power of Sass's nesting and mixin features to make grids and media queries simpler. I've got a friend named Susy that can help with that.

The Susy developers have a great "getting started” guide to show you how to install Susy: http://susy.oddbird.net/guides/getting-started/.

Susy's grid skills
------------------
Susy needs a few variables to get started — things such as how many columns you want to start with and what size and padding those columns should have. Keep in mind that you can use any units of measure for the variables, but make sure you use the same unit of measure for all of Susy's variables. Then we need to set our grid container and the magic begins.

SCSS

.. code-block:: scss

    @import susy;

    $total-columns: 12;           // The number of columns you want
    $column-width: 4em;           // How wide each column should be.
    $gutter-width: 1em;           // Spacing between columns
    $grid-padding: $gutter-width; // Padding on outside the grid

    #page {
      @include container;
    }

Now that we've got Susy started, we can bring our "overview” and "detail” section classes in from the previous example and set them up in Susy.

SCSS

.. code-block:: scss

    section.overview, section.detail {
      @include span-columns(6);
    }
    section.detail {
      @include omega // Omega tells susy this is the last item in the row
    }

Compiled CSS

.. code-block:: css

    section.overview, section.detail {
      width: 49.15254%;
      float: left;
      margin-right: 1.69492%;
      display: inline;
    }

    section.detail {
      float: right;
      margin-right: 0;
      #margin-left: -1em;
      display: inline;
    }

Wait, what's with the percentages? I used "em” as my unit of measure. Susy does the calculations for you and converts the unit to percentages so that your design is fluid. This can be changed with the $container-style variable if you don't want a fluid behavior. You can also see that Susy puts in some cross-browser tweaks to make that unmentionable browser happy.

Susy's responsive skills
------------------------
Now it's time to get responsive. Susy brought a handy at-breakpoint mixin to the party that can be nested in the styles we want to adjust.

SCSS

.. code-block:: scss

    section.overview, section.detail {
      @include span-columns(6);

      // at-breakpoint(<min-width> <layout> <max-width> <ie-fallback>)
      @include at-breakpoint(4 600px) { // Tell susy to switch to a 4 column grid at 600px
        @include span-columns(4 omega);
      }
    }
    section.detail {
      @include omega; // Omega tells susy this is the last item in the row
    }

Compiled CSS

.. code-block:: css

    section.overview, section.detail {
      width: 49.15254%;
      float: left;
      margin-right: 1.69492%;
      display: inline;
    }

    @media (max-width: 600px) {
      section.overview, section.detail {
        width: 100%;
        float: right;
        margin-right: 0;
      }
    }

    section.detail {
      float: right;
      margin-right: 0;
      #margin-left: -1em;
      display: inline;
    }

You can see how easy responsive styles are with the at-breakpoint mixin. Right where you define the default layout you can specify all of your breakpoint changes without leaving the definition of the original style. Of course this mixin can work with any style changes (for example, color, display, font, etc.), not just column spanning.

Susy Next
---------
It's worth noting that Susy is poised to merge with complementary projects to make it even more powerful. The list of developers on board with this initiative is pretty staggering. Great things are in store: http://oddbird.net/2013/01/01/susy-next/.

Sass, Compass and Susy in Drupal
--------------------------------
A large portion of VML projects use Drupal as the CMS. Because Sass is platform-agnostic, we've been able to leverage all of these technologies into the themes of our Drupal projects.

Susy's container-style variable allowed us to set the responsive behavior to a fixed style. The exact width of the container is clearly defined and not fluid. As screens vary slightly, the margin on either side of the page adjusts, but not the content, until you get to a breakpoint.

Gaining ground in the Drupal Community
--------------------------------------
Recently a discussion (http://groups.drupal.org/node/236988) regarding the theme used for drupal.org (Bluecheese) led the community to select Susy as the framework for refactoring Bluecheese. With this decision, more Drupal themes will start adopting Susy for their responsive and grid features.

Using these technologies in our projects allows us to be more nimble and efficient as our creative teams continue to push the envelope of design and experience.
