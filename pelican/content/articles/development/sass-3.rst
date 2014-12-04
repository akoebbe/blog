=================================================================
Taking stylesheets to school with Sass, Compass and Susy (Part 3)
=================================================================

:date: 2013-05-16
:summary: In the previous articles we covered the problem of CSS and the solution of Sass and Compass. But what about those fancy grid frameworks that use presentational class names? How can we leverage Sass to get a great responsive grid system and have our semantic class names?
:category: Development
:tags: sass, compass, susy, css


..

  This article was based on Susy 1.0. So it is outdated (unless you use the `susyone <http://susydocs.oddbird.net/en/latest/susyone/>`_ import). Please see `Susy's upgrade path doc <http://susydocs.oddbird.net/en/latest/upgrade/>`_ for more information on what has changed between version 1 and 2. I hope to have a new article about version 2 in the near future.

In `part 1 <{filename}sass-1.rst>`_ and `part 2 <{filename}sass-2.rst>`_ we covered the problem of CSS and the solution of Sass and Compass. But what about those fancy grid frameworks that use presentational class names? How can we leverage Sass to get a great responsive grid system and have our semantic class names?

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

The Susy developers have a great `"getting started” guide <http://susydocs.oddbird.net/en/latest/install/>`_ to show you how to install Susy.

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
It's worth noting that Susy is poised to merge with complementary projects to make it even more powerful. The list of developers on board with this initiative is pretty staggering. `Great things are in store <http://oddbird.net/2013/01/01/susy-next/>`_.

Sass, Compass and Susy in Drupal
--------------------------------
A large portion of VML projects use Drupal as the CMS. Because Sass is platform-agnostic, we've been able to leverage all of these technologies into the themes of our Drupal projects.

Susy's container-style variable allowed us to set the responsive behavior to a fixed style. The exact width of the container is clearly defined and not fluid. As screens vary slightly, the margin on either side of the page adjusts, but not the content, until you get to a breakpoint.

Gaining ground in the Drupal Community
--------------------------------------
Recently a `discussion <http://groups.drupal.org/node/236988>`_ regarding the theme used for drupal.org (Bluecheese) led the community to select Susy as the framework for refactoring Bluecheese. With this decision, more Drupal themes will start adopting Susy for their responsive and grid features.

Using these technologies in our projects allows us to be more nimble and efficient as our creative teams continue to push the envelope of design and experience.
