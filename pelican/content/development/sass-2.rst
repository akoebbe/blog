=================================================================
Taking stylesheets to school with Sass, Compass and Susy (Part 2)
=================================================================

:date: 2013-05-15


In the `previous article <{filename}sass-1.rst>`_ we bemoaned the failures and shortcomings of the CSS syntax. Sass shores up all of those failings and give us the power to logically structure and generate semantic stylesheets.

----------------------------------------------
Part 2: Sass, you had me at "nested selectors”
----------------------------------------------

`Sass <http://sass-lang.com/>`_ is a scripting language that processes its own stylesheet syntax into regular CSS files (a CSS pre-processor). This is not done browser-side or server-side. The resulting CSS is compiled on save as you develop.

Before I get in to the details of Sass, there are a number of other CSS pre-processors that are great, such as `Stylus <http://learnboost.github.io/stylus/>`_ and `Less <http://lesscss.org/>`_. In my opinion, it's a matter of preference, as they can handle nearly all the same functionality and their syntaxes are similarly structured. I personally prefer Sass, but I hold no ill will to those who prefer alternatives.

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

We can change the $link-color variable to another color and the rest of the colors will be recalculated automatically. In theory you could have Sass build the entire color scheme for your site based on one color variable.

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
With all of these features of Sass (and more), other tools can be built to provide mixins and additional useful functionality to Sass. That's exactly what `Compass <http://compass-style.org/>`_ does. It extends Sass with tons of cross-browser mixins and functions that make styling even easier and more powerful. We'll touch on only a few of my favorite features of Compass.

Cross-browser Mixins
--------------------
The bane of every web developer's existence is dealing with the inconsistencies across browsers. While the worst offending browsers need not be named, even some of the most standards-compliant browsers have their differences. Compass has a number of mixins meant to ease the coding of certain tasks that tend to need extra help when working in differing browsers. Gradients and shadows are commonly cross-browser incompatible without knowing exactly the right syntax and attributes to use. Compass has mixins for those.

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
Compass has some `magical sprite functions <http://compass-style.org/help/tutorials/spriting/>`_ that blew my mind when I first saw them in action. Let's be honest, sprites are great for load times and bandwidth management, but making sprite maps can be a pain, especially if you have to add sprites to your map as you develop. While there are services and applications to help ease the pain, with Compass you don't even have to think about it. Just throw your new sprite in a directory and Compass does the rest.

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

`Continue to Part 3 <{filename}sass-3.rst>`_
