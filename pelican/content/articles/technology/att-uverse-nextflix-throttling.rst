=============================================
Yes Virginia, AT&T is Throttling your Netflix
=============================================

:date: 2014-07-29
:summary: After reading a slashdot article on someone using a VPN to prove that Verizon is throttling Netflix, I thought I do my own similar test with an SSH SOCKS proxy and AT&T Uverse...


Today I read `this article <http://hothardware.com/News/Enraged-Verizon-FiOS-Customer-Posts-Video-Seemingly-Proving-ISP-Throttles-Netflix/>`_ via `Slashdot <http://yro.slashdot.org/story/14/07/26/0324226/enraged-verizon-fios-customer-seemingly-demonstrates-netflix-throttling>`_ that reported a startup CEO, who was very skeptical of Verizon's speed when it came to Netflix, decided to run a pretty simple test to see if throttling was involved. He compared the Netflix down speeds without a VPN and then with a VPN. He found a difference of 375kbps to 3000kbps, respectively. In theory the VPN should be slower because of extra hops and encryption. I had to try this for myself.

So I have a 18mbps Uverse plan from AT&T. Let's see what Sppedtest.net has to say about it.

.. image:: {filename}/images/speedtest.png

Well, I'll be, better than advertised! AT&T must be giving me some love. But I've not been happy with the quality of video coming from Netflix and the regular buffering spinner that shows up, especially with `Adventure Time <http://www.netflix.com/WiMovie/70241425>`_ for some reason.

Now I don't have a VPN to test out, but I do have a server on Linode that I can use as a SOCKS proxy via SSH. This basically results in the same type of test from the article. I'm adding more hops and encryption. So this *should* be slower.

.. image:: {filename}/images/bandwidth.png

Wow! That's a huge difference. Over the SOCKS Proxy, Adventure Time was no longer in the low quality pixelated format. It was super crisp and motion was smooth.

I've tested this twice and the results have been the same. There is nothing else I can think of causing this drastic change in throughput other than AT&T is throttling Netflix and going over an encrypted proxy or VPN is masking the content so that AT&T's throttler is unable to identify it as Netflix content.

So now the question is "AT&T, what do you have to say for yourselves?"

